---
status: completed
status: completed
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
