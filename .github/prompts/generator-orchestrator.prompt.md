---
name: generator-orchestrator
trigger: /generator-orchestrator
description: Dependency-aware orchestrator prompt for root blueprint and MCP generator prompts with strict stage gates and consistency validation.
agent: agent
---

## Description

### Goal

Create one orchestrator prompt that coordinates only the 11 root generator prompts in `.github/prompts` with dependency-aware ordering, conditional MCP/server branching, deterministic execution modes, and strict validation gates.

### Legacy Prompt Details

This prompt preserves the generator-style intent used across root blueprint prompts while adding orchestrator-level dependency management and consistency checks.

## Context

Use this prompt when you need one runbook to generate aligned architecture, workflow, documentation, and optional MCP/server outputs.

### Scope

- Included prompts: root-level generator prompts only (11 files).
- Excluded prompts: subproject prompts, including comicwise-specific generator prompts.
- Output location: `.github/prompts` and generated docs or code paths requested by the run.

## Skills Required

- Dependency graph design for staged orchestration.
- Prompt-composition and deterministic branching.
- Documentation consistency validation and remediation.
- Multi-stack detection for TypeScript, Python, Swift, and Copilot Studio MCP paths.

## Subagents

- No external subagents are required.
- Invoke only the following root generator prompts as sub-prompts:
  - `technology-stack-blueprint-generator.prompt.md`
  - `folder-structure-blueprint-generator.prompt.md`
  - `architecture-blueprint-generator.prompt.md`
  - `project-workflow-analysis-blueprint-generator.prompt.md`
  - `code-exemplars-blueprint-generator.prompt.md`
  - `copilot-instructions-blueprint-generator.prompt.md`
  - `readme-blueprint-generator.prompt.md`
  - `typescript-mcp-server-generator.prompt.md`
  - `python-mcp-server-generator.prompt.md`
  - `swift-mcp-server-generator.prompt.md`
  - `mcp-copilot-studio-server-generator.prompt.md`

## Personas

- Primary persona: Blueprint Orchestrator.
- Behavioral expectations:
  - deterministic and stage-gated
  - strict on dependencies
  - explicit about degraded modes and failures

## Rules

### Inputs

Accept these unified inputs:

- `mode`: `full | quick | custom`
- `scope`: target folders or project boundaries
- `detail-level`: `standard | deep | implementation-ready`
- `validation-level`: `standard | strict`
- `include-code-generation`: `true | false`
- `include-documentation`: `true | false`
- `custom-stage-selection` (custom mode only): list of requested stages

### Deterministic Defaults

When inputs are missing, use:

- `mode=full`
- `scope=workspace-root`
- `detail-level=standard`
- `validation-level=strict`
- `include-code-generation=true`
- `include-documentation=true`
- `custom-stage-selection=[]`

### Outputs

Always produce:

- generated artifact manifest with stage attribution
- cross-linking report between generated docs
- validation report (pass, warn, fail with reasons)
- execution summary with retries, degraded paths, and blocked handoffs

### Orchestration Constraints

- Never run downstream prompts before prerequisite artifacts exist.
- Stage quality gate must pass before advancing.
- Retry policy for missing sections: one retry only with stricter constraints.
- If still invalid after retry, continue in degraded mode and record warning.
- Final consistency gate is mandatory for successful handoff.

## Phases

### Phase 1: Discovery

| Field | Details |
| --- | --- |
| Goal | Inventory and classify the 11 root generator prompts by role and dependency. |
| Inputs | Prompt inventory from `.github/prompts` and explicit root generator list. |
| Outputs | Classification map: analysis, documentation, code-generation; dependency edge list. |
| Validation | Confirm exactly 11 root prompts are in scope and no excluded prompt is referenced. |

### Phase 2: Contract Design

| Field | Details |
| --- | --- |
| Goal | Define deterministic orchestration contract (inputs, defaults, outputs, and mode behavior). |
| Inputs | User parameters and deterministic default matrix. |
| Outputs | Normalized run configuration and expected output schema. |
| Validation | Verify full, quick, and custom modes each resolve to unambiguous stage plans. |

### Phase 3: Execution Graph

| Field | Details |
| --- | --- |
| Goal | Execute Stage A-E graph with dependency-aware ordering and gates. |
| Inputs | Normalized run configuration and dependency graph from prior phases. |
| Outputs | Generated docs/code artifacts and per-stage gate results. |
| Validation | Each stage references only artifacts from completed prerequisite stages. |

### Phase 4: Safety and Recovery

| Field | Details |
| --- | --- |
| Goal | Apply fallback, retry, degraded-mode, and handoff-fail policies consistently. |
| Inputs | Stage outputs, validation failures, and ambiguity signals. |
| Outputs | Retry logs, degraded-mode warnings, and remediation checklist when required. |
| Validation | Confirm ambiguous detection, missing sections, and inconsistency cases are all handled explicitly. |

### Phase 5: Verification and Handoff

| Field | Details |
| --- | --- |
| Goal | Consolidate artifacts, run consistency validation, and issue final pass/fail handoff decision. |
| Inputs | Complete stage outputs and all gate reports. |
| Outputs | Final artifact manifest, consistency results, and execution summary. |
| Validation | Fail handoff if cross-document inconsistencies remain unresolved. |

## Steps

