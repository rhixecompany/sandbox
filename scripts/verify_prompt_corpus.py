#!/usr/bin/env python3
"""Verify all .prompt.md files in .github/prompts/ meet schema + structural standards.

Exit codes:
  0 - all green
  1 - high-severity issues found
  2 - parse error in frontmatter
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

PROMPTS_DIR = Path(__file__).resolve().parent.parent / ".github" / "prompts"
REQUIRED_FIELDS = {"name", "title", "description", "version", "author", "tags"}


def audit_one(path: Path) -> dict:
    issues: list[str] = []
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return {"file": path.name, "fatal": f"read error: {e}", "issues": ["FATAL"]}

    if not content.startswith("---"):
        return {"file": path.name, "fatal": "no frontmatter", "issues": ["HIGH: no frontmatter"]}

    # find first `---` close
    end = content.find("\n---", 3)
    if end == -1:
        return {"file": path.name, "fatal": "unterminated frontmatter", "issues": ["HIGH: bad yaml"]}

    fm_text = content[3:end]
    body = content[end + 4 :]

    # parse yaml
    try:
        fm = yaml.safe_load(fm_text)
        if not isinstance(fm, dict):
            issues.append("HIGH: frontmatter is not a mapping")
            fm = {}
    except yaml.YAMLError as e:
        issues.append(f"HIGH: yaml parse error: {e}")
        fm = {}

    # required fields
    for f in REQUIRED_FIELDS:
        if f not in fm:
            issues.append(f"HIGH: missing field '{f}'")
        elif f in ("name", "title", "description", "version", "author") and not fm[f]:
            issues.append(f"HIGH: empty field '{f}'")

    # tag count
    tags = fm.get("tags", [])
    if isinstance(tags, list):
        if len(tags) < 5:
            issues.append(f"MED: only {len(tags)} tags (want 5-12)")
        elif len(tags) > 12:
            issues.append(f"LOW: {len(tags)} tags (want 5-12)")

    # body checks
    body_lines = len([l for l in body.strip().splitlines() if l.strip()])
    if body_lines < 20:
        issues.append(f"HIGH: thin body ({body_lines} lines)")

    # double fence
    fence_count = len(re.findall(r"^---\s*$", content[:2000], re.M))
    if fence_count > 2:
        issues.append(f"HIGH: double frontmatter fence ({fence_count})")

    # merged close fence
    if "---##" in content[:200] or "|---##" in content[:200]:
        issues.append("HIGH: merged close fence")

    # name matches filename
    expected_name = path.name.replace(".prompt.md", "")
    if fm.get("name") and fm["name"] != expected_name:
        issues.append(f"MED: name '{fm['name']}' != filename stem '{expected_name}'")

    return {
        "file": path.name,
        "size": len(content),
        "body_lines": body_lines,
        "tags_count": len(tags) if isinstance(tags, list) else 0,
        "issues": issues,
    }


def main() -> int:
    files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    print(f"Auditing {len(files)} prompt files in {PROMPTS_DIR}\n")

    results = [audit_one(f) for f in files]

    high = sum(1 for r in results if any("HIGH" in i for i in r["issues"]))
    med = sum(1 for r in results if any("MED" in i for i in r["issues"]))
    low = sum(1 for r in results if any("LOW" in i for i in r["issues"]))
    clean = sum(1 for r in results if not r["issues"])

    print(f"Summary: {len(results)} files")
    print(f"  Clean:    {clean}")
    print(f"  HIGH:     {high}")
    print(f"  MED:      {med}")
    print(f"  LOW:      {low}")
    print()

    if high or med:
        print("Issues by file (HIGH/MED only):")
        for r in results:
            real = [i for i in r["issues"] if "HIGH" in i or "MED" in i]
            if real:
                print(f"  {r['file']:55s} {r.get('body_lines', 0):4d} lines  {r.get('tags_count', 0):2d} tags")
                for i in real:
                    print(f"      - {i}")

    if high:
        print(f"\nFAIL: {high} files have HIGH-severity issues", file=sys.stderr)
        return 1
    print("\nPASS: no high-severity issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
