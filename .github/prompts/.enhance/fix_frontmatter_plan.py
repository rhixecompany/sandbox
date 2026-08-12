#!/usr/bin/env python3
"""Phase 4 (Class D) — frontmatter plan normalization.

Only the `plan` field is touched: quoted/unquoted None -> `plan: null`.
Everything else in the frontmatter (mode:, system:, name:, description:...)
is preserved byte-for-byte — no full yaml round-trip, so `mode: agent` and
`system:` semantics can never drift. Files are written LF-only.

Usage:
    python fix_frontmatter_plan.py          # dry-run report
    python fix_frontmatter_plan.py --apply  # write changes
"""
import re
import sys
from pathlib import Path

root = Path.home() / "Desktop/SandBox/.github/prompts"
APPLY = "--apply" in sys.argv

PLAN_NONE_RE = re.compile(r"^(\s*plan\s*:\s*)(['\"]?)None\2(\s*)$", re.M)

def split_frontmatter(text: str):
    """Return (frontmatter_block, rest) if the file starts with a --- block."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "".join(lines[1:i]), "".join(lines[i:])
    return None, text  # unterminated frontmatter — leave alone

def fix_block(fm: str) -> tuple[str, int]:
    """Replace plan None variants with null. Returns (new_block, count)."""
    def repl(m: re.Match):
        return f"{m.group(1)}null{m.group(3)}"
    new, n = PLAN_NONE_RE.subn(repl, fm)
    return new, n

changed = []
for f in sorted(root.glob("*.md")):
    data = f.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        continue
    fm, rest = split_frontmatter(text)
    if fm is None:
        continue
    new_fm, n = fix_block(fm)
    if n == 0:
        continue
    changed.append((f.name, n, "CRLF" if b"\r\n" in data else "LF"))
    if APPLY:
        out = "---\n" + new_fm + rest
        # normalize the whole file to LF
        out = out.replace("\r\n", "\n")
        f.write_text(out, encoding="utf-8", newline="\n")

print(f"SUMMARY: {len(changed)} file(s) with plan None -> null"
      + ("" if APPLY else " (dry-run — re-run with --apply)"))
for name, n, eol in changed:
    print(f"  {name}: {n} plan fix(es), was {eol}")
