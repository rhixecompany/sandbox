---
agent: "agent"
description: "Hermes-equivalent: create a high-level Epic Architecture Specification from an Epic PRD."
---

## Goal

Turn an Epic PRD into a high-level architecture specification with layers, enablers, and technology guidance.

## Context

- Use when an epic already exists and needs architecture direction.
- Keep the plan high-level and architecture-focused.
- Use Mermaid diagrams for system layering and data flow.
- Do not write implementation code.

## Inputs

- Epic PRD path: `/docs/ways-of-work/plan/{epic-name}/epic.md`
- Optional architecture notes or constraints

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/arch.md`

## Rules

1. Include an architecture overview.
2. Show User, Application, Service, Data, and Infrastructure layers.
3. List features and technical enablers.
4. Recommend a technology stack with short justification.
5. Include a value assessment and t-shirt estimate.
6. Prefer labeled Mermaid subgraphs for clarity.

## Phases

> ### Phase 1: Analyze the epic
> **Goal:** extract the architectural implications of the epic.

> **Full content:** `templates/hermes-breakdown-epic-arch/phases.md`

## Actions Summary

1. Read the Epic PRD.
2. Draft the architecture overview and diagram.
3. Add enablers, stack guidance, and estimates.
4. Verify completeness and path correctness.


## Template References

Templates in `templates/hermes-breakdown-epic-arch/`:
- `phases.md`
