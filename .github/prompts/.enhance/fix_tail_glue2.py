#!/usr/bin/env python3
"""
fix_tail_glue2.py - Fourth-pass fix for glued headings that survived
passes 1-3. Handles three categories, all fence-aware:

  1. Table pipe without leading space: `## Subagents| Subagent | Role |`
     (pass 3 required a space before the pipe; these have none).
  2. camelCase glue: `## Expected OutputUpon running this prompt`
     → `## Expected Output` + `Upon running this prompt`.
     STRICT guard: both the heading prefix and the content suffix must be
     multi-word (contain a space) and the prefix must contain no code
     markers (backticks, `**`, `[`, `{`, `|`). This excludes identifiers
     like `TypeScript`/`PostgreSQL` (prefix would be `Type`/`Postgre`).
  3. Orphaned blockquote marker at end of heading: `### Phase 1: Scope and
     Risk Mapping>>` → strip trailing `>`/`>>` when the line ends with it.

Dry-run by default; --apply writes. Always LF output.
"""

import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")


def looks_like_heading(prefix: str) -> bool:
    p = prefix.strip()
    if not p or len(p) > 70:
        return False
    if re.search(r"[a-z][A-Z]", p):
        return False
    if re.search(r"[A-Z]{2,}[a-z]", p):
        return False
    if re.search(r"[.!?] [a-z]", p):
        return False
    return not any(ch in p for ch in ("**", "`", "[", "{", "|", "<", ">"))


# Suffix first words that are proper-noun / identifier fragments — never split
# before these (GitHub→Hub, SpringDoc→Doc, ComicWise→Wise, BigQuery→Query).
IDENTIFIER_TAILS = {
    "Script",
    "SQL",
    "API",
    "UI",
    "UX",
    "JS",
    "TS",
    "ID",
    "DB",
    "Doc",
    "Wise",
    "Hub",
    "Query",
}


def sentence_glue_boundaries(rest: str):
    """Yield (split_at, prefix, suffix) for sentence-boundary glue first
    (`billed?Locate`), then camelCase glue (`OutputUpon`)."""
    # sentence boundary: punctuation directly followed by a capital letter
    for bm in re.finditer(r"[?.!][A-Z]", rest):
        split_at = bm.start() + 1
        yield split_at, rest[:split_at], rest[split_at:]
    # camelCase boundary
    for bm in re.finditer(r"[a-z][A-Z]", rest):
        split_at = bm.start() + 1
        yield split_at, rest[:split_at], rest[split_at:]


def fix_line(line: str) -> list[str] | None:
    m = re.match(r"^(#{2,4}) (.+)$", line)
    if not m:
        return None
    marker, rest = m.group(1), m.group(2)

    # --- 1. Table pipe (no leading space): `Heading| A | B |` ---
    tm = re.match(r"^(.+?)\| ", rest)
    if tm and "|" not in tm.group(1) and looks_like_heading(tm.group(1)):
        heading = (marker + " " + tm.group(1)).strip()
        content = rest[tm.end() :]
        if heading and content:
            return [heading, "", "| " + content.lstrip("| ")]

    # --- 2. camelCase / sentence-boundary glue ---
    # multi-word heading + multi-word content; prefer sentence boundaries
    # (`billed?Locate`) then camelCase (`OutputUpon`).
    for _, prefix, suffix in sentence_glue_boundaries(rest):
        # heading prefix: multi-word, heading-like
        if " " not in prefix or not looks_like_heading(prefix):
            continue
        # content suffix: multi-word sentence (contains a space), first word >= 3 chars
        sw_raw = suffix.split()[0] if suffix.split() else ""
        if " " not in suffix or len(sw_raw) < 3:
            continue
        sw = re.sub(r"[^A-Za-z]", "", sw_raw)  # strip punctuation for checks
        # suffix first word must be prose, not an identifier fragment:
        # reject acronym-led (`SQL-Specific`), punctuation-led (`API.md`),
        # or kebab/snake identifiers (`foo-bar`, `foo_bar`)
        if re.match(r"^[A-Z]{2,}", sw) or re.search(r"[-_./\\]", sw):
            continue
        # suffix must not start with a known identifier tail
        if sw in IDENTIFIER_TAILS:
            continue
        heading = (marker + " " + prefix).strip()
        if heading and suffix:
            return [heading, "", suffix]

    # --- 3. Orphaned blockquote at end: `Heading>>` ---
    if re.search(r">+$", rest) and looks_like_heading(rest.rstrip(">")):
        heading = (marker + " " + rest.rstrip(">")).strip()
        if heading:
            return [heading]

    return None


def fix_text(text: str) -> tuple[str, int]:
    changes = 0
    new_lines = []
    in_fence = False
    for raw_line in text.split("\n"):
        line = raw_line.rstrip("\r\n")
        fence_markers = line.count("```") + line.count("~~~")
        if in_fence:
            if fence_markers % 2 == 1:
                in_fence = False
            new_lines.append(line)
            continue
        if not line.startswith(("## ", "### ", "#### ")):
            if fence_markers % 2 == 1:
                in_fence = True
            new_lines.append(line)
            continue
        fixed = fix_line(line)
        if fixed is not None:
            new_lines.extend(fixed)
            changes += 1
            if fixed[-1].count("```") % 2 == 1:
                in_fence = True
            continue
        if fence_markers % 2 == 1:
            in_fence = True
        new_lines.append(line)
    new_text = "\n".join(new_lines)
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
        raw = f.read_bytes()
        text = raw.decode("utf-8", errors="replace")
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
