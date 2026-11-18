"""Integration contracts for read-only PMU-to-catalog recommendations."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

from hub import catalog
from hub.recommend import recommend

ROOT = Path(__file__).resolve().parents[1]


class PromptRecommendationTests(unittest.TestCase):
    def test_project_plan_links_real_canonical_hashes(self):
        result = recommend("Criar projeto de software do zero com testes", limit=8)
        self.assertEqual(result["catalog_count"], 797)
        self.assertEqual(result["plan"]["pmu_id"], "PMU-002")
        self.assertEqual(result["execution_status"], "PLAN_ONLY")
        self.assertEqual(result["permissions"], "NO_EXTERNAL_MUTATIONS")
        self.assertEqual(result["publication_gate"], "BLOCKED_PENDING_SOURCE_RIGHTS")
        self.assertEqual(
            [p["id"] for p in result["canonical_references"]],
            [p["id"] for p in result["plan"]["canonical_dependencies"]],
        )
        for entry, dependency in zip(result["canonical_references"],
                                     result["plan"]["canonical_dependencies"]):
            self.assertEqual(entry["sha256"], dependency["sha256"])
            self.assertEqual(entry["namespace"], "canonical")

    def test_related_entries_are_existing_metadata_and_not_approved(self):
        result = recommend("segurança e compliance", limit=5, pmu="PMU-007")
        self.assertEqual(result["plan"]["pmu_id"], "PMU-007")
        source = {(e["namespace"], e["id"]): e for e in catalog.entries()}
        self.assertLessEqual(len(result["related_catalog_entries"]), 5)
        for entry in result["related_catalog_entries"]:
            self.assertEqual(entry, source[(entry["namespace"], entry["id"])])
        self.assertEqual(result["editorial_policy"], "PRESERVE_SOURCE_STATUS")
        self.assertEqual(result["plan"]["permissions"], "NO_EXTERNAL_MUTATIONS")
        self.assertTrue(all(step["gate"] == "BLOCKED_UNTIL_VERIFIED"
                            for step in result["plan"]["steps"]))

    def test_empty_or_invalid_requests_fail_closed(self):
        for goal in ("", "   ", None):
            with self.subTest(goal=goal), self.assertRaises(ValueError):
                recommend(goal)
        for limit in (0, 21, True, 2.5):
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                recommend("auditoria", limit=limit)
        with self.assertRaises(ValueError):
            recommend("auditoria", pmu="PMU-999")

    def test_cli_recommend_keeps_plan_only(self):
        run = subprocess.run(
            [sys.executable, "-m", "hub.cli", "recommend",
             "--goal", "auditar segurança", "--limit", "3"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        data = json.loads(run.stdout)
        self.assertEqual(data["plan"]["pmu_id"], "PMU-003")
        self.assertEqual(data["execution_status"], "PLAN_ONLY")
        self.assertLessEqual(len(data["related_catalog_entries"]), 3)


if __name__ == "__main__":
    unittest.main()
