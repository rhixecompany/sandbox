#!/usr/bin/env python3
"""
Generate a changelog entry for prompt changes.
Run on push to main to update CHANGELOG.md.
"""
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

CHANGELOG = Path("CHANGELOG.md")
PROMPTS_DIR = Path("prompts")

def get_git_changes() -> list[str]:
    """Get list of changed prompt files since last tag."""
    try:
        # Get the last tag
        last_tag = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True, text=True, timeout=10
        ).stdout.strip()
    except Exception:
        last_tag = ""

    if last_tag:
        range_spec = f"{last_tag}..HEAD"
    else:
        range_spec = "HEAD"

    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", range_spec, "--", "prompts/"],
            capture_output=True, text=True, timeout=10
        )
        files = [f for f in result.stdout.strip().split("\n") if f]
        return files
    except Exception:
        return []

def parse_prompt_version(filepath: Path) -> str:
    """Extract version from prompt front-matter."""
    try:
        content = filepath.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                import yaml
                fm = yaml.safe_load(parts[1].strip())
                return fm.get("version", "0.0.0")
    except Exception:
        pass
    return "0.0.0"

def main():
    if not PROMPTS_DIR.exists():
        print("No prompts/ directory.")
        return 0

    changed = get_git_changes()
    if not changed:
        print("No prompt changes detected.")
        return 0

    today = datetime.now().strftime("%Y-%m-%d")
    entry_lines = [f"## [{today}]", ""]

    for f in changed:
        version = parse_prompt_version(Path(f))
        entry_lines.append(f"- **{f}** (v{version}) — Updated")

    entry_lines.append("")

    # Prepend to CHANGELOG.md
    if CHANGELOG.exists():
        existing = CHANGELOG.read_text(encoding="utf-8")
        new_content = "\n".join(entry_lines) + "\n" + existing
    else:
        new_content = "# Changelog\n\n" + "\n".join(entry_lines) + "\n"

    CHANGELOG.write_text(new_content, encoding="utf-8")
    print(f"Updated {CHANGELOG} with {len(changed)} prompt changes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())