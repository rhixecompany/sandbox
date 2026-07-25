#!/usr/bin/env python3
"""Validate VS Code Configs — Validate JSON files in .vscode directories.

Async CLI for checking JSON syntax, required fields, and formatter
conflicts across all .vscode/ directories in a workspace.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate .vscode JSON files across workspace.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exit codes:\n  0 passed or empty scan allowed\n  1 invalid JSON or validation failures\n  2 no .vscode JSON files found",
    )
    parser.add_argument("--workspace", type=str, default=".", help="Root directory (default: .)")
    parser.add_argument("--output", type=str, default="", help="Write a summary report to this file path")
    parser.add_argument("--report", type=str, default="", help="Alias for output report path")
    parser.add_argument(
        "--allow-empty", action="store_true", help="Exit successfully when no .vscode JSON files are found"
    )
    parser.add_argument("--fix", action="store_true", help="Auto-fix simple issues (not yet implemented)")
    return parser.parse_args()


def check_json_syntax(content: str) -> str | None:
    try:
        json.loads(content)
        return None
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e.msg} at line {e.lineno}, col {e.colno}"


def check_formatter_conflicts(data: Any) -> list[str]:
    warnings: list[str] = []
    if not isinstance(data, dict):
        return warnings
    formatter = data.get("editor.defaultFormatter")
    if isinstance(formatter, str) and formatter:
        for key in data:
            if key.startswith("[") and key.endswith("]"):
                lang_settings = data[key]
                if isinstance(lang_settings, dict):
                    lf = lang_settings.get("editor.defaultFormatter")
                    if lf and lf != formatter:
                        warnings.append(f"Potential formatter conflict: global='{formatter}' vs {key}='{lf}'")
    return warnings


async def validate_vscode_file(file_path: Path) -> dict[str, Any]:
    try:
        content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception as exc:
        return {"file": str(file_path), "error": f"Cannot read: {exc}", "passed": False}

    result: dict[str, Any] = {"file": str(file_path), "errors": [], "warnings": [], "passed": True}
    syntax_error = check_json_syntax(content)
    if syntax_error:
        result["errors"].append(syntax_error)
        result["passed"] = False
        return result

    data = json.loads(content)
    if file_path.name == "settings.json":
        conflicts = check_formatter_conflicts(data)
        result["warnings"].extend(conflicts)
    if file_path.name == "extensions.json" and "recommendations" not in data:
        result["warnings"].append("extensions.json missing 'recommendations' array")
    return result


async def main() -> None:
    args = parse_args()
    workspace = Path(args.workspace).resolve()
    report_path = Path(args.report or args.output) if (args.report or args.output) else None
    ignore_parts = {"node_modules", ".git", ".next", "dist", "build", "coverage", "out", ".venv", "venv", "__pycache__"}
    vscode_dirs = list(workspace.rglob(".vscode"))
    json_files: list[Path] = []
    for d in vscode_dirs:
        if d.is_dir() and not any(part in ignore_parts for part in d.parts):
            json_files.extend(f for f in d.glob("*.json") if not any(part in ignore_parts for part in f.parts))

    report_lines = []
    if not json_files:
        empty_message = f"No .vscode JSON files found in {workspace}"
        print(empty_message, file=sys.stderr)
        report_lines.extend(
            [
                "# VS Code Config Validation Report",
                "",
                f"Scanned: {workspace}",
                "",
                "## Result",
                "",
                "- Passed: 0",
                "- Failed: 0",
                "",
                f"**Status:** {empty_message}",
            ]
        )
        if report_path:
            report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
        if args.allow_empty:
            sys.exit(0)
        sys.exit(2)

    results = await asyncio.gather(*(validate_vscode_file(f) for f in json_files))
    passed = [r for r in results if r.get("passed")]
    failed = [r for r in results if not r.get("passed")]
    total_errors = sum(len(r.get("errors", [])) for r in results)
    total_warnings = sum(len(r.get("warnings", [])) for r in results)

    print("\n=== VS Code Config Validation ===")
    print(f"Scanned {len(json_files)} file(s) — Passed: {len(passed)}, Failed: {len(failed)}")
    print(f"Errors: {total_errors}, Warnings: {total_warnings}")
    for r in failed:
        print(f"  FAIL: {r['file']}")
        for e in r.get("errors", []):
            print(f"    ERROR: {e}")
        for w in r.get("warnings", []):
            print(f"    WARN: {w}")
    for r in passed:
        if r.get("warnings"):
            print(f"  PASS (warnings): {r['file']}")
            for w in r["warnings"]:
                print(f"    WARN: {w}")

    report_lines.extend(
        [
            "# VS Code Config Validation Report",
            "",
            f"Scanned: {workspace}",
            "",
            "## Result",
            "",
            f"- Passed: {len(passed)}",
            f"- Failed: {len(failed)}",
            "",
            f"**Status:** {'passed' if not failed else 'failed'}",
        ]
    )
    if report_path:
        report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    sys.exit(0 if len(failed) == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
