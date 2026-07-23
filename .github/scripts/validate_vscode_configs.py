#!/usr/bin/env python3
"""Validate VS Code Configs — Validate JSON files in .vscode directories.

Async CLI for checking JSON syntax, required fields, and formatter
conflicts across all .vscode/ directories in a workspace.
"""

import asyncio
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# Known formatter-setting keys that can conflict
FORMATTER_KEYS = [
    "editor.defaultFormatter",
    "editor.formatOnSave",
    "editor.formatOnPaste",
    "editor.formatOnType",
    "[javascript]",
    "[typescript]",
    "[python]",
    "[go]",
    "[rust]",
]


def check_json_syntax(content: str) -> Optional[str]:
    """Check JSON syntax, return error message if invalid. CPU-bound."""
    try:
        json.loads(content)
        return None
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e.msg} at line {e.lineno}, col {e.colno}"


def check_formatter_conflicts(data: Any) -> List[str]:
    """Detect conflicting formatter settings. CPU-bound."""
    warnings: List[str] = []
    if not isinstance(data, dict):
        return warnings

    # Check for multiple default formatters
    formatter = data.get("editor.defaultFormatter")
    if isinstance(formatter, str) and formatter:
        # Check for language-specific overrides that might conflict
        for key in data:
            if key.startswith("[") and key.endswith("]"):
                lang_settings = data[key]
                if isinstance(lang_settings, dict):
                    lf = lang_settings.get("editor.defaultFormatter")
                    if lf and lf != formatter:
                        warnings.append(
                            f"Potential formatter conflict: global='{formatter}' vs {key}='{lf}'"
                        )

    return warnings


async def validate_vscode_file(file_path: Path) -> Dict[str, Any]:
    """Validate a single .vscode JSON file."""
    try:
        content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception as exc:
        return {
            "file": str(file_path),
            "error": f"Cannot read: {exc}",
            "passed": False,
        }

    result: Dict[str, Any] = {
        "file": str(file_path),
        "errors": [],
        "warnings": [],
        "passed": True,
    }

    syntax_error = check_json_syntax(content)
    if syntax_error:
        result["errors"].append(syntax_error)
        result["passed"] = False
        return result

    data = json.loads(content)

    # Check for formatter conflicts (only in settings.json)
    if file_path.name == "settings.json":
        conflicts = check_formatter_conflicts(data)
        result["warnings"].extend(conflicts)

    # Check for required fields in specific files
    if file_path.name == "extensions.json":
        if "recommendations" not in data:
            result["warnings"].append("extensions.json missing 'recommendations' array")

    return result


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate .vscode JSON files across workspace."
    )
    parser.add_argument(
        "--workspace",
        type=str,
        default=".",
        help="Root directory (default: .)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Auto-fix simple issues (not yet implemented)",
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
        print(f"No .vscode JSON files found in {workspace}", file=sys.stderr)
        sys.exit(1)

    results = await asyncio.gather(*(validate_vscode_file(f) for f in json_files))

    passed = [r for r in results if r.get("passed")]
    failed = [r for r in results if not r.get("passed")]

    total_errors = sum(len(r.get("errors", [])) for r in results)
    total_warnings = sum(len(r.get("warnings", [])) for r in results)

    print(f"\n=== VS Code Config Validation ===")
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

    sys.exit(0 if len(failed) == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
