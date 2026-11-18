#!/usr/bin/env python3
"""Read-only PEOS release evidence preflight, not a license or WCAG certification.

Default mode reports BLOCKED gates but succeeds if metadata is internally valid.
--require-evidence fails closed if a per-commit authorization dossier is missing
or incomplete. No external URLs or rights claims are automatically verified.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
EVIDENCE_URL = re.compile(r"^https://[^\s/]+/[^\s]+$")


def valid_evidence(value):
    return isinstance(value, str) and bool(EVIDENCE_URL.fullmatch(value))


def assess(authorization, provenance, pmu_manifest, agents_manifest, commit_sha):
    """Return explicit blocker codes; fields are documentary assertions only."""
    blockers = []
    sources = provenance.get("sources")
    prompts = pmu_manifest.get("prompts")
    agents = agents_manifest.get("agents")

    if not isinstance(sources, list) or len(sources) != 3 or any(
        not isinstance(s, dict)
        or not SHA256.fullmatch(str(s.get("archive_sha256", "")))
        for s in sources
    ):
        blockers.append("INVALID_SOURCE_PROVENANCE")
    if not isinstance(prompts, list) or len(prompts) != 10 or any(
        not isinstance(p, dict) or p.get("status") != "PROPOSED" for p in prompts
    ):
        blockers.append("UNEXPECTED_PMU_STATE")
    if not isinstance(agents, list) or len(agents) != 10 or any(
        not isinstance(a, dict)
        or a.get("execution_mode") != "PLAN_ONLY"
        or a.get("permissions") != [] for a in agents
    ):
        blockers.append("UNEXPECTED_AGENT_PERMISSIONS")
    if not SHA40.fullmatch(str(commit_sha)):
        blockers.append("INVALID_TARGET_SHA")

    if authorization is None:
        blockers.append("AUTHORIZATION_RECORD_MISSING")
        return blockers
    if not isinstance(authorization, dict):
        blockers.append("INVALID_AUTHORIZATION_RECORD")
        return blockers
    if authorization.get("schema_version") != "1.0.0" or authorization.get("project") != "peos-knowledge-hub":
        blockers.append("INVALID_AUTHORIZATION_RECORD")
    if authorization.get("target_sha") != commit_sha:
        blockers.append("AUTHORIZATION_SHA_MISMATCH")
    if not str(authorization.get("approved_by", "")).strip():
        blockers.append("MISSING_NAMED_MAINTAINER")

    rights = authorization.get("source_rights")
    expected = {s["archive_sha256"] for s in sources} if "INVALID_SOURCE_PROVENANCE" not in blockers else set()
    if not isinstance(rights, list) or len(rights) != 3 or {
        x.get("archive_sha256") for x in rights if isinstance(x, dict)
    } != expected or any(
        not isinstance(x, dict)
        or x.get("permission_scope") != "redistribute_and_modify"
        or not str(x.get("rights_holder", "")).strip()
        or not valid_evidence(x.get("evidence_url"))
        for x in rights
    ):
        blockers.append("SOURCE_RIGHTS_EVIDENCE_INCOMPLETE")

    for key, code in (("manual_accessibility", "ACCESSIBILITY_EVIDENCE_INCOMPLETE"),
                      ("security_review", "SECURITY_EVIDENCE_INCOMPLETE")):
        record = authorization.get(key)
        if not isinstance(record, dict) or record.get("verified") is not True or (
            record.get("tested_sha") != commit_sha
        ) or not valid_evidence(record.get("evidence_url")):
            blockers.append(code)
    editorial = authorization.get("pmu_editorial")
    if not isinstance(editorial, dict) or editorial.get("decision") not in (
        "retain_proposed", "exclude"
    ) or not valid_evidence(editorial.get("evidence_url")):
        blockers.append("PMU_EDITORIAL_DECISION_MISSING")
    return blockers


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def current_sha(root):
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root, text=True, encoding="utf-8", capture_output=True, check=True
    )
    return result.stdout.strip()


def inspect(root=ROOT, commit_sha=None, authorization_path=None):
    try:
        provenance = read_json(root / "provenance/sources.json")
        pmus = read_json(root / "pmu/manifest.json")
        agents = read_json(root / "agents/manifest.json")
        sha = commit_sha if commit_sha is not None else current_sha(root)
        # Evidence must be supplied separately: putting a dossier in the target
        # commit would change its SHA and invalidate its own target_sha field.
        authorization = read_json(authorization_path) if authorization_path is not None and authorization_path.is_file() else None
        return assess(authorization, provenance, pmus, agents, sha)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        return ["PREFLIGHT_INPUT_UNAVAILABLE: " + type(exc).__name__]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-evidence", action="store_true",
                        help="Exit nonzero when any authorization evidence is incomplete")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--target-sha", default=None)
    parser.add_argument("--authorization-file", type=Path, default=None,
                        help="Out-of-tree JSON dossier for the exact candidate commit")
    parser.add_argument("--acknowledge-reviewed-evidence", action="store_true",
                        help="Human attests that all linked evidence was independently examined")
    args = parser.parse_args(argv)
    codes = inspect(args.root, commit_sha=args.target_sha,
                    authorization_path=args.authorization_file)

    if args.require_evidence:
        # A dossier committed *inside* the tree it attests is self-referential.
        if args.authorization_file is not None:
            try:
                args.authorization_file.resolve().relative_to(args.root.resolve())
            except ValueError:
                pass
            else:
                codes.append("AUTHORIZATION_FILE_MUST_BE_EXTERNAL")
        if args.target_sha is not None:
            try:
                actual = current_sha(args.root)
                if args.target_sha != actual:
                    codes.append("TARGET_SHA_NOT_CHECKED_OUT")
            except (OSError, subprocess.CalledProcessError):
                codes.append("PREFLIGHT_INPUT_UNAVAILABLE")
        if not args.acknowledge_reviewed_evidence:
            codes.append("HUMAN_REVIEW_ACKNOWLEDGEMENT_MISSING")
    invalid = any(code.startswith(("INVALID_", "UNEXPECTED_", "PREFLIGHT_INPUT_")) for code in codes)
    print(json.dumps({
        "project": "peos-knowledge-hub",
        "release_readiness": "BLOCKED" if codes else (
            "DOCUMENTARY_EVIDENCE_ACKNOWLEDGED_NOT_LEGAL_CERTIFICATION"
            if args.acknowledge_reviewed_evidence else
            "EVIDENCE_RECORDED_NEEDS_HUMAN_VERIFICATION"
        ),
        "blockers": codes,
        "warning": "URLs/claims are not verified: this never grants redistribution rights or WCAG certification",
    }, ensure_ascii=False, sort_keys=True))
    if invalid or (args.require_evidence and codes):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
