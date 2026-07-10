---
title: "Implement Copilot Agent/Instruction Inventory Cross-Reference v1"
description: "Add bidirectional cross-referencing between 174 Copilot agents and 186 instruction files, validated by the Bash automation toolkit."
goal: "Copilot Agent/Instruction Library Cross-Reference"
status: "draft"
tags:
  - architecture
  - refactoring
  - specification
  - typescript
  - copilot
  - cross-reference
  - inventory
author: "Hermes Agent"
version: "1.0.0"
---

# Implement Copilot Agent/Instruction Inventory Cross-Reference

> **Goal:** Add automated bidirectional cross-referencing between `.github/agents/` and `.github/instructions/` so every agent.md declares which instructions it applies and every instruction is back-referenced from the agents that consume it.

---

## 1. Requirements & Constraints

- **REQ-001**: Each agent `.md` in `.github/agents/` must declare its `applyToInstructions` field (list of instruction filenames).
- **REQ-002**: An inventory script must validate that every referenced instruction file actually exists in `.github/instructions/`.
- **REQ-003**: A report/matrix must be generated showing the bidirectional mapping (agents → instructions & instructions → agents).
- **CON-001**: Do not modify instruction files themselves — only the agent files carry the cross-reference declarations.
- **CON-002**: Agent frontmatter may already have a `description`, `applyTo`, or `instructions` field — preserve all existing fields; only add `applyToInstructions` if missing.
- **CON-003**: The Bash toolkit (`projects/Bash/`) is the execution vehicle — new logic goes into `src/` surfaced through its `.sh`/`.ps1` wrappers.
- **PAT-001**: Follow the existing agent.md YAML frontmatter pattern (see `.github/agents/*.agent.md` for examples).
- **GUD-001**: Run `context-map` before touching the directory to understand dependency scope.

---

## 2. Implementation Steps

### Implementation Phase 1: Discovery & Mapping

- **GOAL-001**: Generate the complete inventory of existing agent frontmatter and instruction files.
- **TASK-001.1**: Run `ls .github/agents/*.agent.md | wc -l` to confirm 174 agents.
- **TASK-001.2**: Run `ls .github/instructions/*.instructions.md | wc -l` to confirm 186 instruction files.
- **TASK-001.3**: Build a Python script (`scripts/build-cross-ref-inventory.py`) that:
  - Parses each `.agent.md` frontmatter (YAML) extracting `name`, `description`, and any existing `applyTo`/`instructions` field.
  - Lists every instruction filename from `.github/instructions/`.
  - Outputs `reports/cross-reference-inventory.json` with the raw mapping data.
- **TASK-001.4**: Validate: inventory JSON contains exactly 174 agent entries and 186 instruction entries.

### Implementation Phase 2: Agent Frontmatter Augmentation

- **GOAL-002**: Add `applyToInstructions` field to every agent that lacks it.
- **TASK-002.1**: For each agent in `.github/agents/`, if frontmatter does not already contain an `applyToInstructions` key, add it with an empty list `[]`.
- **TASK-002.2**: For agents already declaring `applyTo` or `instructions`, migrate those values into `applyToInstructions` as a list, preserving the original.
- **TASK-002.3**: Run YAML validation on every modified file — use `python3 -c "import yaml; yaml.safe_load(open('file'))"` for each.
- **TASK-002.4**: Verify that `grep -rl 'applyToInstructions:' .github/agents/ | wc -l` equals 174.

### Implementation Phase 3: Cross-Reference Report Generation

- **GOAL-003**: Produce a human-readable and machine-parseable cross-reference report.
- **TASK-003.1**: Extend the Python inventory script to generate:
  - `reports/cross-reference-matrix.md` — a Markdown table with columns: Agent Name | File | applyToInstructions.
  - `reports/instruction-usage-report.md` — per-instruction-file list showing which agents reference it.
