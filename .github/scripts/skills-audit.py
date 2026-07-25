#!/usr/bin/env python3
"""Skills Audit — Perform comprehensive audit on skill files.

Async CLI for scanning skill directories and validating structure,
frontmatter, and linked resources.
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = {"name", "title", "description", "version", "author", "tags"}
RECOMMENDED_FIELDS = {"license", "metadata"}


def validate_skill_md(path: Path, content: str) -> tuple[list[str], list[str]]:
    """Validate a SKILL.md file's frontmatter and structure. CPU-bound."""
    errors: list[str] = []
    warnings: list[str] = []

    if not content.startswith("---"):
        errors.append("Missing opening frontmatter delimiter")
        return errors, warnings

    end = content.find("---", 3)
    if end == -1:
        errors.append("Frontmatter not closed")
        return errors, warnings

    fm_block = content[3:end]
    import re

    present_fields = set(re.findall(r"^(\w+)\s*:", fm_block, re.MULTILINE))
    missing_required = REQUIRED_FIELDS - present_fields
    if missing_required:
        errors.append(f"Missing required frontmatter: {', '.join(sorted(missing_required))}")

    missing_recommended = RECOMMENDED_FIELDS - present_fields
    if missing_recommended:
        warnings.append(f"Missing recommended frontmatter: {', '.join(sorted(missing_recommended))}")

    body = content[end + 3 :].strip()
    if not body:
        warnings.append("Empty body after frontmatter")

    return errors, warnings


async def audit_skill_dir(skill_dir: Path) -> dict:
    """Audit a skill directory for required structure. I/O is offloaded."""
    result = {
        "directory": str(skill_dir),
        "errors": [],
        "warnings": [],
        "files_found": [],
        "passed": True,
    }

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        result["errors"].append("Missing SKILL.md")
        result["passed"] = False
        return result

    try:
        content = await asyncio.to_thread(skill_md.read_text, encoding="utf-8")
    except Exception as exc:
        result["errors"].append(f"Cannot read SKILL.md: {exc}")
        result["passed"] = False
        return result

    errors, warnings = validate_skill_md(skill_md, content)
    result["errors"].extend(errors)
    result["warnings"].extend(warnings)
    if errors:
        result["passed"] = False

    # Check linked subdirectories
    for sub in ("references", "templates", "scripts", "assets"):
        sub_path = skill_dir / sub
        if sub_path.is_dir():
            result["files_found"].extend([str(p.relative_to(skill_dir)) for p in sorted(sub_path.iterdir())])

    return result


async def main() -> None:
    parser = argparse.ArgumentParser(description="Audit skill files for quality and structure.")
    parser.add_argument(
        "--skills-dir",
        type=str,
        default=None,
        help="Root skills directory (default: auto-detect)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Report output path (default: stdout)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="JSON output",
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Treat warnings as failures",
    )
    args = parser.parse_args()

    # Determine skills directory
    skills_dir: Path
    if args.skills_dir:
        skills_dir = Path(args.skills_dir).resolve()
    else:
        # Check common Hermes locations
        candidates = [
            Path.home() / ".hermes" / "skills",
            Path.home() / "AppData" / "Local" / "hermes" / "skills",
        ]
        skills_dir = None
        for c in candidates:
            if c.is_dir():
                skills_dir = c
                break
        if skills_dir is None:
            print("Could not auto-detect skills directory. Use --skills-dir.", file=sys.stderr)
            sys.exit(2)

    skill_dirs = sorted([d for d in skills_dir.iterdir() if d.is_dir()])
    if not skill_dirs:
        print(f"No skill subdirectories found in {skills_dir}", file=sys.stderr)
        sys.exit(1)

    results = await asyncio.gather(*(audit_skill_dir(d) for d in skill_dirs))

    passed = [r for r in results if r.get("passed")]
    failed = [r for r in results if not r.get("passed")]

    if args.fail_on_warning:
        # Promote warnings to failures
        for r in results:
            if r.get("warnings") and r.get("passed"):
                r["passed"] = False
                failed.append(r)
                if r in passed:
                    passed.remove(r)

    if args.json:
        output = json.dumps(
            {"results": results, "passed": len(passed), "failed": len(failed)},
            indent=2,
        )
        if args.output:
            await asyncio.to_thread(Path(args.output).write_text, output, encoding="utf-8")
        else:
            print(output)
    else:
        lines = ["\n=== Skills Audit Report ==="]
        lines.append(f"Scanned {len(skill_dirs)} skill(s) — Passed: {len(passed)}, Failed: {len(failed)}")
        for r in results:
            status = "PASS" if r.get("passed") else "FAIL"
            lines.append(f"  [{status}] {r['directory']}")
            for e in r.get("errors", []):
                lines.append(f"          ERROR: {e}")
            for w in r.get("warnings", []):
                lines.append(f"          WARN:  {w}")
        report = "\n".join(lines)
        if args.output:
            await asyncio.to_thread(Path(args.output).write_text, report, encoding="utf-8")
        else:
            print(report)

    sys.exit(0 if len(failed) == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
