#!/usr/bin/env python3
"""Skill Audit — Audit skill files for quality and completeness.

Provides async entry points for validating skill frontmatter, required
sections, and structural integrity.
"""

import asyncio
import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Tuple


REQUIRED_FRONTMATTER = {"name", "title", "description", "version", "author"}


def check_frontmatter(path: Path, content: str) -> Tuple[int, List[str]]:
    """Validate YAML frontmatter has required fields."""
    notes = []
    if not content.startswith("---"):
        return 0, ["Missing frontmatter delimiter"]
    end = content.find("---", 3)
    if end == -1:
        return 0, ["Frontmatter not closed"]
    fm = content[3:end]
    found = set(re.findall(r"^(\w+)\s*:", fm, re.MULTILINE))
    missing = REQUIRED_FRONTMATTER - found
    if missing:
        notes.append(f"Missing frontmatter fields: {', '.join(sorted(missing))}")
        return max(0, 20 - len(missing) * 5), notes
    return 20, notes


def check_sections(content: str) -> Tuple[int, List[str]]:
    """Check for required sections."""
    notes = []
    required = ["Overview", "Usage"]
    has_h2 = re.findall(r"^##\s+(.+)$", content, re.MULTILINE)
    missing = [s for s in required if s not in has_h2]
    score = 20
    if missing:
        notes.append(f"Missing sections: {', '.join(missing)}")
        score -= 10 * len(missing)
    return max(0, score), notes


async def audit_skill(file_path: Path) -> dict:
    """Audit a single skill markdown file."""
    try:
        content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    except Exception as exc:
        return {"file": str(file_path), "error": str(exc), "passed": False}

    fm_score, fm_notes = check_frontmatter(file_path, content)
    sec_score, sec_notes = check_sections(content)

    total = fm_score + sec_score
    notes = fm_notes + sec_notes
    passed = total >= 30

    return {
        "file": str(file_path),
        "scores": {"frontmatter": fm_score, "sections": sec_score},
        "total": total,
        "notes": notes,
        "passed": passed,
    }


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit skill files for quality and completeness."
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
        default="**/SKILL.md",
        help="File glob pattern (default: **/SKILL.md)",
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
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    files = list(workspace.glob(args.pattern))
    if not files:
        print(f"No files matching {args.pattern} in {workspace}", file=sys.stderr)
        sys.exit(1)

    results = await asyncio.gather(*(audit_skill(f) for f in files))

    passed = [r for r in results if r.get("passed")]
    failed = [r for r in results if not r.get("passed")]

    if args.json:
        output = json.dumps(
            {"results": results, "passed": len(passed), "failed": len(failed)},
            indent=2,
        )
        if args.output:
            await asyncio.to_thread(
                Path(args.output).write_text, output, encoding="utf-8"
            )
        else:
            print(output)
    else:
        lines = [f"\n=== Skill Audit Report ==="]
        lines.append(f"Scanned {len(files)} file(s) — Passed: {len(passed)}, Failed: {len(failed)}")
        for r in results:
            status = "PASS" if r.get("passed") else "FAIL"
            total = r.get("total", 0)
            lines.append(f"  [{status}] {total:3d}  {r['file']}")
            for note in r.get("notes", []):
                lines.append(f"          - {note}")
            if r.get("error"):
                lines.append(f"          ERROR: {r['error']}")
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
