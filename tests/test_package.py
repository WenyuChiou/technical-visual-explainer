"""Portable package and documentation checks; these do not inspect images."""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "technical-visual-explainer"


def local_links(path):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        url = urlsplit(target.strip().split(' "', 1)[0])
        if not url.scheme and not url.netloc and url.path:
            yield unquote(url.path)


class PackageTests(unittest.TestCase):
    def test_repository_document_links_resolve(self):
        for doc in ROOT.rglob("*.md"):
            if ".git" in doc.parts:
                continue
            for link in local_links(doc):
                with self.subTest(document=doc.relative_to(ROOT), link=link):
                    target = (doc.parent / link).resolve()
                    self.assertTrue(target.is_relative_to(ROOT))
                    self.assertTrue(target.exists())

    def test_skill_stands_alone_after_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "technical-visual-explainer"
            shutil.copytree(SKILL, destination,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            self.assertTrue((destination / "SKILL.md").is_file())
            self.assertTrue((destination / "agents/openai.yaml").is_file())
            for doc in destination.rglob("*.md"):
                for link in local_links(doc):
                    target = (doc.parent / link).resolve()
                    self.assertTrue(target.is_relative_to(destination), str(target))
                    self.assertTrue(target.exists(), str(target))
            # The optional checker must remain callable outside this repository.
            spec = Path(tmp) / "bad-connection.json"
            spec.write_text(json.dumps({"nodes": [{"id": "input"}],
                                        "edges": [{"source": "input", "target": "missing"}]}),
                            encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(destination / "scripts/check_graph.py"), str(spec)],
                cwd=tmp, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(json.loads(result.stdout)["findings"],
                             ["unknown endpoint: input -> missing"])

    def test_installable_text_has_no_personal_absolute_paths(self):
        for path in SKILL.rglob("*"):
            if path.suffix not in {".md", ".py", ".yaml"}:
                continue
            text = path.read_text(encoding="utf-8")
            with self.subTest(file=path.relative_to(SKILL)):
                self.assertNotRegex(text, r"(?i)[a-z]:[/\\](users|documents and settings)[/\\]")
                self.assertNotRegex(text, r"/(Users|home)/[A-Za-z0-9_.-]+/")


if __name__ == "__main__":
    unittest.main()
