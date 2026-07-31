#!/usr/bin/env python3
"""
fix_tail_glue.py — Third-pass fix for glued headings that survived the
dictionary (pass 1) and structural marker (pass 2) fixers.

Handles heading lines where content is glued with unambiguous markers:

  1. Table pipe:      `## Subagents| Subagent | Role |`
  2. Code fence:      `## Installation```bash ...`
  3. Numbered list:   `## Task1. Take a deep breath` (heading + `N. ` content)

STRICT guards against false positives (learned from dry-run feedback):
  - Never split a legitimate numbered heading like `## 10. Provider Stack` —
    the numbered rule only fires when the heading prefix contains NO digits
    (e.g. `Task1. item` where prefix=`Task`).
  - Bold-content glue (`## File Summary**Description**: ...`) is NOT handled
    here: the `**` split proved unreliable across the library (bullet
    markers, inline bold in headings). Left for manual review.
  - Table rule rejects prefixes containing `**`, backticks, `[`, `{`, `|`.
  - Code-fence rule requires the prefix to be a plausible heading and the
    fence to start a block (` ``` ` with following non-space or lang).

Output: heading + blank line + content. Always LF (matches .gitattributes).
Dry-run by default; --apply writes.
"""
import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")


def looks_like_heading(prefix: str, forbid_bad_chars: bool = True) -> bool:
    """Heuristic: the extracted heading prefix must look like a real heading."""
    p = prefix.strip()
    if not p or len(p) > 70:
        return False
    # must not end mid-word glued to content (camelCase)
    if re.search(r"[a-z][A-Z]", p):
        return False
    # uppercase acronym/word glued directly to a lowercase word
    # (e.g. `WORKFLOWYou will follow...`) — that's content, not a heading
    if re.search(r"[A-Z]{2,}[a-z]", p):
        return False
    # must not contain sentence-ending punctuation mid-way
    if re.search(r"[.!?] [a-z]", p):
        return False
    if forbid_bad_chars:
        # characters that indicate content (not a heading) leaked into prefix
        if any(ch in p for ch in ("**", "`", "[", "{", "|")):
            return False
    return True


def fix_line(line: str) -> list[str] | None:
    m = re.match(r"^(#{2,4}) (.+)$", line)
    if not m:
        return None
    marker, rest = m.group(1), m.group(2)

    # --- 1. Table pipe glue: `Heading| A | B |` ---
    # A table row starts with `| ` (pipe + space) or `||` for empty first cell.
    tm = re.match(r"^(.+?)(?:\| \|| \| |\|\| )", rest)
    if tm and "|" not in tm.group(1) and looks_like_heading(tm.group(1)):
        heading = (marker + " " + tm.group(1)).strip()
        content = rest[tm.end():]
        if heading and content:
            return [heading, "", "| " + content.lstrip("| ")]

    # --- 2. Code fence glue: `Heading```lang ...` ---
    cm = re.match(r"^(.+?)```", rest)
    if cm and looks_like_heading(cm.group(1), forbid_bad_chars=False) and len(cm.group(1)) < 60:
        heading = (marker + " " + cm.group(1)).strip()
        content = rest[cm.end():]
        if heading and content:
            return [heading, "", "```" + content]

    # --- 3. Numbered list glue: `Heading1. item` (prefix has NO digits) ---
    # Regex: prefix must not contain digits; then `N.` where N<=20.
    nm = re.match(r"^([^\d]+?)(\d{1,2})\.(?= |\*\*)", rest)
    if nm and int(nm.group(2)) <= 20 and looks_like_heading(nm.group(1)):
        heading = (marker + " " + nm.group(1)).strip()
        content = rest[nm.start(2):]
        if heading and content:
            return [heading, "", content]

    return None


def fix_text(text: str) -> tuple[str, int]:
    changes = 0
    new_lines = []
    in_fence = False
    for raw_line in text.split("\n"):
        line = raw_line.rstrip("\r\n")
        # A fence marker can appear anywhere in a line (e.g. `**Actions:**```terminal(...`).
        # While inside a fence, never touch heading-looking lines (e.g. `grep -c '^## '`).
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
            # If the extracted content opens a fence (e.g. `## X```bash ...`),
            # the remainder of the block is code — mark fence open.
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
