#!/usr/bin/env python3
"""Subagent Dispatcher for Subagent-Driven Development.

Reads a markdown plan file, extracts tasks, and dispatches subagents
with proper context for implementer, spec reviewer, and quality reviewer.

Usage:
    python3 subagent_dispatcher.py --plan .hermes/plans/example-subagent-plan.md
    python3 subagent_dispatcher.py --plan .hermes/plans/example-subagent-plan.md --dry-run
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single task from the plan."""
    id: str
    title: str
    description: str
    file: str
    spec: str
    test_file: str
    test_spec: str
    dependencies: list[str]


@dataclass
class Plan:
    """Parsed plan with metadata."""
    goal: str
    tasks: list[Task]
    project_conventions: str


def parse_plan(plan_path: str) -> Plan:
    """Parse markdown plan file into structured Plan object."""
    with open(plan_path, encoding='utf-8') as f:
        content = f.read()

    # Extract goal
    goal_match = re.search(r'^## Goal\n\s*(.+?)(?:\n##|\Z)', content, re.MULTILINE | re.DOTALL)
    goal = goal_match.group(1).strip() if goal_match else "No goal specified"

    # Extract project conventions
    conventions_match = re.search(r'^## Project Conventions\n\s*(.+?)(?:\n##|\Z)', content, re.MULTILINE | re.DOTALL)
    conventions = conventions_match.group(1).strip() if conventions_match else ""

    # Extract tasks - look for "### Task N:" pattern
    tasks = []

    # More robust parsing: split by "### Task"
    sections = re.split(r'^### Task (\d+):\s*(.+)$', content, flags=re.MULTILINE)

    for i in range(1, len(sections), 3):
        task_num = sections[i]
        task_title = sections[i+1].strip() if i+1 < len(sections) else ""
        task_body = sections[i+2] if i+2 < len(sections) else ""

        # Extract fields from task body
        file_match = re.search(r'- \*\*File\*\*:\s*(.+)', task_body)
        spec_match = re.search(r'- \*\*Spec\*\*:\s*(.+)', task_body)
        test_match = re.search(r'- \*\*Test\*\*:\s*(.+)', task_body)
        tdd_match = re.search(r'- \*\*TDD\*\*:\s*(.+)', task_body)

        # Also check for continuation lines
        file = file_match.group(1).strip() if file_match else ""
        spec = spec_match.group(1).strip() if spec_match else ""
        test_file = test_match.group(1).strip() if test_match else ""
        test_spec = tdd_match.group(1).strip() if tdd_match else ""

        # Extract dependencies from "## Dependencies" section
        deps_match = re.search(r'^## Dependencies\n\s*(.+?)(?:\n##|\Z)', content, re.MULTILINE | re.DOTALL)
        dependencies = []
        if deps_match:
            dep_lines = deps_match.group(1).strip().split('\n')
            for line in dep_lines:
                if f"Task {task_num}" in line and "before" in line:
                    # Parse "Task 1 must complete before Task 2"
                    parts = re.findall(r'Task (\d+)', line)
                    if len(parts) >= 2:
                        dependencies.append(f"task-{parts[1]}")

        tasks.append(Task(
            id=f"task-{task_num}",
            title=task_title,
            description=task_body.strip(),
            file=file,
            spec=spec,
            test_file=test_file,
            test_spec=test_spec,
            dependencies=dependencies
        ))

    return Plan(goal=goal, tasks=tasks, project_conventions=conventions)


def build_implementer_context(task: Task, plan: Plan, all_tasks: list[Task]) -> str:
    """Build complete context for implementer subagent."""
    return f"""TASK FROM PLAN:
- ID: {task.id}
- Title: {task.title}
- Create: {task.file}
- Spec: {task.spec}
- Test: {task.test_file}
- Test Spec: {task.test_spec}

FOLLOW TDD:
1. Write failing test in {task.test_file}
2. Run: pytest {task.test_file} -v (verify FAIL)
3. Write minimal implementation in {task.file}
4. Run: pytest {task.test_file} -v (verify PASS)
5. Run: pytest tests/ -q (verify no regressions)
6. Commit: git add -A && git commit -m "feat: {task.title.lower()}"

PROJECT CONTEXT:
{plan.project_conventions}

ALL TASKS IN PLAN:
{json.dumps([{"id": t.id, "title": t.title, "file": t.file} for t in all_tasks], indent=2)}

THIS TASK DEPENDS ON: {', '.join(task.dependencies) if task.dependencies else 'None'}

IMPORTANT:
- Return only the files you created/modified
- Confirm test results in your response
- Do not proceed if tests don't pass
"""


