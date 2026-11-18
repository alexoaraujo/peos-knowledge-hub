"""Technical PMU review regression tests; never confer editorial approval."""
import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "audit_pmu_readiness", ROOT / "tools/audit_pmu_readiness.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class PMUReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pmus = json.loads((ROOT / "pmu/manifest.json").read_text(encoding="utf-8"))
        cls.workflows = json.loads((ROOT / "workflows/manifest.json").read_text(encoding="utf-8"))
        cls.agents = json.loads((ROOT / "agents/manifest.json").read_text(encoding="utf-8"))
        cls.catalog = json.loads((ROOT / "catalog/manifest.json").read_text(encoding="utf-8"))

    def assess(self, mutate=None):
        pmu, wf, agents, canonical = map(copy.deepcopy,
                (self.pmus, self.workflows, self.agents, self.catalog))
        if mutate:
            mutate(pmu, wf, agents, canonical)
        return audit.audit_records(pmu, wf, agents, canonical, ROOT)

    def test_ten_original_pmus_have_consistent_technical_contracts(self):
        result = self.assess()
        self.assertEqual(result["technical_gate"], "PASS", result)
        self.assertEqual(len(result["entries"]), 10)
        self.assertTrue(all(entry["technical_gate"] == "PASS" for entry in result["entries"]))
        self.assertTrue(all(entry["editorial_gate"] == "PENDING" for entry in result["entries"]))
        self.assertEqual(result["release_gate"], "BLOCKED")

    def test_pmu_state_must_remain_proposed(self):
        result = self.assess(lambda pmu, *_: pmu["prompts"][0].update(status="ACTIVE"))
        self.assertIn("PMU_EDITORIAL_STATE_CHANGED", result["entries"][0]["findings"])

    def test_hash_tamper_is_detected(self):
        result = self.assess(lambda pmu, *_: pmu["prompts"][0].update(sha256="0"*64))
        self.assertIn("PMU_SHA256_MISMATCH", result["entries"][0]["findings"])

    def test_invalid_canonical_reference_is_detected(self):
        result = self.assess(lambda pmu, *_: pmu["prompts"][0]["refs"].append("9999"))
        self.assertIn("INVALID_CANONICAL_REFERENCES", result["entries"][0]["findings"])

    def test_changed_stage_does_not_match_prompt_or_workflow(self):
        result = self.assess(lambda pmu, *_: pmu["prompts"][0]["stages"].__setitem__(0, "Inventado"))
        self.assertIn("PROMPT_STAGE_MISMATCH", result["entries"][0]["findings"])
        self.assertIn("WORKFLOW_STEPS_MISMATCH", result["entries"][0]["findings"])

    def test_evidence_gate_cannot_be_disabled(self):
        result = self.assess(lambda pmu, wf, *_: wf["workflows"][0]["steps"][0].update(evidence_required=False))
        self.assertIn("WORKFLOW_STEPS_MISMATCH", result["entries"][0]["findings"])

    def test_agent_cannot_gain_permissions(self):
        result = self.assess(lambda pmu, wf, agents, *_:
                             agents["agents"][0].update(permissions=["deployment:write"]))
        self.assertIn("AGENT_EXECUTION_POLICY_MISMATCH", result["entries"][0]["findings"])

    def test_agent_cannot_switch_to_executor(self):
        result = self.assess(lambda pmu, wf, agents, *_:
                             agents["agents"][0].update(execution_mode="EXECUTE"))
        self.assertIn("AGENT_EXECUTION_POLICY_MISMATCH", result["entries"][0]["findings"])

    def test_unsafe_prompt_file_path_is_rejected(self):
        result = self.assess(lambda pmu, *_: pmu["prompts"][0].update(prompt_path="../README.md"))
        self.assertIn("UNSAFE_PROMPT_PATH", result["entries"][0]["findings"])

    def test_duplicate_pmu_is_detected(self):
        def duplicate(pmu, *_):
            pmu["prompts"][1]["id"] = pmu["prompts"][0]["id"]
        result = self.assess(duplicate)
        self.assertIn("PMU_DUPLICATE_OR_MISSING_IDS", result["errors"])
        self.assertEqual(result["technical_gate"], "FAIL")

    def test_cli_emits_read_only_json_with_editorial_pending(self):
        proc = subprocess.run([sys.executable, "tools/audit_pmu_readiness.py"], cwd=ROOT,
                              capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        result = json.loads(proc.stdout)
        self.assertEqual(result["technical_gate"], "PASS")
        self.assertEqual(result["editorial_gate"], "PENDING")
        self.assertEqual(result["release_gate"], "BLOCKED")


if __name__ == "__main__":
    unittest.main()
