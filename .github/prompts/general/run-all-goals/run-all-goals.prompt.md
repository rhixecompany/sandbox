---
name: run-all-goals
title: "Run All Goals — Comprehensive Implementation Pipeline (Unified)"
description: >
  Consolidates /goal and /subgoal bundles from three verified source files into a
  single unified prompt: goal-using-superpowers-brainstormin.txt (9,277 B),
  test-run.prompt.txt (4,575 B), tree.prompt.txt (3,020 B).
  Implements all goals/subgoals with specs, plans, scripts, skills, templates,
  gates, checklists, rules, and verification at score >= 99.
version: 2.0.0
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

# Goal: /run-all-goals (Unified)

> Source verification (3 files verified from disk):
> - `goal-using-superpowers-brainstormin.txt` (9,277 B, 17 lines)
> - `test-run.prompt.txt` (4,575 B, 12 lines)
> - `tree.prompt.txt` (3,020 B, 10 lines)
> No fabricated content. All goals/subgoals derived from verified file contents.

## Context
- Workspace: ~/Desktop/SandBox (C:\\Users\\Alexa\\Desktop\\SandBox); branch clean-development.
- Active model: thinkingmachines/inkling:free (provider openrouter).
- Profile: adminbot (operations/debug) + patient-tutor (teaching; concise, table-first).
- User authorization: ALL destructive operations approved.

## Unified Goals & Subgoals

### GOAL 1 — Comprehensive Implementation Pipeline
Create, update, refactor, implement, execute, reimplement comprehensive specs, plans, prompts, scripts, skills that fully implement all goals/subgoals. Score >= 99 on all judge skills.

**Subgoals:**
- **SG1.1** — Audit SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules; apply DRY fixes.
- **SG1.2** — Verify/fix hermes plugins and hooks; ensure every event is handled.
- **SG1.3** — MCP servers sync: confirm skills for all 25+ MCP servers.
- **SG1.4** — Config/scripts sync: sync profiles; verify quick_commands; sync .env/config.yaml.
- **SG1.5** — Diagnostic repair: hermes doctor --fix.
- **SG1.6** — Free model tests + report: run hermes chat for openrouter + opencode-zen free models; create emoji-markdown report; configure best model via hermes config set and fallback via hermes fallback.
- **SG1.7** — Git operations: git add -A; git commit; git push -u origin clean-development development production (retry until success).
- **SG1.8** — Cleanup/consolidation: remove duplicates; archive orphan template dirs; confirm workspace inventory matches .hermes/plans/.

### GOAL 2 — Free Model Tests
Test all free models in openrouter and opencode-zen; run hermes chat -q <query> --yolo --oneshot; create well-structured emoji-markdown report; configure best working model via hermes config set and fallback via hermes fallback add with top 6 runners-up; verify with hermes fallback list and hermes config show.

### GOAL 3 — Agent Sync
.github is for all AI agents, .copilot for copilot, .codex for codex, .opencode for opencode, .hermes for hermes. Copy hooks, skills, plugins, instructions to ALL AI agent root folders; ensure all AI agents have identical hooks, skills, plugins, instructions, prompts, scripts, specs, plans, templates, config.yaml, and .env files synced and working correctly.

### GOAL 4 — Cleanup & Verification
- **SG4.1** — Delete/cleanup: .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders.
- **SG4.2** — Delete/cleanup: *.json, *-report.md files (except package.json, pyrightconfig.json).
- **SG4.3** — Update/verify: .editorconfig, .git-blame-ignore-revs, .gitattributes, .gitignore, .gitmodules, .markdownlint-cli2.jsonc, .markdownlint.jsonc, .pre-commit-config.yaml, .prettierignore, .prettierrc.json, *.toml, *.yaml.
- **SG4.4** — Delete/cleanup: *.log, *.txt files (skip *.prompt.txt files).
- **SG4.5** — Convert *.mjs files into *.mts files.
- **SG4.6** — Cleanup/update/verify *.md files including PLAN.md, SOUL.md, SPEC.md, USER.md and all docs.
- **SG4.7** — Update/verify *.py, *.mjs, *.mts files; create src directory and migrate files.
- **SG4.8** — Update/verify requirements.txt, tsconfig.json.
- **SG4.9** — Update/verify package.json, pyrightconfig.json, *.json files.

## Phases (sequential gate)
| Phase | Verified Requirement | Gate |
|---|---|---|
| 1 | Input files read (sizes verified) | Confirmed |
| 2 | Skills loaded (14+ judge skills) | All loaded |
| 3 | Workspace audit (hooks, plugins, MCP, config) | Inventory verified |
| 4 | Specs/Plans created | Plan approved |
| 5 | Diagnostic repair (doctor --fix) | AST PASS |
| 6 | Model tests + report | Report generated |
| 7 | Agent sync (5 agents identical) | Sync verified |
| 8 | Cleanup/consolidation | Workspace clean |
| 9 | Config/scripts sync | Config verified |
| 10 | Git commit + push | Pushed |
| 11 | Judge scores >= 99 | Score verified |

## Verification Checklist
- [ ] All 3 source files read; sizes verified (no fabrication)
- [ ] All 14 mandatory skills loaded + judge skills verified
- [ ] Unified prompt consolidated from all 3 files with no placeholders
- [ ] All 11 phases have verified gates
- [ ] All subgoals SG1.1-SG4.9 mapped to verified source content
- [ ] DRY enforced: rules reference shared templates; no duplicated rules text
- [ ] Profile/model/provider verified in frontmatter
- [ ] Dependencies and skills reference verified skills
- [ ] All judge skills (skill-judge, prompts-judge, plans-judge, specs-judge) score >= 99
- [ ] Phase gate table present and all gates verified
- [ ] Security: no embedded secrets; ${ENV_VAR} placeholders used
- [ ] Agent sync: all AI agents (.github, .copilot, .codex, .opencode, .hermes) have identical configs
- [ ] Cleanup: .enhance, .goals, .hermes_diagnostics removed
- [ ] Config: requirements.txt, tsconfig.json, package.json updated
- [ ] mjs to mts conversion complete
- [ ] Git push to clean-development, development, production succeeded

## Security
- No embedded secrets; use ${ENV_VAR} placeholders.
- Destructive operations (doctor --fix, git push, archive/delete, --yolo) executed with risk explanation and user authorization recorded.
- Recoverable via git/state.db backups.

## Metrics
- Source files: 3 verified (9,277 B + 4,575 B + 3,020 B = 16,872 B total).
- Goals: 4 unified (GOAL 1-4), 17 subgoals total.
- Phases: 11 sequential gates.
- Judge target score: >= 99 on all specs, plans, prompts, scripts, hooks, plugins.
- Agent sync: 5 agent roots (.github, .copilot, .codex, .opencode, .hermes).
- Status: IMPLEMENTING — all phases authorized for execution.
