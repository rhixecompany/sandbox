---
status: completed
status: completed
status: completed
---
# Prompt Management Orchestration — Comprehensive Plan

> **Workflow:** Prompt Management (prompt-management skill) applied to `execute-all-prompts.prompt.md` and all 4 sub-prompts it orchestrates.
> **Version:** 1.0.0 | **Author:** OWL (Alexa)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Scope & Objectives](#2-scope--objectives)
3. [Architecture Overview](#3-architecture-overview)
4. [Phase-by-Phase Specification](#4-phase-by-phase-specification)
    - [Phase 0: Verification](#41-phase-0-verification)
    - [Phase 1: Audit Skills Judge Fix](#42-phase-1-audit-skills-judge-fix)
    - [Phase 2: Agents System Prompt Context Fix](#43-phase-2-agents-system-prompt-context-fix)
    - [Phase 3: Sync Hermes Copilot Codex](#44-phase-3-sync-hermes-copilot-codex)
    - [Phase 4: Test Providers & Models](#45-phase-4-test-providers--models)
5. [Safety & Validation Architecture](#5-safety--validation-architecture)
6. [Timeline & Resource Requirements](#6-timeline--resource-requirements)
7. [Risk Mitigation](#7-risk-mitigation)
8. [Deliverables Matrix](#8-deliverables-matrix)
9. [Rollback Procedures](#9-rollback-procedures)
10. [Success Criteria](#10-success-criteria)

---

## 1. Executive Summary

### 1.1 Objectives

The primary objective is to design, specify, and execute a comprehensive prompt orchestration workflow that manages, audits, and validates the full Hermes Agent prompt library. This encompasses five chained prompts that systematically:

1. **Audit and remediate** all 370+ local skills (score, judge, fix, deduplicate)
2. **Generate and verify** agent system prompt context files (architecture docs, VS Code configs)
3. **Bidirectionally sync** skills, plugins, and hooks across Hermes, Copilot, and Codex agents
4. **Inventory and benchmark** all authorized LLM providers and their free-tier models
5. **Orchestrate** the above four into a single sequential pipeline with "only then" constraints

### 1.2 Scope

| Dimension | Included | Excluded |
|-----------|----------|----------|
| Prompts | `execute-all-prompts.prompt.md` + 4 sub-prompts | Other 247 prompts in library |
| Skills | 370+ local skills in `~/AppData/Local/hermes/skills/` | Bundled/hub-installed skills (read-only) |
| Agents | Hermes, GitHub Copilot, OpenCode Codex | Other AI agents |
| Providers | copilot, huggingface, nous, ollama-cloud, openai-api, openrouter, xai-oauth | Providers without auth |
| Platforms | Windows 11 (git-bash/MSYS), VS Code | Linux, macOS, other editors |

### 1.3 Constraints

- **Strict sequential** — Each phase must complete fully before the next begins ("only then")
- **No parallel phase execution** — Sub-phases within a phase may be parallelized where independent
- **No destructive operations without rollback** — Every delete/overwrite must have a documented recovery path
- **Git-based rollback** — No `.bak`/`.backup`/timestamped copies permitted
- **MSYS path safety** — All scripts derive from `$HOME`/`$USERPROFILE`, never hardcoded `C:\Users\...`
- **Verification gates** — Every phase requires post-execution verification before proceeding

---

## 2. Scope & Objectives

### 2.1 Primary Goals

| Goal | Target | Success Metric |
|------|--------|----------------|
| G1 | Audit and inventory all local skills | 100% of skills audited, `docs/local-skills.md` generated |
| G2 | Categorize uncategorized skills | 0 skills in "uncategorized" state |
| G3 | Deduplicate overlapping skills | 0 duplicate skill names across library |
| G4 | Judge and remediate all skills | Avg score ≥ 75, count of FAIL (<60) = 0, count of WARN (60-79) minimized |
| G5 | Generate architecture context files | 59+ docs in `docs/Project_Architecture/` |
| G6 | Validate VS Code JSON configs | 0 invalid JSON files across root and subprojects |
| G7 | Sync Hermes ↔ Copilot ↔ Codex | Zero drift in plugins, hooks, skills |
| G8 | Inventory all LLM providers | All 7 authorized providers captured with auth status |

### 2.2 Secondary Goals

| Goal | Target | Priority |
|------|--------|----------|
| S1 | Extract DRY shared templates | Prompts with identical sections (skills tables, rules) wired to `_shared/` |
| S2 | Tag all prompts with meaningful metadata | 0 prompts with empty `tags:` fields |
| S3 | Fix broken skill references across prompts | 0 unresolved `skill:/` or `skill:unknown` refs |
| S4 | Generate cross-provider benchmark report | Comparison of free-tier model performance |

---

## 3. Architecture Overview

### 3.1 Prompt Hierarchy

```
execute-all-prompts.prompt.md (Orchestrator)
│
├── audit-skills-judge-fix.prompt.md (Phase 1)
│   ├── Phase 1.1: Skills Audit & Inventory
│   ├── Phase 1.2: Categorize Skills
│   ├── Phase 1.3: Deduplicate & Consolidate
│   ├── Phase 1.4: Judge Skills (batches of 10)
│   ├── Phase 1.5: Remediate (<80 scores)
│   ├── Phase 1.6: Consolidate Umbrellas
│   └── Phase 1.7: Verify & Finalize
│
├── agents-system-prompt-context-fix.prompt.md (Phase 2)
│   ├── Phase 2.1: Generate Context Files
│   ├── Phase 2.2: Audit VS Code Config
│   └── Phase 2.3: Verify & Implement
│
├── sync-hermes-copilot-codex.prompt.md (Phase 3)
│   ├── Phase 3.1: Inventory Instructions & Agents
│   ├── Phase 3.2: Identify Root Folders
│   ├── Phase 3.3: Sync Assets Bidirectionally
│   └── Phase 3.4: Verify & Confirm
│
└── test-providers-models.prompt.md (Phase 4)
    ├── Phase 4.1: Auth Inventory
    ├── Phase 4.2: Model Catalog Discovery
    ├── Phase 4.3: Free Model Extraction
    ├── Phase 4.4: Provider-by-Provider Benchmark
    ├── Phase 4.5: Cross-Provider Comparison
    ├── Phase 4.6: Rate Limit & Fallback Analysis
    └── Phase 4.7: Script Creation & Automation
```

### 3.2 Data Flow

```
Skills Library ──► Audit ──► Categorize ──► Deduplicate ──► Judge ──► Remediate ──► Verify
                      │                                                     │
                      └── docs/local-skills.md                              └── docs/final-verification.md
                              
Project Root ──► Architecture Gen ──► VS Code Audit ──► Verify
                    │                       │
                    └── docs/Project_       └── .vscode/*.json validated
                        Architecture/

Hermes ──┬── Skills ──► Sync ──► Copilot Skills
         ├── Plugins ──► Sync ──► Copilot Plugins
         └── Hooks ────► Sync ──► Copilot Hooks

Providers ──► Auth ──► Catalog ──► Extract ──► Benchmark ──► Report
```

### 3.3 File System Map

```
$HOME/Desktop/SandBox/
├── prompts/
│   ├── execute-all-prompts.prompt.md
│   ├── audit-skills-judge-fix.prompt.md
│   ├── agents-system-prompt-context-fix.prompt.md
│   ├── sync-hermes-copilot-codex.prompt.md
│   ├── test-providers-models.prompt.md
│   ├── templates/
│   │   ├── _shared/ (12 templates)
│   │   └── {prompt-name}/ (phases.md, README.md)
│   └── ...
├── docs/
│   ├── local-skills.md
│   ├── dedupe-report.md
│   ├── consolidation-report.md
│   ├── final-verification.md
│   ├── categorization-plan.md
│   ├── Project_Architecture/ (59+ files)
│   └── orchestrator-verification.md
├── judge_results/
│   ├── all_results.tsv
│   ├── summary.md
│   └── batch_*.md (35 batch files)
└── .vscode/ (5 config files)
    └── projects/*/.vscode/ (107 subproject configs)

$HOME/AppData/Local/hermes/
├── skills/ (143 dirs, 489 SKILL.md files)
├── scripts/ (7 automation scripts)
├── hooks/ (3 active hooks)
└── plugins/ (4 active plugins)
```

---

## 4. Phase-by-Phase Specification

### 4.1 Phase 0: Verification

**Profile:** `research-analyst`
**Duration:** 5 minutes
**Dependencies:** None (entry point)

| Step | Action | Input | Output | Verification |
|------|--------|-------|--------|-------------|
| 0.1 | Inventory target prompts | `prompts/*.prompt.md` | Target list (5 prompts) | All 5 files exist, frontmatter parseable |
| 0.2 | Verify template directories | `prompts/templates/{name}/` | Dir status report | Each target has template dir or known missing |
| 0.3 | Check shared templates | `prompts/templates/_shared/` | Shared template inventory | 12 templates present |
| 0.4 | Check scripts | `~/AppData/Local/hermes/scripts/` | Script inventory | Python/bash scripts present |
| 0.5 | Check Git status | `git status` | Clean working tree | No blocking uncommitted changes |
| 0.6 | Verify Hermes profile | `hermes profile show` | Active profile confirmed | Profile = default (opencode-zen) |

**Safety Gate G0:** All 5 prompts must exist and parse. Missing prompts = BLOCK (check alternate extensions `.prompts.md`). Template dirs are advisory — missing non-shared dirs produce WARNING but not BLOCK.

### 4.2 Phase 1: Audit Skills Judge Fix

**Profile:** `code-architect` (primary), `research-analyst` (judging)
**Duration:** 60-90 minutes
**Dependencies:** Phase 0 complete

#### Sub-phase 1.1: Skills Audit & Inventory

| Step | Action | Command/Tool | Expected Output |
|------|--------|-------------|-----------------|
| 1.1.1 | Run `hermes skills audit` | `terminal` | 111+ skills scanned, SAFE/BLOCKED verdicts |
| 1.1.2 | Count skills by type | `execute_code` | Flat count, nested count, total |
| 1.1.3 | Build inventory document | `write_file` | `docs/local-skills.md` |
| 1.1.4 | Build path mapping | `write_file` | `docs/skill_name_to_path.json` |

**Safety Gate G1.1:** If `hermes skills audit` returns 0 skills or non-zero exit, retry once. If still zero, BLOCK — report Hermes installation issue.

#### Sub-phase 1.2: Categorize Skills

| Step | Action | Input | Output |
|------|--------|-------|--------|
| 1.2.1 | Identify uncategorized flat skills | `skills/` dir listing | List of 46 flat skills |
| 1.2.2 | Map each to correct category | Category mapping table | Categorization plan |
| 1.2.3 | Move or add frontmatter category | `patch`/`skill_manage` | 41+ skills with metadata.category |

**Safety Gate G1.2:** Never move a skill directory that has a duplicate in its target category. Always deduplicate first (G1.3).

#### Sub-phase 1.3: Deduplicate

| Step | Action | Detection Method | Resolution |
|------|--------|-----------------|------------|
| 1.3.1 | Find same-name duplicates | `basename` comparison | 9 identified (creative-ideation, peft, etc.) |
| 1.3.2 | Compare content sizes | `du -b` or `len()` | Cat copy is canonical (larger) |
| 1.3.3 | Remove flat copy | `rm -rf skills/{name}` | `skill_manage` delete or direct rm |
| 1.3.4 | Report | `write_file` | `docs/dedupe-report.md` |

**Safety Gate G1.3:** Before removing ANY skill, verify the canonical copy exists and has same or larger content. Never remove without verification.

#### Sub-phase 1.4: Judge Skills

| Step | Action | Method |
|------|--------|--------|
| 1.4.1 | Run skill-judge in batches | `skill_judge` on 10 skills/batch |
| 1.4.2 | Collect results per batch | Save to `judge_results/batch_NNNN.md` |
| 1.4.3 | Aggregate all results | Generate `judge_results/all_results.tsv` |
| 1.4.4 | Summary statistics | `judge_results/summary.md` |

**Dimensions scored (skill-judge v1.1.0):**
- Completeness (0-20)
- Clarity (0-20)
- Correctness (0-20)
- Actionability (0-20)
- Safety (0-20)
- **Total (0-100)**

**Safety Gate G1.4:** If judge results show >10% FAIL (<60), stop and investigate scoring calibration before continuing.

#### Sub-phase 1.5: Remediate

| Threshold | Action | Scope |
|-----------|--------|-------|
| FAIL (<60) | Full rewrite of SKILL.md | 2 skills (bundled — blocked) |
| WARN (60-79) | Patch frontmatter, structure, refs | 259 skills |
| PASS (≥80) | No action | 89 skills |

**Safety Gate G1.5:** After remediation, re-run judge on a 10-skill sample. If average hasn't improved, BLOCK — examine remediation strategy.

#### Sub-phase 1.6: Consolidate Umbrellas

Identify overlapping thin skills (<100 lines) and merge into umbrella skills using `skill_manage(action='delete', absorbed_into='umbrella')`.

#### Sub-phase 1.7: Verify

**Checklist:**
- [ ] Skills inventory saved ✅
- [ ] All categorized (0 uncategorized) ✅
- [ ] Duplicates removed (0 same-name collisions) ✅
- [ ] Judge results saved to `judge_results/` ✅
- [ ] All FAIL remediated or noted as bundled ✅
- [ ] Umbrella skills documented ✅
- [ ] Final verification saved ✅

---

### 4.3 Phase 2: Agents System Prompt Context Fix

**Profile:** `code-architect` + `tech-writer`
**Duration:** 30-45 minutes
**Dependencies:** Phase 1 complete

#### Sub-phase 2.1: Generate Agent Context Files

| Step | Skill | Output Location | Expected |
|------|-------|----------------|----------|
| 2.1.1 | `architecture-blueprint-generator` | `docs/Project_Architecture/` | Architecture context files |
| 2.1.2 | `folder-structure-blueprint-generator` | `docs/Project_Architecture/` | Folder structure docs |
| 2.1.3 | `technology-stack-blueprint-generator` | `docs/Project_Architecture/` | Tech stack documents |

#### Sub-phase 2.2: Audit VS Code Configuration

| Step | Action | Tool | Expected |
|------|--------|------|----------|
| 2.2.1 | List all .vscode JSON files | `find .vscode -name '*.json'` | File count |
| 2.2.2 | Validate each JSON | `python3 -c 'json.load(open(f))'` | 0 parse errors |
| 2.2.3 | Triage configs by type | Manual classification | settings, tasks, launch, extensions, mcp |
| 2.2.4 | Enhance known gaps | `patch` | Missing settings added |

**Safety Gate G2:** JSON validation errors must be fixed, not skipped. If a file contains invalid JSON, read it, fix the syntax error, re-validate.

---

### 4.4 Phase 3: Sync Hermes Copilot Codex

**Profile:** `code-architect` + `devops`
**Duration:** 30-45 minutes
**Dependencies:** Phase 2 complete

#### Sub-phase 3.1: Inventory Instructions & Agents

| Check | Source | Expected Count |
|-------|--------|---------------|
| Instructions | `.github/instructions/` | 186 files |
| Agents | `.github/agents/` | 174 files |
| Personalities to create | Instructions → personality mapping | 186 max |
| Profiles to create | Agents → profile mapping | 174 max |

#### Sub-phase 3.2: Identify Root Folders

| Agent | Root Path | Status |
|-------|-----------|--------|
| Hermes | `~/AppData/Local/hermes/` | Active |
| Copilot | `~/.copilot/` (or `.github/` in workspace) | Active |
| Codex | `~/.codex/` | Check existence |

#### Sub-phase 3.3: Sync Assets Bidirectionally

| Asset | Direction | Method |
|-------|-----------|--------|
| Skills | Hermes ↔ Copilot | `rsync` or `cp` with exclusion list |
| Plugins | Hermes ↔ Copilot | Directory comparison → sync |
| Hooks | Hermes ↔ Copilot | Directory comparison → sync |

#### Sub-phase 3.4: Verify

**Zero drift check:**
- ✅ Same number of plugins (4/4)
- ✅ Same number of hooks (3/3)  
- ✅ Skills may differ (different agent scopes)
- ✅ All cross-refs resolve

---

### 4.5 Phase 4: Test Providers & Models

**Profile:** `research-analyst` + `code-architect`
**Duration:** 45-60 minutes
**Dependencies:** Phase 3 complete

#### Sub-phase 4.1: Auth Inventory

| Provider | Auth Method | Status |
|----------|------------|--------|
| copilot | gh auth token, GITHUB_TOKEN | Rate-limited (429) — ready to retry |
| huggingface | HF_TOKEN env var | Active |
| nous | OAuth (device code) | Exhausted (2m 48s left) |
| ollama-cloud | OLLAMA_API_KEY env var | Active |
| openai-api | api_key + OPENAI_API_KEY | Active |
| openrouter | OPENROUTER_API_KEY env var | Rate-limited (429) — 2h 1m left |
| xai-oauth | OAuth (loopback_pkce) | Active |

#### Sub-phase 4.2-4.7: Discovery → Benchmarking → Report

| Sub-phase | Action | Output |
|-----------|--------|--------|
| 4.2 | Discover model catalogs | `docs/model-catalogs.md` |
| 4.3 | Extract free-tier models | Filtered model list |
| 4.4 | Run standardized benchmarks | `judge_results/provider-benchmarks.md` |
| 4.5 | Cross-provider comparison | `docs/provider-comparison.md` |
| 4.6 | Rate limit analysis | `docs/rate-limit-report.md` |
| 4.7 | Create automation scripts | `~/AppData/Local/hermes/scripts/benchmark*.py` |

**Safety Gate G4:** Never hardcode API keys in scripts. Use `$ENV_VAR` references only. If a provider is rate-limited, note the retry-after time, do NOT retry aggressively.

---

## 5. Safety & Validation Architecture

### 5.1 Multi-Gate Pattern

Every phase implements the following safety gate pattern:

```
                    ┌─────────────────────────────────┐
                    │    PRE-TRANSFORMATION AUDIT      │
                    │  Extract critical constraints    │
                    │  from current state              │
                    └──────────┬──────────────────────┘
                               │
                               ▼
                    ┌─────────────────────────────────┐
                    │    TRANSFORMATION RULES          │
                    │  What is allowed vs. prohibited  │
                    │  Defined per phase               │
                    └──────────┬──────────────────────┘
                               │
                               ▼
                    ┌─────────────────────────────────┐
                    │    POST-TRANSFORMATION VERIFY    │
                    │  Constraints still present?      │
                    │  Output quality check            │
                    └──────────┬──────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
              PASS ✓                  FAIL ✗
          ──► Next Phase          ──► Log + Rollback
```

### 5.2 Gate Registry

| Gate | Phase | Condition | Violation Action |
|------|-------|-----------|-----------------|
| G0 | 0 | All 5 prompts exist | Report missing → ask user |
| G1.1 | 1.1 | Audit returns non-zero skills | Retry once → BLOCK |
| G1.3 | 1.3 | Canonical copy verified before delete | BLOCK delete |
| G1.4 | 1.4 | ≤10% FAIL in judge results | Stop → investigate calibration |
| G1.5 | 1.5 | Remediation improves avg score | BLOCK if no improvement |
| G2 | 2 | All VS Code JSONs valid | Read → fix → re-validate |
| G3 | 3 | Zero plugin/hook drift | List diffs → sync → re-check |
| G4 | 4 | No API keys in script output | grep for hardcoded keys → BLOCK |

### 5.3 Rollback Architecture

| Scenario | Rollback Method |
|----------|----------------|
| Skill accidentally deleted | `git checkout` from last commit (skills in git) |
| Broken SKILL.md | `git checkout` individual file |
| VS Code config broken | `git checkout .vscode/` |
| Duplicate removed incorrectly | Restore from `.curator_backups/` if exists |
| Wrong provider benchmark | Re-run with corrected parameters |

**Golden rule:** Before every destructive operation, `git add` and `git commit` the current state so rollback is a single `git checkout`.

---

## 6. Timeline & Resource Requirements

### 6.1 Time Budget

| Phase | Min Duration | Max Duration | Cumulative |
|-------|-------------|-------------|------------|
| Phase 0: Verification | 3 min | 5 min | 5 min |
| Phase 1: Audit Judge Fix | 45 min | 90 min | 95 min |
| Phase 2: Context Fix | 20 min | 45 min | 140 min |
| Phase 3: Sync Agents | 15 min | 30 min | 170 min |
| Phase 4: Test Providers | 20 min | 45 min | 215 min |
| **Total** | **~103 min** | **~215 min** | **~3.5 hours** |

### 6.2 Resource Requirements

| Resource | Requirement | Notes |
|----------|-------------|-------|
| Tokens (model) | ~500K-1M input, ~100K-200K output | DeepSeek V4 via opencode-zen |
| Disk space | <50MB for all artifacts | Mostly text files |
| Network | Required for Phase 4 (provider benchmarks) | openrouter, huggingface |
| Hermes CLI | `hermes skills audit`, `hermes auth list` | Must be functional |
| Git | Working tree with `git status` clean | Rollback enabled |
| MSYS bash | `terminal` tool via git-bash | Path resolution via $HOME |
| VS Code | Workspace configuration access | JSON file validation |

---

## 7. Risk Mitigation

### 7.1 Risk Register

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| R1 | `hermes skills audit` blocks dangerous skills | Medium | Medium | Use `--force` where appropriate; note blocked skills |
| R2 | Judge scores inconsistent across batches | Low | High | Calibrate first batch, lock thresholds, re-score sample |
| R3 | Sub-agent stalls during delegation | Medium | High | Check signature artifacts on disk after 2-5 min; proceed if present |
| R4 | OpenRouter/API rate limits block Phase 4 | High | Medium | Capture current state; schedule retry after backoff |
| R5 | Memory write approval blocks save | Low | Low | Stage writes; confirm via TUI `/memory pending` |
| R6 | Duplicate detection misses similar-but-different skills | Medium | Medium | Use both name comparison AND content comparison |
| R7 | VS Code JSON validation fails on encoded paths | Low | Low | Use Python's `json.load()` not shell tools |
| R8 | Prompt file uses `.prompts.md` (plural) instead of `.prompt.md` | Low | Medium | Run `ls *.prompt*.md` during Phase 0 to discover both |
| R9 | Cross-profile access blocked by soft guard | Low | Low | Set `cross_profile=true` only on explicit user direction |
| R10 | Phase 1 fails silently due to skill count mismatch | Medium | Medium | Count before and after each sub-phase |

### 7.2 Contingency Plans

| Risk | Plan A | Plan B |
|------|--------|--------|
| R1 (blocked skills) | Use `--force` on CAUTION verdicts | Skip DANGEROUS verdicts (not overridable) |
| R3 (stalled sub-agent) | Check artifacts, proceed | Re-delegate with simpler goal |
| R4 (rate limited) | Note state, skip to next provider | Schedule cron job for retry |
| R6 (overlap missed) | Accept false negatives; document | Manual review of suspect pairs |

---

## 8. Deliverables Matrix

### 8.1 Primary Artifacts

| ID | Artifact | Phase | Format | Location | Required |
|----|----------|-------|--------|----------|----------|
| D1 | Skills inventory | 1.1 | Markdown | `docs/local-skills.md` | Yes |
| D2 | Path mapping | 1.1 | JSON | `docs/skill_name_to_path.json` | Yes |
| D3 | Categorization plan | 1.2 | Markdown | `docs/categorization-plan.md` | Yes |
| D4 | Dedupe report | 1.3 | Markdown | `docs/dedupe-report.md` | Yes |
| D5 | Judge results | 1.4 | TSV | `judge_results/all_results.tsv` | Yes |
| D6 | Batch results (×35) | 1.4 | Markdown | `judge_results/batch_*.md` | Yes |
| D7 | Summary stats | 1.4 | Markdown | `judge_results/summary.md` | Yes |
| D8 | Remediation report | 1.5 | Markdown | `docs/remediation-report.md` | Yes |
| D9 | Consolidation report | 1.6 | Markdown | `docs/consolidation-report.md` | Yes |
| D10 | Final verification | 1.7 | Markdown | `docs/final-verification.md` | Yes |
| D11 | Architecture docs (59+) | 2.1 | Markdown | `docs/Project_Architecture/` | Yes |
| D12 | VS Code validation | 2.2 | Terminal output | Verified configs | Yes |
| D13 | Provider inventory | 4.1 | Terminal output | `hermes auth list` | Yes |
| D14 | Orchestrator progress | All | Markdown | `docs/orchestrator-progress.md` | Yes |
| D15 | Orchestrator verification | All | Markdown | `docs/orchestrator-verification.md` | Yes |

### 8.2 Secondary Artifacts

| ID | Artifact | Phase | Format | Location |
|----|----------|-------|--------|----------|
| S1 | Prompt validation report | Cross | Markdown | `docs/prompt-validation-report.md` |
| S2 | Prompt inventory | Cross | Markdown | `docs/prompt-inventory.md` |
| S3 | Agent cross-reference | 3 | Markdown | `docs/agents-cross-reference.md` |
| S4 | Provider comparison | 4 | Markdown | `docs/provider-comparison.md` |

---

## 9. Rollback Procedures

### 9.1 Git-Based Rollback

```bash
# Before any destructive operation:
git add -A && git commit -m "checkpoint: before <operation>"

# To roll back:
git checkout HEAD~1 -- path/to/restored/file

# Full phase rollback:
git log --oneline -10    # find the phase commit
git revert <commit-hash>  # safe revert (not destructive)
```

### 9.2 Per-Phase Rollback

| Phase | Rollback Command | Notes |
|-------|-----------------|-------|
| 1.3 (dedupe) | Skills are in git; `git checkout HEAD~1 -- skills/` | Directory restore |
| 1.5 (remediate) | `git checkout HEAD~1 -- skills/*/SKILL.md` | Only SKILL.md affected |
| 2.2 (VS Code) | `git checkout HEAD~1 -- .vscode/` | All configs restored |
| 3.3 (sync) | `rsync -a .github/backup/ .github/` | If backup exists |
| 4.x (providers) | No rollback needed (read-only operations) | N/A |

### 9.3 Emergency Stop

If any phase produces unexpected destructive behavior:
1. Stop all operations immediately
2. Run `git status` to see what changed
3. Run `git checkout -- .` to discard all working tree changes
4. Report the issue

---

## 10. Success Criteria

### 10.1 Completion Gates

| Gate | Condition | Verified By |
|------|-----------|-------------|
| Phase 0 | 5/5 prompts exist, all templates verified | File inventory |
| Phase 1 | All 7 sub-phases complete, artifacts saved | `docs/final-verification.md` |
| Phase 2 | Context files generated, VS Code configs valid | 59 docs, 0 JSON errors |
| Phase 3 | Zero drift in plugins/hooks, 174+186 agents/instructions | Directory comparison |
| Phase 4 | 7 providers inventoried, auth statuses captured | `hermes auth list` output |

### 10.2 Quality Gates

| Quality | Threshold | Measurement |
|---------|-----------|-------------|
| Skill coverage | 100% inventoried | Count vs `find` |
| Judge completeness | 350+ scored | `judge_results/all_results.tsv` |
| Remediation improvement | Avg ≥ 73.6 | Before/after comparison |
| JSON validity | 100% valid | `json.load` per file |
| Sync drift | 0% for plugins+hooks | Directory comparison |
| Provider coverage | 7/7 authorized | `hermes auth list` |

### 10.3 Final Acceptance

The pipeline is accepted as COMPLETE when:
1. All 4 phases are verified with artifacts
2. `docs/orchestrator-verification.md` shows all ✅
3. No blocking errors remain
4. User confirms acceptance

---

*End of Comprehensive Plan — 856 lines*
