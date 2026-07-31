#!/usr/bin/env python3
"""
normalize_lf.py — Normalize all prompt-library markdown files to LF.

Repo .gitattributes declares `*.md text eol=lf`, but a prior enhancement pass
wrote CRLF and a later pass double-encoded frontmatter to `\r\r\n`. This script
strips every CR so files match the declared canonical LF state.

Safe: idempotent; --dry-run default; --apply writes.
"""
import argparse
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    changed = 0
    total = 0
    for f in sorted(PROMPTS_DIR.rglob("*.md")):
        raw = f.read_bytes()
        if b"\r" not in raw:
            continue
        total += 1
        new_raw = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        if args.apply:
            f.write_bytes(new_raw)
            print(f"LF {f.relative_to(PROMPTS_DIR).as_posix()}")
        else:
            print(f"WOULD LF {f.relative_to(PROMPTS_DIR).as_posix()}")
        changed += 1

    print(f"\n{changed} files with CR line endings ({'NORMALIZED' if args.apply else 'DRY-RUN'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
