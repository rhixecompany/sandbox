"""Tests for scripts/research_uk_earning_sites.py."""
import unittest

from research_test_common import make_research_tests

TestUkEarningSitesResearchScript = make_research_tests(
    script_name="research_uk_earning_sites.py",
    topic_marker="UK money earning sites",
    sample_file="research/uk-earning-sites-comparison.md",
)

if __name__ == "__main__":
    unittest.main()