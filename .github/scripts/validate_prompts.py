#!/usr/bin/env python3
"""Validate Prompts — Validate prompt frontmatter and references.

Async CLI for checking prompt file frontmatter completeness,
semver versions, non-empty tags, and internal references.
"""

import asyncio
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# Required frontmatter fields for prompt files
REQUIRED_FIELDS = {"name", "title", "description", "version", "tags"}
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?(\+[a-zA-Z0-9.]+)?$")


def parse_frontmatter(content: str) -> Tuple[Optional[Dict[str, Any]], str, int]:
    """Parse frontmatter from a .prompt.md file. CPU-bound."""
    if not content.startswith("---"):
        return None, "Missing opening frontmatter delimiter", 0

    end = content.find("---", 3)
    if end == -1:
        return None, "Frontmatter not closed", 0

    fm_text = content[3:end]
    fm: Dict[str, Any] = {}
    for match in re.finditer(r"^(\w+)\s*:\s*(.+)$", fm_text, re.MULTILINE):
        key = match.group(1)
        val = match.group(2).strip().strip('"').strip("'")
        fm[key] = val

    return fm, "", end + 3


def validate_frontmatter(fm: Dict[str, Any]) -> List[str]:
    """Validate frontmatter content. CPU-bound."""
    errors: List[str] = []
    missing = REQUIRED_FIELDS - set(fm.keys())
    if missing:
        errors.append(f"Missing required fields: {', '.join(sorted(missing))}")

    # Validate version is semver
    version = fm.get("version", "")
    if version and not SEMVER_RE.match(version):
        errors.append(f"Version '{version}' is not valid semver")

    # Tags should be non-empty
    tags = fm.get("tags", "")
    if isinstance(tags, str) and not tags.strip():
        errors.append("Tags field is empty")
    elif isinstance(tags, list) and not tags:
        errors.append("Tags list is empty")

    return errors


def check_references(content: str) -> List[str]:
    """Check internal references resolve. CPU-bound."""
    errors: List[str] = []
    refs = re.findall(r"\[.*?\]\(((?:\.\.?/)[^)]+)\)", content)
    # Note: full cross-reference resolution requires workspace context
    # Here we flag all relative refs for manual check
    if refs:
        for ref in refs[:5]:  # limit to first 5 to avoid noise
            errors.append(f"Relative reference needs verification: {ref}")
    return errors


async def validate_prompt(file_path: Path) -> dict:
    """Validate a single prompt file."""
    try:
        content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception as exc:
        return {"file": str(file_path), "error": str(exc), "passed": False}

    fm, parse_error, _ = parse_frontmatter(content)
    errors: List[str] = []
    warnings: List[str] = []

    if parse_error:
        errors.append(parse_error)
        return {
            "file": str(file_path),
            "errors": errors,
            "warnings": warnings,
            "passed": False,
        }

    if fm is None:
        errors.append("Empty frontmatter")
        return {
            "file": str(file_path),
            "errors": errors,
            "warnings": warnings,
            "passed": False,
        }

    errors.extend(validate_frontmatter(fm))
    warnings.extend(check_references(content))

    return {
        "file": str(file_path),
        "fields_present": list(fm.keys()),
        "errors": errors,
        "warnings": warnings,
        "passed": len(errors) == 0,
    }


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate prompt files against frontmatter schema."
    )
    parser.add_argument(
        "--file",
        type=str,
        default=None,
        help="Single prompt file to validate",
    )
    parser.add_argument(
        "--workspace",
        type=str,
        default=".",
        help="Root directory (default: .)",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default="**/*.prompt.md",
        help="File glob (default: **/*.prompt.md)",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=0,
        help="Minimum passing fields count (default: 0)",
    )
    parser.add_argument(
        "--fail-on-error",
        action="store_true",
        help="Exit with code 1 on any validation error",
    )
    parser.add_argument(
        "--output-json",
        type=str,
        default=None,
        help="JSON output file path",
    )
    parser.add_argument(
        "--report",
        type=str,
        default=None,
        help="Markdown report output path",
    )
    args = parser.parse_args()

    if args.file:
        files = [Path(args.file).resolve()]
    else:
        workspace = Path(args.workspace).resolve()
        files = list(workspace.glob(args.pattern))

    if not files:
        print(f"No prompt files found to validate", file=sys.stderr)
        sys.exit(2)

    results = await asyncio.gather(*(validate_prompt(f) for f in files))

    passed = [r for r in results if r.get("passed")]
    failed = [r for r in results if not r.get("passed")]

    if args.output_json:
        output_path = Path(args.output_json).resolve()
        await asyncio.to_thread(
            output_path.write_text,
            json.dumps(
                {
                    "total": len(results),
                    "passed": len(passed),
                    "failed": len(failed),
                    "results": results,
                },
                indent=2,
            ),
            encoding="utf-8",
        )

    if args.report:
        report_path = Path(args.report).resolve()
        lines = [
            "# Prompt Validation Report",
            "",
            f"**Total:** {len(results)}  ",
            f"**Passed:** {len(passed)}  ",
            f"**Failed:** {len(failed)}  ",
            "",
            "---",
            "",
        ]
        for r in failed:
            lines.append(f"## FAIL: {r['file']}")
            for e in r.get("errors", []):
                lines.append(f"- ERROR: {e}")
            for w in r.get("warnings", []):
                lines.append(f"- WARN: {w}")
            lines.append("")
        await asyncio.to_thread(
            report_path.write_text, "\n".join(lines), encoding="utf-8"
        )

    # Console output
    print(f"\n=== Prompt Validation ===")
    print(f"Total: {len(results)} | Passed: {len(passed)} | Failed: {len(failed)}")
    for r in failed:
        print(f"  FAIL: {r['file']}")
        for e in r.get("errors", []):
            print(f"    ERROR: {e}")
        for w in r.get("warnings", []):
            print(f"    WARN: {w}")

    exit_code = 0
    if args.fail_on_error and failed:
        exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    asyncio.run(main())
