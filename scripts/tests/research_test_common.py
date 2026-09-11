#!/usr/bin/env python3
"""Factory for research digest script tests.

No TestCase lives at module level here — each test file builds exactly one
class via make_research_tests(), so unittest discovery never collects the
shared base with empty configuration.
"""
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
SCRIPTS = ROOT / "scripts"


def make_research_tests(script_name: str, topic_marker: str, sample_file: str):
    """Return a unittest.TestCase class exercising one research_* script.

    Tests: list mode exits 0, list mode prints marker, digest mode works,
    bad flag fails, missing file fails.
    """
    cls_name = (
        "Test"
        + pathlib.Path(script_name).stem.replace("research_", "", 1).replace("_", " ").title().replace(" ", "")
        + "Script"
    )

    def run_script(self, *args) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(SCRIPTS / script_name), *args],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )

    def test_list_mode_exit_zero(self):
        r = run_script(self)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_list_mode_prints_topic(self):
        r = run_script(self)
        self.assertIn(topic_marker, r.stdout)

    def test_digest_mode(self):
        r = run_script(self, "--file", sample_file)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("# ", r.stdout)

    def test_bad_flag_fails(self):
        r = run_script(self, "--bogus")
        self.assertNotEqual(r.returncode, 0)

    def test_missing_file_fails(self):
        r = run_script(self, "--file", "research/nope/missing.md")
        self.assertNotEqual(r.returncode, 0)

    return type(
        cls_name,
        (unittest.TestCase,),
        {
            "run_script": run_script,
            "test_list_mode_exit_zero": test_list_mode_exit_zero,
            "test_list_mode_prints_topic": test_list_mode_prints_topic,
            "test_digest_mode": test_digest_mode,
            "test_bad_flag_fails": test_bad_flag_fails,
            "test_missing_file_fails": test_missing_file_fails,
        },
    )


if __name__ == "__main__":
    unittest.main()