- **TASK-003.2**: Add validation: flag any `applyToInstructions` entry that does not match a file in `.github/instructions/` (the value must be `*` or an exact filename).
- **TASK-003.3**: Output summary stats: `N agents with empty applyToInstructions`, `M agents populated`, `K orphan references detected`.

### Implementation Phase 4: Bash Toolkit Integration

- **GOAL-004**: Wire the cross-reference logic into the Bash toolkit automation pipeline.
- **TASK-004.1**: Add a TypeScript module `projects/Bash/src/cross-reference.ts` that wraps the Python inventory script and surfaces its output.
- **TASK-004.2**: Add a shell wrapper `projects/Bash/cross-reference.sh` that invokes the TypeScript module.
- **TASK-004.3**: Add a CI workflow `.github/workflows/validate-cross-reference.yml` that runs on PRs touching `.github/agents/` or `.github/instructions/`.

---

## 3. Alternatives

- **ALT-001**: **Manual cross-reference via a single spreadsheet.** Rejected — not automatable and will drift out of date.
- **ALT-002**: **Embed instruction references only in `.github/copilot-instructions.md`.** Rejected — that file is a single global pointer, not per-agent granularity.

---

## 4. Dependencies

- **DEP-001**: Python 3 with `pyyaml` installed (`pip install pyyaml` or available via `venv`).
- **DEP-002**: `projects/Bash/` TypeScript build chain (Bun) for the TS module wrapper.
- **DEP-003**: Existing agent `.agent.md` files must have parsable YAML frontmatter (all 174 currently do per workspace audit).

---

## 5. Files

- **FILE-001**: `.github/agents/*.agent.md` — all 174 files, each receiving a possible `applyToInstructions` frontmatter addition.
- **FILE-002**: `scripts/build_cross_ref_inventory.py` — new Python inventory + validation script (under `.github/scripts/`).
- **FILE-003**: `reports/cross-reference-matrix.md` — generated agent→instruction matrix report.
- **FILE-004**: `reports/instruction-usage-report.md` — generated instruction→agent reverse report.
- **FILE-005**: `reports/cross-reference-inventory.json` — raw machine-parseable inventory.
- **FILE-006**: `projects/Bash/src/cross-reference.ts` — TypeScript wrapper module.
- **FILE-007**: `projects/Bash/cross-reference.sh` — shell wrapper.
- **FILE-008**: `.github/workflows/validate-cross-reference.yml` — CI workflow.

---

## 6. Testing

- **TEST-001**: `scripts/build_cross_ref_inventory.py --validate` — exit code 0 when all `applyToInstructions` entries resolve to real files in `.github/instructions/`.
- **TEST-002**: After Phase 2, `grep -rl 'applyToInstructions:' .github/agents/ | wc -l` must equal the total agent count (174).
- **TEST-003**: After Phase 3, the generated report must have exactly as many rows as there are agents with non-empty `applyToInstructions`.

---

## 7. Risks & Assumptions

- **RISK-001**: Some agents may have custom frontmatter schemas (extra fields like `category`, `version`) — the Python parser must not crash on unknown fields; only check/add `applyToInstructions`.
- **ASSUMPTION-001**: All 174 agent `.md` files have valid YAML frontmatter delimited by `---`.
- **ASSUMPTION-002**: Instruction filenames are unique within `.github/instructions/` (verified true as of 2026-07-09).
- **ASSUMPTION-003**: The Bash toolkit CI matrix can be extended without breaking existing workflows.

---

## 8. Related Specifications / Further Reading

- [`AGENTS.md` — Section 1: Workspace Big Picture](../AGENTS.md)
- [`AGENTS.md` — Section 2: Directory Map](../AGENTS.md#2-directory-map-verified)
- [Bash Toolkit README](../projects/Bash/README.md)
- [Copilot agent.md spec (GitHub Docs)](https://docs.github.com/en/copilot/managing-copitor/managing-ai-assistants/managing-github-copilot-custom-agents)