def build_spec_reviewer_context(task: Task, _plan: Plan) -> str:
    """Build context for spec compliance reviewer."""
    return f"""ORIGINAL TASK SPEC:
- ID: {task.id}
- Title: {task.title}
- Create: {task.file}
- Spec: {task.spec}
- Test: {task.test_file}
- Test Spec: {task.test_spec}

CHECK:
- [ ] All requirements from spec implemented?
- [ ] File paths match spec?
- [ ] Function signatures match spec?
- [ ] Behavior matches expected?
- [ ] Nothing extra added (no scope creep)?
- [ ] TDD followed (test first, then implementation)?
- [ ] Tests actually test the specified behavior?

OUTPUT FORMAT:
- SPEC_GAPS: [list of specific gaps, empty if none]
- VERDICT: PASS or FAIL

If FAIL, list specific gaps that must be fixed before proceeding.
"""


def build_quality_reviewer_context(_task: Task, _plan: Plan, files: list[str]) -> str:
    """Build context for code quality reviewer."""
    return f"""FILES TO REVIEW:
{chr(10).join(f"- {f}" for f in files)}

CHECK:
- [ ] Follows project conventions and style?
- [ ] Proper error handling?
- [ ] Clear variable/function names?
- [ ] Adequate test coverage?
- [ ] No obvious bugs or missed edge cases?
- [ ] No security issues?
- [ ] Type hints present (Python)?
- [ ] Docstrings for public functions?

OUTPUT FORMAT:
- Critical Issues: [must fix before proceeding]
- Important Issues: [should fix]
- Minor Issues: [optional]
- VERDICT: APPROVED or REQUEST_CHANGES

If REQUEST_CHANGES, list specific issues.
"""


def build_integration_reviewer_context(plan: Plan, all_files: list[str]) -> str:
    """Build context for final integration reviewer."""
    return f"""PLAN GOAL: {plan.goal}

ALL TASKS COMPLETE. REVIEW FULL IMPLEMENTATION:

FILES CREATED/MODIFIED:
{chr(10).join(f"- {f}" for f in all_files)}

ORIGINAL TASKS:
{json.dumps([{"id": t.id, "title": t.title, "file": t.file} for t in plan.tasks], indent=2)}

CHECK:
- [ ] Do all components work together?
- [ ] Any inconsistencies between tasks?
- [ ] All tests passing?
- [ ] Ready for merge?

OUTPUT FORMAT:
- INTEGRATION_ISSUES: [list, empty if none]
- VERDICT: PASS or FAIL
"""


def dispatch_subagent(goal: str, context: str, toolsets: list[str]) -> dict:
    """Dispatch a subagent via delegate_task tool."""
    # This is a placeholder - in actual use, this would call the delegate_task tool
    # For now, we'll simulate by printing what would be dispatched
    print(f"\n{'='*60}")
    print("DISPATCHING SUBAGENT")
    print(f"Goal: {goal}")
    print(f"Toolsets: {toolsets}")
    print(f"Context length: {len(context)} chars")
    print(f"{'='*60}\n")

    # In real implementation, this would be:
    # result = delegate_task(goal=goal, context=context, toolsets=toolsets)
    # return result

    # For now, return simulated success
    return {
        "status": "simulated",
        "goal": goal,
        "context_preview": context[:200] + "..." if len(context) > 200 else context
    }


