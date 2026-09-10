---
name: run-all-goals-implementation
title: "Run All Goals — Implementation Plan (Tree-Primary v3.0)"
description: >
  Tree-primary unified implementation plan. Primary source: tree.prompt.txt
  (cleanup, config, mjs->mts). tree.prompt.txt defines the cleanup-first
  execution pipeline. Secondary: goal-using-superpowers-brainstormin.txt,
  test-run.prompt.txt. Implements all goals/subgoals with specs, plans,
  scripts, skills, templates, gates, checklists, rules, and verification
  at score >= 99.
version: 3.0.0
author: Alexa
license: MIT
tags: [implementation, execution, unified, tree-primary, score-99, cleanup-first]
status: in_progress
phases: 11
subgoals: 17
---

# Run All Goals — Implementation Plan

## Overview
Tree-primary implementation plan. **Primary source: `tree.prompt.txt`** (cleanup-first pipeline).
tree.prompt.txt defines the cleanup-first execution pipeline with 4 goals, 17 subgoals, and 11 phases.
Target score: >= 99 on all judge skills (specs-judge, plans-judge, prompts-judge, skill-judge).

## Primary Source
**`tree.prompt.txt`** (C:\Users\Alexa\Desktop\SandBox\tree.prompt.txt) is the authoritative primary source.
All goals, subgoals, phases, and rules derive from tree.prompt.txt. Secondary sources (goal-using-superpowers-brainstormin.txt, test-run.prompt.txt) supplement but never override tree.prompt.txt.

## Goals (tree-derived)

### GOAL 1 — Cleanup & Delete
Delete and cleanup workspace clutter. tree.prompt.txt primary directive.

**Subgoals:**
1. SG1.1 — Delete/cleanup folders: .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders
2. SG1.2 — Search, delete and cleanup *.json, *-report.md files (except package.json, pyrightconfig.json)
3. SG1.3 — Search, delete and cleanup *.log, *.txt files (skip *.prompt.txt files)

### GOAL 2 — Config Files Update & Verify
Update, refactor, and verify configuration files.

**Subgoals:**
4. SG2.1 — Update/verify: .editorconfig, .git-blame-ignore-revs, .gitattributes, .gitignore, .gitmodules, .markdownlint-cli2.jsonc, .markdownlint.jsonc, .pre-commit-config.yaml, .prettierignore, .prettierrc.json, *.toml, *.yaml
5. SG2.2 — Update/verify requirements.txt, tsconfig.json
6. SG2.3 — Update/verify package.json, pyrightconfig.json, *.json files

### GOAL 3 — Code Conversion & Migration
Convert and migrate source code files.

**Subgoals:**
7. SG3.1 — Convert, update, refactor, verify *.mjs files into mts files
8. SG3.2 — Update/verify *.py, *.mjs, *.mts files; create src directory and migrate files into src
9. SG3.3 — Cleanup, update, refactor, verify *.md files including PLAN.md, SOUL.md, SPEC.md, USER.md and all files in docs

### GOAL 4 — Unified Pipeline (Implementation/Execution)
Create, update, refactor comprehensive specs, plans, prompts, scripts, skills that fully implement all goals/subgoals. Score >= 99 on all judge skills.

**Subgoals:**
10. SG4.1 — Audit SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules; apply DRY fixes
11. SG4.2 — Verify/fix hermes plugins and hooks; ensure every event is handled
12. SG4.3 — MCP servers sync: confirm skills for all 25+ MCP servers
13. SG4.4 — Config/scripts sync: sync profiles; verify quick_commands; sync .env/config.yaml
14. SG4.5 — Diagnostic repair: hermes doctor --fix
15. SG4.6 — Free model tests + report: run hermes chat for openrouter + opencode-zen free models; create emoji-markdown report; configure best model via hermes config set and fallback via hermes fallback
16. SG4.7 — Git operations: git add -A; git commit; git push -u origin clean-development development production
17. SG4.8 — Cleanup/consolidation: remove duplicates; archive orphan template dirs; confirm workspace inventory matches .hermes/plans/

## Phases (tree-cleanup-first, sequential gate)
| Phase | Task | Gate | Status |
|---|---|---|---|
| 1 | **Tree Cleanup** — Delete .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts | Cleanup verified | pending |
| 2 | **Config Cleanup** — Delete *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt (skip *.prompt.txt) | Cleanup verified | pending |
| 3 | **Config Files Update** — Update/verify .editorconfig, .gitignore, .markdownlint, .prettier, *.toml, *.yaml, requirements.txt, tsconfig.json | Config verified | pending |
| 4 | **Package Config** — Update/verify package.json, pyrightconfig.json, *.json | Config verified | pending |
| 5 | **mjs->mts Conversion** — Convert all *.mjs to *.mts | No .mjs remains | pending |
| 6 | **Docs & Markdown Cleanup** — Cleanup/update *.md files (PLAN.md, SOUL.md, SPEC.md, USER.md, docs) | Docs verified | pending |
| 7 | **Source Migration** — Update/verify *.py/*.mjs/*.mts; create src directory | Migration verified | pending |
| 8 | **Agent Sync** — Copy hooks, skills, plugins, instructions to ALL AI agent roots (.github, .copilot, .codex, .opencode, .hermes) | 5 agents identical | pending |
| 9 | **Config/scripts Sync** — Sync profiles; verify quick_commands; sync .env/config.yaml | Config verified | pending |
| 10 | **Diagnostic Repair** — hermes doctor --fix | AST PASS | pending |
| 11 | **Judge Scores >= 99** — All judge skills score >= 99 | Score verified | pending |

## Scripts
- scripts/test_run_all_goals.py — Run all subgoal tests (includes tree-specific: mjs->mts check, .enhance/.goals cleanup, config validation)
- scripts/verify_run_all_goals.py — Verify output exists, no placeholders, tree-specific validation

## Verification Checklist (tree-specific)
- [ ] tree.prompt.txt verified as primary source (read, sizes confirmed)
- [ ] All 11 phases have verified gates matching tree.prompt.txt goals
- [ ] **Cleanup Phase (Phase 1):** .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders deleted
- [ ] **Cleanup Phase (Phase 2):** *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt (skip *.prompt.txt) cleaned
- [ ] **Config Phase (Phase 3):** .editorconfig, .gitignore, .markdownlint, .prettier, *.toml, *.yaml, requirements.txt, tsconfig.json updated/verified
- [ ] **mjs->mts Conversion (Phase 5):** No .mjs files remain; all converted to .mts
- [ ] **Docs Phase (Phase 6):** *.md files (PLAN.md, SOUL.md, SPEC.md, USER.md, docs) cleaned and updated
- [ ] **Source Migration (Phase 7):** src directory created; *.py/*.mjs/*.mts migrated
- [ ] **Agent Sync:** 5 AI agents (.github, .copilot, .codex, .opencode, .hermes) identical
- [ ] All judge skills score >= 99
- [ ] Config files (package.json, pyrightconfig.json, tsconfig.json, requirements.txt) validated
- [ ] No placeholders in any artifact
- [ ] DRY enforced: rules reference shared templates
- [ ] Security: no embedded secrets; ${ENV_VAR} placeholders used
- [ ] Git push succeeded on clean-development, development, production

## Security
- No embedded secrets; use ${ENV_VAR} placeholders
- All destructive operations user-authorized
- Tree-first approach: cleanup before construction
