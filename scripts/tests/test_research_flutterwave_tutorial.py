"""Tests for scripts/research_flutterwave_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestFlutterwaveResearchScript = make_research_tests(
    script_name="research_flutterwave_tutorial.py",
    topic_marker="flutterwave-tutorial",
    sample_file="research/flutterwave-tutorial/flutterwave-transfers-api-introduction.md",
)

if __name__ == "__main__":
    unittest.main()