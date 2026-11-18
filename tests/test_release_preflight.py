"""Fail-closed release evidence tests. No publishing, external requests, or secrets."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("release_preflight", ROOT / "tools/release_preflight.py")
preflight = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preflight)
SHA = "a" * 40


class ReleasePreflightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = json.loads((ROOT / "provenance/sources.json").read_text(encoding="utf-8"))
        cls.pmus = json.loads((ROOT / "pmu/manifest.json").read_text(encoding="utf-8"))
        cls.agents = json.loads((ROOT / "agents/manifest.json").read_text(encoding="utf-8"))

    def valid_record(self):
        return {
            "schema_version": "1.0.0",
            "project": "peos-knowledge-hub",
            "target_sha": SHA,
            "approved_by": "maintainer",
            "source_rights": [
                {"archive_sha256": x["archive_sha256"],
                 "rights_holder": "Evidence owner to validate",
                 "permission_scope": "redistribute_and_modify",
                 "evidence_url": "https://github.com/example/evidence/issues/1"}
                for x in self.sources["sources"]
            ],
            "manual_accessibility": {
                "verified": True, "tested_sha": SHA,
                "evidence_url": "https://github.com/example/evidence/issues/2"},
            "security_review": {
                "verified": True, "tested_sha": SHA,
                "evidence_url": "https://github.com/example/evidence/issues/3"},
            "pmu_editorial": {
                "decision": "retain_proposed",
                "evidence_url": "https://github.com/example/evidence/issues/4"},
        }

    def evaluate(self, record):
        return preflight.assess(record, self.sources, self.pmus, self.agents, SHA)

    def test_no_approval_is_blocked(self):
        self.assertIn("AUTHORIZATION_RECORD_MISSING", self.evaluate(None))

    def test_complete_documentary_record_is_parseable_not_legal_proof(self):
        self.assertEqual(self.evaluate(self.valid_record()), [])

    def test_commit_mismatch_is_blocked(self):
        record = self.valid_record()
        record["target_sha"] = "b" * 40
        self.assertIn("AUTHORIZATION_SHA_MISMATCH", self.evaluate(record))

    def test_missing_source_rights_is_blocked(self):
        record = self.valid_record()
        record["source_rights"].pop()
        self.assertIn("SOURCE_RIGHTS_EVIDENCE_INCOMPLETE", self.evaluate(record))

    def test_duplicate_source_rights_is_blocked(self):
        record = self.valid_record()
        record["source_rights"][1] = dict(record["source_rights"][0])
        self.assertIn("SOURCE_RIGHTS_EVIDENCE_INCOMPLETE", self.evaluate(record))

    def test_rights_scope_cannot_be_read_only(self):
        record = self.valid_record()
        record["source_rights"][0]["permission_scope"] = "read_only"
        self.assertIn("SOURCE_RIGHTS_EVIDENCE_INCOMPLETE", self.evaluate(record))

    def test_untrusted_evidence_url_is_rejected(self):
        record = self.valid_record()
        record["source_rights"][0]["evidence_url"] = "file:///tmp/fake"
        self.assertIn("SOURCE_RIGHTS_EVIDENCE_INCOMPLETE", self.evaluate(record))

    def test_accessibility_requires_current_sha(self):
        record = self.valid_record()
        record["manual_accessibility"]["tested_sha"] = "b" * 40
        self.assertIn("ACCESSIBILITY_EVIDENCE_INCOMPLETE", self.evaluate(record))

    def test_security_review_requires_evidence(self):
        record = self.valid_record()
        record["security_review"]["verified"] = False
        self.assertIn("SECURITY_EVIDENCE_INCOMPLETE", self.evaluate(record))

    def test_pmu_editorship_requires_explicit_decision(self):
        record = self.valid_record()
        record["pmu_editorial"]["decision"] = "ACTIVE"
        self.assertIn("PMU_EDITORIAL_DECISION_MISSING", self.evaluate(record))

    def test_agents_must_not_gain_permissions(self):
        record = self.valid_record()
        agents = json.loads(json.dumps(self.agents))
        agents["agents"][0]["permissions"] = ["deploy"]
        self.assertIn("UNEXPECTED_AGENT_PERMISSIONS",
                      preflight.assess(record, self.sources, self.pmus, agents, SHA))

    def test_pmu_status_must_not_silently_become_active(self):
        record = self.valid_record()
        pmus = json.loads(json.dumps(self.pmus))
        pmus["prompts"][0]["status"] = "ACTIVE"
        self.assertIn("UNEXPECTED_PMU_STATE",
                      preflight.assess(record, self.sources, pmus, self.agents, SHA))

    def test_status_mode_reports_blocked_without_failing_ci(self):
        p = subprocess.run([sys.executable, "tools/release_preflight.py"],
                           cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)["release_readiness"], "BLOCKED")

    def test_strict_requires_separate_file_and_explicit_acknowledgement(self):
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, encoding="utf-8").strip()
        dossier = self.valid_record()
        dossier["target_sha"] = sha
        dossier["manual_accessibility"]["tested_sha"] = sha
        dossier["security_review"]["tested_sha"] = sha
        with tempfile.TemporaryDirectory() as folder:
            external_file = Path(folder) / "approval.json"
            external_file.write_text(json.dumps(dossier), encoding="utf-8")
            cmd = [sys.executable, "tools/release_preflight.py",
                   "--require-evidence", "--authorization-file", str(external_file)]
            without_ack = subprocess.run(cmd, cwd=ROOT, capture_output=True,
                                         text=True, encoding="utf-8")
            self.assertEqual(without_ack.returncode, 2)
            self.assertIn("HUMAN_REVIEW_ACKNOWLEDGEMENT_MISSING", without_ack.stdout)
            # This is only a structural fixture: URLs are intentionally synthetic.
            with_ack = subprocess.run(cmd + ["--acknowledge-reviewed-evidence"],
                                      cwd=ROOT, capture_output=True,
                                      text=True, encoding="utf-8")
            self.assertEqual(with_ack.returncode, 0, with_ack.stdout + with_ack.stderr)
            self.assertIn("NOT_LEGAL_CERTIFICATION", with_ack.stdout)

    def test_strict_rejects_in_tree_dossier_and_wrong_sha(self):
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, encoding="utf-8").strip()
        dossier = self.valid_record()
        dossier["target_sha"] = sha
        dossier["manual_accessibility"]["tested_sha"] = sha
        dossier["security_review"]["tested_sha"] = sha
        with tempfile.TemporaryDirectory(dir=ROOT) as folder:
            in_tree = Path(folder) / "approval.json"
            in_tree.write_text(json.dumps(dossier), encoding="utf-8")
            cmd = [sys.executable, "tools/release_preflight.py",
                   "--require-evidence", "--authorization-file", str(in_tree),
                   "--acknowledge-reviewed-evidence"]
            result = subprocess.run(cmd, cwd=ROOT, capture_output=True,
                                    text=True, encoding="utf-8")
            self.assertEqual(result.returncode, 2)
            self.assertIn("AUTHORIZATION_FILE_MUST_BE_EXTERNAL", result.stdout)
        with tempfile.TemporaryDirectory() as folder:
            external_file = Path(folder) / "approval.json"
            external_file.write_text(json.dumps(dossier), encoding="utf-8")
            result = subprocess.run([sys.executable, "tools/release_preflight.py",
                                     "--require-evidence",
                                     "--authorization-file", str(external_file),
                                     "--acknowledge-reviewed-evidence",
                                     "--target-sha", "b" * 40],
                                    cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(result.returncode, 2)
            self.assertIn("TARGET_SHA_NOT_CHECKED_OUT", result.stdout)

    def test_strict_mode_fails_closed(self):
        p = subprocess.run([sys.executable, "tools/release_preflight.py", "--require-evidence"],
                           cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(p.returncode, 2, p.stdout + p.stderr)
        self.assertIn("AUTHORIZATION_RECORD_MISSING", p.stdout)


if __name__ == "__main__":
    unittest.main()
