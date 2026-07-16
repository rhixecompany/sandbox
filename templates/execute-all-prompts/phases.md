# Phases Reference

Use this file as the canonical phase content for the `execute-all-prompts` orchestrator.
Each phase assumes the corresponding prompt lives at `~/AppData/Local/hermes/prompts/`.

---

## Phase 1: Audit Skills Judge Fix

**Prompt file:** `audit-skills-judge-fix.prompt.md`

1. Run local skills audit and collect findings.
2. Categorize skill health, duplicates, and dead entries.
3. Run judge scoring on the affected skills.
4. Remediate fixable issues in staging/docs, not destructive deletion by default.
5. Consolidate replacement mappings and refs.
6. Verify with tooling/commands before claiming phase done.
7. Write or update local audit reports under `docs/`.

**Exit condition:** Audit report generated and no unverified changes in phase artifacts.

---

## Phase 2: Agents System Prompt Context Fix

**Prompt file:** `agents-system-prompt-context-fix.prompt.md`

1. Inspect `.github/agents/` and `.github/instructions/` for malformed frontmatter, missing fields, and stale context references.
2. Repair frontmatter-only issues; do not alter agent behavior beyond prompt/spec correctness.
3. Ensure context/spec references point to existing files in this repo.
4. Verify each repaired artifact can be parsed as valid markdown/YAML frontmatter.

**Skip condition:** If no `.agent.md` or `.instructions.md` repair targets exist, mark phase complete with evidence.

---

## Phase 3: Sync Hermes Copilot Codex

**Prompt file:** `sync-hermes-copilot-codex.prompt.md`

1. Inventory repostitory instruction/agent assets:
   - `.github/instructions/*.instructions.md`
   - `.github/agents/*.agent.md`
2. Identify root templates and derived assets to sync.
3. Sync corrective diffs from root to derived/copied assets where applicable.
4. Run verification on file counts and parse checks after sync.

**Safety:** Do not overwrite intentionally customized copies unless the prompt explicitly authorizes replacement.

---

## Phase 4: Test Providers & Models

**Prompt file:** `test-providers-models.prompt.md`

1. Inventory configured providers/models in Hermes config for this workspace.
2. Validate availability publicly where possible via read-only checks.
3. Extract free-tier or zero-cost model candidates.
4. Benchmark availability/latency only if explicitly enabled; otherwise produce availability report only.
5. Report results to `docs/` and summarize in progress tracker.

**Parallel-safe reads:** Provider/model inventory, local config read, and schema checks may run together.
**Sequential gates:** Any network-based check must run after local inventory and schema validation.
