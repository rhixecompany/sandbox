---
trigger: /execute-all-prompts
description: >
  Orchestrates sequential execution of all 4 workspace prompt files:
  audit-skills-judge-fix, agents-system-prompt-context-fix,
  sync-hermes-copilot-codex, and test-providers-models.
  Each prompt runs to completion before the next begins.
tags:
  - orchestrator
  - pipeline
  - sequential
  - audit
  - sync
  - benchmark
  - context
dependencies:
  - using-superpowers
  - user-communication-preferences
  - plans-and-specs
  - executing-plans
  - verification-before-completion
skills:
  - using-superpowers
  - user-communication-preferences
  - plans-and-specs
  - executing-plans
  - verification-before-completion
metadata:
  hermes:
    related_skills:
      - using-superpowers
      - user-communication-preferences
      - plans-and-specs
      - executing-plans
      - verification-before-completion
---

# Execute All Prompts Orchestrator

> Sequentially executes all 4 workspace prompt files. Each prompt must complete fully before the next begins ("only then" constraint).

## Description

This orchestrator runs 4 prompt files in order, each as a self-contained workflow. Execution is strictly sequential — Phase N+1 begins only after Phase N is fully verified complete.

**Critical rules:**
- Execute prompts in the exact order listed below
- Each prompt must be fully verified before moving to the next
- Do not skip phases within any prompt
- All Python scripts go to `~/AppData/Local/hermes/scripts/`
- Track progress in `docs/orchestrator-progress.md`

## Context

- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Prompt files:** 4 files in workspace root
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Skills Required

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Workflow foundation, session startup |
| `user-communication-preferences` | Execution style and preferences |
| `plans-and-specs` | Phase planning and progress tracking |
| `executing-plans` | Execute written plans with checkpoints |
| `verification-before-completion` | Verify each phase before claiming done |

## Rules

1. **Strict sequential execution** — Prompts execute in order; each must complete before the next begins
2. **Phase integrity** — All phases within a prompt must complete; do not skip
3. **Verification gates** — Each prompt's verification checklist must pass before proceeding
4. **Progress tracking** — Append progress to `docs/orchestrator-progress.md` after each prompt
5. **No reordering** — The prompt order is fixed; do not reorder based on perceived priority

## Phases

### Phase 1: Audit Skills Judge Fix

**Prompt file:** `audit-skills-judge-fix.prompt.md`
**Trigger:** `/audit-skills-judge-fix`

**Goal:** Run full skills audit, categorize, dedupe, consolidate, judge in batches of 10, remediate all issues.

**Sub-phases:**
1. **Phase 1.1 — Skills Audit & Inventory:** Run `hermes skills audit`, build inventory at `docs/local-skills.md`
2. **Phase 1.2 — Categorize Skills:** Move skills to correct category folders per mapping table
3. **Phase 1.3 — Deduplicate & Consolidate:** Find/remove duplicate skills, merge overlapping into umbrellas
4. **Phase 1.4 — Judge Skills:** Score all skills in batches of 10 using skill-judge v1.1.0 criteria
5. **Phase 1.5 — Remediate Skills:** Fix all skills scoring < 80 (patch 60-79, rewrite <60)
6. **Phase 1.6 — Consolidate Umbrella Skills:** Merge overlapping skills into well-structured umbrellas
7. **Phase 1.7 — Verify & Finalize:** Confirm all skills ≥ 80, categorized, deduped

**Verification:**
- [ ] All skills audited and inventoried
- [ ] All skills categorized (0 empty categories)
- [ ] Duplicates removed/merged
- [ ] All skills judged, results saved
- [ ] All skills scoring < 80 remediated
- [ ] Umbrella skills consolidated
- [ ] Final verification: all skills ≥ 80

**Only then** proceed to Phase 2.

---

### Phase 2: Agents System Prompt Context Fix

**Prompt file:** `agents-system-prompt-context-fix.prompt.md`
**Trigger:** `/agents-system-prompt-context-fix`

**Goal:** Create/update agent context files across project and subprojects, audit and enhance VS Code workspace configuration.

