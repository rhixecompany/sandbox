---
name: generator-orchestrator
title: Generator Orchestrator
description: Dependency-aware orchestrator prompt for root blueprint and MCP generator prompts with strict stage gates and consistency validation.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - subagent-driven-development
formatter: default
plan: 'None'
dependencies:
  - "skill:subagent-driven-development"
tags:
  - architecture
  - backend
  - documentation
  - generator
  - mcp
  - prompts
  - typescript
  - workflow
  - git
trigger: /generator-orchestrator
metadata:
  hermes: {}
---

## Goal

Dependency-aware orchestrator prompt for root blueprint and MCP generator prompts with strict stage gates and consistency validation.

## Description

### Goal

Create one orchestrator prompt that coordinates only the 11 root generator prompts in `prompts` with dependency-aware ordering, conditional MCP/server branching, deterministic execution modes, and strict validation gates.

## Context

Use this prompt when you need one runbook to generate aligned architecture, workflow, documentation, and optional MCP/server outputs.

### Scope

- Included prompts: root-level generator prompts only (11 files).
- Excluded prompts: subproject prompts, including comicwise-specific generator prompts.
- Output location: `prompts` and generated docs or code paths requested by the run.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Dependency graph design for staged orchestration.
- Prompt-composition and deterministic branching.
- Documentation consistency validation and remediation.
- Multi-stack detection for TypeScript, Python, Swift, and Copilot Studio MCP paths.

## Subagents

- No external subagents are required.
- Invoke only the following root generator prompts as sub-prompts:  - `technology-stack-blueprint-generator.prompt.md`  - `folder-structure-blueprint-generator.prompt.md`  - `architecture-blueprint-generator.prompt.md`  - `project-workflow-analysis-blueprint-generator.prompt.md`  - `code-exemplars-blueprint-generator.prompt.md`  - `copilot-instructions-blueprint-generator.prompt.md`  - `readme-blueprint-generator.prompt.md`  - `typescript-mcp-server-generator.prompt.md`  - `python-mcp-server-generator.prompt.md`  - `swift-mcp-server-generator.prompt.md`  - `mcp-copilot-studio-server-generator.prompt.md`

## Personas

- Primary persona: Blueprint Orchestrator.
- Behavioral expectations:  - deterministic and stage-gated  - strict on dependencies  - explicit about degraded modes and failures

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)
> Accept these unified inputs:>
>
> - `mode`: `full | quick | custom`
> **Full content:** `templates/generator-orchestrator/rules.md`

## Phases

### Phase 1: Discovery

### Phase 2: Contract Design

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
- Subtask 1.2.1 — Encode Stage A -

> Stage B -
> Stage C dependencies.

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

Detailed templates in `templates/generator-orchestrator/`:- `phases.md`- `rules.md`- `steps.md`

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |
