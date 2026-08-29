#!/usr/bin/env python3
"""Add missing frontmatter fields to all prompts (DRY bulk).

Adds safe defaults for fields that are missing:
  - toolsets: [file, terminal]
  - skills: [skill:using-superpowers]
  - dependencies: []
  - formatter: markdown
  - metadata.hermes.profile: default
  - metadata.copilot: { context_size: medium, extensions: [] }
  - metadata.opencode: { command: 'opencode /<trigger>' }
  - metadata.codex: { model_override: null }
  - license: MIT

Existing values are preserved (does not overwrite).

Usage:
  python scripts/prompt_dry_bulk_fields.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# Default additions: field name -> default value (only added if missing)
DEFAULTS: dict[str, str] = {
    "toolsets": "toolsets:\n  - file\n  - terminal",
    "skills": "skills:\n  - skill:using-superpowers",
    "dependencies": "dependencies: []",
    "formatter": "formatter: markdown",
    "metadata": "metadata:\n  hermes:\n    profile: default\n    context_size: medium\n  copilot:\n    context_size: medium\n    extensions: []\n  opencode:\n    command: \"opencode /{trigger}\"\n    flags: {{}}\n  codex:\n    model_override: null",
    "license": "license: MIT",
}


def has_field(fm: str, field: str) -> bool:
    """Check if a top-level field is present in the frontmatter (line-anchored)."""
    return bool(re.search(rf"^{re.escape(field)}\s*:", fm, re.M))


def derive_trigger(filename: str) -> str:
    stem = filename.replace(".prompt.md", "")
    return "/" + re.sub(r"[^a-z0-9-]", "-", stem.lower()).strip("-")


def patch_file(path: Path) -> tuple[int, list[str]]:
    """Add missing fields to a prompt's frontmatter. Returns (count_added, list_of_added)."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return 0, []
    end = text.find("\n---", 3)
    if end < 0:
        return 0, []
    fm = text[3:end]
    body = text[end + 4:]
    trigger = derive_trigger(path.name)
    added: list[str] = []
    new_fm = fm.rstrip() + "\n"
    for field, default in DEFAULTS.items():
        if not has_field(fm, field):
            if field == "metadata" and "trigger" in fm:
                # Use actual trigger in opencode command
                default = default.replace("{trigger}", trigger)
            elif field == "metadata" and "name:" in fm:
                # Try to use the name from FM
                m = re.search(r"^name:\s*(\S+)", fm, re.M)
                if m:
                    default = default.replace("{trigger}", "/" + m.group(1))
            elif field == "metadata":
                default = default.replace("{trigger}", trigger)
            new_fm += default + "\n"
            added.append(field)
    if added:
        new_text = "---" + new_fm + "---" + body
        path.write_text(new_text, encoding="utf-8")
    return len(added), added


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--prompts-dir", default=".github/prompts")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    prompts_dir = Path(args.prompts_dir)
    if not prompts_dir.exists():
        print(f"Not found: {prompts_dir}", file=sys.stderr)
        return 2
    total_added = 0
    files_touched = 0
    for f in sorted(prompts_dir.glob("*.prompt.md")):
        n, added = patch_file(f)
        if n:
            files_touched += 1
            total_added += n
            if args.dry_run:
                print(f"  {f.name}: would add {added}")
    print(f"\n{('Would add' if args.dry_run else 'Added')} {total_added} fields across {files_touched} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
