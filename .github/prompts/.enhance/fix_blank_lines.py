#!/usr/bin/env python3
"""fix_blank_lines.py — normalize blank lines around headings/fences/lists.

Fixes markdownlint MD022 (blanks around headings), MD031 (blanks around
fences), MD032 (blanks around lists) on files that currently have errors,
after the Class B split pass. Conservative: only inserts blank lines, never
removes content; only processes files flagged by markdownlint.

Usage: python fix_blank_lines.py [--apply] [--files a.md ...]
Default: dry-run.
"""
import pathlib
import re
import subprocess
import sys

P = pathlib.Path(__file__).resolve().parent.parent  # .github/prompts
APPLY = "--apply" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]

HEADING = re.compile(r"^#{1,6}\s+\S")
FENCE_OPEN = re.compile(r"^\s*`{3,}\S*$")
FENCE_CLOSE = re.compile(r"^\s*`{3,}\s*$")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")


def find_error_files() -> list[pathlib.Path]:
    if args:
        return [P / a for a in args]
    # run markdownlint and collect files with MD022/MD031/MD032
    r = subprocess.run(
        ["npx", "markdownlint-cli2", ".github/prompts/**/*.md"],
        cwd=P.parent, capture_output=True, text=True
    )
    files = set()
    for line in r.stdout.splitlines():
        if "error MD022" in line or "error MD031" in line or "error MD032" in line:
            f = line.split(":")[0].strip()
            if f.endswith(".md"):
                files.add(P / f)
    return sorted(files)


def fix_file(path: pathlib.Path) -> int:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    if "\r\n" in text:
        text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    out = []
    n = len(lines)
    changed = 0
    for i, ln in enumerate(lines):
        out.append(ln)
        nxt = lines[i + 1] if i + 1 < n else ""
        # MD022: heading followed by blank (unless EOF or already blank)
        if HEADING.match(ln) and nxt.strip() != "":
            out.append("")
            changed += 1
        # MD031: fence opener followed by blank; fence closer preceded by blank
        elif FENCE_OPEN.match(ln) and nxt.strip() != "":
            out.append("")
            changed += 1
        elif FENCE_CLOSE.match(ln):
            # blank before closer already ensured by previous iteration; ensure
            # closer is followed by blank (unless EOF)
            if nxt.strip() != "":
                out.append("")
                changed += 1
        # MD032: list item followed by blank when next is a heading/block start
        elif LIST_ITEM.match(ln) and nxt.strip() != "":
            nxt2 = lines[i + 2] if i + 2 < n else ""
            if HEADING.match(nxt) or (FENCE_OPEN.match(nxt) and nxt2.strip() != ""):
                out.append("")
                changed += 1
    new_text = "\n".join(out)
    if new_text != text and APPLY:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return changed


def main() -> int:
    files = find_error_files()
    total = 0
    for p in files:
        c = fix_file(p)
        if c:
            total += c
            if APPLY:
                print(f"{p.name}: +{c} blank lines")
    print(f"---\n{'APPLIED' if APPLY else 'DRY-RUN'}: files={len(files)} blank_lines_added={total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
