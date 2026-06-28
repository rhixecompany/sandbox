#!/usr/bin/env python3
"""
Validate prompt front-matter YAML.
Ensures required fields exist and have correct types.
"""
import os
import sys
import yaml
from pathlib import Path

REQUIRED_FIELDS = ["name", "description", "version"]
OPTIONAL_FIELDS = ["permissions", "toolsets", "references"]

def validate_prompt_file(filepath: Path) -> list[str]:
    errors = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Failed to read {filepath}: {e}"]

    # Extract front-matter (between --- delimiters)
    if not content.startswith("---"):
        return [f"{filepath}: Missing front-matter (--- delimiter)"]

    parts = content.split("---", 2)
    if len(parts) < 3:
        return [f"{filepath}: Malformed front-matter"]

    fm_text = parts[1].strip()
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return [f"{filepath}: Invalid YAML in front-matter: {e}"]

    if not isinstance(fm, dict):
        return [f"{filepath}: Front-matter must be a mapping"]

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"{filepath}: Missing required field '{field}'")
        elif not fm[field]:
            errors.append(f"{filepath}: Required field '{field}' is empty")

    # Check optional fields types
    if "permissions" in fm and not isinstance(fm["permissions"], list):
        errors.append(f"{filepath}: 'permissions' must be a list")
    if "toolsets" in fm and not isinstance(fm["toolsets"], list):
        errors.append(f"{filepath}: 'toolsets' must be a list")
    if "references" in fm and not isinstance(fm["references"], list):
        errors.append(f"{filepath}: 'references' must be a list")

    # Validate version format (semver-ish)
    if "version" in fm:
        version = fm["version"]
        if not isinstance(version, str) or not version[0].isdigit():
            errors.append(f"{filepath}: 'version' should be a string starting with a digit (e.g., '1.0.0')")

    return errors


def main():
    prompts_dir = Path("prompts")
    if not prompts_dir.exists():
        print("No prompts/ directory found, skipping.")
        return 0

    all_errors = []
    for md_file in prompts_dir.rglob("*.md"):
        all_errors.extend(validate_prompt_file(md_file))

    if all_errors:
        print("VALIDATION FAILED:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print("All prompt front-matter valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())