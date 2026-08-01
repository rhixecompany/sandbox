#!/usr/bin/env python3
"""
fix_residual_glue.py — Second-pass fix for glued headings missed by
fix_glued_headings.py (dictionary-based). Handles structural glue:

  1. `## Heading> quote...`         (blockquote glued; may contain `- ` later)
  2. `## Heading{...}`              (brace content glued)
  3. `## Heading- [ ] task...`      (task list glued to heading)
  4. `## Heading- **bold**...`      (bold content glued)
  5. `## Heading- plain text...`    (dash + space, content glued)

Splits into heading + blank line + content. Preserves CRLF. Dry-run default.

Word-hyphen headings (`Cross-Cutting`, `0-24h`) are NOT glue and are skipped.
Blockquote is detected BEFORE dash because quote content frequently contains
`- ` items — matching dash first would split at the wrong place.
"""

import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

# Word-hyphen guard: any letter-hyphen-letter inside the heading candidate.
WORD_HYPHEN = re.compile(r"[A-Za-z]-[A-Za-z]")
# Numeric-hyphen guard: digit-hyphen-digit (e.g. "0-24h", "5-10").
NUM_HYPHEN = re.compile(r"\d-\d")


def split_blockquote_content(rest: str) -> list[str]:
    """Turn '> A> B' into ['> A', '> B'] preserving blockquote structure."""
    parts = [p.strip() for p in re.split(r"(?=> )", rest) if p.strip()]
    out = []
    for p in parts:
        if p.startswith("> "):
            out.append(p)
        elif p.startswith(">"):
            out.append("> " + p[1:].strip())
        else:
            out.append(p)
    return out


def fix_line(line: str) -> list[str] | None:
    """Fix one glued heading line. Returns list of replacement lines or None."""
    # --- 1. Blockquote glue: `Heading> content` ---
    m2 = re.match(r"^(#{2,4}) ([^\n]+?)> ?(?=\S)", line)
    if m2:
        heading = m2.group(1) + " " + m2.group(2).strip()
        rest = line[m2.end() :]
        # If the text right after > looks like content (not another heading word),
        # and the heading has no internal `>` mid-word, treat as glue.
        if heading and not re.search(r"[a-z]>[a-z]", heading) and len(rest) > 3:
            return [heading, "", *split_blockquote_content("> " + rest)]

    # --- 2. Tight dash before task/bold: `Heading- [ ]` / `Heading- **` ---
    m = re.match(r"^(#{2,4}) ([^\n]+?)-(?= \[|\*\*)", line)
    if m and not WORD_HYPHEN.search(m.group(2)) and not NUM_HYPHEN.search(m.group(2)):
        heading = (m.group(1) + " " + m.group(2)).strip()
        content = "- " + line[m.end() :].lstrip()
        if heading and content.strip() != "-":
            return [heading, "", content]

    # --- 3. Dash + space: `Heading- content` ---
    m = re.match(r"^(#{2,4}) ([^\n]+?)- (?=\S)", line)
    if m and not WORD_HYPHEN.search(m.group(2)) and not NUM_HYPHEN.search(m.group(2)):
        heading = (m.group(1) + " " + m.group(2)).strip()
        content = "- " + line[m.end() :].lstrip()
        if heading and content.strip() != "-":
            return [heading, "", content]

    # --- 4. Brace glue: `Heading{content}` ---
    # Only when { is IMMEDIATELY after the heading (no content markers before it).
    m = re.match(r"^(#{2,4}) ([^\n]+?)\{(?=\S)", line)
    if m:
        heading = (m.group(1) + " " + m.group(2)).strip()
        content = line[m.end() :].rstrip("}")
        # guard: heading must not contain content markers (dash-space, bold, quote)
        if (
            heading
            and content
            and not heading.endswith(("{", "-"))
            and "- " not in heading
            and "**" not in heading
            and "> " not in heading
        ):
            return [heading, "", content]

    return None


def fix_text(text: str) -> tuple[str, int]:
    """Apply all residual glue fixes. Returns (new_text, total_changes)."""
    changes = 0
    new_lines = []
    for raw_line in text.split("\n"):
        line = raw_line.rstrip("\r\n")
        if line.startswith(("## ", "### ", "#### ")):
            fixed = fix_line(line)
            if fixed is not None:
                new_lines.extend(fixed)
                changes += 1
                continue
        new_lines.append(line)

    new_text = "\n".join(new_lines)
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)
    # Normalize to LF (matches .gitattributes `*.md text eol=lf`).
    # Never re-apply CRLF on top of existing CRLF — that double-encodes.
    new_text = new_text.replace("\r\n", "\n").replace("\r", "\n")
    return new_text, changes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--file", help="Process only this filename substring")
    args = ap.parse_args()

    files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    total_files = 0
    total_changes = 0
    for f in files:
        if args.file and args.file not in f.name:
            continue
        raw = f.read_bytes()
        text = raw.decode("utf-8", errors="replace")
        new_text, changes = fix_text(text)
        if changes:
            total_files += 1
            total_changes += changes
            if args.apply:
                f.write_text(new_text, encoding="utf-8", newline="")
                print(f"FIXED {f.name}: {changes}")
            else:
                print(f"WOULD FIX {f.name}: {changes}")
    print(f"\n{total_files} files, {total_changes} fixes ({'APPLIED' if args.apply else 'DRY-RUN'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
