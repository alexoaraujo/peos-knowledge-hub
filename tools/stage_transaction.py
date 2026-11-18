#!/usr/bin/env python3
"""Safe preparation and best-effort rollback for PEOS library version staging.

Runs the existing stage command in a disposable copy, validates the resulting
catalog, and only then promotes generated changes. This is not crash-atomic
across files; a killed process still requires recovery from version control.
"""
from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

GENERATED_DIRS = ("contracts", "releases", "indices", "dist")
GENERATED_FILES = (
    "catalog/manifest.json",
    "catalog/events.jsonl",
    "hub-portal/catalog.json",
    "colecoes/programacao-design/INDEX.md",
    "colecoes/programacao-design/CANDIDATOS_A_NOVOS_PROMPTS.md",
)
INPUT_DIRS = ("prompts", "originais", "pmu/prompts")
INPUT_FILES = (
    "catalog/taxonomy.json",
    "catalog/relations.json",
    "colecoes/programacao-design/manifest.json",
)
OMIT = {".git", ".venv", "venv", "node_modules", "test-results",
        "playwright-report", "__pycache__", ".pytest_cache"}


def _walk(root, directories=(), files=()):
    result = {}
    for dirname in directories:
        folder = root / dirname
        if not folder.exists():
            continue
        for path in folder.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Symbolic link in guarded tree: {path}")
            if path.is_file():
                result[path.relative_to(root).as_posix()] = path
    for name in files:
        path = root / name
        if path.is_symlink():
            raise ValueError(f"Symbolic link in guarded file: {path}")
        if path.is_file():
            result[name] = path
    return result


def _digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _run(root, command, env=None):
    result = subprocess.run(
        [sys.executable, *command], cwd=root, env=env,
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode:
        detail = (result.stdout + "\n" + result.stderr).strip()
        raise ValueError(f"Staging preflight failed ({result.returncode}): {detail[-1200:]}")
    return result.stdout


def _replace(path, content):
    """Single-file atomic replace; the set of files is not crash-atomic."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = None
    try:
        with tempfile.NamedTemporaryFile(
            prefix=".peos-stage-", dir=path.parent, delete=False
        ) as handle:
            tmp = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        if path.exists():
            os.chmod(tmp, path.stat().st_mode & 0o777)
        os.replace(tmp, path)
    finally:
        if tmp is not None:
            tmp.unlink(missing_ok=True)



def promote_generated(root, backup, prepared):
    """Promote selected outputs; restore already changed files if promotion fails."""
    done = []
    try:
        for name in sorted(prepared):
            target = root / name
            if prepared[name] is None:
                target.unlink(missing_ok=True)
            else:
                _replace(target, prepared[name])
            done.append(name)
    except BaseException:
        rollback_errors = []
        for name in reversed(done):
            try:
                if backup[name] is None:
                    (root / name).unlink(missing_ok=True)
                else:
                    _replace(root / name, backup[name])
            except OSError as exc:
                rollback_errors.append(f"{name}: {exc}")
        if rollback_errors:
            raise RuntimeError("Partial rollback; restore from Git: " + "; ".join(rollback_errors))
        raise

def stage_with_preflight(root, version, reason):
    root = Path(root).resolve()
    lock = root / ".peos-stage.lock"
    try:
        lock_fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ValueError("A PEOS stage lock already exists; inspect the prior run before retry") from exc
    try:
        os.write(lock_fd, f"pid={os.getpid()}\n".encode())
        os.close(lock_fd)
        with tempfile.TemporaryDirectory(prefix="peos-stage-preflight-") as folder:
            scratch = Path(folder) / "repo"
            shutil.copytree(root, scratch, ignore=shutil.ignore_patterns(*OMIT, ".peos-stage.lock"))
            before = _walk(root, GENERATED_DIRS, GENERATED_FILES)
            base = {p: _digest(f) for p, f in before.items()}
            original_inputs = _walk(root, INPUT_DIRS, INPUT_FILES)
            staged_inputs = _walk(scratch, INPUT_DIRS, INPUT_FILES)
            if set(original_inputs) != set(staged_inputs):
                raise ValueError("Source file set changed while creating preflight copy")
            source_hashes = {p: _digest(f) for p, f in staged_inputs.items()}

            child_env = os.environ.copy()
            child_env["PEOS_STAGE_PREPARED_CHILD"] = "1"
            output = _run(scratch, ["tools/library.py", "stage",
                                    "--version", version, "--reason", reason], child_env)
            _run(scratch, ["tools/build_hub_index.py"])
            _run(scratch, ["tools/library.py", "validate"])
            _run(scratch, ["tools/build_hub_index.py", "--check"])

            # Do not promote outputs if the developer changed source files or
            # generated files while the disposable preflight was running.
            now_inputs = _walk(root, INPUT_DIRS, INPUT_FILES)
            if set(now_inputs) != set(source_hashes) or any(
                _digest(f) != source_hashes[p] for p, f in now_inputs.items()
            ):
                raise ValueError("Sources changed during preflight; retry from a stable checkout")
            now = _walk(root, GENERATED_DIRS, GENERATED_FILES)
            if set(now) != set(base) or any(_digest(f) != base[p] for p, f in now.items()):
                raise ValueError("Generated files changed during preflight; refusing to overwrite")

            staged = _walk(scratch, GENERATED_DIRS, GENERATED_FILES)
            before_keys, after_keys = set(before), set(staged)
            changed = sorted(p for p in before_keys | after_keys if (
                p not in before or p not in staged or base[p] != _digest(staged[p])
            ))
            if not changed:
                raise ValueError("No versioned output changes were produced")
            backup = {p: before[p].read_bytes() if p in before else None for p in changed}
            prepared = {p: staged[p].read_bytes() if p in staged else None for p in changed}
            promote_generated(root, backup, prepared)
            print(output.rstrip())
            print(f"STAGE PREFLIGHT PASS: validated and promoted {len(changed)} generated files")
            print("NOTE: best-effort rollback on errors; use Git for recovery after abrupt termination")
    finally:
        lock.unlink(missing_ok=True)
