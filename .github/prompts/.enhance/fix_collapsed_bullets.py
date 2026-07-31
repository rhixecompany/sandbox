#!/usr/bin/env python3
"""
fix_collapsed_bullets.py — Repair collapsed bullet runs in prompt files.

Bug: a newline between list items was removed, gluing items together:
    `- DOC-001: Context- DOC-002: Containers- DOC-003: Components`
should be:
    - DOC-001: Context
    - DOC-002: Containers
    - DOC-003: Components

Signature: within a `- ` bullet line, a `- <CODE>-NNN:` token boundary after
non-whitespace (e.g. `component- ANA-002:`). CODE is 2-6 uppercase letters,
NNN is 3 digits — a structured ID format that never legitimately follows
content without a newline.

Dry-run by default; --apply writes. LF output.
"""
import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

# split BEFORE a structured item marker glued after non-whitespace
ITEM_SPLIT = re.compile(r"(?<=\S)(?=- [A-Z]{2,6}-\d{3}:)")


def fix_text(text: str) -> tuple[str, int]:
    changes = 0
    out = []
    in_fence = False
    for raw_line in text.split("\n"):
        line = raw_line.rstrip("\r\n")
        fm = line.count("```") + line.count("~~~")
        if in_fence:
            if fm % 2 == 1:
                in_fence = False
            out.append(line)
            continue
        if fm % 2 == 1:
            in_fence = True
            out.append(line)
            continue
        if line.lstrip().startswith("- ") and ITEM_SPLIT.search(line):
            indent = line[: len(line) - len(line.lstrip())]
            parts = [p.strip() for p in ITEM_SPLIT.split(line) if p.strip()]
            if len(parts) > 1:
                for p in parts:
                    out.append(indent + p)
                changes += 1
                continue
        out.append(line)
    new_text = "\n".join(out)
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)
    new_text = new_text.replace("\r\n", "\n").replace("\r", "\n")
    return new_text, changes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--file", help="Process only this filename substring")
    args = ap.parse_args()

    files = sorted(PROMPTS_DIR.glob("*.prompt.md")) + sorted(PROMPTS_DIR.glob("templates/**/*.md"))
    total_files = 0
    total_changes = 0
    for f in files:
        if args.file and args.file not in f.name:
            continue
        if not f.is_file():
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        new_text, changes = fix_text(text)
        if changes:
            total_files += 1
            total_changes += changes
            if args.apply:
                f.write_text(new_text, encoding="utf-8", newline="")
                print(f"FIXED {f.relative_to(PROMPTS_DIR).as_posix()}: {changes}")
            else:
                print(f"WOULD FIX {f.relative_to(PROMPTS_DIR).as_posix()}: {changes}")
    print(f"\n{total_files} files, {total_changes} fixes ({'APPLIED' if args.apply else 'DRY-RUN'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
