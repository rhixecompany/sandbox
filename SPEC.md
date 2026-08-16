---
name: SandBox-root
title: "SandBox-root — Spec"
description: "Spec for SandBox-root — AI-ready Bun monorepo with full plan/spec coverage across root and all subrepos"
version: 2.0.0
status: in_progress
created: 2026-08-16
tags: [spec, repo, ai-ready, bun]
requirements:
  - R1: Root workspace uses Bun as package manager with bun.lock (already met)
  - R2: All subrepos that have a package.json use Bun as packageManager
  - R3: All subrepos without package.json get a Bun-based package.json added
  - R4: Each repo (root + subrepos) has a SPEC.md and PLAN.md with status in_progress
  - R5: All SPEC.md files have requirements and acceptance_criteria sections
  - R6: All PLAN.md files have phases and acceptance criteria
  - R7: Git add/commit/push succeeds on root and all subrepos with no errors
  - R8: toolings (lint, format, typecheck, markdownlint, spellcheck) pass or findings are triaged
acceptance_criteria:
  - AC1: Root package.json has "packageManager": "bun@1.3.14" (verified)
  - AC2: All subrepos with package.json have "packageManager": "bun@<version>" 
  - AC3: All subrepos without package.json have one added with Bun as manager
  - AC4: SPEC.md exists and is valid (status != not_started) for root + each subrepo
  - AC5: PLAN.md exists and is valid (status != not_started) for root + each subrepo
  - AC6: Git operations succeed with zero errors across all repos
  - AC7: bun run check passes at root (or failing items are documented as REPORT debt)
  - AC8: Subrepo-level checks pass where tooling exists
---

# SandBox-root — Spec (v2)

## Purpose

Make the SandBox workspace and all its subrepos AI-ready by standardizing on Bun as the package manager, creating/updating SPEC.md and PLAN.md for every repo, and committing all changes with zero git errors.

## Scope

### Repos in scope

| Repo | Path | Current PM | Has PKG | Has SPEC | Has PLAN | Action |
|------|------|-----------|---------|----------|----------|--------|
| SandBox-root | `.` | bun | yes | yes (stub) | yes (in_progress) | Update SPEC/PLAN |
| Banking | `projects/Banking` | bun | yes | yes | yes | Verify/update |
| comicwise | `projects/comicwise` | pnpm | yes | yes | ? | Switch to bun + add PLAN |
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | bun | yes | yes | ? | Add PLAN |
| Python-projects | `projects/Python-projects` | none | no | yes | yes | Add bun PKG |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | none | no | yes | ? | Add bun PKG + PLAN |
| ecom | `projects/ecom` | none | no | yes | ? | Add bun PKG + PLAN |
| profile | `projects/profile` | none | no | yes | ? | Add bun PKG + PLAN |
| rhixe_scans | `projects/rhixe_scans` | bun | yes | yes | ? | Add PLAN |
| selenium_webdriver | `projects/selenium_webdriver` | bun | yes | yes | ? | Add PLAN |
| university-libary-jsm | `projects/university-libary-jsm` | bun | yes | yes | ? | Add PLAN |
| xamehi | `projects/xamehi` | bun | yes | yes | ? | Add PLAN |
| xamehi.tv | `projects/xamehi.tv` | none | no | ? | ? | Add bun PKG + SPEC + PLAN |
| youtube-downloader | `projects/youtube-downloader` | none | no | ? | ? | Add bun PKG + SPEC + PLAN |
| openrouter-client | `packages/openrouter-client` | bun | yes | no | no | Add SPEC + PLAN |
| openrouter-client-py | `packages/openrouter-client-py` | pip | no | no | no | Add pyproject + SPEC |

## Requirements

### R1: Bun standardization
Every repo with a JavaScript/TypeScript component must declare `"packageManager": "bun@X.Y.Z"` in its package.json, matching the version locked in the root bun.lock.

### R2: Spec completeness  
Every repo must have a SPEC.md with:
- YAML frontmatter (name, title, description, version, status, tags, requirements, acceptance_criteria)
- Purpose section
- Requirements list (R1, R2, ...)
- Acceptance criteria list (AC1, AC2, ...)
- Status: in_progress during implementation, done when complete

### R3: Plan completeness
Every repo must have a PLAN.md with:
- YAML frontmatter (name, title, description, version, status, created, tags)
- Overview section
- Phases (numbered, with actionable steps)
- Acceptance criteria checklist
- Status: in_progress → done

### R4: Git hygiene
All repos must be clean after changes:
- `git status` shows no uncommitted changes
- `git push` succeeds for root and each submodule
- No merge conflicts from parallel work

### R5: Tooling pass
Where tooling exists (eslint, prettier, typecheck, markdownlint, spellcheck), run and either pass or document as REPORT debt.

## Out of Scope

- Subrepo internal code changes beyond package.json/SPEC/PLAN additions
- Python subrepos that have no JS/TS component (cookiecutter-django-tailwind, ecom backend, profile) — add minimal package.json for Bun metadata only
- Credential or secrets handling
