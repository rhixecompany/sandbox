#!/usr/bin/env python3
"""repair_doubled_pipes.py — Class A: strip doubled leading/trailing table pipes.

For every line in .github/prompts/*.md that starts with '|' (table row):
  - collapse leading run of 2+ pipes to a single '|'  (^||+  -> |)
  - collapse trailing run of 2+ pipes to a single '|'  (||+$ -> |)
  - drop pure-pipe lines (only '|' chars, no content) — unrecoverable artifacts

Lossless for content: only the pipe-prefix/suffix changes; cell text untouched.

Usage: python repair_doubled_pipes.py [--apply] [--files a.md b.md]
Default is dry-run (prints per-file counts). --apply writes files (LF-only).
"""
import pathlib
import re
import sys

P = pathlib.Path(__file__).resolve().parent.parent  # .github/prompts
APPLY = "--apply" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
files = [P / a for a in args] if args else sorted(P.glob("*.md"))

LEAD = re.compile(r"^\|{2,}")
TRAIL = re.compile(r"\|{2,}\s*$")
PURE = re.compile(r"^\|+\s*$")


def fix_line(line: str) -> str | None:
    """Return fixed line, or None if the line should be dropped."""
    if not line.startswith("|"):
        return line
    if PURE.match(line):
        return None
    out = LEAD.sub("|", line)
    out = TRAIL.sub("|", out)
    return out


def fix_file(path: pathlib.Path) -> tuple[int, int]:
    """Return (changed_lines, dropped_lines)."""
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return (0, 0)
    if "\r\n" in text:
        text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    changed = 0
    dropped = 0
    out = []
    for ln in lines:
        fixed = fix_line(ln)
        if fixed is None:
            dropped += 1
            continue
        if fixed != ln:
            changed += 1
        out.append(fixed)
    new_text = "\n".join(out)
    if new_text != text:
        if APPLY:
            path.write_text(new_text, encoding="utf-8", newline="\n")
        return (changed, dropped)
    return (0, 0)


def main() -> int:
    total_changed = 0
    total_dropped = 0
    affected = 0
    for p in files:
        c, d = fix_file(p)
        if c or d:
            affected += 1
            total_changed += c
            total_dropped += d
            if APPLY or d:
                print(f"{p.name}: changed={c} dropped={d}")
    print(f"---\n{'APPLIED' if APPLY else 'DRY-RUN'}: files_affected={affected} lines_changed={total_changed} lines_dropped={total_dropped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
