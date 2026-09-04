#!/usr/bin/env python3
"""
Comprehensive Implementation Plan — Execution Script
Validates, executes, and verifies the implementation plan.
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Configuration
WORKSPACE = Path(os.environ.get("WORKSPACE", Path.home() / "Desktop" / "SandBox"))
PLANS_DIR = WORKSPACE / ".hermes" / "plans"
SPECS_DIR = WORKSPACE / ".hermes" / "specs"
REPORTS_DIR = WORKSPACE / ".hermes" / "reports"


def run_cmd(cmd: str, cwd: Path = WORKSPACE) -> tuple[int, str]:
    """Run a shell command and return (exit_code, output)."""
    result = subprocess.run(
        cmd, shell=True, cwd=str(cwd),
        capture_output=True, text=True, timeout=120
    )
    return result.returncode, (result.stdout + result.stderr).strip()


def validate_yaml_frontmatter(path: Path) -> list[str]:
    """Validate a markdown file has proper YAML frontmatter."""
    issues: list[str] = []
    if not path.exists():
        issues.append(f"File not found: {path}")
        return issues

    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        issues.append(f"Missing YAML frontmatter: {path.name}")
        return issues

    end = content.find("---", 3)
    if end == -1:
        issues.append(f"Unclosed YAML frontmatter: {path.name}")
        return issues

    frontmatter = content[3:end].strip()
    required = ["name", "title", "description", "version", "author", "license", "tags"]
    for key in required:
        if f"{key}:" not in frontmatter:
            issues.append(f"Missing '{key}' in frontmatter: {path.name}")

    return issues


def validate_plan(path: Path) -> dict:
    """Validate an implementation plan document."""
    issues: list[str] = []
    content = path.read_text(encoding="utf-8")

    issues.extend(validate_yaml_frontmatter(path))

    required_sections = ["## Phases", "## Milestones", "## Timeline"]
    for section in required_sections:
        if section not in content:
            issues.append(f"Missing section '{section}': {path.name}")

    if "| Task |" not in content and "|Task|" not in content:
        issues.append(f"No task tables found: {path.name}")

    return {
        "file": str(path),
        "valid": len(issues) == 0,
        "issues": issues,
        "size_bytes": path.stat().st_size
    }


def validate_spec(path: Path) -> dict:
    """Validate a specification document."""
    issues: list[str] = []
    content = path.read_text(encoding="utf-8")

    issues.extend(validate_yaml_frontmatter(path))

    if "### FR-" not in content:
        issues.append(f"No requirements found: {path.name}")

    if "Acceptance Criteria:" not in content:
        issues.append(f"No acceptance criteria: {path.name}")

    return {
        "file": str(path),
        "valid": len(issues) == 0,
        "issues": issues,
        "size_bytes": path.stat().st_size
    }


def generate_timeline(plan_path: Path) -> dict:
    """Generate a timeline from the plan."""
    content = plan_path.read_text(encoding="utf-8")

    milestones: list[dict] = []
    for line in content.split("\n"):
        if "| M" in line and "|" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4 and parts[1].startswith("M"):
                milestones.append({
                    "id": parts[1],
                    "name": parts[2],
                    "date": parts[3] if len(parts) > 3 else "TBD",
                    "criteria": parts[4] if len(parts) > 4 else "TBD"
                })

    return {
        "generated": datetime.now().isoformat(),
        "milestones": milestones,
        "total_duration_days": len(milestones) * 2
    }


def verify_workspace_state() -> dict:
    """Verify workspace is in a clean state for execution."""
    issues: list[str] = []

    code, output = run_cmd("git status --porcelain")
    if output.strip():
        issues.append(f"Uncommitted changes present")

    backups = list(WORKSPACE.rglob("*.bak")) + list(WORKSPACE.rglob("*.backup"))
    if backups:
        issues.append(f"Backup files found: {len(backups)}")

    return {
        "clean": len(issues) == 0,
        "issues": issues,
        "timestamp": datetime.now().isoformat()
    }


def run_verification_pipeline() -> dict:
    """Run the full verification pipeline."""
    checks: list[dict] = []

    # Lint
    code, output = run_cmd("bun run lint 2>&1 | tail -5")
    checks.append({
        "name": "lint",
        "passed": code == 0,
        "output": output[-500:]
    })

    # Type-check
    code, output = run_cmd("bun run typecheck 2>&1 | tail -5")
    checks.append({
        "name": "typecheck",
        "passed": code == 0,
        "output": output[-500:]
    })

    # Format check
    code, output = run_cmd("bun run format 2>&1 | tail -5")
    checks.append({
        "name": "format",
        "passed": code == 0,
        "output": output[-500:]
    })

    # Full check
    code, output = run_cmd("bun run check 2>&1 | tail -5")
    checks.append({
        "name": "full_check",
        "passed": code == 0,
        "output": output[-500:]
    })

    all_passed = all(c.get("passed", False) for c in checks)

    return {
        "timestamp": datetime.now().isoformat(),
        "checks": checks,
        "all_passed": all_passed
    }


def main():
    """Main execution entry point."""
    if len(sys.argv) < 2:
        print("Usage: comprehensive-implementation.py <command> [args]")
        print("Commands: validate, timeline, verify, pipeline, report")
        sys.exit(1)

    command = sys.argv[1]

    if command == "validate":
        results: dict = {"plans": [], "specs": [], "issues": []}

        for plan_file in PLANS_DIR.glob("*.md"):
            r = validate_plan(plan_file)
            results["plans"].append(r)
            results["issues"].extend(r["issues"])

        for spec_file in SPECS_DIR.glob("*.md"):
            r = validate_spec(spec_file)
            results["specs"].append(r)
            results["issues"].extend(r["issues"])

        print(json.dumps(results, indent=2))
        sys.exit(0 if not results["issues"] else 1)

    elif command == "timeline":
        plan_path = Path(sys.argv[2]) if len(sys.argv) > 2 else PLANS_DIR / "comprehensive-implementation-plan.md"
        timeline = generate_timeline(plan_path)
        print(json.dumps(timeline, indent=2))

    elif command == "verify":
        state = verify_workspace_state()
        print(json.dumps(state, indent=2))
        sys.exit(0 if state["clean"] else 1)

    elif command == "pipeline":
        results = run_verification_pipeline()
        print(json.dumps(results, indent=2))
        sys.exit(0 if results["all_passed"] else 1)

    elif command == "report":
        report = {
            "generated": datetime.now().isoformat(),
            "workspace": str(WORKSPACE),
            "plans_count": len(list(PLANS_DIR.glob("*.md"))),
            "specs_count": len(list(SPECS_DIR.glob("*.md"))),
            "workspace_state": verify_workspace_state(),
            "pipeline": run_verification_pipeline()
        }

        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        report_path = REPORTS_DIR / f"implementation-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Report saved: {report_path}")
        print(json.dumps(report, indent=2))

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
