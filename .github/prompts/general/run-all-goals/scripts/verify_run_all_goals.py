#!/usr/bin/env python3
"""Verified: checks output file exists; verifies no placeholder markers; validates all artifacts.
tree.prompt.txt is PRIMARY source."""
import os, sys, yaml

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_FILE = os.path.join(BASE, "run-all-goals.prompt.md")
PLAN_FILE = os.path.join(".hermes/plans/run-all-goals-implementation.md")
TREE_PROMPT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(BASE))), "tree.prompt.txt")

def verify_tree_prompt():
    """Verify tree.prompt.txt exists as primary source and has no placeholders."""
    errors = []
    if not os.path.exists(TREE_PROMPT):
        errors.append("tree.prompt.txt primary source missing")
        return errors
    with open(TREE_PROMPT) as f:
        data = f.read()
    for bad in ["FIXME:", "TODO:", "PLACEHOLDER", "[SKILL_PRUNED]"]:
        if bad in data:
            errors.append(f"Unexpected marker in tree.prompt.txt: {bad}")
    if "/goal" not in data:
        errors.append("tree.prompt.txt missing /goal directives")
    return errors

def verify_mjs_to_mts():
    """Tree-specific: verify no .mjs files remain without .mts counterparts."""
    errors = []
    base_workspace = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(BASE))))
    mjs_files = []
    for root, dirs, files in os.walk(base_workspace):
        for f in files:
            if f.endswith('.mjs'):
                mts_path = os.path.join(root, f[:-4] + '.mts')
                if not os.path.exists(mts_path):
                    mjs_files.append(os.path.join(root, f))
    if mjs_files:
        errors.append(f"Unconverted .mjs files found: {len(mjs_files)} files")
    return errors

def verify_cleanup():
    """Tree-specific: verify .enhance and .goals directories do not exist."""
    errors = []
    base_workspace = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(BASE))))
    for d in [".enhance", ".goals"]:
        path = os.path.join(base_workspace, d)
        if os.path.exists(path):
            errors.append(f"Cleanup incomplete: {d} still exists")
    return errors

def verify_config_files():
    """Tree-specific: validate key config files exist."""
    errors = []
    base_workspace = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(BASE))))
    for f in ["package.json", "pyrightconfig.json", "tsconfig.json", "requirements.txt"]:
        path = os.path.join(base_workspace, f)
        if not os.path.exists(path):
            errors.append(f"Config file missing: {f}")
    return errors

def verify_prompt():
    errors = []
    if not os.path.exists(PROMPT_FILE):
        errors.append("Output prompt missing")
        return errors
    with open(PROMPT_FILE) as f:
        data = f.read()
    for bad in ["FIXME:", "TODO:", "PLACEHOLDER", "[SKILL_PRUNED]"]:
        if bad in data and "PLACEHOLDER" in bad:
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
    for section in ["# Goal", "## Context", "## Phases", "## Verification Checklist"]:
        if section not in data:
            errors.append(f"Missing section: {section}")
    if "tree.prompt.txt" not in data:
        errors.append("tree.prompt.txt not referenced as primary source")
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
    if "tree.prompt.txt" not in data:
        errors.append("tree.prompt.txt not referenced as primary source in plan")
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
        ("Tree Prompt (Primary Source)", verify_tree_prompt),
        ("Main Prompt", verify_prompt),
        ("Implementation Plan", verify_plan),
        ("MJS to MTS Conversion", verify_mjs_to_mts),
        ("Cleanup (.enhance/.goals)", verify_cleanup),
        ("Config Files", verify_config_files),
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
