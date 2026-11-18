"""Cross-platform contracts for PEOS canonical content and test harness.

These tests are read-only and never update the historical SHA-256 baseline.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PlatformIntegrityTests(unittest.TestCase):
    def test_canonical_paths_use_forward_slashes(self):
        from tools import library
        manifest = library.load(library.MANIFEST)
        for entry in manifest["prompts"]:
            path = entry["content_path"]
            self.assertNotIn("\\", path, entry["id"])
            self.assertEqual((ROOT / path).relative_to(ROOT).as_posix(), path)
        self.assertEqual(len(manifest["prompts"]), 659)

    def test_source_and_prompt_checkout_use_lf(self):
        manifest = json.loads((ROOT / "catalog" / "manifest.json").read_text(encoding="utf-8"))
        sources = [ROOT / src["path"] for src in manifest["sources"].values()]
        prompts = [ROOT / row["content_path"] for row in manifest["prompts"]]
        for file in sources + prompts:
            raw = file.read_bytes()
            self.assertNotIn(b"\r\n", raw, str(file))

    def test_git_attributes_protect_historical_text(self):
        attrs = (ROOT / ".gitattributes").read_text(encoding="utf-8")
        for extension in ("md", "json", "jsonl", "txt", "csv", "py"):
            self.assertIn(f"*.{extension} text eol=lf", attrs)

    def test_utf8_child_and_fixture_roundtrip(self):
        message = "Índice, coleção, canônico — validação"
        env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        result = subprocess.run(
            [sys.executable, "-c", f"print({message!r})"],
            text=True, encoding="utf-8", capture_output=True, check=False, env=env
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), message)
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "fixture.json"
            target.write_text(json.dumps({"message": message}, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(json.loads(target.read_text(encoding="utf-8"))["message"], message)


if __name__ == "__main__":
    unittest.main()
