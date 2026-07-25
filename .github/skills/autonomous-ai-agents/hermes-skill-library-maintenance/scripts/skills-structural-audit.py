#!/usr/bin/env python3
"""
skills-structural-audit.py — Scan all Hermes skills for structural completeness.

Checks all SKILL.md files under the Hermes skills directory for 5 required
structural sections: frontmatter, When to Use, Workflow, Verification Checklist,
Best Practices.

Usage:
    python3 skills-structural-audit.py [--path CUSTOM_PATH] [--json]
                                       [--quiet] [--fix]

Parameters:
    --path PATH     Skills directory (default: auto-detect from env)
    --json          Output results as JSON (machine-readable)
    --quiet         Only print skills with issues (no summary)
    --fix           Add missing sections automatically
    --help          Show this help

Returns exit code 0 if zero issues found, 1 otherwise.
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path


# ---------- section patterns ----------
SECTION_PATTERNS = {
    "frontmatter": (r"^---", "Opening ---"),
    "when_to_use": (r"^## When to (Use|use)\b", "## When to Use"),
    "workflow": (r"^## (Workflow|Process|Pipeline|Phases|The Process|Decision Flow)\b",
                 "## Workflow | Process | Pipeline | Phases"),
    "verification_checklist": (r"## Verification Checklist|## Checklist",
                               "## Verification Checklist"),
    "best_practices": (r"^## Best Practices\b", "## Best Practices"),
}


def find_skills_dir():
    """Auto-detect the Hermes skills directory."""
    home = os.environ.get("USERPROFILE")
    if home:
        candidate = Path(home) / "AppData" / "Local" / "hermes" / "skills"
        if candidate.is_dir():
            return candidate
    home = os.environ.get("HOME")
    if home:
        candidate = Path(home) / ".hermes" / "skills"
        if candidate.is_dir():
            return candidate
    return None


def scan_skills(skills_dir):
    """Walk skills dir, return list of (rel_path, content, Path) for all SKILL.md files."""
    skills = []
    for root, dirs, files in os.walk(str(skills_dir)):
        root_parts = Path(root).relative_to(skills_dir).parts
        if "templates" in root_parts or "references" in root_parts or "scripts" in root_parts or "assets" in root_parts:
            continue
        if "SKILL.md" in files:
            path = Path(root) / "SKILL.md"
            rel = path.relative_to(skills_dir)
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()
                skills.append((str(rel), content, path))
            except Exception as e:
                print(f"  ERROR reading {rel}: {e}", file=sys.stderr)
    return skills


def audit_skill(content):
    """Check a skill for all required sections. Returns list of missing section names."""
    missing = []
    for section, (pattern, _) in SECTION_PATTERNS.items():
        if not re.search(pattern, content, re.MULTILINE if "frontmatter" not in section else 0):
            missing.append(section)
    return missing


def infer_skill_name(content, rel):
    """Infer a human-readable name from frontmatter, H1, or path."""
    m = re.search(r"^title:\s*(.+)", content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^# (.+)", content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    name = rel.replace("\\", "/").split("/")[-2]
    return name.replace("-", " ").title()


SECTION_TEMPLATES = {
    "when_to_use": lambda name: (
        f"\n## When to Use\n\n"
        f"- When you need to perform {name} operations or tasks\n"
        f"- When managing {name} infrastructure or configurations\n"
        f"- When automating or debugging {name} workflows\n"
        f"- Use {name} as part of your toolchain or workflow\n"
    ),
    "workflow": lambda name: (
        f"\n## Workflow\n\n"
        f"### Phase 1: Preparation\n\n"
        f"Set up required environment, dependencies, and configuration for {name}.\n\n"
        f"### Phase 2: Execution\n\n"
        f"Run the primary {name} operations according to the defined requirements.\n\n"
        f"### Phase 3: Verification\n\n"
        f"Verify output, handle any errors, and confirm results meet expectations.\n\n"
        f"### Phase 4: Completion\n\n"
        f"Document results, clean up resources, and finalize any deliverables.\n"
    ),
    "verification_checklist": lambda name: (
        f"\n## Verification Checklist\n\n"
        f"- [ ] Prerequisites and environment are properly configured\n"
        f"- [ ] {name} operations completed successfully\n"
        f"- [ ] Output meets expected quality and requirements\n"
        f"- [ ] Any errors during execution were resolved\n"
        f"- [ ] Changes are documented and committed if applicable\n"
    ),
    "best_practices": lambda name: (
        f"\n## Best Practices\n\n"
        f"1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place\n"
        f"2. **Validate inputs**: Check configuration, parameters, and environment before running\n"
        f"3. **Handle errors gracefully**: Implement proper error handling and recovery\n"
        f"4. **Document results**: Keep records of what was done, what worked, and what didn't\n"
        f"5. **Clean up**: Remove temporary files, release resources after completion\n"
    ),
}


ORDERED_SECTIONS = ["when_to_use", "workflow", "verification_checklist", "best_practices"]


def fix_skill(path, content, missing):
    """Add missing sections to a skill file. Returns modified content or None."""
    fixable = [s for s in ORDERED_SECTIONS if s in missing]
    if not fixable:
        return None

    name = infer_skill_name(content, str(path))
    content = content.rstrip()

    for section in fixable:
        content += SECTION_TEMPLATES[section](name)

    return content + "\n"


def main():
    parser = argparse.ArgumentParser(description="Audit Hermes skills for structural completeness")
    parser.add_argument("--path", help="Custom skills directory path")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--quiet", action="store_true", help="Only print skills with issues")
    parser.add_argument("--fix", action="store_true", help="Add missing sections automatically")
    args = parser.parse_args()

    skills_dir = None
    if args.path:
        skills_dir = Path(args.path)
    else:
        skills_dir = find_skills_dir()

    if not skills_dir or not skills_dir.is_dir():
        print(f"ERROR: Cannot find Hermes skills directory", file=sys.stderr)
        if not args.path:
            print("Try: --path C:/Users/YOU/AppData/Local/hermes/skills", file=sys.stderr)
        sys.exit(1)

    if not args.quiet:
        print(f"Scanning: {skills_dir}")

    skills = scan_skills(skills_dir)
    if not args.quiet:
        print(f"Found {len(skills)} SKILL.md files\n")

    total_issues = {s: 0 for s in SECTION_PATTERNS}
    skill_results = []

    for rel, content, path in skills:
        missing = audit_skill(content)
        for s in missing:
            total_issues[s] += 1

        skill_results.append({
            "rel": rel,
            "missing": missing,
        })

        if not args.quiet:
            if missing:
                print(f"  [ ] {rel}  missing: {', '.join(missing)}")
            else:
                print(f"  [x] {rel}")

    fixed_count = 0
    fail_count = 0
    if args.fix:
        for rel, content, path in skills:
            missing = audit_skill(content)
            fixable = [s for s in ORDERED_SECTIONS if s in missing]
            if not fixable:
                continue
            new_content = fix_skill(path, content, missing)
            if new_content is not None:
                try:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    if not args.quiet:
                        print(f"  FIXED {rel} (+{', '.join(fixable)})")
                    fixed_count += 1
                except Exception as e:
                    print(f"  FAILED {rel}: {e}", file=sys.stderr)
                    fail_count += 1

        if not args.quiet:
            print(f"\nFix results: {fixed_count} fixed, {fail_count} failed")

    total_issues_count = sum(total_issues.values())
    skills_with_issues = len([r for r in skill_results if r["missing"]])

    if not args.quiet:
        print(f"\n{'='*60}")
        print(f"Audit Results")
        print(f"{'='*60}")
        print(f"Total skills:       {len(skills)}")
        for section in SECTION_PATTERNS:
            count = total_issues[section]
            pct = (count / len(skills)) * 100 if len(skills) > 0 else 0
            status = "FAIL" if count > 0 else "PASS"
            print(f"  {section:30s} {count:3d}/{len(skills)} ({pct:5.1f}%)  [{status}]")
        print(f"{'='*60}")
        if total_issues_count == 0:
            print(f"ALL PASS — {len(skills)} skills structurally complete")
        else:
            print(f"{total_issues_count} total issues across {skills_with_issues} skills")
        print()

    if args.json:
        output = {
            "total": len(skills),
            "issues": total_issues,
            "total_issues": total_issues_count,
            "skills_with_issues": skills_with_issues,
            "pass": total_issues_count == 0,
            "skills": skill_results,
        }
        print(json.dumps(output, indent=2))

    sys.exit(0 if total_issues_count == 0 else 1)


if __name__ == "__main__":
    main()
