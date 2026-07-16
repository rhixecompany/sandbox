---
trigger: /repo-management
name: repo-management
title: Repo Management Pipeline
description: 'Execute repo management operations across all project repos: branch
  normalization, ignore file audit, dependency audit, and CI setup. Runs AFTER the
  repo-research-pipeline phase completes.

  Also provides Quick Repo Overview (Phase 0): repo summary, entrypoint detection,
  and disk usage on demand.

  '
version: 2.1.0
author: Hermes Agent
license: MIT
tags:
- audit
- frontend
- git
- mcp
- onboarding
- prompts
- skills
- vscode
- workflow
dependencies:
- skill:finishing-a-development-branch
- skill:gh-cli
- skill:git-commit
- skill:git-helper
- skill:git-submodule-workflow
- skill:github-actions-efficiency
- skill:github-repo-management
- skill:mcp-filesystem
- skill:mcp-sequential-thinking
- skill:monorepo-pr-workflow
- skill:repo-research-pipeline
- skill:vscode-cli
- skill:vscode-workspace-configurator
- skill:web-research-pipeline
- skill:workspace-audit
- skill:writing-plans
skills:
- finishing-a-development-branch
- gh-cli
- git-commit
- git-helper
- git-submodule-workflow
- github-actions-efficiency
- github-repo-management
- mcp-filesystem
- mcp-sequential-thinking
- monorepo-pr-workflow
- repo-research-pipeline
- vscode-cli
- vscode-workspace-configurator
- web-research-pipeline
- workspace-audit
- writing-plans
metadata:
  hermes:
    related_skills:
    - finishing-a-development-branch
    - gh-cli
    - git-commit
    - git-helper
    - git-submodule-workflow
    - github-actions-efficiency
    - github-repo-management
    - mcp-filesystem
    - mcp-sequential-thinking
    - monorepo-pr-workflow
    - repo-research-pipeline
    - vscode-cli
    - vscode-workspace-configurator
    - web-research-pipeline
    - workspace-audit
toolsets:
- browser
- code_execution
- file
- terminal
---
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

### Phase 0: Repo Overview (Onboarding)

Run when the user asks about repo structure, disk usage, or needs an initial summary.

**Steps:**
1. **Summarize the repo** — Read AGENTS.md, README.md, package manifest. 5 bullets + entrypoint.
2. **Check disk usage** — Scan from repo root, exclude noise dirs, show top 5.
3. **Detect CI status** — Check if `.github/workflows/` exists.

```bash
# Disk usage
du -sh --exclude='.git' --exclude='node_modules' --exclude='venv' --exclude='__pycache__' --exclude='dist' --exclude='build' --exclude='target' */ 2>/dev/null | sort -rh | head -5

# Entrypoint detection
grep -E '"main"|"start"|main\.py|def main|if __name__|fn main' package.json pyproject.toml src/*.{py,ts} 2>/dev/null | head -10
```

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
