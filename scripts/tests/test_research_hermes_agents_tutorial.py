"""Tests for scripts/research_hermes_agents_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestHermesAgentsResearchScript = make_research_tests(
    script_name="research_hermes_agents_tutorial.py",
    topic_marker="hermes-agents-tutorial",
    sample_file="research/hermes-agents-tutorial/hermes-agent-deep-dive-build-your-own-guide.md",
)

if __name__ == "__main__":
    unittest.main()