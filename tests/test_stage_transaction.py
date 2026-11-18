"""Safety contracts for future PEOS library stage operations.

All version staging in these tests occurs in disposable directory copies.
"""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "stage_transaction", ROOT / "tools/stage_transaction.py")
transaction = importlib.util.module_from_spec(spec)
spec.loader.exec_module(transaction)


class StageSafetyTests(unittest.TestCase):
    def test_promote_restores_previous_files_if_second_write_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.txt").write_bytes(b"old a")
            (root / "b.txt").write_bytes(b"old b")
            original = transaction._replace
            calls = [0]

            def fail_second(target, data):
                calls[0] += 1
                if calls[0] == 2:
                    raise OSError("test simulated interrupted promotion")
                return original(target, data)

            with patch.object(transaction, "_replace", side_effect=fail_second):
                with self.assertRaisesRegex(OSError, "simulated interrupted"):
                    transaction.promote_generated(
                        root,
                        {"a.txt": b"old a", "b.txt": b"old b"},
                        {"a.txt": b"new a", "b.txt": b"new b"},
                    )
            self.assertEqual((root / "a.txt").read_bytes(), b"old a")
            self.assertEqual((root / "b.txt").read_bytes(), b"old b")

    def test_promote_can_create_and_delete_generated_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "old.txt").write_bytes(b"old")
            transaction.promote_generated(
                root, {"old.txt": b"old", "new.txt": None},
                {"old.txt": None, "new.txt": b"new"},
            )
            self.assertFalse((root / "old.txt").exists())
            self.assertEqual((root / "new.txt").read_bytes(), b"new")

    def test_stage_full_version_uses_preflight_and_validates_promoted_outputs(self):
        with tempfile.TemporaryDirectory(prefix="peos-stage-safety-test-") as folder:
            root = Path(folder) / "working"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(
                *transaction.OMIT, ".peos-stage.lock"))
            prompt = root / "prompts/0000-0099/0001.md"
            prompt.write_text(
                prompt.read_text(encoding="utf-8") +
                "\nObservação de teste da transação — somente no diretório descartável.\n",
                encoding="utf-8"
            )
            source_before = prompt.read_bytes()
            result = subprocess.run(
                [sys.executable, "tools/library.py", "stage",
                 "--version", "2.1.1", "--reason", "Ensaio isolado de staging seguro"],
                cwd=root, capture_output=True, text=True, encoding="utf-8",
                timeout=180,
            )
            self.assertEqual(result.returncode, 0, result.stdout + "\n" + result.stderr)
            self.assertIn("STAGE PREFLIGHT PASS", result.stdout)
            self.assertTrue((root / "releases/v2.1.1.json").is_file())
            self.assertTrue((root / "dist/Biblioteca_Mestre_TI_Estruturada_v2.1.1.md").is_file())
            self.assertEqual(prompt.read_bytes(), source_before)
            self.assertFalse((root / ".peos-stage.lock").exists())
            valid = subprocess.run(
                [sys.executable, "tools/library.py", "validate"], cwd=root,
                capture_output=True, text=True, encoding="utf-8", timeout=120,
            )
            self.assertEqual(valid.returncode, 0, valid.stdout + valid.stderr)
            index = subprocess.run(
                [sys.executable, "tools/build_hub_index.py", "--check"], cwd=root,
                capture_output=True, text=True, encoding="utf-8", timeout=120,
            )
            self.assertEqual(index.returncode, 0, index.stdout + index.stderr)

    def test_invalid_release_does_not_mutate_live_manifest(self):
        with tempfile.TemporaryDirectory(prefix="peos-stage-failure-test-") as folder:
            root = Path(folder) / "working"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(
                *transaction.OMIT, ".peos-stage.lock"))
            path = root / "catalog/manifest.json"
            before = path.read_bytes()
            result = subprocess.run(
                [sys.executable, "tools/library.py", "stage",
                 "--version", "2.1.0", "--reason", "Version regression should fail"],
                cwd=root, capture_output=True, text=True, encoding="utf-8",
                timeout=180,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(path.read_bytes(), before)
            self.assertFalse((root / ".peos-stage.lock").exists())
            self.assertFalse((root / "releases/v2.1.1.json").exists())


if __name__ == "__main__":
    unittest.main()
