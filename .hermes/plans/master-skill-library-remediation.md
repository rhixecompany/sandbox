---
name: master-skill-library-remediation
title: "Master Skill Library Remediation — Run All Goals + Full Audit to 99+"
description: |
  Comprehensive master plan merging run-all-goals phases 3-11 with full skill library
  audit/remediation across all 1,278 active skills targeting 99+ on all judge skills
  (skill-judge, plans-judge, prompts-judge, specs-judge, hooks-judge, plugins-judge, scripts-judge).
version: 1.0.0
author: Alexa
license: MIT
tags: [master, remediation, skills, audit, run-all-goals, score-99]
status: in_progress
phases: 15
subgoals: 42
---

# Master Skill Library Remediation — Run All Goals + Full Audit to 99+

## Overview
This master plan consolidates:
- **Run-all-goals Phases 3-11** (8 phases, 9 subgoals) — workspace audit, diagnostic repair, model tests, agent sync, cleanup, config sync, git push, judge scores
- **Full Skill Library Audit/Remediation** (7 phases, 33 subgoals) — dedup, judge all 1,278 skills, structured remediation, re-judge, stub removal, 99+ verification

**Target**: All 7 judge skills score ≥99 on all artifacts.

## Goals

### GOAL 1 — Complete Run-All-Goals Pipeline (Phases 3-11)
| Phase | Task | Gate | Status |
|-------|------|------|--------|
| 3 | Workspace audit + skill inventory | Inventory verified | pending |
| 4 | Specs/Plans created | Plan approved | pending |
| 5 | Diagnostic repair | `hermes doctor --fix` PASS | pending |
| 6 | Free model tests + report | Report generated | pending |
| 7 | Agent sync (5 agents) | 5 agents identical | pending |
| 8 | Cleanup/consolidation | Workspace clean | pending |
| 9 | Config/scripts sync | Config verified | pending |
| 10 | Git push (3 branches) | 3 branches pushed | pending |
| 11 | Judge scores ≥ 99 | All scores verified | pending |

### GOAL 2 — Full Skill Library Remediation to 99+
| Phase | Task | Gate | Status |
|-------|------|------|--------|
| S1 | Archive cleanup + dedup | Archive removed, dedup complete | pending |
| S2 | Baseline judge all 1,278 skills | Distribution captured | pending |
| S3 | Batch remediation (frontmatter, structure) | 0 FAIL, avg ≥72 | pending |
| S4 | Deep remediation (refs, templates, examples) | Avg ≥80, near-PASS ≥85 | pending |
| S5 | Targeted 99+ push (code blocks, error handling, platform) | All skills ≥90 | pending |
| S6 | All 7 judge skills verification | All 7 judges ≥99 | pending |
| S7 | Final verification + git commit | All gates pass | pending |

## Phase Breakdown

### Phase 3: Workspace Audit & Skill Inventory (Run-All-Goals)
- **3.1** Run `hermes skills audit` → capture security/path/integrity issues
- **3.2** Run `hermes skills check` → capture available updates
- **3.3** Run full skill inventory (count, categories, duplicates)
- **3.4** Scan `.archive` and `.restore-backups.DISABLED` for removal
- **3.5** Identify flat-root vs categorized duplicates
- **3.6** Create inventory artifact at `.hermes/plans/verification/skill-inventory.md`

### Phase 4: Specs/Plans Created
- **4.1** This master plan created ✓
- **4.2** Create run-all-goals SPEC.md for phases 5-11
- **4.3** Create skill-remediation SPEC.md with judge criteria
- **4.4** Link specs to plan phases

### Phase 5: Diagnostic Repair
- **5.1** Run `hermes doctor --fix` → capture output
- **5.2** Run `hermes mcp test all` → verify all 11 MCP servers
- **5.3** Run `hermes hooks list` + `hermes plugins list` → verify registration
- **5.4** Run `hermes profile use adminbot` → verify profile switching
- **5.5** Verify tooling MCP servers (python-quality, tooling-config, tooling-lint)

### Phase 6: Free Model Tests + Report
- **6.1** Test all free models on openrouter (`:free` models)
- **6.2** Test all free models on opencode-zen
- **6.3** Create emoji-markdown report with capabilities/vision/reasoning
- **6.4** Configure best model + fallback chain in config.yaml

### Phase 7: Agent Sync (5 Agents)
- **7.1** Sync hooks to `.github/copilot`, `.codex`, `.opencode`, `.hermes`
- **7.2** Sync skills to all 5 agent roots
- **7.3** Sync plugins to all 5 agent roots
- **7.4** Sync instructions/context files
- **7.5** Verify identical configs across all 5

### Phase 8: Cleanup & Consolidation
- **8.1** Delete `.enhance`, `.goals`, `.hermes_diagnostics`, `.mcp`, `.*_cache`, `.worktrees`
- **8.2** Cleanup `*.json`, `*.log`, `*.txt` temp files
- **8.3** Convert `*.mjs` → `*.mts` (ESM modules)
- **8.4** Update all config files (package.json, tsconfig, etc.)
- **8.5** Verify workspace clean

### Phase 9: Config/Scripts Sync
- **9.1** Sync `.env` across profiles
- **9.2** Sync `config.yaml` (use `hermes config set` only)
- **9.3** Sync `quick_commands.json`
- **9.4** Verify all profiles have consistent configs

### Phase 10: Git Push (3 Branches)
- **10.1** Commit all changes to `clean-development`
- **10.2** Push to `origin/clean-development`
- **10.3** Merge/verify `development` branch
- **10.4** Merge/verify `production` branch
- **10.5** Tag release

