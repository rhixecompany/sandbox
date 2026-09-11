#!/usr/bin/env python3
"""Research digest CLI: root-level uk earning-sites research files."""
import sys

from research_common import RESEARCH, digest, list_root_files

TOPIC = "uk-earning-sites"
TITLE = "UK money earning sites - comparison and 2026 research"
FILES = [f for f in list_root_files() if f.startswith("uk-")]


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[0] == "--file":
        title, headings = digest(argv[1])
        print(f"# {title}")
        print("\n".join(headings))
        return 0
    if argv:
        print("usage: research_uk_earning_sites.py [--file <research-path.md>]", file=sys.stderr)
        return 2
    print(f"# {TITLE}")
    print(f"{len(FILES)} file(s):")
    for f in FILES:
        print(f"  - {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))