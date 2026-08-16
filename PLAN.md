---
name: SandBox-root
title: "SandBox-root — Plan"
description: "Plan for SandBox-root — AI-ready Bun monorepo, specs/plans for all repos, git commit/push"
version: 2.0.0
status: in_progress
created: 2026-08-16
tags: [plan, repo, ai-ready, bun, git]
---

# SandBox-root — Plan (v2)

## Overview

Standardize Bun as package manager across root + all subrepos, create/update SPEC.md and PLAN.md for every repo, validate, then git add/commit/push with zero errors.

## Stack

- Root: Bun 1.3.14 + TypeScript
- Subrepos: mixed (Bun, pnpm, pip, none)
- Tooling: eslint, prettier, typecheck, markdownlint, spellcheck, ruff, pyright

## Phases

### Phase 1: Root SPEC/PLAN validation
- [x] SPEC.md updated with full requirements/acceptance criteria (done)
- [x] PLAN.md updated with full phases (done)
- [ ] Run `bun run check` at root, triage failures

### Phase 2: Subrepo audit — package.json + SPEC + PLAN inventory
- [ ] For each subrepo, check: package.json exists, has bun packageManager, SPEC.md exists, PLAN.md exists
- [ ] Catalog gaps in a report file

### Phase 3: Add/repair package.json for subrepos missing Bun
- [ ] `projects/Python-projects/` — add package.json with bun packageManager (metadata only)
- [ ] `projects/cookiecutter-django-tailwind/` — add package.json with bun packageManager
- [ ] `projects/ecom/` — add package.json with bun packageManager
- [ ] `projects/profile/` — add package.json with bun packageManager
- [ ] `projects/xamehi.tv/` — add package.json with bun packageManager
- [ ] `projects/youtube-downloader/` — add package.json with bun packageManager
- [ ] `packages/openrouter-client-py/` — add pyproject.toml with bun metadata (or package.json if it has any TS)

### Phase 4: Fix pnpm → bun for comicwise
- [ ] `projects/comicwise/package.json` — change packageManager from pnpm to bun@1.3.14
- [ ] Delete `pnpm-lock.yaml` if present, create `bun.lock` via `bun install`

### Phase 5: Create missing SPEC.md + PLAN.md
- [ ] `packages/openrouter-client/` — SPEC.md + PLAN.md
- [ ] `packages/openrouter-client-py/` — SPEC.md + PLAN.md
- [ ] `projects/xamehi.tv/` — SPEC.md + PLAN.md
- [ ] `projects/youtube-downloader/` — SPEC.md + PLAN.md
- [ ] Any subrepo with SPEC.md status=not_started → update status

### Phase 6: Update existing PLAN.md files
- [ ] For each subrepo with PLAN.md, update status to in_progress, ensure phases are actionable
- [ ] For subrepos missing PLAN.md, create one

### Phase 7: Subrepo-level tooling checks
- [ ] For each subrepo with tooling: run `bun run check` or equivalent
- [ ] Triage failures: FIX vs REPORT

### Phase 8: Git operations — root
- [ ] `git add` all changed files at root
- [ ] `git commit` with conventional message
- [ ] `git push` to origin/development

### Phase 9: Git operations — submodules
- [ ] For each submodule: `cd` into it, `git add`, `git commit`, `git push`
- [ ] Handle any push failures (auth, conflicts) and retry

### Phase 10: Final validation
- [ ] Re-run `bun run check` at root
- [ ] Verify `git status` clean at root and all submodules
- [ ] Confirm all SPEC.md statuses are in_progress or done
- [ ] Report completion summary

## Acceptance

- [ ] Root SPEC.md: status in_progress, all requirements listed
- [ ] Root PLAN.md: status in_progress, all phases actionable
- [ ] All 13 submodules have package.json with bun packageManager (or metadata-only)
- [ ] All repos have SPEC.md with requirements + acceptance_criteria
- [ ] All repos have PLAN.md with phases + acceptance checklist
- [ ] Git add/commit/push succeeds at root with zero errors
- [ ] Git add/commit/push succeeds in every submodule with zero errors
- [ ] `bun run check` at root passes or failures are documented

## Risks

- Submodule push may fail if remote auth is stale — need `gh auth` or SSH key
- Some subrepos have no bun installable deps (pure Python/Django) — package.json is metadata only
- `bun run check` at root may surface pre-existing lint/format issues unrelated to this plan
