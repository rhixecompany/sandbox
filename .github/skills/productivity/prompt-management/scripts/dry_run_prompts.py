#!/usr/bin/env python3
"""
Dry-run prompt execution - smoke test that verifies prompts can be loaded
and their dependencies resolve without actually running the full execution.
"""
import os
import sys
import yaml
from pathlib import Path
import subprocess

def check_profile_exists(profile_name: str) -> bool:
    """Check if a Hermes profile exists."""
    try:
        result = subprocess.run(
            ["hermes", "profile", "show", profile_name],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0
    except Exception:
        return False

def check_toolsets_available(toolsets: list) -> list[str]:
    """Check which toolsets are available."""
    # This is a simplified check - in reality you'd query Hermes
    known_toolsets = {
        "web", "browser", "terminal", "file", "code_execution",
        "vision", "image_gen", "moa", "tts", "skills", "todo",
        "memory", "context_engine", "session_search", "clarify",
        "delegation", "cronjob", "search"
    }
    missing = [t for t in toolsets if t if t not in known_toolsets]
    return missing

def dry_run_prompt(prompt_path: Path) -> list[str]:
    errors = []
    try:
        content = prompt_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Failed to read {prompt_path}: {e}"]

    if not content.startswith("---"):
        return [f"{prompt_path}: Missing front-matter"]

    parts = content.split("---", 2)
    if len(parts) < 3:
        return [f"{prompt_path}: Malformed front-matter"]

    fm_text = parts[1].strip()
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return [f"{prompt_path}: Invalid YAML: {e}"]

    # Check profile
    profile = fm.get("profile", "default")
    if not check_profile_exists(profile):
        errors.append(f"{prompt_path}: Profile '{profile}' not found")

    # Check toolsets
    toolsets = fm.get("toolsets", [])
    if toolsets:
        missing = check_toolsets_available(toolsets)
        if missing:
            errors.append(f"{prompt_path}: Unknown toolsets: {missing}")

    # Check referenced files exist
    references = fm.get("references", [])
    for ref in references:
        ref_path = Path(ref)
        if not ref_path.exists():
            errors.append(f"{prompt_path}: Referenced file '{ref}' does not exist")

    # Check script files exist
    scripts = fm.get("scripts", [])
    for script in scripts:
        script_path = Path(script)
        if not script_path.exists():
            errors.append(f"{prompt_path}: Script file '{script}' does not exist")

    return errors


def main():
    prompts_dir = Path("prompts")
    if not prompts_dir.exists():
        print("No prompts/ directory found, skipping.")
        return 0

    all_errors = []
    for md_file in prompts_dir.rglob("*.md"):
        all_errors.extend(dry_run_prompt(md_file))

    if all_errors:
        print("DRY-RUN FAILED:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print("All prompts passed dry-run validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())