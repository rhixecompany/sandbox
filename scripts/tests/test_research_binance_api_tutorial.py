"""Tests for scripts/research_binance_api_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestBinanceResearchScript = make_research_tests(
    script_name="research_binance_api_tutorial.py",
    topic_marker="binance-api-tutorial",
    sample_file="research/binance-api-tutorial/binance-python-api-a-step-by-step-guide.md",
)

if __name__ == "__main__":
    unittest.main()