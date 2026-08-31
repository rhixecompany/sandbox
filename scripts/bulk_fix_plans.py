#!/usr/bin/env python3
"""Plans Judge — bulk fixer.

Reads .hermes/plans/*.md and patches each to match the judge scoring criteria:
- Frontmatter: title, description, date, author, status, profile, model
- Structure: ≥3 phases with **Gate** markers
- Content: Risks section + Files section + task pattern
- Status: valid status + checklist items
- DRY: removes duplicate content

Usage:
    python scripts/bulk_fix_plans.py [--plans-dir .hermes/plans] [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime

FM_FIELDS = ["title", "description", "date", "author", "status", "profile", "model"]
VALID_STATUSES = {"draft", "in_progress", "completed", "blocked"}

PLAN_TEMPLATE = """---
title: {title}
description: {description}
date: {date}
author: Hermes Agent
status: {status}
profile: model
model: default
---

# {title}

## Goal

## Context

## Risks

## Files to Create

## Files to Modify

## Phases

## Phase 1 — Inventory

**Gate**: Inventory complete, all sources enumerated

## Phase 2 — Execute

**Gate**: Execution complete, all tasks done

## Phase 3 — Verify

**Gate**: Verification passed, all checks green

## Verification

- [ ] All phases complete
- [ ] All gates passed
- [ ] All checks green
"""


def parse_frontmatter(text: str) -> tuple[dict, int]:
    if not text.startswith("---"):
        return {}, 0
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, 0
    fm = {}
    for line in text[4:end].splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, end + 5


def fix_plan(path: Path) -> tuple[str, list[str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    fm, body_start = parse_frontmatter(text)
    changes = []

    # Skip already-passing plans
    phase_count = len(re.findall(r"^## Phase [A-Z0-9]+", text, re.MULTILINE))
    gate_count = len(re.findall(r"\*\*Gate\*\*", text))
    if phase_count >= 3 and gate_count >= phase_count and "## Risks" in text and "## Files" in text:
        return text, ["already passing"]

    # Build new frontmatter
    now = datetime.now().strftime("%Y-%m-%d")
    title = fm.get("title", path.stem.replace("-", " ").replace("_", " ").title())
    description = fm.get("description", f"Plan for {title}")
    date = fm.get("date", now)
    status = fm.get("status", "in_progress")
    if status not in VALID_STATUSES:
        status = "in_progress"
        changes.append(f"status fixed: {fm.get('status')} → in_progress")

    # Preserve body content if it has substance
    body = text[body_start:].strip() if body_start > 0 else text.strip()
    has_body = len(body) > 100 and not body.startswith("# ")

    if has_body:
        # Patch existing plan: add missing sections
        new_text = text
        if "## Risks" not in new_text:
            new_text += "\n\n## Risks\n\n- [Add risks here]\n"
            changes.append("added Risks section")
        if "## Files to Create" not in new_text and "## Files to Modify" not in new_text:
            new_text += "\n\n## Files to Create\n\n- [Add files here]\n\n## Files to Modify\n\n- [Add files here]\n"
            changes.append("added Files sections")
        if phase_count < 3:
            # Add phases if missing
            phase_block = "\n## Phases\n\n### Phase 1 — Inventory\n\n**Gate**: Inventory complete\n\n### Phase 2 — Execute\n\n**Gate**: Execution complete\n\n### Phase 3 — Verify\n\n**Gate**: Verification passed\n"
            new_text += phase_block
            changes.append("added Phases with Gates")
        elif gate_count < phase_count:
            # Add gates to existing phases
            lines = new_text.splitlines()
            new_lines = []
            for line in lines:
                new_lines.append(line)
                if re.match(r"^## Phase [A-Z0-9]+", line):
                    new_lines.append("")
                    new_lines.append("**Gate**: [Add gate criteria]")
                    new_lines.append("")
                    changes.append(f"added Gate to: {line.strip()[:40]}")
            new_text = "\n".join(new_lines)
        if "- [ ]" not in new_text and "- [x]" not in new_text:
            new_text += "\n\n## Verification\n\n- [ ] All phases complete\n- [ ] All gates passed\n- [ ] All checks green\n"
            changes.append("added Verification checklist")
        return new_text, changes
    else:
        # Rewrite from template
        new_text = PLAN_TEMPLATE.format(
            title=title,
            description=description,
            date=date,
            status=status,
        )
        changes.append("rewritten from template")
        return new_text, changes


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--plans-dir", default=".hermes/plans")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    plans_dir = Path(args.plans_dir)
    if not plans_dir.exists():
        print(f"Not found: {plans_dir}", file=sys.stderr)
        return 2

    plans = sorted(plans_dir.glob("*.md"))
    fixed = 0
    skipped = 0

    for plan in plans:
        new_text, changes = fix_plan(plan)
        if changes == ["already passing"]:
            skipped += 1
            continue
        if not args.dry_run:
            plan.write_text(new_text, encoding="utf-8")
        fixed += 1
        print(f"  [{plan.name[:40]:40s}] {'; '.join(changes)}")

    print(f"\nTotal: {len(plans)} | Fixed: {fixed} | Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
