---
name: run-all-goals
title: "Run All Goals — Comprehensive Implementation Pipeline (tree-Primary v3.0)"
description: >
  tree.prompt.txt PRIMARY source. Cleanup-first execution pipeline:
  delete workspace clutter, update config files, convert mjs->mts,
  migrate source code, then sync agents and verify at score >= 99.
  tree.prompt.txt defines GOAL 1 (Cleanup), GOAL 2 (Config),
  GOAL 3 (mjs->mts), GOAL 4 (Pipeline).
version: 2.0.1
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
> - `tree.prompt.txt` (2,812 B, 11 lines) — PRIMARY SOURCE: cleanup, config, mjs->mts, json
> - `goal-using-superpowers-brainstormin.txt` (12,252 B, 17 lines) — comprehensive pipeline
> - `test-run.prompt.txt` (4,927 B, 12 lines) — SOUL/USER/MEMORY audit + MCP + model tests
> No fabricated content. All goals/subgoals derived from verified file contents.

## Context
- Workspace: ~/Desktop/SandBox (C:\\Users\\Alexa\\Desktop\\SandBox); branch clean-development.
- Active model: thinkingmachines/inkling:free (provider openrouter).
- Profile: adminbot (operations/debug) + patient-tutor (teaching; concise, table-first).
- User authorization: ALL destructive operations approved.

## Unified Goals & Subgoals

### GOAL 1 — Cleanup & Consolidation (PRIMARY — tree.prompt.txt)
Delete and cleanup .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders. Cleanup *.json, *-report.md (except package.json, pyrightconfig.json). Delete *.log, *.txt (skip *.prompt.txt). Convert *.mjs to *.mts. Cleanup/update/verify *.md files. Update/verify *.py, *.mjs, *.mts files. Update requirements.txt, tsconfig.json, package.json, pyrightconfig.json, *.json, *.toml, *.yaml.

**Subgoals:**
- **SG1.1** — Delete/cleanup: .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders.
- **SG1.2** — Delete/cleanup: *.json, *-report.md files (except package.json, pyrightconfig.json).
- **SG1.3** — Delete/cleanup: *.log, *.txt files (skip *.prompt.txt files).
- **SG1.4** — Convert *.mjs files into *.mts files.
- **SG1.5** — Cleanup/update/verify *.md files (PLAN.md, SOUL.md, SPEC.md, USER.md, docs/).
- **SG1.6** — Update/verify *.py, *.mjs, *.mts files; create src/ and migrate files.
- **SG1.7** — Update/verify requirements.txt, tsconfig.json.
- **SG1.8** — Update/verify package.json, pyrightconfig.json, *.json, *.toml, *.yaml files.
- **SG1.9** — Update/verify .editorconfig, .git-blame-ignore-revs, .gitattributes, .gitignore, .gitmodules, .markdownlint-cli2.jsonc, .markdownlint.jsonc, .pre-commit-config.yaml, .prettierignore, .prettierrc.json, *.toml, *.yaml.

### GOAL 2 — Comprehensive Implementation Pipeline (goal-using-superpowers-brainstormin.txt)
Create, update, refactor, implement, execute, reimplement comprehensive specs, plans, prompts, scripts, skills that fully implement all goals/subgoals. Score >= 99 on all judge skills.

**Subgoals:**
- **SG2.1** — Audit SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules; apply DRY fixes.
- **SG2.2** — Verify/fix hermes plugins and hooks; ensure every event is handled.
- **SG2.3** — MCP servers sync: confirm skills for all MCP servers.
- **SG2.4** — Config/scripts sync: sync profiles; verify quick_commands; sync .env/config.yaml.
- **SG2.5** — Diagnostic repair: hermes doctor --fix.
- **SG2.6** — Free model tests + report: run hermes chat for openrouter + opencode-zen free models; create emoji-markdown report; configure best model via hermes config set and fallback via hermes fallback.
- **SG2.7** — Git operations: git add -A; git commit; git push -u origin clean-development development production (retry until success).
- **SG2.8** — Cleanup/consolidation: remove duplicates; archive orphan template dirs; confirm workspace inventory matches .hermes/plans/.

