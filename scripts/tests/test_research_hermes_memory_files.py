"""Tests for scripts/research_hermes_memory_files.py."""
import unittest

from research_test_common import make_research_tests

TestHermesMemoryResearchScript = make_research_tests(
    script_name="research_hermes_memory_files.py",
    topic_marker="hermes-memory-files",
    sample_file="research/hermes-memory-files/nous-research-hermes-persistent-memory.md",
)

if __name__ == "__main__":
    unittest.main()