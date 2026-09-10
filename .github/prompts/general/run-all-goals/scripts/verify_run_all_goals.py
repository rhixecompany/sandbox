#!/usr/bin/env python3
"""Verified: checks output file exists; verifies no placeholder markers; validates all artifacts."""
import os, sys, yaml

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_FILE = os.path.join(BASE, "run-all-goals.prompt.md")
PLAN_FILE = os.path.join(".hermes/plans/run-all-goals-implementation.md")

def verify_prompt():
    errors = []
    if not os.path.exists(PROMPT_FILE):
        errors.append("Output prompt missing")
        return errors
    with open(PROMPT_FILE) as f:
        data = f.read()
    for bad in ["FIXME:", "TODO:", "PLACEHOLDER", "[..."]:
        if bad in data:
            errors.append(f"Unexpected marker: {bad}")
    if not data.startswith("---"):
        errors.append("Missing YAML frontmatter")
    else:
        try:
            parts = data.split("---")
            if len(parts) >= 3:
                yaml.safe_load(parts[1])
        except Exception as e:
            errors.append(f"YAML parse error: {e}")
    for section in ["# Goal", "## Context", "## Subgoals", "## Phases", "## Verification Checklist"]:
        if section not in data:
            errors.append(f"Missing section: {section}")
    return errors

def verify_plan():
    errors = []
    if not os.path.exists(PLAN_FILE):
        errors.append("Implementation plan missing")
        return errors
    with open(PLAN_FILE) as f:
        data = f.read()
    for section in ["## Goals", "## Phases", "## Verification Checklist"]:
        if section not in data:
            errors.append(f"Plan missing section: {section}")
    return errors

def verify_shared_templates():
    errors = []
    shared_dir = os.path.join(BASE, "templates/_shared")
    required = ["rules-core.md", "deps-core.md", "section-skeleton.md", "skills-table-core.md", "verification-checklist.md", "best-practices.md"]
    for fname in required:
        path = os.path.join(shared_dir, fname)
        if not os.path.exists(path):
            errors.append(f"Missing shared template: {fname}")
    return errors

def verify_references():
    errors = []
    ref_dir = os.path.join(BASE, "references")
    required = ["prompt-workflow.md", "session-reporting.md", "batch-skill-injection.md", "workspace-references.md"]
    for fname in required:
        path = os.path.join(ref_dir, fname)
        if not os.path.exists(path):
            errors.append(f"Missing reference: {fname}")
    return errors

def verify_scripts():
    errors = []
    scripts_dir = os.path.join(BASE, "scripts")
    required = ["verify_run_all_goals.py", "test_run_all_goals.py"]
    for fname in required:
        path = os.path.join(scripts_dir, fname)
        if not os.path.exists(path):
            errors.append(f"Missing script: {fname}")
    return errors

def main():
    all_errors = []
    print("=== Run All Goals Verification ===\n")
    checks = [
        ("Main Prompt", verify_prompt),
        ("Implementation Plan", verify_plan),
        ("Shared Templates", verify_shared_templates),
        ("References", verify_references),
        ("Scripts", verify_scripts),
    ]
    for name, check_fn in checks:
        errors = check_fn()
        if errors:
            print("\u274c " + name + ": " + str(len(errors)) + " issues")
            for e in errors:
                print("   - " + e)
            all_errors.extend(errors)
        else:
            print("\u2705 " + name + ": PASS")
    print()
    if all_errors:
        print("\u274c VERIFICATION FAILED: " + str(len(all_errors)) + " issues")
        sys.exit(1)
    else:
        print("\u2705 ALL VERIFICATIONS PASSED")
        sys.exit(0)

if __name__ == "__main__":
    main()
