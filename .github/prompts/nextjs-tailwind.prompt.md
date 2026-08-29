---
name: nextjs-tailwind
title: Next.js + Tailwind Component Build
description: Plans and implements typed, accessible Next.js components with Tailwind CSS, covering server/client boundaries, validation, and responsive styling.
trigger: /nextjs-tailwind
version: 1.0.0
author: Hermes Agent
tags:
  - nextjs
  - tailwind
  - typescript
  - frontend
  - ui
  - design-system
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---
## Table of Contents

## Goal

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
  - [Phase 1: Architecture and Type Planning](#phase-1:-architecture-and-type-planning)
  - [Phase 2: Implementation and Styling](#phase-2:-implementation-and-styling)
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



- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Architecture and Type Planning](#phase-1:-architecture-and-type-planning)
- [Phase 2: Implementation and Styling](#phase-2:-implementation-and-styling)
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





Use when "Comprehensive Next.js and Tailwind implementation prompt aligned to project standards." to accomplish the associated tasks and objectives.

## Description

Implement or review Next.js App Router and Tailwind code with emphasis on server-first architecture, strict typing, security, and performance.


Use this prompt for TypeScript, TSX, JSX, JS, and CSS changes in Next.js + Tailwind projects where architecture, data fetching, and UI behavior must align to standards.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Next.js App Router architecture and React Server Components
- Tailwind CSS responsive and semantic styling
- Type-safe data and runtime validation with Zod

## Subagents

| Subagent | Role | When to Use || --

- | --- | --- || Next.js Architect | Designs server/client boundaries and routing | New features and refactors || Styling Reviewer | Enforces Tailwind consistency and semantics | UI and CSS changes || Security Reviewer | Validates auth, sanitization, and API route safety | Input and API work |

## Personas

- Next.js Architect: Defaults to server components and minimal client boundaries.
- Styling Reviewer: Ensures responsive, semantic, and maintainable Tailwind patterns.
- Security Reviewer: Applies strict validation and safe handling of external inputs.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Prefer Server Components and mark client components only when necessary.
- Plan component hierarchy before implementation.
- Validate external input using strict schemas and explicit error handling.
- Include loading and error states for async boundaries.
- Use Next.js optimization features for images, fonts, and code splitting.


### Phase 1: Architecture and Type Planning

### Phase 2: Implementation and Styling

## Steps

1. Plan route and component structure with server-first defaults.
2. Define interfaces and schema-based runtime validation.
3. Implement data fetching, loading states, and error boundaries.
4. Apply Tailwind styles with responsive and semantic patterns.
5. Validate security and performance characteristics.

## Tasks

- Task 1.1 — Define component hierarchy and server/client execution boundaries.
- Task 1.2 — Implement type-safe data and input validation paths.
- Task 1.3 — Build UI with responsive Tailwind and semantic markup.
- Task 1.4 — Add error/loading handling for async and route-level states.
- Task 1.5 — Verify optimization and security controls before completion.

## Subtasks

- Subtask 1.1.1 — Mark client components only when interactivity requires it.
- Subtask 1.2.1 — Use schema validation at trust boundaries.
- Subtask 1.3.1 — Keep color and spacing consistent with project patterns.
- Subtask 1.4.1 — Handle retry paths and fallback rendering behavior.
- Subtask 1.5.1 — Confirm image/font optimization and safe API route logic.

## Actions Summary

1. Plan architecture first.
2. Implement with strict typing and validation.
3. Style with semantic Tailwind patterns.
4. Validate performance and security before handoff.

## Template References

Templates in `templates/nextjs-tailwind/`:- `phases.md`

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section