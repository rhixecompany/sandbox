#!/usr/bin/env python3
"""split_glued_headings.py — Class B: split headings glued to body content.

CONSERVATIVE auto-split — only provably-safe structural boundaries, zero
content fabrication:
  1. Fence glue:  `### Phase 2: ...   ```bash   # ...`  -> heading + fence line
  2. Table glue:  `## Access Patterns Analysis| # | ...` -> heading + table row
                  (only when `|` follows heading with NO space)
  3. 2+ space:    `## 🔍 Executive Summary   [Brief ...]` -> heading + body
  4. Placeholder: `## Design Philosophy[Explain ...]`    -> heading + placeholder
                  (only when `[` follows heading with NO space)

Everything ambiguous (camelCase glue like `MODESVerify`, bold-embedded
headings, numbered `### Step 1: **...**` etc.) is REPORTED for manual review —
never auto-split.

Usage: python split_glued_headings.py [--apply] [--files a.md ...]
Default is dry-run. --apply writes LF-only.
"""
import pathlib
import re
import sys

P = pathlib.Path(__file__).resolve().parent.parent  # .github/prompts
APPLY = "--apply" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
files = [P / a for a in args] if args else sorted(P.glob("*.md"))

HEAD = re.compile(r"^(#{2,4})\s+(.+)$")


def safe_split(line: str) -> tuple[str, str] | None:
    """Return (heading_line, body_line) only for provably-safe boundaries."""
    m = HEAD.match(line)
    if not m:
        return None
    hashes, body = m.group(1), m.group(2)

    # 1. Fence glue: fence opener appears after heading (2+ spaces or glued)
    fm = re.search(r"(`{3,})", body)
    if fm:
        head = body[: fm.start()].rstrip()
        if head and len(head) <= 90:
            return f"{hashes} {head}", body[fm.start():]
        return None

    # 2. Table glue: `|` right after heading, no space
    tm = re.match(r"^(.+?)(\|.*)$", body)
    if tm and len(tm.group(1)) <= 90 and not body.startswith("|"):
        head = tm.group(1).rstrip()
        # heading must not contain `|` already and must not end with `:`
        if "|" not in head and not head.endswith(":"):
            return f"{hashes} {head}", tm.group(2)
        return None

    # 3. 2+ space boundary: heading then body sentence
    sm = re.match(r"^(.+?)\s{2,}(\S.*)$", body)
    if sm:
        head = sm.group(1).rstrip()
        rest = sm.group(2)
        # heading must be short and not contain markdown inline markers
        if len(head) <= 90 and "`" not in head and "**" not in head:
            return f"{hashes} {head}", rest
        return None

    # 4. Placeholder glue: `[` right after heading, no space
    pm = re.match(r"^(.+?)(\[.*)$", body)
    if pm:
        head = pm.group(1).rstrip()
        if len(head) <= 90 and not head.endswith((":", "]", ")")) and "`" not in head and "**" not in head:
            return f"{hashes} {head}", pm.group(2)
        return None

    return None


def is_ambiguous(line: str) -> bool:
    """Detect camelCase glue / bold-embedded glue that needs manual review."""
    m = HEAD.match(line)
    if not m:
        return False
    body = m.group(2)
    # camelCase glue: lowercase->uppercase mid-word (e.g. MODESVerify, TaskApply)
    if re.search(r"[a-z][A-Z][a-z]", body):
        return True
    # glued sentence: heading followed directly by capital-letter body
    # e.g. `## Labels`epic``, `## When to Use` or `
    if re.match(r"^[^`\s]+`[^`]*`[,.]?\s", body):
        return True
    return False


def fix_file(path: pathlib.Path) -> tuple[int, list[str]]:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return (0, [])
    if "\r\n" in text:
        text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    changed = 0
    manual = []
    out = []
    for ln in lines:
        if HEAD.match(ln):
            split = safe_split(ln)
            if split:
                head, rest = split
                out.append(head)
                out.append(rest)
                changed += 1
                continue
            if is_ambiguous(ln):
                manual.append(ln[:140])
        out.append(ln)
    new_text = "\n".join(out)
    if new_text != text:
        if APPLY:
            path.write_text(new_text, encoding="utf-8", newline="\n")
        return (changed, manual)
    return (0, manual)


def main() -> int:
    total_changed = 0
    total_manual = 0
    affected = 0
    manual_files = set()
    for p in files:
        c, manual = fix_file(p)
        if c:
            affected += 1
            total_changed += c
            if APPLY:
                print(f"{p.name}: split={c}")
        if manual:
            total_manual += len(manual)
            manual_files.add(p.name)
            if not APPLY:
                for mline in manual:
                    print(f"  MANUAL {p.name}: {mline}")
    print(f"---\n{'APPLIED' if APPLY else 'DRY-RUN'}: files_affected={affected} splits={total_changed} manual_review={total_manual} manual_files={len(manual_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
