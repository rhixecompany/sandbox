---
name: typescript
title: TypeScript and Next.js Code Quality
description: Produce strict, maintainable TypeScript and Next.js code using server-first patterns, safe configuration access, and validated external input handling.
trigger: /typescript
category: development
version: 1.0.0
author: Hermes Agent
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Produce strict, maintainable TypeScript and Next.js code using server-first patterns, safe configuration access, and validated external input handling.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Type and Boundary Design](#phase-1:-type-and-boundary-design)
  - [Phase 2: Implementation with Strict Safety](#phase-2:-implementation-with-strict-safety)
- [Steps](#steps)
- [Tasks](#tasks)
- [Subtasks](#subtasks)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Type and Boundary Design](#phase-1:-type-and-boundary-design)
- [Phase 2: Implementation with Strict Safety](#phase-2:-implementation-with-strict-safety)
- [Steps](#steps)
- [Tasks](#tasks)
- [Subtasks](#subtasks)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Use when "Comprehensive TypeScript and Next.js code quality prompt aligned to repository standards." to accomplish the associated tasks and objectives.

## Description

Produce strict, maintainable TypeScript and Next.js code using server-first patterns, safe configuration access, and validated external input handling.


Use this prompt for .ts and .tsx updates where code quality, correctness, and architectural consistency are required.

## Skills Required

> See full table with per-domain purposes:
> [`templates/skills-table-core.md`](templates/skills-table-core.md)

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

> Core rules: [`templates/rules-core.md`](templates/rules-core.md)

- Use strict TypeScript patterns and avoid unsafe typing shortcuts.
- Prefer server components and add use client only when justified.
- Route all DB interactions through DAL helpers when applicable.
- Validate external inputs with Zod and consistent error handling.
- Avoid direct process.env access in app logic; use centralized app config.


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
- Task 1.2 — Implement runtime validation and strong error paths.
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

Templates in `templates/`:- `phases.md`

## Personality

See [`templates/personality.md`](templates/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/best-practices.md`](templates/best-practices.md) for cross-cutting best practices.

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

See [`templates/deps-core.md`](templates/deps-core.md) for shared dependency patterns.

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

## Workflow

<content>

Same-family prompts:

- [`typescript-mcp-server-generator.prompt.md`](typescript-mcp-server-generator.prompt.md)
```
# Prompt template
Execute the workflow defined in this file.
```
