#!/usr/bin/env python3
"""Validate VS Code JSON — Walk entire workspace and validate all .vscode JSON.

Async CLI that discovers and validates every JSON file under any .vscode/
directory in the workspace tree.
"""

import asyncio
import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


def json_syntax_check(content: str) -> Optional[str]:
    """Check JSON syntax, return error if invalid. CPU-bound."""
    try:
        json.loads(content)
        return None
    except json.JSONDecodeError as e:
        return f"JSON error at line {e.lineno}, col {e.colno}: {e.msg}"


async def validate_json_file(file_path: Path) -> Dict[str, Any]:
    """Validate a single JSON file. I/O offloaded to thread."""
    try:
        content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception as exc:
        return {
            "file": str(file_path),
            "error": f"Cannot read: {exc}",
            "passed": False,
        }

    error = json_syntax_check(content)
    if error:
        return {"file": str(file_path), "error": error, "passed": False}

    return {"file": str(file_path), "passed": True}


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Walk entire workspace and validate all .vscode JSON files."
    )
    parser.add_argument(
        "--workspace",
        type=str,
        default=".",
        help="Root directory (default: .)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file for report (default: stdout)",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    ignore_parts = {"node_modules", ".git", ".next", "dist", "build", "coverage", "out", ".venv", "venv", "__pycache__"}
    vscode_dirs = list(workspace.rglob(".vscode"))
    json_files: List[Path] = []
    for d in vscode_dirs:
        if d.is_dir() and not any(part in ignore_parts for part in d.parts):
            json_files.extend(f for f in d.glob("*.json") if not any(part in ignore_parts for part in f.parts))

    if not json_files:
        msg = f"No .vscode JSON files found in {workspace}"
        if args.output:
            await asyncio.to_thread(
                Path(args.output).write_text, msg + "\n", encoding="utf-8"
            )
        else:
            print(msg, file=sys.stderr)
        sys.exit(1)

    results = await asyncio.gather(*(validate_json_file(f) for f in json_files))

    passed = [r for r in results if r.get("passed")]
    failed = [r for r in results if not r.get("passed")]

    lines = [f"=== VS Code JSON Validation ==="]
    lines.append(f"Scanned: {len(json_files)} | Passed: {len(passed)} | Failed: {len(failed)}")
    lines.append("")

    if failed:
        lines.append("--- FAILURES ---")
        for r in failed:
            lines.append(f"  FAIL: {r['file']}")
            lines.append(f"    {r.get('error', 'unknown error')}")
        lines.append("")

    if passed:
        lines.append("--- ALL PASSED ---")
        for r in passed:
            lines.append(f"  OK: {r['file']}")

    report = "\n".join(lines)

    if args.output:
        await asyncio.to_thread(
            Path(args.output).write_text, report, encoding="utf-8"
        )
    else:
        print(report)

    sys.exit(0 if len(failed) == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
