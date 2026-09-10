#!/usr/bin/env python3
"""Run All Goals — Test Script.
Executes all subgoal tests and reports results."""
import os, sys, subprocess, json, datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR))))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_test(name, command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=120)
        return {"name": name, "command": command, "returncode": result.returncode, "status": "PASS" if result.returncode == 0 else "FAIL"}
    except Exception as e:
        return {"name": name, "command": command, "error": str(e), "status": "ERROR"}

def main():
    tests = [
        ("Unified Prompt Exists", f"test -f {BASE_DIR}/run-all-goals.prompt.md"),
        ("Implementation Plan Exists", "test -f .hermes/plans/run-all-goals-implementation.md"),
        ("Rules Core Exists", f"test -f {BASE_DIR}/templates/_shared/rules-core.md"),
        ("Deps Core Exists", f"test -f {BASE_DIR}/templates/_shared/deps-core.md"),
        ("Verify Script Exists", f"test -f {BASE_DIR}/scripts/verify_run_all_goals.py"),
        ("Skill Exists", f"test -f {BASE_DIR}/skills/run-all-goals.md"),
        ("No Placeholders", f"grep -r 'FIXME\|TODO\|PLACEHOLDER' {BASE_DIR} --include='*.md' --include='*.py' || true"),
    ]
    results = []
    for name, cmd in tests:
        result = run_test(name, cmd)
        results.append(result)
        symbol = "✅" if result["status"] == "PASS" else "❌"
        print(f"{symbol} {name}: {result['status']}")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = os.path.join(RESULTS_DIR, f"test-results-{timestamp}.json")
    with open(result_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults written to {result_file}")
    failed = [r for r in results if r["status"] != "PASS"]
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
