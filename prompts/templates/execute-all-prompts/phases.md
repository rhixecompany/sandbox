# Phases

> Extracted from `execute-all-prompts.prompt.md`.

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
