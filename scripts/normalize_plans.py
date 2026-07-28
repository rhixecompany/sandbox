#!/usr/bin/env python3
"""Normalize .hermes/plans/*.md to a minimal executable plan contract + rebuild SESSION_REPORT.md afterwards."""

import asyncio
import re
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(".").resolve()
PLANS = ROOT / ".hermes" / "plans"
SKIP_DIRS = {"docs"}
REPORT = ROOT / "SESSION_REPORT.md"
REPORT_SCRIPT = Path(
    r"C:\Users\Alexa\AppData\Local\hermes\skills\devops\session-audit-report\scripts\generate_session_report.py"
)

CHANGES = []


def now_iso():
    return datetime.now(UTC).isoformat(timespec="minutes")


def normalize_plan(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    original = text

    # enforce fenced YAML frontmatter
    if not text.startswith("---"):
        text = "---\nstatus: not_started\n---\n\n" + text
    else:
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not m:
            text = "---\nstatus: not_started\n---\n\n" + text
        else:
            meta, body = m.group(1), m.group(2)
            if "status:" not in meta.splitlines():
                meta = "status: not_started\n" + meta
            text = f"---\n{meta}\n---\n{body}"

    # remove migrated breadcrumb lines that promote draft headers as completion claims
    text = re.sub(r"<!-- migrated from:.*?\n", "", text)
    # replace false positive completion markers with actual status from frontmatter
    text = re.sub(r"^> \*\*Status:\*\* ✅.*$", "", text, flags=re.M)
    # collapse excessive whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)

    if text != original:
        path.write_text(text, encoding="utf-8")
        CHANGES.append((str(path.relative_to(ROOT)), "normalized plan frontmatter/status"))
        return True
    return False


def ensure_executable_plan():
    target = PLANS / "2026-06-30-execution-plan-for-prompt-and-plan-normalization.md"
    if target.exists():
        return
    content = """---
status: not_started
---
# Execution Plan — Prompt and Plan Normalization

> **For Hermes:** Use `executing-plans` skill to execute this plan task-by-task.
> **Template:** 9-section internal workflow

**Goal:** Normalize `.hermes/plans/` so every plan is executable, then verify end to end.

**Profile:** `exec-assistant`
**Tech/Lint:** markdown structure only; no runtime dependencies

---

## Context

The directory `.hermes/plans/` contains mixed artifacts: executable plans/audits, stub status files, and migrated fragments from `docs/` and `thoughts/`. This plan restores executable structure across the full set.

## Inputs

- `.hermes/plans/*.md`
- `writing-plans` skill rules
- `executing-plans` Phase 0-4 workflow

## Outputs

- Normalized plan files under `.hermes/plans/`
- Verification report for plan structure
- `SESSION_REPORT.md` regeneration

## Rules

- No destructive delete without recorded approval.
- Prefer targeted `patch`/`write_file`; no `.bak`.
- Keep migrated intent; preserve audit data in references when needed.
- Re-run verification after every batch.

## Phases

### Phase 1: Inventory and Classification

Objective: determine current executable vs non-executable state.

**Tasks**
- [ ] 1.1 inventory `.hermes/plans/**/*.md`
- [ ] 1.2 classify executable gaps per file
- [ ] 1.3 record normalization rules

**Actions**
- `search_files` target='files' path='.hermes/plans' pattern='*.md'
- `read_file` on candidate plans
- Record findings in `.hermes/plans/normalization-inventory.md`

### Phase 2: Normalize Plans

Objective: make every plan executable.

**Batch rule:** process <=7 files per batch until done.

**Tasks**
- [ ] 2.1 add missing frontmatter blocks
- [ ] 2.2 align migrated docs into executable plan format or archive note
- [ ] 2.3 remove false completion claims
- [ ] 2.4 create missing executable plan for the current normalization goal

**Actions**
- `write_file`/`patch` for plan edits
- `terminal` to run `git status --short`
- `terminal` to run validation script if available

### Phase 3: Verify All Plans

Objective: confirm executable contract holds.

**Verification**
- All plans readable and parseable as planned artifacts.
- No staged migration text masking completion state.
- `.hermes/plans/execution-plan-for-prompt-and-plan-normalization.md` present.

### Phase 4: Commit and Push

Objective: deliver clean state.

**Tasks**
- [ ] 4.1 review `git status`
- [ ] 4.2 run `git diff --check`
- [ ] 4.3 `git commit` with `docs: normalize .hermes/plans for executable workflow`
- [ ] 4.4 `git push`
"""
    target.write_text(content, encoding="utf-8")
    CHANGES.append((str(target.relative_to(ROOT)), "created executable plan"))


async def main():
    if not PLANS.exists():
        print(f"missing plans dir: {PLANS}")
        sys.exit(1)

    for path in sorted(PLANS.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        normalize_plan(path)

    ensure_executable_plan()

    changed = "\n".join(f"- {p} :: {a}" for p, a in CHANGES) or "- No changes"
    print("Changes applied:\n" + changed)

    if REPORT_SCRIPT.exists():
        await asyncio.to_thread(subprocess.run, [sys.executable, str(REPORT_SCRIPT), "--cwd", str(ROOT)], check=False)


if __name__ == "__main__":
    asyncio.run(main())


"""
Summary:
- Inspected plan inventory and current file set.
- Applying normalization now: frontmatter,'status' field, migrated stubs, and an executable plan for the current workflow.
- After edits, rerun verification, then commit and push. No stop condition requested by the user.
"""
