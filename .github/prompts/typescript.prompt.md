---
name: typescript
title: 'TypeScript & Next.js'
description: Comprehensive TypeScript and Next.js code quality prompt aligned to repository standards.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - architecture
  - backend
  - configuration
  - frontend
  - ml
  - nextjs
  - prompts
  - skills
  - typescript
trigger: /typescript
dependencies: []
metadata:
  hermes: {}
---

## Goal

Use when "Comprehensive TypeScript and Next.js code quality prompt aligned to repository standards." to accomplish the associated tasks and objectives.

## Description

Produce strict, maintainable TypeScript and Next.js code using server-first patterns, safe configuration access, and validated external input handling.

## Context

Use this prompt for .ts and .tsx updates where code quality, correctness, and architectural consistency are required.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Advanced TypeScript typing and API design
- Next.js server/client boundary management
- Runtime validation and error modeling

## Subagents

| Subagent | Role | When to Use || --

- | --- | --- || Type Architect | Designs strict interfaces and type-safe contracts | Always || Next.js Reviewer | Enforces server-component-first architecture | UI and route changes || Validation Reviewer | Verifies Zod and runtime safety boundaries | External input paths |

## Personas

- Type Architect: Prefers explicit, safe types over implicit or any-based code.
- Next.js Reviewer: Minimizes client code and enforces clean component boundaries.
- Validation Reviewer: Requires consistent runtime validation and error handling.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Use strict TypeScript patterns and avoid unsafe typing shortcuts.
- Prefer server components and add use client only when justified.
- Route all DB interactions through DAL helpers when applicable.
- Validate external inputs with Zod and consistent error handling.
- Avoid direct process.env access in app logic; use centralized app config.

## Phases

### Phase 1: Type and Boundary Design

### Phase 2: Implementation with Strict Safety

## Steps

1. Define strict type contracts and boundary expectations.
2. Implement with explicit typing and schema validation.
3. Keep Next.js execution model server-first.
4. Use approved config and data-access abstractions.
5. Review maintainability and document complex types.

## Tasks

- Task 1.1 — Design strict interfaces and data flow contracts.
- Task 1.2 — Implement runtime validation and robust error paths.
- Task 1.3 — Enforce server/client boundaries and DAL usage patterns.
- Task 1.4 — Eliminate unsafe environment-access and typing patterns.
- Task 1.5 — Add documentation for complex types and assumptions.

## Subtasks

- Subtask 1.1.1 — Model optional and error states explicitly.
- Subtask 1.2.1 — Add schema parsing at external boundaries.
- Subtask 1.3.1 — Minimize use client and avoid unnecessary client bundle expansion.
- Subtask 1.4.1 — Route configuration reads through app-config abstractions.
- Subtask 1.5.1 — Add concise TSDoc for non-trivial type shapes.

## Actions Summary

1. Plan strict types and boundaries.
2. Implement safe runtime-validated logic.
3. Align with Next.js and DAL conventions.
4. Deliver maintainable strongly-typed code.

## Template References

Templates in `templates/typescript/`:- `phases.md`

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
