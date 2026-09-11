#!/usr/bin/env python3
"""Shared helpers for research/* digest scripts.

Single source of truth for topic metadata. Scripts stay thin wrappers.
"""
from __future__ import annotations

import pathlib
import sys

RESEARCH = pathlib.Path(__file__).resolve().parent.parent / "research"

# topic-dir slug -> display title
TOPIC_TITLES = {
    "binance-api-tutorial": "Binance Spot API - auth, endpoints, order types, rate limits, testnet",
    "busha-api-tutorial": "Busha Business API - request-quote-execute transfers, KYB, 2FA",
    "cryptocurrency-wallets-api-tutorial": "Crypto Wallet APIs - CryptoAPIs/MPC wallet generation",
    "face-mask-video-call-tutorial": "Face masking for video calls - UV4L Raspberry Pi, VSDC",
    "flutterwave-tutorial": "Flutterwave Transfers API - 4-step transfer flow",
    "hermes-agents-tutorial": "Hermes Agent - quickstart, architecture, agent loop",
    "hermes-memory-files": "Hermes memory - SOUL.md/MEMORY.md/state.db, memory tool",
    "paypal-tutorial": "PayPal - how it works, payments, rewards",
    "paystack-tutorial": "Paystack - getting started, developer documentation",
    "python-asyncio-tutorial": "Python asyncio - concepts, patterns, complete guides",
}


def list_topic_files(topic: str) -> list[str]:
    """Return research-relative paths of markdown files for a topic dir."""
    d = RESEARCH / topic
    if not d.is_dir():
        print(f"error: unknown topic dir: {topic}", file=sys.stderr)
        sys.exit(2)
    return sorted(str(p.relative_to(RESEARCH)) for p in d.glob("*.md"))


def list_root_files(pattern: str = "*.md") -> list[str]:
    """Return research-relative paths of root-level markdown files."""
    return sorted(str(p.relative_to(RESEARCH)) for p in RESEARCH.glob(pattern))


def digest(path: str) -> tuple[str, list[str]]:
    """Extract (title, headings) from a markdown file. Exit 2 on bad input."""
    p = pathlib.Path(path)
    if not p.is_file() or p.suffix != ".md":
        print(f"error: not a markdown file: {path}", file=sys.stderr)
        sys.exit(2)
    try:
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        print(f"error: cannot read {path}: {exc}", file=sys.stderr)
        sys.exit(2)
    title = next((ln[2:].strip() for ln in lines if ln.startswith("# ")), p.name)
    headings = [ln for ln in lines if ln.startswith("#")]
    return title, headings


def run_topic_cli(topic: str, argv: list[str]) -> int:
    """Shared CLI for topic scripts: no args = list files; --file <md> = digest.

    Returns process exit code: 0 success, 2 usage/input error.
    """
    if len(argv) == 2 and argv[0] == "--file":
        title, headings = digest(argv[1])
        print(f"# {title}")
        print("\n".join(headings))
        return 0
    if argv:
        print("usage: research_<topic>.py [--file <research-path.md>]", file=sys.stderr)
        return 2
    files = list_topic_files(topic)
    print(f"# {TOPIC_TITLES.get(topic, topic)}")
    print(f"{len(files)} file(s):")
    for f in files:
        print(f"  - {f}")
    return 0