"""PEOS repository hygiene and Actions supply-chain regression contracts."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
PINNED_ACTION = re.compile(r"^\s*uses:\s+[^\s@]+@[0-9a-f]{40}(?:\s+#.*)?\s*$")


class RepositorySecurityTests(unittest.TestCase):
    def test_all_actions_are_commit_pinned(self):
        files = sorted(WORKFLOWS.glob("*.yml"))
        self.assertGreaterEqual(len(files), 8)
        for file in files:
            for line in file.read_text(encoding="utf-8").splitlines():
                if line.strip().startswith("uses:"):
                    self.assertRegex(line, PINNED_ACTION, str(file))

    def test_workflows_are_read_only_and_no_pull_request_target(self):
        for file in sorted(WORKFLOWS.glob("*.yml")):
            data = file.read_text(encoding="utf-8")
            with self.subTest(file=file.name):
                self.assertIn("permissions:\n  contents: read", data)
                self.assertNotIn("pull_request_target", data)

    def test_local_credentials_and_build_artifacts_are_ignored(self):
        patterns = set((ROOT / ".gitignore").read_text(encoding="utf-8").splitlines())
        for pattern in (".env", ".env.*", "node_modules/", "test-results/",
                        "playwright-report/", ".npmrc", ".pypirc", ".venv/"):
            with self.subTest(pattern=pattern):
                self.assertIn(pattern, patterns)


if __name__ == "__main__":
    unittest.main()
