#!/usr/bin/env python3
"""
Strip known template boilerplate from SKILL.md, .prompts.md, or any markdown file.

Safe to re-run — only removes exact known bad patterns, never custom content.

Usage:
  python scripts/strip-boilerplate.py                     # Scan Hermes skills dir
  python scripts/strip-boilerplate.py --dry-run            # Preview only
  python scripts/strip-boilerplate.py --path ./docs        # Scan a folder
  python scripts/strip-boilerplate.py --path ./file.md     # Single file
  python scripts/strip-boilerplate.py --glob "*.md"        # Custom glob
  python scripts/strip-boilerplate.py --exclude "node_modules/*"
"""

import os
import re
import sys
from pathlib import Path

# ── Defaults ──────────────────────────────────────────────────────────────

DEFAULT_PATH = os.path.expanduser("~/AppData/Local/hermes/skills")
DEFAULT_GLOB = "*SKILL.md"

# ── Known boilerplate patterns ────────────────────────────────────────────

# Pattern 1: Overview with broken self-reference
# "The Skills\...\skill.md skill provides tools and workflows for managing..."
OVERVIEW_PATTERN = re.compile(
    r"## Overview\n\n\nThe .*? skill provides tools and workflows for managing .*? operations efficiently\.\n",
    re.DOTALL
)

# Pattern 2: Generic Workflow Phase 1-4
WORKFLOW_PATTERN = re.compile(
    r"## Workflow\n\n### Phase 1: Preparation\n\nSet up required environment, dependencies, and configuration for .*?\.\n\n### Phase 2: Execution\n\nRun the primary .*? operations according to the defined requirements\.\n\n### Phase 3: Verification\n\nVerify output, handle any errors, and confirm results meet expectations\.\n\n### Phase 4: Completion\n\nDocument results, clean up resources, and finalize any deliverables\.\n",
    re.DOTALL
)

# Pattern 3: Generic When to Use (exact 4-bullet format with triggers line)
WHEN_TO_USE_PATTERN = re.compile(
    r"## When to Use\n\n- When you need to perform .*? operations or tasks\n- When managing .*? infrastructure or configurations\n- When automating or debugging .*? workflows\n- \*\*Triggers\*\*: \".*?\" required for a project\n",
    re.DOTALL
)

# Pattern 4: Generic Best Practices (5 numbered items)
BEST_PRACTICES_PATTERN = re.compile(
    r"## Best Practices\n\n1\. \*\*Prepare before executing\*\*: Ensure all prerequisites and dependencies are in place\n2\. \*\*Validate inputs\*\*: Check configuration, parameters, and environment before running\n3\. \*\*Handle errors gracefully\*\*: Implement proper error handling and recovery\n4\. \*\*Document results\*\*: Keep records of what was done, what worked, and what didn't\n5\. \*\*Clean up\*\*: Remove temporary files, release resources after completion\n",
    re.DOTALL
)

# Pattern 5: Generic Verification Checklist (5 generic checkboxes)
VERIFICATION_CHECKLIST_PATTERN = re.compile(
    r"## Verification Checklist\n\n- \[ \] Prerequisites and environment are properly configured\n- \[ \] .*? operations completed successfully\n- \[ \] Output meets expected quality and requirements\n- \[ \] Any errors during execution were resolved\n- \[ \] Changes are documented and committed if applicable\n",
    re.DOTALL
)

# Pattern 6: Stray broken path ", use skills\...\skill.md" — full line
STRAY_PATH_PATTERN = re.compile(
    r', use skills\\.+?skill\.md\s*\n?',
)

PATTERNS: list[tuple[str, re.Pattern]] = [
    ("Overview (self-ref)",        OVERVIEW_PATTERN),
    ("Workflow (generic Phase 1-4)", WORKFLOW_PATTERN),
    ("When to Use (generic)",      WHEN_TO_USE_PATTERN),
    ("Best Practices (generic 5-item)", BEST_PRACTICES_PATTERN),
    ("Verification Checklist (generic)", VERIFICATION_CHECKLIST_PATTERN),
    ("Stray path ref",             STRAY_PATH_PATTERN),
]


# ── Core logic ────────────────────────────────────────────────────────────

