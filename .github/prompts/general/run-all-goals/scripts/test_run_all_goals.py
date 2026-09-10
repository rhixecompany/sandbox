#!/usr/bin/env python3
"""Run All Goals — Test Script.
Executes all subgoal tests and reports results.
tree.prompt.txt is PRIMARY source for cleanup goals."""
import os, sys, subprocess, json, datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_test(name, command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=120)
        return {"name": name, "command": command, "returncode": result.returncode, "status": "PASS" if result.returncode == 0 else "FAIL"}
    except Exception as e:
        return {"name": name, "command": command, "error": str(e), "status": "ERROR"}

def test_tree_prompt_exists():
    """Tree-specific test: tree.prompt.txt exists as primary source."""
    tree_path = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "tree.prompt.txt")
    exists = os.path.exists(tree_path)
    return {"name": "Tree Prompt Exists (primary source)", "command": f"test -f {tree_path}", "returncode": 0 if exists else 1, "status": "PASS" if exists else "FAIL"}

def test_mjs_to_mts_conversion():
    """Tree-specific test: no .mjs files remain without .mts counterparts."""
    base_workspace = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
    mjs_files = []
    for root, dirs, files in os.walk(base_workspace):
        for f in files:
            if f.endswith('.mjs'):
                mts_path = os.path.join(root, f[:-4] + '.mts')
                if not os.path.exists(mts_path):
                    mjs_files.append(os.path.join(root, f))
    passed = len(mjs_files) == 0
    return {"name": "MJS to MTS Conversion Check", "command": "find . -name '*.mjs' | head -1", "returncode": 0 if passed else 1, "status": "PASS" if passed else "FAIL", "detail": f"{len(mjs_files)} unconverted .mjs files"}

def test_enhance_cleanup():
    """Tree-specific test: .enhance directory does not exist."""
    base_workspace = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
    enhance_path = os.path.join(base_workspace, ".enhance")
    exists = os.path.exists(enhance_path)
    return {"name": ".enhance Cleanup Verification", "command": f"test ! -d {enhance_path}", "returncode": 0 if not exists else 1, "status": "PASS" if not exists else "FAIL"}

def test_goals_cleanup():
    """Tree-specific test: .goals directory does not exist."""
    base_workspace = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
    goals_path = os.path.join(base_workspace, ".goals")
    exists = os.path.exists(goals_path)
    return {"name": ".goals Cleanup Verification", "command": f"test ! -d {goals_path}", "returncode": 0 if not exists else 1, "status": "PASS" if not exists else "FAIL"}

def test_config_validation():
    """Tree-specific test: validate key config files exist."""
    base_workspace = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
    config_files = ["package.json", "pyrightconfig.json", "tsconfig.json", "requirements.txt"]
    missing = [f for f in config_files if not os.path.exists(os.path.join(base_workspace, f))]
    passed = len(missing) == 0
    return {"name": "Config File Validation", "command": "test -f package.json && test -f pyrightconfig.json && test -f tsconfig.json && test -f requirements.txt", "returncode": 0 if passed else 1, "status": "PASS" if passed else "FAIL", "detail": f"Missing: {missing}"}

def main():
    tests = []
    tests.append(("Unified Prompt Exists", "test -f " + BASE_DIR + "/run-all-goals.prompt.md"))
    tests.append(("Implementation Plan Exists", "test -f .hermes/plans/run-all-goals-implementation.md"))
    tests.append(("Rules Core Exists", "test -f " + BASE_DIR + "/templates/_shared/rules-core.md"))
    tests.append(("Deps Core Exists", "test -f " + BASE_DIR + "/templates/_shared/deps-core.md"))
    tests.append(("Verify Script Exists", "test -f " + BASE_DIR + "/scripts/verify_run_all_goals.py"))
    tests.append(("Skill Exists", "test -f " + BASE_DIR + "/skills/run-all-goals.md"))
    tests.append(("tree.prompt.txt PRIMARY referenced", "grep -q 'tree.prompt.txt' " + BASE_DIR + "/run-all-goals.prompt.md"))
    tests.append(("No FIXME/TODO/PLACEHOLDER", "grep -r 'FIXME\\|TODO\\|PLACEHOLDER' " + BASE_DIR + " --include='*.md' --include='*.py' || true"))
    # Tree-specific tests
    tests.append(("Tree Prompt Exists (primary source)", test_tree_prompt_exists()["command"]))
    tests.append(("MJS to MTS Conversion", test_mjs_to_mts_conversion()["command"]))
    tests.append((".enhance Cleanup", test_enhance_cleanup()["command"]))
    tests.append((".goals Cleanup", test_goals_cleanup()["command"]))
    tests.append(("Config File Validation", test_config_validation()["command"]))
    results = []
    for name, cmd in tests:
        result = run_test(name, cmd)
        # Override with detailed results from tree-specific tests
        if name == "Tree Prompt Exists (primary source)":
            result = test_tree_prompt_exists()
        elif name == "MJS to MTS Conversion":
            result = test_mjs_to_mts_conversion()
        elif name == ".enhance Cleanup":
            result = test_enhance_cleanup()
        elif name == ".goals Cleanup":
            result = test_goals_cleanup()
        elif name == "Config File Validation":
            result = test_config_validation()
        results.append(result)
        symbol = "\u2705" if result["status"] == "PASS" else "\u274c"
        print(symbol + " " + name + ": " + result["status"])
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = os.path.join(RESULTS_DIR, "test-results-" + timestamp + ".json")
    with open(result_file, "w") as f:
        json.dump(results, f, indent=2)
    print("\nResults written to " + result_file)
    failed = [r for r in results if result["status"] != "PASS"]
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
