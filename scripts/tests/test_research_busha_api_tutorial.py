"""Tests for scripts/research_busha_api_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestBushaResearchScript = make_research_tests(
    script_name="research_busha_api_tutorial.py",
    topic_marker="busha-api-tutorial",
    sample_file="research/busha-api-tutorial/busha-business-api-a-primer.md",
)

if __name__ == "__main__":
    unittest.main()