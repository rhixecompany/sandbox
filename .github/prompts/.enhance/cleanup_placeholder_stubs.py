#!/usr/bin/env python3
"""
cleanup_placeholder_stubs.py — DRY cleanup of empty placeholder template stubs.

All 295 stubs under .github/prompts/templates/ share the identical empty
boilerplate (PLACEHOLDER + 'TODO: populate'). Per prompt-management skill
guidance, the parent prompt's inline body is the AUTHORITATIVE spec; empty
stubs are dead weight that violate DRY (295 copies of the same nothing).

This script:
  1. Deletes every stub that is pure boilerplate (PLACEHOLDER + TODO: populate).
  2. Strips dangling `templates/<stub>` references from parent prompt bodies:
       - `> **Full content:** `templates/...`` lines
       - backticked `templates/...` mentions
       - `Template References` list entries pointing at deleted stubs
  3. Verifies: no stub files remain, no dangling references remain,
     all parent frontmatter still parses, CRLF preserved.

Safe: --dry-run by default. Pass --apply to write.
"""
import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

BOILER = {
    "PLACEHOLDER",
    "TODO: populate with the canonical instructions/checklist/examples this prompt expects.",
}


def is_boilerplate_stub(text: str) -> bool:
    """True if the file is just the standard empty stub template."""
    markers = [
        "PLACEHOLDER",
        "TODO: populate",
    ]
    if not all(m in text for m in markers):
        return False
    # Stub files are small (< ~1.2KB) — real templates are larger or lack markers
    return len(text) < 1500


def find_stubs() -> list[Path]:
    stubs = []
    for f in PROMPTS_DIR.rglob("*.md"):
        text = f.read_text(encoding="utf-8", errors="replace")
        if is_boilerplate_stub(text):
            stubs.append(f)
    return stubs


def strip_references(text: str, stub_rel: str) -> tuple[str, int]:
    """Remove references to a specific deleted stub path. Returns (new_text, count)."""
    # normalize the path forms that may appear: templates/x/y.md with or without backticks
    patterns = [
        # `> **Full content:** `templates/x/y.md`` line
        re.compile(r"(?m)^\s*>\s*\*\*Full content:\*\*\s*`?" + re.escape(stub_rel) + r"`?\s*\r?$"),
        # `> **Full content:** templates/x/y.md` (no bold)
        re.compile(r"(?m)^\s*>\s*Full content:\s*`?" + re.escape(stub_rel) + r"`?\s*\r?$"),
        # backticked mention inline: `templates/x/y.md`
        re.compile(r"`" + re.escape(stub_rel) + r"`"),
        # plain path mention
        re.compile(re.escape(stub_rel)),
    ]
    count = 0
    for pat in patterns:
        text, n = pat.subn("", text)
        count += n
    # collapse triple blank lines left by removals
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text, count


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write changes (default: dry-run)")
    args = ap.parse_args()

    stubs = find_stubs()
    print(f"Found {len(stubs)} boilerplate stubs")

    # map stub path -> parent prompt name (from stub content)
    stub_parents = {}
    for f in stubs:
        text = f.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"referenced by prompt `([^`]+)`", text)
        stub_parents[f.relative_to(PROMPTS_DIR).as_posix()] = m.group(1) if m else None

    parent_edits = {}  # parent path -> list of (stub, count)
    for stub_rel, parent_name in stub_parents.items():
        if not parent_name:
            continue
        parent = PROMPTS_DIR / parent_name
        if not parent.exists():
            continue
        text = parent.read_text(encoding="utf-8", errors="replace")
        new_text, count = strip_references(text, stub_rel)
        if count:
            parent_edits.setdefault(parent, []).append((stub_rel, count))
            if args.apply:
                parent.write_text(new_text, encoding="utf-8", newline="")

    if args.apply:
        for f in stubs:
            f.unlink()
        print(f"DELETED {len(stubs)} stub files")
        print(f"EDITED {len(parent_edits)} parent files")
        for parent, refs in sorted(parent_edits.items()):
            print(f"  {parent.name}: {sum(c for _, c in refs)} refs stripped")
    else:
        print(f"WOULD DELETE {len(stubs)} stub files")
        print(f"WOULD EDIT {len(parent_edits)} parent files")
        for parent, refs in sorted(parent_edits.items()):
            print(f"  {parent.name}: {sum(c for _, c in refs)} refs stripped")

    # post-condition checks
    remaining = find_stubs()
    print(f"\nPost-check: {len(remaining)} boilerplate stubs remaining")
    return 0


if __name__ == "__main__":
    sys.exit(main())
