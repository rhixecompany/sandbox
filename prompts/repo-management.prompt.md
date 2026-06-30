---
trigger: repo-management
name: repo-management
title: "Repo Management Pipeline"
description: >
  Execute repo management operations across all project repos: branch
  normalization, ignore file audit, dependency audit, and CI setup. Runs
  AFTER the repo-research-pipeline phase completes.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, repos, git, maintenance, ci]
dependencies:
  - skill:git-helper
  - skill:repo-research-pipeline
  - skill:web-research-pipeline
  - skill:github-repo-management
  - skill:finishing-a-development-branch
  - skill:workspace-audit
skills:
  - git-helper — Branch normalization and git workflow
  - repo-research-pipeline — Prerequisite research before management
  - web-research-pipeline — Web research for CI patterns and config
  - github-repo-management — Remote repo operations (default branch, settings)
  - finishing-a-development-branch — Clean branch lifecycle
  - workspace-audit — Multi-repo workspace scanning
metadata:
  hermes:
    related_skills:
      - git-helper
      - repo-research-pipeline
      - web-research-pipeline
      - github-repo-management
      - finishing-a-development-branch
      - workspace-audit
---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.

## Goal

Leave every repo with:
- Clean branch structure: `development` + `production` only
- Complete `.gitignore` with standard patterns
- Dependency files audited and pruned
- GitHub Actions CI workflows present

## Prerequisites

- [ ] `repo-research-pipeline` completed for this project
- [ ] Working directory is the SandBox root

## Workflow

### Phase 1: Branch Normalization

Per git-helper skill steps: normalize to `development` + `production`, set `production` as GitHub default.

```bash
git branch | grep -v -E "development|production" | xargs -r git branch -D
git push origin --delete <branch> || true
gh repo edit <owner>/<repo> --default-branch production
```

### Phase 2: Ignore File Audit

For each repo, verify `.gitignore` covers: `node_modules/`, `.env`, `*.pyc`, `__pycache__/`, `dist/`, `build/`, `.next/`, `venv/`, `.DS_Store`. Add missing entries.

### Phase 3: Dependency Audit

| Repo type | Tool | Audit command |
|-----------|------|---------------|
| JS/TS (Bun) | `bun pm ls` | `bun audit` for vulns |
| Python | `pip list` | `pip-audit` for vulns |

### Phase 4: CI Workflow Setup

Create `.github/workflows/ci.yml` per repo type (JS/TS uses `oven-sh/setup-bun`, Python uses `actions/setup-python`).

## Rules

1. **Prerequisite gate** — Confirm all RESEARCH_REPORT.md files exist before starting Phase 1.
2. **Verify after each pass** — After every phase, verify the result before moving on.
3. **Idempotent** — Safe to re-run without side effects.
4. **Rollback** — Every destructive operation records pre-state.

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