def strip_boilerplate(text: str) -> tuple[str, list[str]]:
    """Return (cleaned_text, list_of_removed_pattern_names)."""
    removed = []
    for name, pattern in PATTERNS:
        before = text
        text = pattern.sub("", text)
        if text != before:
            removed.append(name)
    return text, removed


def collect_files(path: str, glob: str, excludes: list[str]) -> list[str]:
    """Collect files matching glob under path, respecting excludes."""
    p = Path(path)
    if p.is_file():
        return [str(p)]

    # Convert simple glob patterns (spaces) to regex for exclusion
    exclude_patterns = [re.compile(fnm.translate(ex)) for ex in excludes] if excludes else []

    files = []
    for f in p.rglob(glob):
        f_str = str(f)
        if not f.is_file():
            continue
        if any(ex.search(f_str) for ex in exclude_patterns):
            continue
        files.append(f_str)
    return sorted(files)


def scan_and_fix(
    files: list[str],
    dry_run: bool = False,
) -> dict:
    """Scan files, optionally fix."""
    stats = {
        "scanned": 0, "affected": 0, "fixed": 0,
        "errors": 0, "removals": 0,
        "details": [],
    }

    for fpath in files:
        stats["scanned"] += 1
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                original = f.read()

            cleaned, removed = strip_boilerplate(original)

            if not removed:
                continue

            stats["affected"] += 1
            stats["removals"] += len(removed)

            base = os.path.relpath(fpath)
            stats["details"].append((base, removed))

            if not dry_run:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(cleaned)
                stats["fixed"] += 1

        except Exception as e:
            stats["errors"] += 1
            stats["details"].append((os.path.relpath(fpath), [f"ERROR: {e}"]))

    return stats


def print_report(stats: dict, dry_run: bool):
    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"{'='*60}")
    print(f"  {mode} — Markdown Boilerplate Cleanup")
    print(f"{'='*60}\n")
    print(f"  Scanned:  {stats['scanned']} file(s)")
    print(f"  Affected: {stats['affected']} file(s) with boilerplate")
    if not dry_run:
        print(f"  Fixed:    {stats['fixed']} file(s)")
    print(f"  Errors:   {stats['errors']}\n")

    if not stats["details"]:
        print("  ✅ No boilerplate found.")
        return

    # Sort by severity (most patterns removed first)
    stats["details"].sort(key=lambda x: -len(x[1]))

    for fpath, removed in stats["details"]:
        tags = ", ".join(removed)
        print(f"  📄 {fpath}")
        print(f"     → removed: {tags}")

    print(f"\n  Total boilerplate removals: {stats['removals']}")
    print(f"  Total affected files: {stats['affected']}")
    print()


# ── CLI ───────────────────────────────────────────────────────────────────

def parse_args(argv: list[str]) -> dict:
    args = {
        "dry_run": "--dry-run" in argv,
        "path": None,
        "glob": None,
        "excludes": [],
    }

    i = 0
    while i < len(argv):
        if argv[i] == "--dry-run":
            args["dry_run"] = True
        elif argv[i] == "--path" and i + 1 < len(argv):
            args["path"] = argv[i + 1]
            i += 1
        elif argv[i] == "--glob" and i + 1 < len(argv):
            args["glob"] = argv[i + 1]
            i += 1
        elif argv[i] == "--exclude" and i + 1 < len(argv):
            args["excludes"].append(argv[i + 1])
            i += 1
        i += 1

    return args


# We need fnmatch for translate
import fnmatch as fnm


def main():
    opts = parse_args(sys.argv[1:])

    target_path = opts["path"] or os.environ.get("BOILERPLATE_PATH", DEFAULT_PATH)
    target_glob = opts["glob"] or os.environ.get("BOILERPLATE_GLOB", DEFAULT_GLOB)

    if not os.path.exists(target_path):
        print(f"❌ Path not found: {target_path}")
        sys.exit(1)

    files = collect_files(target_path, target_glob, opts["excludes"])

    if not files:
        print(f"  No files matching '{target_glob}' under {target_path}")
        sys.exit(0)

    stats = scan_and_fix(files, dry_run=opts["dry_run"])
    print_report(stats, dry_run=opts["dry_run"])

    if stats["errors"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
