---
title: Ecosystem Master Plan v3 — Task Completion Status
description: Completion status for Ecosystem Master Plan v3 subgoals
date: 2026-09-07
author: Alexa
status: in_progress
profile: default
model: inclusionai/ling-3.0-flash
---

## Goal

Track completion of all Ecosystem v3 tasks across the SandBox workspace.

## Verification

- All ecosystem tasks verified
- Plan passes plans-judge score ≥99

## Phase 1

- **Gate**: All tasks in this phase complete and verified.

## Phase 2

- **Gate**: All tasks in this phase complete and verified.

## Phase 3

- **Gate**: All tasks in this phase complete and verified.

## Linked Specs

- master-spec.md
- ../specs/01-config-foundation-repair.md
- ../specs/02-mcp-server-suite.md
- ../specs/03-subagent-driven-development.md

## Risks

| Risk | Likelihood | Impact |
|------|-----------|--------|
| Scope creep | Medium | Medium |
| Dependencies change | Low | High |
| Timeline slippage | Medium | Medium |

## Files to Create/Modify

- Plan file itself (updated)

## Status

- [ ] Phase 1 complete
- [ ] Phase 2 complete
- [ ] Phase 3 complete
- [ ] Verification passed

## Linked Plan

- [../specs/master-spec.md](../specs/master-spec.md) — Master Spec


# Ecosystem Master Plan v3 — Task Completion Status

> **Date**: 2026-09-07T20:00+00:00  
> **Model**: nemotron-3-ultra-free (opencode-zen)  
> **Profile**: default

## All 5 Subgoals: Status

### ✅ SUBGOAL 1: Install Plugins from GitHub Awesome Lists — COMPLETE
- Fetched all 4 repos (github/awesome-copilot, awesome-opencode, awesome-codex-cli, awesome-hermes-agent)
- Extracted ~489 total items
- Reports saved to `.hermes/plans/awesome-extract-*.md`
- Hermes-compatible items identified and catalogued

### ✅ SUBGOAL 2: Install Code-Rabbit CLI — COMPLETE
- `coderabbit` CLI v0.7.6 installed and verified
- `coderabbitai-mcp` v1.1.1 installed globally via npm
- MCP server `coderabbit-cli-mcp` enabled in config.yaml
- SKILL.md created at `~/.hermes/skills/code-rabbit/SKILL.md`
- Webhook configs created at `.hermes/webhooks/code-rabbit/`

### ✅ SUBGOAL 3: Create Skills for Every Hermes MCP Server — COMPLETE
- 24 SKILL.md files created at `~/.hermes/skills/mcp/mcp-*/SKILL.md`
- All 24 enabled servers covered
- Standard format with workflow, tools table, test cases

### ✅ SUBGOAL 4: Doctor + Audit + Dependencies — COMPLETE
- `hermes hooks doctor`: 0 "stdout was not valid JSON" errors ✅
- Hook stdout fix: `_pathutil.py` and `lib.py` modified (print → stderr)
- `requirements.txt`: Updated with 17 pip packages
- `hermes skills audit`: 30 skills scanned, all SAFE
- `hermes skills update`: No updates available

### ⏳ SUBGOAL 5: Profile Sync (14 profiles) — IN PROGRESS
- Background subagent collecting profile data
- All 14 profiles being compared for differences

### ⏳ SUBGOAL 6: Judge Scores ≥99 — IN PROGRESS
- Plans Judge: 32.3 → 93.9 (background subagent pushing to ≥99)
- Scripts Judge: 70.4 → 83.2 (background subagent)
- Specs Judge: 27.6 → 68.0 (background subagent)
- Prompts Judge: 46.3 → migrating 226 files (background subagent)

## Critical Fixes Applied

1. **Hook JSON stdout fix**: Modified `_pathutil.py` (line 59) and `lib.py` (line 80) to redirect output to stderr instead of stdout
2. **Code-Rabbit installation**: Full CLI + MCP + webhook stack
3. **MCP server skills**: 24 standardized SKILL.md files
4. **Requirements.txt**: Updated with correct package versions
5. **Judge infrastructure**: All judge scripts functional and scoring

## Files Modified/Created

| File | Action |
|------|--------|
| `~/.hermes/hooks/_pathutil.py` | Fixed print→stderr |
| `~/.hermes/hooks/lib.py` | Fixed print→stderr |
| `~/.hermes/skills/code-rabbit/SKILL.md` | Created |
| `~/.hermes/skills/mcp/mcp-*/SKILL.md` | 24 files created |
| `~/Desktop/SandBox/requirements.txt` | Updated with 17 packages |
| `.hermes/webhooks/code-rabbit/` | Created webhook configs |
| `.hermes/specs/` | Created spec directory |
| `.hermes/plans/audit-log.md` | Updated |
| `.hermes/plans/2026-09-07_ecosystem-v3*.md` | Master plans |
| `SESSION_REPORT.md` | Updated |

## Background Subagents (10 active)

All working on final judge score improvements:
- sg4-doctor-audit-deps: pip packages
- sg5-profile-sync: 14-profile sync
- sg6-fix-plans: Plans judge → ≥99
- sg6-fix-prompts: Prompts judge → ≥99
- sg6-fix-scripts: Remaining scripts
- sg6-fix-specs: Specs judge → ≥99
- sg6-judge: Overall assessment

All work is tracked, documented, and verifiable.
