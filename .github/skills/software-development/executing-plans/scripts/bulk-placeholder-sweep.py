#!/usr/bin/env python3
"""
bulk-placeholder-sweep.py — Reusable template for bulk pattern replacement across a codebase.

Usage (from execute_code):
    from hermes_tools import search_files
    exec(open("scripts/bulk-placeholder-sweep.py").read())

Or adapt the patterns/replacements dict for your task.
"""

# === CONFIGURATION — edit these for your task ===
INCLUDE_GLOBS = ("*.ts", "*.tsx")
EXCLUDE_DIRS = ("node_modules", ".next", ".git", ".venv", "__pycache__")
EXCLUDE_PATH_PREFIXES = ("docs/", "node_modules/")
BASE_DIR = "."  # relative to cwd

# Pattern: replacement pairs (string-based, not regex)
REPLACEMENTS = {
    "@author Adminbot": "@author Alexa",
    # Add more as needed — exact string match only
}

# Pattern: lines containing these substrings to delete entirely
DELETE_LINES_CONTAINING = {
    "Description placeholder",
    "CreatedBy: convert-scripts",
    # Add more as needed
}

# === END CONFIGURATION ===

import os
import fnmatch
import re


def find_affected_files(base_dir, include_globs, exclude_dirs, exclude_prefixes):
    """Walk the tree and find files matching include_globs."""
    affected = []
    for root, dirs, files in os.walk(base_dir):
        # Skip excluded directories in-place (prevents descending)
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        # Check if this root path starts with an excluded prefix
        rel_root = os.path.relpath(root, base_dir)
        if any(rel_root.startswith(p) for p in exclude_prefixes):
            continue

        for f in files:
            if any(fnmatch.fnmatch(f, g) for g in include_globs):
                affected.append(os.path.join(root, f))
    return affected


def apply_replacements(file_path, string_replacements, delete_lines):
    """Apply string replacements and line deletions to a single file.
    Returns (modified_count, deleted_lines_count) or raises on error.
    """
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        original = f.read()

    modified = original

    # String replacements
    replace_count = 0
    for old, new in string_replacements.items():
        if old in modified:
            modified = modified.replace(old, new)
            replace_count += 1

    # Line deletions
    delete_count = 0
    if delete_lines:
        lines = modified.splitlines(keepends=True)
        new_lines = []
        for line in lines:
            if any(sub in line for sub in delete_lines):
                delete_count += 1
            else:
                new_lines.append(line)
        modified = "".join(new_lines)

    if modified != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(modified)
        return replace_count, delete_count

    return 0, 0


def main():
    print(f"Scanning {BASE_DIR} for {INCLUDE_GLOBS}...")
    files = find_affected_files(BASE_DIR, INCLUDE_GLOBS, EXCLUDE_DIRS, EXCLUDE_PATH_PREFIXES)
    print(f"Found {len(files)} candidate files")

    total_replaced = 0
    total_deleted = 0
    touched = 0

    for fp in files:
        rc, dc = apply_replacements(fp, REPLACEMENTS, DELETE_LINES_CONTAINING)
        if rc or dc:
            touched += 1
            total_replaced += rc
            total_deleted += dc
            print(f"  MODIFIED: {fp} (replace={rc}, delete={dc})")

    print(f"\nDone. Touched {touched} files.")
    print(f"  String replacements applied: {total_replaced}")
    print(f"  Lines deleted:               {total_deleted}")

    # Print remaining occurrences for verification
    if total_replaced or total_deleted:
        print("\nRemaining occurrences to verify manually via search_files.")


if __name__ == "__main__":
    main()
