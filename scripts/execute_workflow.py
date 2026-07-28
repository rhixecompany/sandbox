#!/usr/bin/env python3
"""Execute workflow — run a predefined workflow or pipeline of tasks.

Usage:
    python execute_workflow.py [--workflow FILE] [--dry-run] [--verbose] [--parallel]
"""

import argparse
import asyncio
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class WorkflowStep:
    name: str
    command: str
    description: str = ""
    timeout: int = 60
    retries: int = 0


@dataclass
class StepResult:
    step: str
    success: bool
    duration: float
    output: str
    error: str = ""


DEFAULT_WORKFLOW = {
    "name": "Default Workflow",
    "description": "Sample workflow with common tasks",
    "steps": [
        {"name": "validate", "command": "echo 'Validation OK'", "description": "Validate setup"},
        {"name": "build", "command": "echo 'Build OK'", "description": "Build project"},
        {"name": "test", "command": "echo 'Tests passed'", "description": "Run tests"},
    ],
}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Execute a workflow")
    parser.add_argument("--workflow", default=None, help="Path to workflow JSON file")
    parser.add_argument("--dry-run", action="store_true", help="Preview steps without executing")
    parser.add_argument("--verbose", action="store_true", help="Detailed output")
    parser.add_argument("--parallel", action="store_true", help="Run independent steps in parallel")
    return parser.parse_args(argv)


def load_workflow(path: str | None) -> dict[str, Any]:
    """Load workflow definition from file or return default."""
    if not path:
        return DEFAULT_WORKFLOW
    filepath = Path(path)
    if not filepath.exists():
        print(f"ERROR: workflow file not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    return json.loads(filepath.read_text(encoding="utf-8"))


async def execute_step(step: WorkflowStep, verbose: bool) -> StepResult:
    """Execute a single workflow step asynchronously."""
    start = time.monotonic()
    if verbose:
        print(f"  Executing: {step.name} — {step.description or step.command}")

    for attempt in range(step.retries + 1):
        try:
            proc = await asyncio.create_subprocess_shell(
                step.command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=step.timeout)
            elapsed = time.monotonic() - start
            output = stdout.decode("utf-8", errors="replace").strip()
            error = stderr.decode("utf-8", errors="replace").strip()

            if proc.returncode == 0:
                if verbose:
                    print(f"    ✓ {step.name} ({elapsed:.2f}s)")
                    if output:
                        print(f"      {output[:200]}")
                return StepResult(step=step.name, success=True, duration=elapsed, output=output, error=error)
            else:
                if attempt < step.retries:
                    if verbose:
                        print(f"    Retrying {step.name} (attempt {attempt + 2})...")
                    continue
                if verbose:
                    print(f"    ✗ {step.name} ({elapsed:.2f}s): {error[:200]}")
                return StepResult(step=step.name, success=False, duration=elapsed, output=output, error=error)

        except TimeoutError:
            if attempt < step.retries:
                if verbose:
                    print(f"    Timeout on {step.name}, retrying...")
                continue
            elapsed = time.monotonic() - start
            return StepResult(step=step.name, success=False, duration=elapsed, output="", error="Timeout")

    return StepResult(
        step=step.name, success=False, duration=time.monotonic() - start, output="", error="All retries failed"
    )


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    workflow_data = load_workflow(args.workflow)

    workflow_name = workflow_data.get("name", "Unnamed Workflow")
    steps_data = workflow_data.get("steps", [])

    if not steps_data:
        print("ERROR: workflow has no steps", file=sys.stderr)
        sys.exit(1)

    steps = [
        WorkflowStep(**s) if isinstance(s, dict) else WorkflowStep(name=str(s), command=str(s)) for s in steps_data
    ]

    print(f"Workflow: {workflow_name}")
    print(f"Steps: {len(steps)}")
    print(f"Mode: {'parallel' if args.parallel else 'sequential'}")
    if args.dry_run:
        print(f"{'Dry-run' if args.dry_run else ''}")
    print()

    if args.dry_run:
        print("Dry-run: steps that would execute:")
        for i, step in enumerate(steps, 1):
            print(f"  {i}. {step.name}: {step.description or step.command}")
        return

    total_start = time.monotonic()
    results: list[StepResult] = []

    if args.parallel:
        # Run all steps concurrently
        tasks = [execute_step(step, args.verbose) for step in steps]
        results = await asyncio.gather(*tasks)
    else:
        # Run sequentially
        for step in steps:
            result = await execute_step(step, args.verbose)
            results.append(result)
            if not result.success:
                print(f"\nStep '{step.name}' failed. Aborting workflow.")
                break

    total_elapsed = time.monotonic() - total_start
    success_count = sum(1 for r in results if r.success)
    fail_count = sum(1 for r in results if not r.success)

    print(f"\n{'=' * 40}")
    print(f"Workflow Complete: {workflow_name}")
    print(f"  Total time: {total_elapsed:.2f}s")
    print(f"  Passed: {success_count} / {len(steps)}")
    print(f"  Failed: {fail_count} / {len(steps)}")

    if fail_count > 0:
        print("\nFailed steps:")
        for r in results:
            if not r.success:
                print(f"  ✗ {r.step}: {r.error[:150]}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
