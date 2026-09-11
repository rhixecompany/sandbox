"""Tests for scripts/research_paypal_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestPaypalResearchScript = make_research_tests(
    script_name="research_paypal_tutorial.py",
    topic_marker="paypal-tutorial",
    sample_file="research/paypal-tutorial/how-paypal-works-paypal-us.md",
)

if __name__ == "__main__":
    unittest.main()