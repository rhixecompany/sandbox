"""Tests for scripts/research_python_asyncio_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestAsyncioResearchScript = make_research_tests(
    script_name="research_python_asyncio_tutorial.py",
    topic_marker="python-asyncio-tutorial",
    sample_file="research/python-asyncio-tutorial/python-asyncio-part-1-basic-concepts-and-patterns.md",
)

if __name__ == "__main__":
    unittest.main()