**Sub-phases:**
1. **Phase 2.1 — Generate Agent Context Files:** Run architecture-blueprint-generator, folder-structure-blueprint-generator, technology-stack-blueprint-generator
2. **Phase 2.2 — Audit VS Code Configuration:** List, triage, audit, debug, enhance, verify all `.vscode/**/*.json` files
3. **Phase 2.3 — Verify & Implement:** Verify plan, implement, confirm completion

**Verification:**
- [ ] Architecture context files generated
- [ ] Folder structure documents created
- [ ] Tech stack documents created
- [ ] All VS Code JSON files triaged and audited
- [ ] Configurations enhanced and verified
- [ ] Plan and specs verified complete

**Only then** proceed to Phase 3.

---

### Phase 3: Sync Hermes Copilot Codex

**Prompt file:** `sync-hermes-copilot-codex.prompt.md`
**Trigger:** `/sync-hermes-copilot-codex`

**Goal:** Sync skills, plugins, and hooks across Hermes, Copilot, and Codex agents; create personalities and profiles.

**Sub-phases:**
1. **Phase 3.1 — Inventory Instructions & Agents:** List `.github/instructions/` and `.github/agents/`, create personalities and profiles
2. **Phase 3.2 — Identify Root Folders:** Locate Hermes, Copilot, and Codex root directories
3. **Phase 3.3 — Sync Assets:** Bidirectional sync of skills, plugins, and hooks across all three agents
4. **Phase 3.4 — Verify & Implement:** Verify plan, implement, confirm completion

**Verification:**
- [ ] All instructions scanned and personalities created
- [ ] All agents scanned and profiles created
- [ ] Hermes, Copilot, and Codex roots identified
- [ ] Skills synced bidirectionally
- [ ] Plugins synced bidirectionally
- [ ] Hooks synced bidirectionally
- [ ] Plan and specs verified complete

**Only then** proceed to Phase 4.

---

### Phase 4: Test Providers & Models

**Prompt file:** `test-providers-models.prompt.md`
**Trigger:** `/test-providers-models`

**Goal:** Inventory all authorized LLM providers, discover free-tier models, run standardized benchmarks, produce comparison report.

**Sub-phases:**
1. **Phase 4.1 — Auth & Provider Inventory:** Run `hermes auth list`, capture credential status for all 6 providers
2. **Phase 4.2 — Model Catalog Discovery:** Query each provider for available models
3. **Phase 4.3 — Free Model Extraction:** Filter and extract zero-cost/free-tier models
4. **Phase 4.4 — Provider-by-Provider Benchmarking:** Run 3-task benchmark on each free model
5. **Phase 4.5 — Cross-Provider Comparison & Report:** Compile results into comparison report with recommendations
6. **Phase 4.6 — Script Creation & Automation:** Create/update `test_models.py` multi-provider test harness

**Verification:**
- [ ] All 6 providers captured from `hermes auth list`
- [ ] Model catalogs queried per provider
- [ ] Free models extracted and tabulated
- [ ] Benchmark run on all accessible free models
- [ ] Cross-provider comparison report generated
- [ ] Test harness script supports all 6 providers
- [ ] Rate limits and errors documented per provider

---

## Actions Summary

1. Run skills audit → categorize → dedupe → judge → remediate → consolidate → verify
2. Generate agent context files → audit VS Code configs → verify
3. Inventory instructions/agents → identify roots → sync assets → verify
4. Inventory providers → discover models → extract free → benchmark → report

## Verification Checklist (Orchestrator Level)

- [ ] Phase 1: Audit Skills Judge Fix — all 7 sub-phases complete
- [ ] Phase 2: Agents System Prompt Context Fix — all 3 sub-phases complete
- [ ] Phase 3: Sync Hermes Copilot Codex — all 4 sub-phases complete
- [ ] Phase 4: Test Providers & Models — all 6 sub-phases complete
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`

## Pitfalls

- **Skipping phases:** Never skip sub-phases within a prompt; each builds on the previous
- **Stale artifacts:** Re-read prompt files from disk before executing; don't rely on cached context
- **Context limits:** Each prompt is a large workflow; process in batches and write progress artifacts
- **Credential constraints:** API keys (especially OPENROUTER_API_KEY) are in Hermes' secure store, not env vars; route through `hermes chat -q --provider`
- **Sequential constraint:** The "only then" rule is absolute — never start a prompt before the previous one is verified complete
