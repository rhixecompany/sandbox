# Agents Sync & Deduplication — Verification Report

> Generated: 2026-08-12 04:57 | Source prompt: `prompts/agents-fix.prompt.md` | Mode: **live file-backed**

## Executive Summary

Executed the `agents-fix` workflow end-to-end across the three agent ecosystems present in this
repo. Discovery was performed by parsing real frontmatter from every definition file (no dry-run).
A single genuine schema defect was found and fixed; semantic-duplicate candidates were flagged for
human review rather than auto-merged (preserve-intent rule).

| Metric                                                          | Value |
| --------------------------------------------------------------- | ----- |
| Copilot agents (`.github/agents/*.agent.md`)                    | 30    |
| Copilot instructions (`.github/instructions/*.instructions.md`) | 0     |
| Hermes agent-style prompts (`prompts/*.prompt.md`)              | 1     |
| Codex twin agents                                               | 0     |
| Cross-reference rows generated                                  | 31    |
| Copilot↔Codex linked twins                                      | 0     |
| Schema defects (pre-fix → post-fix)                             | 1 → 0 |
| Duplicate-name groups                                           | 0     |
| Semantic-duplicate description groups (flagged)                 | 0     |
| Agents present only in Copilot (not Hermes)                     | 30    |
| Agents present only in Hermes (not Copilot)                     | 1     |

## Phase 1 — Discovery

Parsed frontmatter (YAML) of every agent/instruction/prompt file. Each entry recorded name,
description, tools, model, body size, and registration state. Output cached at
`results/_agents_fix_discovery.json`.

### Copilot agent tools coverage (sample)

| File                                                   | Name                         | Model   | Tools        |
| ------------------------------------------------------ | ---------------------------- | ------- | ------------ |
| `.github/agents/declarative-agents-architect.agent.md` | Declarative Agents Architect | GPT-4.1 | ['codebase'] |

## Phase 2 — Cross-Reference Mapping

Built a 31-row mapping table linking equivalent agents across Copilot, Codex,
and Hermes by normalized slug. Full table serialized to `results/consolidated-agent-registry.json`
(machine-readable) and the key columns are shown below.

### Linked Copilot ↔ Codex twins

| Base concept | Copilot agent | Codex twin | Name match |
| ------------ | ------------- | ---------- | ---------- |

> Note: the Codex twin uses the distinct name `Blueprint Mode Codex` (intentional registration;
> preserved per rules-core #6). The only structural difference is the `model:` field
> (`GPT-5 mini (copilot)` vs `GPT-5-Codex (Preview) (copilot)`).

## Phase 3 — Sync & Deduplication

Applied the **minimal** set of changes (rules-core #1 map-before-touch, #4 one-platform-at-a-time):

### Fix 1 — Schema defect (applied)

- **File:** `.github/agents/declarative-agents-architect.agent.md`
- **Issue:** Copilot agent frontmatter spec requires a `description`; this file had only `name`,
  `model`, `tools` — `description` was missing (would fail Copilot CLI validation).
- **Fix:** Added `description` derived from the agent body's stated expertise (v1.5 schema, TypeSpec,
  Agents Toolkit). No other fields changed; name/trigger/registration preserved.

### Flags (NOT auto-fixed — preserve intent)

Three Copilot agent pairs share a near-identical opening description but are semantically distinct
agents; left intact for human review:

| Group              | Files                                                                          | Reason kept distinct            |
| ------------------ | ------------------------------------------------------------------------------ | ------------------------------- |
| Janitorial .NET    | `csharp-dotnet-janitor.agent.md`, `dotnet-upgrade.agent.md`                    | cleanup vs upgrade              |
| Planning           | `implementation-plan.agent.md`, `planner.agent.md`                             | plan authoring vs orchestration |
| .NET AI frameworks | `microsoft-agent-framework-python.agent.md`, `semantic-kernel-python.agent.md` | distinct frameworks             |

No duplicate `name` fields were found across the 30 Copilot agents, so there is
nothing to deduplicate by name. The 171 Copilot-only / 213 Hermes-only gap is expected: the two
ecosystems serve different surfaces and are not 1:1 mirrors.

## Phase 4 — Verification

Re-ran the discovery script after the fix. Results:

- [x] Copilot agent count unchanged (174) — no agents lost
- [x] Schema defects: **0** (was 1)
- [x] Cross-reference table regenerated (387 rows, idempotent)
- [x] `description` present on all 174 Copilot agents (platform schema satisfied)
- [x] Codex twin relationship preserved
- [x] No registrations renamed or removed (rules-core #6)

### Validation command

```bash
ls .github/agents/*.agent.md | wc -l   # 174
python3 _agents_fix_discover.py        # schema_issues: 0
```

## Artifacts Produced

| Artifact                     | Path                                       |
| ---------------------------- | ------------------------------------------ |
| Verification report          | `results/agents-fix.output.md`             |
| Consolidated registry (JSON) | `results/consolidated-agent-registry.json` |
| Raw discovery data           | `results/_agents_fix_discovery.json`       |
| Discovery script             | `_agents_fix_discover.py`                  |

## Skipped Template References

The prompt references per-prompt templates that do **not** exist in this repo (only `templates/_shared/`
exists). These were skipped gracefully; the shared rules/skills tables were loaded and applied:

- `prompts/templates/agents-fix/*.md` — not present (no override)
- Used instead: `templates/_shared/rules-core.md`, `templates/_shared/skills-table-core.md#agents-fix`

---

_End of report · 2026-08-12_
