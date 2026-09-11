"""Tests for scripts/research_cryptocurrency_wallets_api_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestCryptoWalletsResearchScript = make_research_tests(
    script_name="research_cryptocurrency_wallets_api_tutorial.py",
    topic_marker="cryptocurrency-wallets-api-tutorial",
    sample_file="research/cryptocurrency-wallets-api-tutorial/crypto-wallet-api-quickstart-generate-wallets-in-10-minutes.md",
)

if __name__ == "__main__":
    unittest.main()