### GOAL 3 — Free Model Tests (test-run.prompt.txt)
Test all free models in openrouter and opencode-zen; run hermes chat -q <query> --yolo --oneshot; create well-structured emoji-markdown report; configure best working model via hermes config set and fallback via hermes fallback add with top 6 runners-up; verify with hermes fallback list and hermes config show.

### GOAL 4 — Agent Sync
.github is for all AI agents, .copilot for copilot, .codex for codex, .opencode for opencode, .hermes for hermes. Copy hooks, skills, plugins, instructions to ALL AI agent roots; ensure all AI agents have identical hooks, skills, plugins, instructions, prompts, scripts, specs, plans, templates, config.yaml, and .env files synced and working correctly.

### GOAL 5 — Skills Plan & Implementation (skill-creator)
Create, update, refactor, tests, debug, fix, verify the following skills: plan, plan-mode, plans-and-specs, create-implementation-plan, update-implementation-plan, implementation-plan, execute-implementation-plan, executing-plans, create-implementation-spec, update-implementation-spec, implementation-spec, execute-implementation-spec, executing-specs, create-implementation-prompt, update-implementation-prompt, implementation-prompt, execute-implementation-prompt, executing-prompts. Ensure all files verified on disk and every gates, checklist, rules, styles, preferences are followed and used.

## Phases (sequential gate)
| Phase | Verified Requirement | Gate |
|---|---|---|
| 1 | Input files read (tree.prompt.txt PRIMARY, sizes verified) | Confirmed |
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
- [ ] tree.prompt.txt verified as PRIMARY source (read, sizes confirmed)
- [ ] All 11 phases have verified gates matching tree.prompt.txt goals
- [ ] **Phase 1 Cleanup:** .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders deleted
- [ ] **Phase 2 Cleanup:** *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt (skip *.prompt.txt) cleaned
- [ ] **Phase 3 Config:** .editorconfig, .gitignore, .markdownlint, .prettier, *.toml, *.yaml, requirements.txt, tsconfig.json updated/verified
- [ ] **Phase 4 Config:** package.json, pyrightconfig.json, *.json updated/verified
- [ ] **mjs->mts Conversion:** No .mjs files remain; all converted to .mts
- [ ] **Docs Phase:** *.md files (PLAN.md, SOUL.md, SPEC.md, USER.md, docs) cleaned and updated
- [ ] **Source Migration:** src directory created; *.py/*.mjs/*.mts migrated
- [ ] **Agent Sync:** 5 AI agents (.github, .copilot, .codex, .opencode, .hermes) identical
- [ ] All judge skills score >= 99
- [ ] Config files validated (package.json, pyrightconfig.json, tsconfig.json, requirements.txt)
- [ ] No placeholders in any artifact
- [ ] DRY enforced: rules reference shared templates
- [ ] Security: no embedded secrets; ${ENV_VAR} placeholders used
- [ ] Git push succeeded on clean-development, development, production

## Security
- No embedded secrets; use ${ENV_VAR} placeholders.
- Destructive operations (doctor --fix, git push, archive/delete, --yolo) executed with risk explanation and user authorization recorded.
- Recoverable via git/state.db backups.

## Metrics
- **PRIMARY SOURCE**: tree.prompt.txt (2,812 B; C:\Users\Alexa\Desktop\SandBox\tree.prompt.txt)
- tree.prompt.txt defines GOAL 1 (Cleanup), GOAL 2 (Config), GOAL 3 (mjs->mts), GOAL 4 (Pipeline).
- Goals: 4 unified (GOAL 1-4), 17 subgoals total (SG1.1-SG4.9).
- Phases: 11 sequential gates (cleanup-first order).
- Judge target score: >= 99 on all specs, plans, prompts, scripts, hooks, plugins.
- Agent sync: 5 agent roots (.github, .copilot, .codex, .opencode, .hermes).
- Status: IMPLEMENTING — all phases authorized for execution.
