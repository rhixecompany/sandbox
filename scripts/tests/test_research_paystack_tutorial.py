"""Tests for scripts/research_paystack_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestPaystackResearchScript = make_research_tests(
    script_name="research_paystack_tutorial.py",
    topic_marker="paystack-tutorial",
    sample_file="research/paystack-tutorial/getting-started-with-paystack.md",
)

if __name__ == "__main__":
    unittest.main()