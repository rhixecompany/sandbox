#!/usr/bin/env python3
"""Research digest CLI: busha-api-tutorial."""
import sys

from research_common import run_topic_cli

if __name__ == "__main__":
    sys.exit(run_topic_cli("busha-api-tutorial", sys.argv[1:]))