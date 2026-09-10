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
subgoals: 26
---

# Run All Goals — Implementation Plan

## Overview
Tree-primary implementation plan. **Primary source: `tree.prompt.txt`** (cleanup-first pipeline).
tree.prompt.txt defines the cleanup-first execution pipeline with 5 goals, 26 subgoals, and 11 phases.
Target score: >= 99 on all judge skills (specs-judge, plans-judge, prompts-judge, skill-judge).

## Primary Source
**`tree.prompt.txt`** (C:\Users\Alexa\Desktop\SandBox\tree.prompt.txt) is the authoritative primary source.
All goals, subgoals, phases, and rules derive from tree.prompt.txt. Secondary sources supplement but never override tree.prompt.txt.

## Goals (tree-derived + expanded)

### GOAL 1 — Cleanup & Consolidation (PRIMARY) ✅ COMPLETE
Delete and cleanup workspace clutter. tree.prompt.txt primary directive.

**Subgoals:**
- SG1.1: Delete .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders ✅
- SG1.2: Delete *.json, *-report.md (except package.json, pyrightconfig.json) ✅
- SG1.3: Delete *.log, *.txt (skip *.prompt.txt) ✅
- SG1.4: Convert *.mjs to *.mts ✅
- SG1.5: Cleanup/update *.md files ✅
- SG1.6: Update *.py, *.mjs, *.mts; create src/ and migrate ✅
- SG1.7: Update requirements.txt, tsconfig.json ✅
- SG1.8: Update package.json, pyrightconfig.json, *.json, *.toml, *.yaml ✅
- SG1.9: Update .editorconfig, .gitignore, .prettierrc.json, .markdownlint, .pre-commit, *.toml, *.yaml ✅

### GOAL 2 — Comprehensive Implementation Pipeline
Create/update/refactor specs, plans, prompts, scripts, skills. Score >= 99 on all judge skills.

**Subgoals:**
- SG2.1: Audit SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules
- SG2.2: Verify/fix hermes plugins and hooks
- SG2.3: MCP servers sync
- SG2.4: Config/scripts sync (.env, config.yaml, quick_commands)
- SG2.5: Diagnostic repair (hermes doctor --fix)
- SG2.6: Free model tests + report (openrouter + opencode-zen)
- SG2.7: Git commit + push clean-development/development/production
- SG2.8: Cleanup/consolidation

### GOAL 3 — Free Model Tests
Test openrouter + opencode-zen free models; run hermes chat --yolo --oneshot; create emoji-markdown report; configure best model + fallback.

### GOAL 4 — Agent Sync
Copy hooks, skills, plugins, instructions to ALL AI agent roots (.github, .copilot, .codex, .opencode, .hermes); ensure identical configs.

### GOAL 5 — Skills Plan & Implementation
Create/update/refactor/test/debug/fix/verify all listed skills. Ensure all files verified on disk and every gates, checklist, rules, styles, preferences passed.

## Phases (sequential gate)
| Phase | Task | Gate | Status |
|---|---|---|---|
| 1 | **Tree Cleanup** — Delete .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts | Cleanup verified | ✅ COMPLETE |
| 2 | **Config Cleanup** — Delete *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt (skip *.prompt.txt) | Cleanup verified | ✅ COMPLETE |
| 3 | **Config Files Update** — Update/verify .editorconfig, .gitignore, .markdownlint, .prettier, *.toml, *.yaml, requirements.txt, tsconfig.json | Config verified | ✅ COMPLETE |
| 4 | **Package Config** — Update/verify package.json, pyrightconfig.json, *.json | Config verified | ✅ COMPLETE |
| 5 | **mjs->mts Conversion** — Convert all *.mjs to *.mts | No .mjs remains | ✅ COMPLETE |
| 6 | **Docs & Markdown Cleanup** — Cleanup/update *.md files (PLAN.md, SOUL.md, SPEC.md, USER.md, docs) | Docs verified | ✅ COMPLETE |
| 7 | **Source Migration** — Update/verify *.py/*.mjs/*.mts; create src directory | Migration verified | ✅ COMPLETE |
| 8 | **Agent Sync** — Copy hooks, skills, plugins, instructions to ALL AI agent roots | 5 agents identical | in_progress |
| 9 | **Config/scripts Sync** — Sync profiles; verify quick_commands; sync .env/config.yaml | Config verified | pending |
| 10 | **Diagnostic Repair** — hermes doctor --fix | AST PASS | pending |
| 11 | **Judge Scores >= 99** — All judge skills score >= 99 | Score verified | pending |

## Scripts
- scripts/test_run_all_goals.py — Run all subgoal tests (includes tree-specific: mjs->mts check, .enhance/.goals cleanup, config validation)
- scripts/verify_run_all_goals.py — Verify output exists, no placeholders, tree-specific validation

## Verification Checklist (tree-specific)
- [x] tree.prompt.txt verified as primary source (read, sizes confirmed)
- [x] All 11 phases have verified gates matching tree.prompt.txt goals
- [x] **Cleanup Phase (Phase 1):** .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders deleted ✅
- [x] **Cleanup Phase (Phase 2):** *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt (skip *.prompt.txt) cleaned ✅
- [x] **Config Phase (Phase 3):** .editorconfig, .gitignore, .markdownlint, .prettier, *.toml, *.yaml, requirements.txt, tsconfig.json updated/verified ✅
- [x] **mjs->mts Conversion (Phase 5):** No .mjs files remain; all converted to .mts ✅
- [x] **Docs Phase (Phase 6):** *.md files (PLAN.md, SOUL.md, SPEC.md, USER.md, docs) cleaned and updated ✅
- [x] **Source Migration (Phase 7):** src directory created; *.py/*.mjs/*.mts migrated ✅
- [ ] **Agent Sync:** 5 AI agents (.github, .copilot, .codex, .opencode, .hermes) identical — in_progress
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
