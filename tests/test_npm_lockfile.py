"""Verify reproducible browser CI dependencies and lockfile integrity."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class NpmLockfileTests(unittest.TestCase):
    def test_manifest_and_lockfile_agree(self):
        manifest = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        lock = json.loads((ROOT / "package-lock.json").read_text(encoding="utf-8"))
        self.assertTrue(manifest["private"])
        self.assertEqual(lock["lockfileVersion"], 3)
        self.assertEqual(lock["packages"][""]["devDependencies"], manifest["devDependencies"])
        self.assertIn("@playwright/test", manifest["devDependencies"])
        self.assertIn("@axe-core/playwright", manifest["devDependencies"])
        for package, metadata in lock["packages"].items():
            if package:
                with self.subTest(package=package):
                    self.assertTrue(metadata.get("resolved"), "missing registry resolution")
                    self.assertTrue(metadata.get("integrity", "").startswith("sha"), "missing integrity hash")

    def test_browser_ci_uses_lockfile_and_dependabot_tracks_npm(self):
        workflow = (ROOT / ".github/workflows/portal-browser-e2e.yml").read_text(encoding="utf-8")
        dependabot = (ROOT / ".github/dependabot.yml").read_text(encoding="utf-8")
        self.assertIn("npm ci --ignore-scripts --no-audit --no-fund", workflow)
        self.assertNotIn("--package-lock=false", workflow)
        self.assertEqual(workflow.count("      - 'package.json'"), 2)
        self.assertEqual(workflow.count("      - 'package-lock.json'"), 2)
        self.assertIn("package-ecosystem: npm", dependabot)


if __name__ == "__main__":
    unittest.main()
