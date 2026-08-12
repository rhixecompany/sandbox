---
name: repo-management
title: Repo Management Pipeline
description: 'Execute repo management operations across all project repos: branch
  normalization, ignore file audit, dependency audit, and CI setup. Runs AFTER the
  repo-research-pipeline phase completes. Also provides Quick Repo Overview (Phase
  0): repo summary, entrypoint detection, and disk usage on demand.'
version: 2.2.0
license: MIT
author: Hermes Agent
toolsets:
- browser
- code_execution
- file
- mcp
- terminal
- web
scripts: []
skills:
- finishing-a-development-branch
- gh-cli
- git-commit
- git-helper
- git-submodule-workflow
- github-actions-efficiency
- github-repo-management
- vscode-workspace-configurator
- workspace-audit
- writing-plans
- subagent-driven-development
formatter: default
plan: null
dependencies:
- prompt:repo-research-pipeline
- skill:finishing-a-development-branch
- skill:gh-cli
- skill:git-commit
- skill:git-helper
- skill:git-submodule-workflow
- skill:github-actions-efficiency
- skill:github-repo-management
- skill:vscode-workspace-configurator
- skill:workspace-audit
- skill:writing-plans
- tool:mcp-tavily
- tool:mcp-filesystem
- tool:mcp-sequential-thinking
- skill:subagent-driven-development
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
trigger: /repo-management
metadata:
  hermes: {}
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

> **⚠️ Destructive — requires explicit approval.** Deleting branches (local + remote) is irreversible. Do NOT execute the deletion commands until the user has approved the exact branch list.

**Steps:**

1. **Dry-run inventory:** list every branch that is NOT `development`/`production`:
   `git branch | grep -v -E "development|production"`
2. **Show remote candidates:** `git branch -r | grep -v -E "development|production"` — confirm which branches exist on origin.
3. **Present the list to the user** with a proposed action per branch (delete local / delete remote / keep). Wait for explicit typed approval (e.g. `approved`) before running any deletion.
4. **Execute only after approval:**

   ```bash
   # Local: delete one branch at a time after approval
   git branch -D <branch>
   # Remote: delete one branch at a time after approval
   git push origin --delete <branch> || true
   ```

5. **Set default branch:** `gh repo edit <owner>/<repo> --default-branch production`
6. **Verify:** `git branch` shows only `development` + `production`.

**Rollback:** a deleted local branch can be restored via `git reflog` if not yet pruned; a deleted remote branch can be re-pushed from its local ref if the local branch still exists. Record pre-state (`git branch -a` output) before deletion.

```bash
# NEVER run this without per-branch approval:
# git branch | grep -v -E "development|production" | xargs -r git branch -D
# git push origin --delete <branch> || true
```

### Phase 2: Ignore File Audit

For each repo, verify `.gitignore` covers: `node_modules/`, `.env`, `*.pyc`, `__pycache__/`, `dist/`, `build/`, `.next/`, `venv/`, `.DS_Store`. Add missing entries.

### Phase 3: Dependency Audit

| Repo type   | Tool        | Audit command         |
| ----------- | ----------- | --------------------- |
| JS/TS (Bun) | `bun pm ls` | `bun audit` for vulns |
| Python      | `pip list`  | `pip-audit` for vulns |

### Phase 4: CI Workflow Setup

Create `.github/workflows/ci.yml` per repo type (JS/TS uses `oven-sh/setup-bun`, Python uses `actions/setup-python`).

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. **Prerequisite gate** — Confirm all RESEARCH_REPORT.md files exist before starting Phase 1.
2. **Verify after each pass** — After every phase, verify the result before moving on.
3. **Idempotent** — Safe to re-run without side effects.
4. **Rollback** — Every destructive operation records pre-state.

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona       | When to Use                            |
| ------------- | -------------------------------------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer**  | Code review, quality assurance         |
| **User**      | General purpose, operations            |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate       | Criterion                           |
| - | ---------- | ----------------------------------- |
| 1 | Scope      | Change matches the original request |
| 2 | Quality    | Meets project standards             |
| 3 | Tests      | Tests pass (if applicable)          |
| 4 | Regression | No unintended side effects          |
| 5 | Docs       | Changes documented if needed        |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill                            | Purpose                       |
| -------------------------------- | ----------------------------- |
| `using-superpowers`              | Foundational skill workflow   |
| `systematic-debugging`           | Root cause analysis and fix   |
| `git-patch-management`           | Patch creation and management |
| `executing-plans`                | Execute plans step by step    |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| Server                | Purpose                                   |
| --------------------- | ----------------------------------------- |
| `tavily`              | Web search + URL extraction               |
| `filesystem`          | File read/write operations                |
| `github`              | GitHub API operations                     |
| `sequential-thinking` | Structured reasoning for complex problems |
| `ast-grep`            | AST-based code search and replace         |
| `fetch`               | Web page content extraction               |
| `playwright`          | Browser automation for interactive pages  |

## Hooks

The following workspace hooks run around this prompt's execution (see `.github/hooks/README.md`):

| Hook                     | When              | Behavior                     |
| ------------------------ | ----------------- | ---------------------------- |
| `session-logger`         | session start/end | Logs session metadata        |
| `governance-audit`       | session events    | Audits governance compliance |
| `session-auto-commit`    | session end       | Auto-commits session state   |
| `pre-exec-validate.sh`   | before commands   | Validates command execution  |
| `post-exec-state-log.py` | after commands    | Appends state log            |

## Scripts

- `scripts/repo-init.py` — Scaffold/verify AI-agent context files for a repo (see repo-init.prompt.md)
- `.github/prompts/.enhance/analyze_prompts.py` — Prompt-library analyzer (audit/verify)
- `.github/hooks/*` — Hook implementations listed in the Hooks section

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions
