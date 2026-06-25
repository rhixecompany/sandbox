---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "generator-orchestrator"
title: "Generator Orchestrator"
description: "Dependency-aware orchestrator prompt for root blueprint and MCP generator prompts with strict stage gates and consistency validation."
tags:
  - hermes
  - codegen
---

## Description

### Goal

Create one orchestrator prompt that coordinates only the 11 root generator prompts in `.github/prompts` with dependency-aware ordering, conditional MCP/server branching, deterministic execution modes, and strict validation gates.

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

> Accept these unified inputs:
> - `mode`: `full | quick | custom`

> **Full content:** `templates/generator-orchestrator/rules.md`

## Phases

> ### Phase 1: Discovery
> ### Phase 2: Contract Design

> **Full content:** `templates/generator-orchestrator/phases.md`

## Steps

> 1. Build inventory and role classification for the 11 root generators.
> 2. Normalize inputs using deterministic defaults.

> **Full content:** `templates/generator-orchestrator/steps.md`

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


## Template References

Detailed templates in `templates/generator-orchestrator/`:
- `phases.md`
- `rules.md`
- `steps.md`
