#!/usr/bin/env python3
"""
Sync prompts from an external library.
Run on schedule (nightly) to import new/updated prompts.
"""
import os
import sys
import json
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
from urllib.request import urlopen
from urllib.error import URLError

LIBRARY_URL = os.getenv("PROMPT_LIBRARY_URL")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not LIBRARY_URL:
    print("PROMPT_LIBRARY_URL not set, skipping sync.")
    sys.exit(0)

PROMPTS_DIR = Path("prompts")
TEMPLATES_DIR = Path("templates/prompt_template.md")

def fetch_library_index() -> list[dict]:
    """Fetch the index of available prompts from the library."""
    try:
        req = urlopen(LIBRARY_URL + "/index.json", timeout=30)
        return json.load(req)
    except URLError as e:
        print(f"Failed to fetch library index: {e}")
        return []

def fetch_prompt(url: str) -> str | None:
    """Fetch a single prompt markdown file."""
    try:
        req = urlopen(url, timeout=30)
        return req.read().decode("utf-8")
    except URLError as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def adapt_prompt(content: str, source_meta: dict) -> str:
    """Adapt external prompt to our template."""
    # Ensure front-matter has required fields
    if not content.startswith("---"):
        # Wrap in our template
        fm = {
            "name": source_meta.get("name", "imported-prompt"),
            "description": source_meta.get("description", "Imported from library"),
            "version": source_meta.get("version", "1.0.0"),
            "source": {
                "library": source_meta.get("library", "unknown"),
                "url": source_meta.get("url", ""),
                "version": source_meta.get("version", ""),
                "imported_at": datetime.now().strftime("%Y-%m-%d")
            }
        }
        import yaml
        fm_text = yaml.dump(fm, sort_keys=False)
        content = f"---\n{fm_text}---\n\n{content}"
    return content

def save_prompt(name: str, content: str) -> Path:
    """Save prompt to prompts/ directory."""
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = PROMPTS_DIR / f"{name}.md"
    filepath.write_text(content, encoding="utf-8")
    return filepath

def commit_changes(changed_files: list[Path]) -> bool:
    """Commit new/updated prompts."""
    if not changed_files:
        return False
    try:
        subprocess.run(["git", "add"] + [str(f) for f in changed_files], check=True)
        msg = f"sync: update {len(changed_files)} prompts from library ({datetime.now().strftime('%Y-%m-%d')})"
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git commit failed: {e}")
        return False

def main():
    if not TEMPLATES_DIR.exists():
        print("Template not found, cannot adapt prompts.")
        return 1

    print(f"Syncing from {LIBRARY_URL}...")
    index = fetch_library_index()
    if not index:
        print("No prompts in library index.")
        return 0

    changed = []
    for item in index:
        url = item.get("url")
        if not url:
            continue
        content = fetch_prompt(url)
        if not content:
            continue
        adapted = adapt_prompt(content, item)
        name = item.get("name", "unknown").replace(" ", "-").lower()
        filepath = save_prompt(name, adapted)
        changed.append(filepath)
        print(f"  Imported: {name}")

    if changed:
        if commit_changes(changed):
            print(f"Committed {len(changed)} prompts.")
        else:
            print("Commit failed, changes staged locally.")
    else:
        print("No new prompts to import.")

    return 0

if __name__ == "__main__":
    sys.exit(main())