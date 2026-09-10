---
name: run-all-goals
title: "Run All Goals — Comprehensive Implementation Pipeline (tree-Primary v3.0)"
description: >
  tree.prompt.txt PRIMARY source. Cleanup-first execution pipeline:
  delete workspace clutter, update config files, convert mjs->mts,
  migrate source code, then sync agents and verify at score >= 99.
  tree.prompt.txt defines GOAL 1 (Cleanup), GOAL 2 (Config),
  GOAL 3 (mjs->mts), GOAL 4 (Pipeline).
version: 3.0.0
author: Alexa
license: MIT
tags:
  - implementation
  - execution
  - audit
  - verification
  - systematic-debugging
  - subagent-driven-development
  - brainstorming
  - unified-pipeline
  - score-99
  - tree-primary
dependencies:
  - skill:using-superpowers
  - skill:brainstorming
  - skill:user-communication-preferences
  - skill:mcp-sequential-thinking
  - skill:systematic-debugging
  - skill:subagent-driven-development
  - skill:hermes-diagnostic-repair
  - skill:log-analysis-and-triage
  - skill:plans-and-specs
  - skill:create-implementation-plan
  - skill:implementation-plan
  - skill:executing-plans
  - skill:writing-clearly-and-concisely
  - skill:skill-creator
  - skill:prompt-management
  - skill:skill-judge
  - skill:prompts-judge
  - skill:plans-judge
  - skill:specs-judge
  - tool:filesystem
  - tool:github
  - tool:memory
  - tool:playwright
  - tool:sequential-thinking
  - tool:ast-grep
  - tool:code-sandbox
  - tool:fetch
  - tool:tavily
  - tool:mcp-docker
  - tool:neon
  - tool:honcho
  - tool:context7
  - tool:python-quality
  - tool:tooling-config
  - tool:tooling-lint
skills:
  - using-superpowers
  - brainstorming
  - user-communication-preferences
  - mcp-sequential-thinking
  - systematic-debugging
  - subagent-driven-development
  - hermes-diagnostic-repair
  - log-analysis-and-triage
  - plans-and-specs
  - create-implementation-plan
  - implementation-plan
  - executing-plans
  - writing-clearly-and-concisely
  - skill-creator
  - prompt-management
  - skill-judge
  - prompts-judge
  - plans-judge
  - specs-judge
triggers:
  - /run-all-goals
toolsets:
  - terminal
  - filesystem
  - git
  - python-quality
  - code-sandbox
personality: patient-tutor
provider: openrouter
model: thinkingmachines/inkling:free
profile: adminbot
category: general
trigger: /run-all-goals
references:
  - templates/_shared/rules-core.md
  - templates/_shared/deps-core.md
  - templates/_shared/section-skeleton.md
  - templates/_shared/skills-table-core.md
  - templates/_shared/verification-checklist.md
  - templates/_shared/best-practices.md
  - references/prompt-workflow.md
  - references/session-reporting.md
  - references/batch-skill-injection.md
  - references/workspace-references.md
  - references/run-all-goals-verified-pattern.md
---

# Goal: /run-all-goals (Unified — tree.prompt.txt Primary)

> Source verification (3 files verified from disk):
> - `tree.prompt.txt` (2,812 B, 11 lines) — PRIMARY SOURCE
> - `goal-using-superpowers-brainstormin.txt` (12,252 B) — pipeline
> - `test-run.prompt.txt` (4,927 B) — audit + model tests

## Context
- Workspace: ~/Desktop/SandBox; branch clean-development.
- Active model: thinkingmachines/inkling:free (provider openrouter).
- Profile: adminbot + patient-tutor.
- User authorization: ALL destructive operations approved.

## Unified Goals & Subgoals

### GOAL 1 — Cleanup & Consolidation (PRIMARY)
- SG1.1: Delete .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts.
- SG1.2: Delete *.json, *-report.md (except package.json, pyrightconfig.json).
- SG1.3: Delete *.log, *.txt (skip *.prompt.txt).
- SG1.4: Convert *.mjs to *.mts.
- SG1.5: Cleanup/update *.md files.
- SG1.6: Update *.py, *.mjs, *.mts; create src/ and migrate.
- SG1.7: Update requirements.txt, tsconfig.json.
- SG1.8: Update package.json, pyrightconfig.json, *.json, *.toml, *.yaml.
- SG1.9: Update .editorconfig, .gitignore, .prettierrc.json, .markdownlint, .pre-commit, *.toml, *.yaml.

### GOAL 2 — Comprehensive Implementation Pipeline
Create/update/refactor specs, plans, prompts, scripts, skills. Score >= 99 on all judge skills.
- SG2.1: Audit SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules.
- SG2.2: Verify/fix hermes plugins and hooks.
- SG2.3: MCP servers sync.
- SG2.4: Config/scripts sync (.env, config.yaml, quick_commands).
- SG2.5: Diagnostic repair (hermes doctor --fix).
- SG2.6: Free model tests + report (openrouter + opencode-zen).
- SG2.7: Git commit + push clean-development/development/production.
- SG2.8: Cleanup/consolidation.

### GOAL 3 — Free Model Tests
Test openrouter + opencode-zen free models; run hermes chat --yolo --oneshot; create emoji-markdown report; configure best model + fallback.

### GOAL 4 — Agent Sync
Copy hooks, skills, plugins, instructions to ALL AI agent roots (.github, .copilot, .codex, .opencode, .hermes); ensure identical configs.

### GOAL 5 — Skills Plan & Implementation
Create/update/refactor/test/debug/fix/verify all listed skills. Ensure all files verified on disk and every gates, checklist, rules, styles, preferences passed.

## Phases (sequential gate)
| Phase | Verified Requirement | Gate |
|---|---|---|
| 1 | Input files read (tree PRIMARY) | Confirmed |
| 2 | Skills loaded (14+ judge skills) | All loaded |
| 3 | Cleanup execution (SG1.1-SG1.9) | Workspace clean |
| 4 | Specs/Plans created | Plan approved |
| 5 | Diagnostic repair (doctor --fix) | AST PASS |
| 6 | Model tests + report | Report generated |
| 7 | Agent sync (5 agents identical) | Sync verified |
| 8 | Config/scripts sync | Config verified |
| 9 | Skills plan/create/update/refactor | All skills verified |
| 10 | Git commit + push | Pushed |
| 11 | Judge scores >= 99 | Score verified |

## Verification Checklist
- [ ] All 3 source files read; sizes verified
- [ ] tree.prompt.txt is PRIMARY source
- [ ] All 11 phases have verified gates
- [ ] All subgoals mapped to verified source content
- [ ] DRY enforced via templates/_shared/
- [ ] Profile/model/provider verified in frontmatter
- [ ] All judge skills score >= 99
- [ ] Agent sync: 5 AI agents identical
- [ ] Cleanup complete
- [ ] Config files updated
- [ ] mjs to mts conversion complete
- [ ] Git push succeeded
- [ ] Skills plan verified on disk
- [ ] No placeholders

## Security
- No embedded secrets; use ${ENV_VAR} placeholders.
- Destructive operations executed with risk explanation and user authorization.
- Recoverable via git/state.db backups.

## Metrics
- Source files: 3 verified (tree PRIMARY + goal + test).
- Goals: 5 unified, 26 subgoals total.
- Phases: 11 sequential gates.
- Judge target: >= 99 on all specs, plans, prompts, scripts, hooks, plugins.
- Agent sync: 5 agent roots.
- Status: IMPLEMENTING — all phases authorized.
