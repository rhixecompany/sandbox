---
name: skills-debug-prompt
title: Skills Debug Execution Prompt
description: 'Execute the skills-debug remediation plan: fix C-grade skill issues (missing frontmatter fields, missing core sections), then bulk-fix B-grade frontmatter, verify with hermes skills check + re-audit, and commit.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets: [code_execution, file, terminal]
trigger: /skills-debug-prompt
tags: [skills, audit, remediation, fix]
---

# Skills Debug Execution Prompt

Execute the remediation plan at `docs/plan/skills-debug-plan.md` against the Hermes default skill library.

## Goal

Fix all remaining C-grade and B-grade skill issues found by the `/skills-fix` audit, verify the fixes, and commit.

## Context

- Skills root: `C:\Users\Alexa\AppData\Local\hermes\skills\`
- Audit results: `docs/skills-debug-context.md` (master index) + `docs/skills-audit/<skill>.md` (per-skill reports)
- Plan: `docs/plan/skills-debug-plan.md`
- Baseline: A=39 | A-=289 | B=241 | C=22 | F=0

## Rules

1. Fix in priority order: C-grade first, then B-grade.
2. Use `patch()` for targeted fixes; `write_file()` only for full rewrites.
3. Do not create backup files — git is the rollback mechanism.
4. Never delete a skill unless its canonical copy is verified (already done in Phase 1).
5. Preserve CRLF line endings on Windows skill files (normalize to LF only in memory).
6. Run `hermes skills check <name>` after each patch.
7. Keep `docs/plan/skills-debug-plan.md` checklist updated.
8. Do NOT rewrite working command examples; stale patterns (`pip install`) are documented warnings only.

## Steps

1. Load C-grade list from `docs/skills-debug-context.md`.
2. For each C-grade skill: add missing frontmatter `tags`, add compact missing core sections (derive trigger text from `description:`).
3. For each B-grade skill: bulk-add missing frontmatter `version: 1.0.0`, `author: Hermes Agent`, `license: MIT`, `tags: [imported]` (only where absent; preserve existing values).
4. Re-run audit script → verify F=0, record C/B delta.
5. Run `hermes skills check` on a sample of patched skills.
6. Update plan checklist; report deltas.
7. Commit: `chore(skills): remediate C/B-grade issues from skills-fix audit`.

## Verification Checklist

| # | Gate | Criterion |
|---|------|-----------|
| 1 | Scope | Only SKILL.md files under skills root touched |
| 2 | Quality | `hermes skills check` passes for patched skills |
| 3 | Tests | Re-audit shows F=0 and reduced C/B counts |
| 4 | Regression | No skills deleted, no canonical copies lost |
| 5 | Docs | Plan checklist + master index updated |
