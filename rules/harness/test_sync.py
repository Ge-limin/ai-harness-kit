"""Exercise the public shell CLI with isolated files under the worktree."""

import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

HARNESS = Path(__file__).resolve().parent


class SyncTests(unittest.TestCase):
    def setUp(self):
        scratch = HARNESS.parents[1] / ".tmp"
        scratch.mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="principles-tests-", dir=scratch)
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        # Chinese fixtures preserve the source documents' heading syntax.
        self.general = "# General\n\n## 一、基本\n\n### 1.1 原则\n\ngeneral\n\n### 1.3 执行\n\nexecute\n"
        self.extra = "# Codex\n\n## 一、基本\n\n### 1.1 原则\n\ncodex\n\n### 1.2 沟通\n\ncommunicate\n"
        self.write("general.md", self.general)
        self.write("extra.md", self.extra)
        self.configure([
            {"sources": ["general.md"], "path": "single.md"},
            {"sources": ["general.md", "extra.md"], "path": "merged.md"},
        ])

    def write(self, name, content):
        (self.directory / name).write_bytes(content.encode("utf-8"))

    def configure(self, targets):
        self.write("targets.yaml", yaml.safe_dump({"targets": targets}))

    def run_cli(self, *args):
        return subprocess.run(
            ["bash", str(HARNESS / "sync.sh"), "--targets", str(self.directory / "targets.yaml"), *args],
            cwd=self.directory, capture_output=True, text=True, check=False,
        )

    def test_merge_and_exact_single_source_without_final_newline(self):
        self.write("general.md", self.general.rstrip("\n"))
        self.write("extra.md", self.extra.rstrip("\n"))
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.directory / "single.md").read_bytes(), self.general.rstrip("\n").encode())
        self.assertEqual((self.directory / "merged.md").read_text(),
                         "# General\n\n## 一、基本\n\n### 1.1 原则\n\ngeneral\n\ncodex\n\n"
                         "### 1.2 沟通\n\ncommunicate\n\n### 1.3 执行\n\nexecute\n")

    def test_missing_supplement_chapters_and_new_subsections(self):
        self.write("general.md", self.general + "\n## 二、其他\n\n### 2.1 测试\n\nother\n")
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("## 二、其他\n\n### 2.1 测试\n\nother", (self.directory / "merged.md").read_text())

    def test_body_headings_in_code_quotes_and_h4_remain_verbatim(self):
        body = "\n```markdown\n# Fake\n## 错误\n### 9.9 Fake\n```\n\n> ## 引用\n> ### 9.9 引用\n\n#### 普通标题\n\n原始正文\n"
        self.write("extra.md", self.extra + body)
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(body.rstrip("\n"), (self.directory / "merged.md").read_text())

    def test_invalid_structure_never_writes_any_target_or_backup(self):
        invalid_documents = [
            (self.extra.replace("1.1 原则", "1.1 异名"), "Title mismatch for the same number"),
            (self.extra.replace("一、基本", "一、异名"), "Title mismatch for the same number"),
            (self.extra + "\n### 1.2 沟通\n", "Duplicate subsection number"),
            (self.extra + "\n## 一、基本\n", "Duplicate chapter number"),
            (self.extra.replace("1.2 沟通", "2.2 沟通"), "does not belong to the current parent chapter"),
            ("# Codex\n\n### 1.1 原则\n", "Invalid heading level"),
            ("正文\n", "Missing H1"),
            ("# Codex\n\n## 1、基本\n", "Invalid chapter number"),
            (self.extra.replace("1.2 沟通", "1.0 沟通"), "Invalid subsection number"),
            ("# Codex\n\n## 二、其他\n\n## 一、基本\n", "Chapter numbers out of order"),
            (self.extra.replace("1.1 原则", "1.3 原则"), "Subsection numbers out of order"),
            ("# Codex\n\n## 二、其他\n", "does not exist in the baseline document"),
            (self.extra + "\n# Again\n", "Duplicate H1"),
            (self.extra + "\n#### 子标题\n\n##### 太深\n", "Invalid heading level"),
        ]
        for name in ["single.md", "merged.md", "single.md.bak-old", "merged.md.bak-old"]:
            self.write(name, "retain " + name)
        for document, message in invalid_documents:
            for args in [(), ("--dry-run",)]:
                with self.subTest(message=message, args=args):
                    self.write("extra.md", document)
                    before = {path.name: path.read_bytes() for path in self.directory.iterdir()}
                    result = self.run_cli(*args)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(message, result.stderr)
                    self.assertRegex(result.stderr, r"extra\.md:\d+:")
                    after = {path.name: path.read_bytes() for path in self.directory.iterdir()}
                    self.assertEqual(before, after)

    def test_dry_run_validates_without_creating_files(self):
        before = set(self.directory.iterdir())
        result = self.run_cli("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before, set(self.directory.iterdir()))

    def test_missing_source_leaves_targets_and_backups_untouched(self):
        (self.directory / "extra.md").unlink()
        self.write("single.md", "old")
        self.write("single.md.bak-old", "older")
        result = self.run_cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("extra.md", result.stderr)
        self.assertEqual((self.directory / "single.md").read_text(), "old")
        self.assertEqual((self.directory / "single.md.bak-old").read_text(), "older")
        self.assertFalse((self.directory / "merged.md").exists())

    def test_backup_contains_previous_target_and_replaces_older_backup(self):
        self.write("single.md", "previous")
        self.write("single.md.bak-old", "older")
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        backups = list(self.directory.glob("single.md.bak-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), "previous")
        self.assertFalse((self.directory / "single.md.bak-old").exists())


if __name__ == "__main__":
    unittest.main()
