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

    def test_checkout_never_persists_token_in_git_config(self):
        for file in sorted(WORKFLOWS.glob("*.yml")):
            lines = file.read_text(encoding="utf-8").splitlines()
            for index, line in enumerate(lines):
                if "uses: actions/checkout@" in line:
                    with self.subTest(file=file.name, line=index + 1):
                        self.assertIn(
                            "persist-credentials: false",
                            "\\n".join(lines[index + 1:index + 5]),
                        )

    def test_codeql_has_exact_needed_upload_permission(self):
        codeql = WORKFLOWS / "peos-codeql-security.yml"
        content = codeql.read_text(encoding="utf-8")
        self.assertIn("  security-events: write", content)
        self.assertIn("  actions: read", content)
        self.assertIn("matrix:", content)
        self.assertIn("python, javascript-typescript", content)
        for file in sorted(WORKFLOWS.glob("*.yml")):
            if file == codeql:
                continue
            with self.subTest(file=file.name):
                self.assertNotIn("security-events: write", file.read_text(encoding="utf-8"))

    def test_codeql_init_and_analyze_share_exact_action_sha(self):
        content = (WORKFLOWS / "peos-codeql-security.yml").read_text(encoding="utf-8")
        ids = re.findall(
            r"github/codeql-action/(?:init|analyze)@([0-9a-f]{40})", content
        )
        self.assertEqual(len(ids), 2)
        self.assertEqual(ids[0], ids[1], "CodeQL steps must be updated atomically")

    def test_codeql_runs_when_npm_manifest_or_lockfile_changes(self):
        content = (WORKFLOWS / "peos-codeql-security.yml").read_text(encoding="utf-8")
        for manifest in ("package.json", "package-lock.json"):
            with self.subTest(manifest=manifest):
                self.assertEqual(
                    content.count("      - '" + manifest + "'"),
                    2,
                    "Both pull_request and push must include npm changes",
                )

    def test_dependabot_monitors_github_actions_without_auto_merge(self):
        config = (ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")
        self.assertIn("package-ecosystem: github-actions", config)
        self.assertIn("interval: weekly", config)
        self.assertIn("codeql-actions:", config)
        self.assertIn("github/codeql-action/*", config)
        self.assertNotIn("auto-merge", config)

    def test_npm_advisory_gate_is_read_only_and_has_weekly_coverage(self):
        content = (WORKFLOWS / "peos-npm-audit.yml").read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", content)
        self.assertIn("npm audit --package-lock-only --audit-level=high", content)
        self.assertIn("persist-credentials: false", content)
        self.assertIn("schedule:", content)
        self.assertIn("workflow_dispatch:", content)
        for name in ("package.json", "package-lock.json"):
            with self.subTest(name=name):
                self.assertEqual(content.count("      - '" + name + "'"), 2)
        self.assertNotIn("pull_request_target", content)

    def test_local_credentials_and_build_artifacts_are_ignored(self):
        patterns = set((ROOT / ".gitignore").read_text(encoding="utf-8").splitlines())
        for pattern in (".env", ".env.*", "node_modules/", "test-results/",
                        "playwright-report/", ".npmrc", ".pypirc", ".venv/"):
            with self.subTest(pattern=pattern):
                self.assertIn(pattern, patterns)


if __name__ == "__main__":
    unittest.main()