### Phase 11: Judge Scores ≥ 99 (Run-All-Goals)
- **11.1** Run `plans-judge` on `.hermes/plans/*.md`
- **11.2** Run `specs-judge` on `.hermes/specs/*.md`
- **11.3** Run `prompts-judge` on `.github/prompts/**/*.prompt.md`
- **11.4** Run `skill-judge` on all skills
- **11.5** Run `hooks-judge` on all hooks
- **11.6** Run `plugins-judge` on all plugins
- **11.7** Run `scripts-judge` on `scripts/`
- **11.8** Verify all ≥99

### Phase S1: Archive Cleanup + Dedup (Skill Library)
- **S1.1** Remove `.archive/` directory (32 skills)
- **S1.2** Remove `.restore-backups.DISABLED/` if exists
- **S1.3** Run dedupe script → identify flat-root vs categorized duplicates
- **S1.4** Remove non-canonical flat copies (keep categorized versions)
- **S1.5** Verify dedup: no duplicate skill names across paths

### Phase S2: Baseline Judge All 1,278 Skills
- **S2.1** Run `batch_skill_judge.py` on all active skills
- **S2.2** Capture baseline distribution (PASS/WARN/FAIL)
- **S2.3** Generate `judge_results/summary.md` and `all_results.tsv`
- **S2.4** Identify top 20 worst skills for priority remediation

### Phase S3: Batch Remediation (Structure)
- **S3.1** Run `batch_remediate.py` → add frontmatter, pitfalls, verification
- **S3.2** Run `fix_yaml_frontmatter.py` → fix YAML formatting
- **S3.3** Run `patch_fail_structure.py` → add workflow phases, Skills Required
- **S3.4** Run `patch_all_fail_sections.py` → inject all 7 critical sections
- **S3.5** Run `boost_near_pass_refs.py` → create domain reference files
- **S3.6** Re-judge → verify 0 FAIL, avg ≥72

### Phase S4: Deep Remediation (Content Depth)
- **S4.1** For skills 70-79: add platform detection blocks
- **S4.2** Add error handling blocks with code examples
- **S4.3** Create `templates/` and `scripts/` directories with real content
- **S4.4** Add explicit reference citations in SKILL.md body
- **S4.5** Add ≥3 code blocks per skill
- **S4.6** Re-judge → verify avg ≥80, near-PASS ≥85

### Phase S5: Targeted 99+ Push
- **S5.1** Run `skill-judge --folder` on all skills with threshold 90
- **S5.2** For each skill <90: apply targeted fixes per judge feedback
- **S5.3** Add comprehensive examples, edge cases, integration patterns
- **S5.4** Ensure all reference files are substantive (>200 chars)
- **S5.5** Verify all skills ≥90 on skill-judge
- **S5.6** Run all 6 other judges on relevant artifacts

### Phase S6: All 7 Judge Skills Verification
- **S6.1** Run `plans-judge` → verify ≥99
- **S6.2** Run `specs-judge` → verify ≥99
- **S6.3** Run `prompts-judge` → verify ≥99
- **S6.4** Run `hooks-judge` → verify ≥99
- **S6.5** Run `plugins-judge` → verify ≥99
- **S6.6** Run `scripts-judge` → verify ≥99
- **S6.7** Run `skill-judge` → verify ≥99

### Phase S7: Final Verification + Git Commit
- **S7.1** Run full verification scripts
- **S7.2** Run `test_run_all_goals.py` and `verify_run_all_goals.py`
- **S7.3** Commit all changes with conventional messages
- **S7.4** Push to all 3 branches
- **S7.5** Generate final SESSION_REPORT.md

## Scripts Required

| Script | Purpose | Phase |
|--------|---------|-------|
| `scripts/run_all_phases.py` | Orchestrate phases 3-11 | 3-11 |
| `scripts/batch_skill_judge.py` | Score all skills | S2, S3, S4, S5, S6 |
| `scripts/batch_remediate.py` | Structural fixes | S3 |
| `scripts/fix_yaml_frontmatter.py` | YAML formatting | S3 |
| `scripts/patch_fail_structure.py` | Add workflow sections | S3 |
| `scripts/patch_all_fail_sections.py` | Inject critical sections | S3 |
| `scripts/boost_near_pass_refs.py` | Create reference files | S3 |
| `scripts/deep_remediate.py` | Content depth fixes | S4 |
| `scripts/push_to_99.py` | Targeted 99+ fixes | S5 |
| `scripts/verify_all_judges.py` | Run all 7 judges | S6, 11 |

## Verification Checklist

- [ ] Phase 3: Workspace audit complete, inventory verified
- [ ] Phase 4: Specs created and linked
- [ ] Phase 5: Diagnostic repair PASS
- [ ] Phase 6: Model tests complete, report generated
- [ ] Phase 7: 5 agents synced identically
- [ ] Phase 8: Workspace clean
- [ ] Phase 9: Configs synced
- [ ] Phase 10: 3 branches pushed
- [ ] Phase 11: All 7 judges ≥99 on run-all-goals artifacts
- [ ] Phase S1: Archive removed, dedup complete
- [ ] Phase S2: Baseline captured
- [ ] Phase S3: 0 FAIL, avg ≥72
- [ ] Phase S4: Avg ≥80, near-PASS ≥85
- [ ] Phase S5: All skills ≥90 on skill-judge
- [ ] Phase S6: All 7 judges ≥99
- [ ] Phase S7: Final commit, push, report

## Security

- No embedded secrets; use `${ENV_VAR}` placeholders
- All destructive operations pre-authorized per user confirmation
- Git reflog available for rollback

## Resource Allocation

| Resource | Allocation |
|----------|------------|
| Subagents | Parallel batches of 7 for judge/remediate |
| Time | As fast as possible — parallel execution |
| Disk | ~2GB for artifacts, judge results, backups |
| Model | nemotron-3-ultra-free (primary), deepseek-v4-flash-free (fallback) |