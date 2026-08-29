#!/usr/bin/env python3
"""Add missing `trigger:` field to all prompts.

Derives the trigger from the filename (kebab-case the .prompt.md stem and prepend /).
Skips files that already have a `trigger:` field.

Usage:
  python scripts/prompt_dry_fix.py [--prompts-dir .github/prompts] [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def has_trigger(text: str) -> bool:
    """Check if frontmatter already has a trigger: field."""
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end < 0:
        return False
    fm = text[3:end]
    return bool(re.search(r"^trigger\s*:", fm, re.M))


def derive_trigger(filename: str) -> str:
    """Derive /trigger from filename: foo-bar.prompt.md -> /foo-bar"""
    stem = filename.replace(".prompt.md", "")
    # sanitize: only [a-z0-9-]
    stem = re.sub(r"[^a-z0-9-]", "-", stem.lower())
    stem = re.sub(r"-+", "-", stem).strip("-")
    return f"/{stem}"


def add_trigger(path: Path) -> str:
    """Insert `trigger: <derived>` into frontmatter. Returns the trigger used, or empty if skipped."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if has_trigger(text):
        return ""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end < 0:
        return ""
    fm = text[3:end]
    trigger = derive_trigger(path.name)
    # Insert after the description: line, or after title: if no description
    new_fm = re.sub(
        r"(description:\s*[^\n]*\n)",
        rf"\1trigger: {trigger}\n",
        fm,
        count=1,
    )
    if new_fm == fm:
        # No description found; insert after title
        new_fm = re.sub(
            r"(title:\s*[^\n]*\n)",
            rf"\1trigger: {trigger}\n",
            fm,
            count=1,
        )
    if new_fm == fm:
        # No title either; insert at end of frontmatter
        new_fm = fm.rstrip() + f"\ntrigger: {trigger}\n"
    new_text = "---" + new_fm + "\n---" + text[end + 4:]
    path.write_text(new_text, encoding="utf-8")
    return trigger


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--prompts-dir", default=".github/prompts")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    prompts_dir = Path(args.prompts_dir)
    if not prompts_dir.exists():
        print(f"Not found: {prompts_dir}", file=sys.stderr)
        return 2
    added: list[tuple[str, str]] = []
    skipped: list[str] = []
    for f in sorted(prompts_dir.glob("*.prompt.md")):
        if has_trigger(f.read_text(encoding="utf-8", errors="ignore")):
            skipped.append(f.name)
            continue
        if not args.dry_run:
            trigger = add_trigger(f)
            added.append((f.name, trigger))
        else:
            added.append((f.name, derive_trigger(f.name)))
    print(f"Triggers to add: {len(added)}")
    for name, trig in added:
        print(f"  {name} -> {trig}")
    print(f"\nSkipped (already has trigger): {len(skipped)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
