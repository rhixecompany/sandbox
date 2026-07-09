---
trigger: /plan-batch-fix
name: plan-batch-fix
title: "Batch Fix Errors, Warnings & Deprecations"
description: >
  Scan a codebase for errors, warnings, and deprecations, then fix them
  systematically in batches. Supports lint issues, TypeScript errors,
  deprecated API usage, and code quality problems.
version: 1.0.0
author: "Hermes Agent (consolidated)"
license: MIT
tags:
  - fix
  - linting
  - automation
  - hermes
  - prompts
  - code-quality
  - dry
dependencies:
  - skill:systematic-debugging
  - skill:subagent-driven-development
  - skill:simplify
  - skill:verification-before-completion
  - skill:brainstorming
  - tool:terminal
  - tool:search_files
skills:
  - systematic-debugging
  - subagent-driven-development
  - simplify
  - verification-before-completion
  - brainstorming
---

> **Shared template references:**
> - [Core rules](../prompts/templates/_shared/rules-core.md)
> - [Skills table](../prompts/templates/_shared/skills-table-core.md)
> - [Verification checklist](../prompts/templates/_shared/verification-checklist.md)

## Goal

Identify and fix all errors, warnings, and deprecations across a codebase. Operates in batches to avoid overwhelming context, with verification after each batch.

**Consolidates:** `plan-batch-fix-all-scan` + `plan-batch-fix-errors-warnings`
(which were near-duplicate prompts for the same purpose).

## Input

- **Target directory** — Codebase root to scan (default: workspace root)
- **Tools to run** — e.g. `tsc --noEmit`, `eslint .`, `pylint`, `cargo check`
- **Batch size** — Files to fix per batch (default: 7)
- **Ignore patterns** — Files/directories to skip

## Core Rules

See [`prompts/templates/_shared/rules-core.md`](../prompts/templates/_shared/rules-core.md).

Additional batch-fix rules:

1. **Scan before fix** — Always run the full scan first to understand scope.
2. **One category at a time** — Fix errors first, then warnings, then deprecations.
3. **Verify each batch** — Re-run the tool on the fixed files before moving on.
4. **No auto-ignore** — Don't silently skip hard errors; report them as blockers.
5. **Git commit per batch** — Every batch gets its own commit for easy rollback.

## Workflow

### Phase 1: Full scan

Run the relevant lint/type-check tool across the entire target:

```bash
# For TypeScript:
tsc --noEmit 2>&1 | tee docs/batch-fix-scan-results.txt

# For Python:
pylint **/*.py 2>&1 | tee docs/batch-fix-scan-results.txt

# For generalized errors:
grep -rn "error\|warning\|deprecated" src/ --include="*.ts" --include="*.tsx" > docs/batch-fix-scan-results.txt
```

Categorise issues:
- **High:** Compile/type errors (must fix)
- **Medium:** Warnings and lint violations (should fix)
- **Low:** Deprecation notices (fix when encountered)

### Phase 2: Batch fixes

For each batch (default: 7 files per batch):

1. Pick the batch of files with the highest-priority issues.
2. Fix each file using `systematic-debugging` approach.
3. Re-run the scan on the fixed files to confirm fix.
4. `git add -A && git commit -m "fix(batch): <tool> errors batch <N> — <files>"`

### Phase 3: Full re-scan

After all batches complete, run the full scan again.
- If zero errors remain → done.
- If errors remain but are pre-existing or out of scope → document in report.

### Phase 4: Report

Write report to `docs/batch-fix-report.md`:
- Total issues found: errors / warnings / deprecations
- Issues fixed: errors / warnings / deprecations
- Issues remaining: errors / warnings / deprecations
- Files modified
- Git commits

## Verification Checklist
- [ ] Full scan completed and results saved
- [ ] Errors fixed and verified per batch
- [ ] Warnings fixed and verified per batch
- [ ] Full re-scan shows reduction
- [ ] Git commits created per batch
- [ ] Report written with before/after counts
- [ ] No regressions introduced (tests pass if applicable)