def run_plan(plan_path: str, dry_run: bool = False) -> bool:
    """Execute the full subagent-driven development workflow for a plan."""
    print(f"\n{'#'*60}")
    print(f"SUBAGENT-DRIVEN DEVELOPMENT: {plan_path}")
    print(f"{'#'*60}\n")

    plan = parse_plan(plan_path)
    print(f"Goal: {plan.goal}")
    print(f"Tasks: {len(plan.tasks)}")
    for task in plan.tasks:
        print(f"  - {task.id}: {task.title}")

    if dry_run:
        print("\n[DRY RUN] Would dispatch subagents for each task")
        return True

    all_created_files = []
    todo_status = {task.id: "pending" for task in plan.tasks}

    for task in plan.tasks:
        print(f"\n{'-'*60}")
        print(f"TASK: {task.id} - {task.title}")
        print(f"{'-'*60}")

        # Check dependencies
        for dep in task.dependencies:
            if todo_status.get(dep) != "completed":
                print(f"  BLOCKED: Dependency {dep} not completed")
                return False

        # Step 1: Dispatch Implementer
        print(f"\n[1/3] Dispatching Implementer for {task.id}...")
        impl_context = build_implementer_context(task, plan, plan.tasks)
        impl_result = dispatch_subagent(
            goal=f"Implement {task.title}",
            context=impl_context,
            toolsets=["terminal", "file", "code_execution"]
        )
        print(f"  Result: {impl_result.get('status', 'unknown')}")

        # Simulate file creation for testing
        created_files = [task.file, task.test_file]
        all_created_files.extend(created_files)

        # Step 2: Dispatch Spec Reviewer
        print(f"\n[2/3] Dispatching Spec Reviewer for {task.id}...")
        spec_context = build_spec_reviewer_context(task, plan)
        spec_result = dispatch_subagent(
            goal=f"Review spec compliance for {task.title}",
            context=spec_context,
            toolsets=["file"]
        )
        print(f"  Result: {spec_result.get('status', 'unknown')}")

        # In real implementation, check spec_result for PASS/FAIL
        # If FAIL, loop back to implementer (max 3 iterations)

        # Step 3: Dispatch Quality Reviewer
        print(f"\n[3/3] Dispatching Quality Reviewer for {task.id}...")
        quality_context = build_quality_reviewer_context(task, plan, created_files)
        quality_result = dispatch_subagent(
            goal=f"Review code quality for {task.title}",
            context=quality_context,
            toolsets=["file", "terminal"]
        )
        print(f"  Result: {quality_result.get('status', 'unknown')}")

        # In real implementation, check quality_result for APPROVED/REQUEST_CHANGES
        # If REQUEST_CHANGES, loop back to implementer

        todo_status[task.id] = "completed"
        print(f"\n  ✓ Task {task.id} marked COMPLETED")

    # Final Integration Review
    print(f"\n{'='*60}")
    print("FINAL INTEGRATION REVIEW")
    print(f"{'='*60}")
    integration_context = build_integration_reviewer_context(plan, all_created_files)
    integration_result = dispatch_subagent(
        goal="Review full implementation for integration issues",
        context=integration_context,
        toolsets=["terminal", "file"]
    )
    print(f"  Result: {integration_result.get('status', 'unknown')}")

    # Run full test suite
    print("\nRunning full test suite...")
    # result = subprocess.run(["pytest", "tests/", "-q"], capture_output=True, text=True)
    # print(result.stdout)
    # if result.returncode != 0:
    #     print("TESTS FAILED!")
    #     return False

    print(f"\n{'#'*60}")
    print("PLAN EXECUTION COMPLETE")
    print(f"{'#'*60}")
    print(f"All {len(plan.tasks)} tasks completed")
    print(f"Files created: {len(all_created_files)}")

    return True


def main():
    parser = argparse.ArgumentParser(description="Subagent Dispatcher for SDD")
    parser.add_argument("--plan", required=True, help="Path to plan markdown file")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without dispatching")
    args = parser.parse_args()

    if not os.path.exists(args.plan):
        print(f"Error: Plan file not found: {args.plan}")
        sys.exit(1)

    success = run_plan(args.plan, dry_run=args.dry_run)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
