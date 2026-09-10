---
name: run-all-goals-implementation
title: "Run All Goals — Implementation Plan (Unified v2.0)"
description: >
  Comprehensive implementation plan merging goal-using-superpowers-brainstormin.txt,
  test-run.prompt.txt, and tree.prompt.txt into a single execution pipeline.
version: 2.0.0
author: Alexa
license: MIT
tags: [implementation, execution, unified, score-99]
status: in_progress
phases: 11
subgoals: 17
---

# Run All Goals — Implementation Plan

## Overview
Unified implementation plan consolidating 3 source files into 4 goals, 17 subgoals, 11 phases.
Target score: >= 99 on all judge skills (specs-judge, plans-judge, prompts-judge, skill-judge).

## Goals

### GOAL 1 — Comprehensive Implementation Pipeline
Create/update/refactor/implement/execute/reimplement comprehensive specs, plans, prompts, scripts, skills.

**Subgoals:**
1. SG1.1 — Audit context files (SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules)
2. SG1.2 — Verify/fix hermes plugins and hooks
3. SG1.3 — MCP servers sync (25+ servers)
4. SG1.4 — Config/scripts sync (.env, config.yaml, quick_commands)
5. SG1.5 — Diagnostic repair (hermes doctor --fix)
6. SG1.6 — Free model tests + report (openrouter + opencode-zen)
7. SG1.7 — Git commit + push (clean-development, development, production)
8. SG1.8 — Cleanup/consolidation

### GOAL 2 — Free Model Tests
Test all free models in openrouter and opencode-zen; create emoji-markdown report; configure best model + fallback.

### GOAL 3 — Agent Sync
Copy hooks, skills, plugins, instructions to ALL AI agent roots (.github, .copilot, .codex, .opencode, .hermes); ensure identical configs.

### GOAL 4 — Cleanup & Verification
Delete .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, etc.; cleanup *.json, *.log, *.txt; mjs->mts; update all config files.

## Phases
| Phase | Task | Gate | Status |
|---|---|---|---|
| 1 | Input files verified | Sizes confirmed | done |
| 2 | Skills loaded | 14+ judge skills | done |
| 3 | Workspace audit | Inventory verified | in_progress |
| 4 | Specs/Plans created | Plan approved | pending |
| 5 | Diagnostic repair | doctor --fix PASS | pending |
| 6 | Model tests + report | Report generated | pending |
| 7 | Agent sync | 5 agents identical | pending |
| 8 | Cleanup/consolidation | Workspace clean | pending |
| 9 | Config/scripts sync | Config verified | pending |
| 10 | Git push | 3 branches pushed | pending |
| 11 | Judge scores >= 99 | All scores verified | pending |

## Scripts
- scripts/test_run_all_goals.py — Run all subgoal tests
- scripts/verify_run_all_goals.py — Verify output exists, no placeholders

## Verification Checklist
- [ ] All 3 source files read; sizes verified
- [ ] All 11 phases have verified gates
- [ ] All subgoals mapped to verified source content
- [ ] All judge skills score >= 99
- [ ] Agent sync: 5 AI agents identical
- [ ] Cleanup complete
- [ ] Config files updated
- [ ] Git push succeeded
- [ ] No placeholders in any artifact

## Security
- No embedded secrets; use ${ENV_VAR} placeholders
- All destructive operations user-authorized