1. Build inventory and role classification for the 11 root generators.
2. Normalize inputs using deterministic defaults.
3. Resolve execution plan by mode:
    - `full`: run Stage A, B, C, optional D by conditions, then E.
    - `quick`: run Stage A and minimal Stage B (`architecture` only), then Stage E.
    - `custom`: run user-selected stages if prerequisites are satisfied; otherwise auto-insert missing prerequisite stages.
4. Execute Stage A (parallel):
    - `technology-stack-blueprint-generator.prompt.md`
    - `folder-structure-blueprint-generator.prompt.md`
5. Run Stage A quality gate:
    - stack summary exists and includes confidence or ambiguity marker
    - folder structure artifact exists and is parseable
6. Execute Stage B (gated):
    - `architecture-blueprint-generator.prompt.md` (requires Stage A)
    - `project-workflow-analysis-blueprint-generator.prompt.md` (requires Stage A)
    - `code-exemplars-blueprint-generator.prompt.md` (requires Stage A)
7. Run Stage B quality gate:
    - each artifact has required top-level sections
    - references point to existing files or generated artifacts only
8. Execute Stage C (gated):
    - `copilot-instructions-blueprint-generator.prompt.md` (requires Stage A and B)
    - `readme-blueprint-generator.prompt.md` (requires Stage A and B)
9. Run Stage C quality gate:
    - instruction and README outputs cross-link to architecture/workflow/stack artifacts
    - no contradictory tech or workflow claims across generated docs
10. Execute Stage D (conditional MCP generation):
     - run only if `include-code-generation=true`
     - route by detected stack and mode:
        - TypeScript or Node indicators -> `typescript-mcp-server-generator.prompt.md`
        - Python indicators -> `python-mcp-server-generator.prompt.md`
        - Swift indicators -> `swift-mcp-server-generator.prompt.md`
        - Copilot Studio or Power Platform indicators -> `mcp-copilot-studio-server-generator.prompt.md`
11. Run Stage D quality gate:
     - generated server artifacts include runnable entry points and dependency metadata
     - output schemas and transport choices are documented
12. Execute Stage E consolidation and consistency validation:
     - compile final artifact manifest
     - compute cross-document consistency checks
     - produce pass/fail handoff decision

## Tasks

- Task 1.1 — Inventory root generator prompts and classify by role.
- Task 1.2 — Define dependency edges and prerequisite matrix.
- Task 2.1 — Normalize run inputs and resolve deterministic defaults.
- Task 2.2 — Map mode to stage-selection behavior.
- Task 3.1 — Execute Stage A in parallel and enforce gate.
- Task 3.2 — Execute Stage B in dependency order and enforce gate.
- Task 3.3 — Execute Stage C and enforce cross-link gate.
- Task 3.4 — Execute Stage D conditionally by stack and mode.
- Task 4.1 — Apply retry and degraded-mode policy for incomplete outputs.
- Task 5.1 — Run final consistency gate and decide handoff pass/fail.
- Task 5.2 — Emit manifest, validation report, and execution summary.

## Subtasks

- Subtask 1.1.1 — Confirm included set contains exactly 11 root prompts.
- Subtask 1.1.2 — Classify each prompt into analysis, documentation, or code-generation.
- Subtask 1.2.1 — Encode Stage A -> Stage B -> Stage C dependencies.
- Subtask 1.2.2 — Encode Stage D as conditional on stack detection and include-code-generation.
- Subtask 2.1.1 — Apply default `mode=full` when missing.
- Subtask 2.1.2 — Apply default `validation-level=strict` when missing.
- Subtask 2.2.1 — For custom mode, insert prerequisite stages automatically.
- Subtask 3.1.1 — Run stack and folder prompts concurrently.
- Subtask 3.1.2 — Block Stage B unless Stage A gate passes or degraded mode is recorded.
- Subtask 3.2.1 — Run architecture, workflow, and code exemplars after Stage A artifacts exist.
- Subtask 3.3.1 — Run instructions and README prompts only after Stage B gate passes.
- Subtask 3.4.1 — Trigger MCP generators per detected technology indicators.
- Subtask 4.1.1 — Retry once with stricter constraints when required sections are missing.
- Subtask 4.1.2 — Continue degraded with explicit warning if retry fails.
- Subtask 5.1.1 — Fail handoff when cross-document inconsistencies are unresolved.
- Subtask 5.1.2 — Emit targeted remediation checklist for failed handoffs.

## Actions Summary

### Invocation Order and Branching

- Stage A (parallel): technology-stack + folder-structure.
- Stage B (gated): architecture + workflow-analysis + code-exemplars.
- Stage C (gated): copilot-instructions + readme.
- Stage D (conditional): TypeScript, Python, Swift, and Copilot Studio MCP generators based on detected stack and mode.
- Stage E (final): consolidation, consistency validation, and handoff decision.

### Failure Handling Policy

- Ambiguous stack detection: keep auto-detect and continue with generic-safe defaults.
- Missing required sections: retry once with stricter constraints, then continue degraded with warning.
- Cross-document inconsistency: fail handoff and emit remediation checklist.

### Verification Checklist

1. Static prompt lint pass: all required sections exist and section order is valid.
2. Dependency trace check: each stage references only prior completed outputs.
3. Conditional-path check: full, quick, and custom modes are deterministic.
4. Safety check: fallback and failure handling are explicit.
5. Handoff check: manifest and consistency results are present and actionable.
