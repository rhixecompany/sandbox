#!/usr/bin/env python3
"""Fetch or parse the github/awesome-copilot skills catalog.

Usage:
  python parse_copilot_catalog.py                # fetch live from API
  python parse_copilot_catalog.py cache.md       # parse a web_extract cache file
  python parse_copilot_catalog.py --count        # print only the count
"""
import json
import re
import sys
import urllib.request

API = "https://api.github.com/repos/github/awesome-copilot/contents/skills?ref=main"


def fetch_live():
    req = urllib.request.Request(API, headers={"User-Agent": "hermes"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    return sorted({e["name"] for e in data if e.get("type") == "dir"})


def parse_cache(path):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    return sorted(set(re.findall(r'"name":\s*"([^"]+)"', txt)))


def main():
    count_only = "--count" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if args:
        names = parse_cache(args[0])
    else:
        names = fetch_live()

    if count_only:
        print(len(names))
    else:
        print(f"TOTAL SKILLS: {len(names)}")
        for n in names:
            print(n)


if __name__ == "__main__":
    main()
