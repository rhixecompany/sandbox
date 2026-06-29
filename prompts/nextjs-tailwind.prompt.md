---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "nextjs-tailwind"
title: "Nextjs Tailwind"
description: "Comprehensive Next.js and Tailwind implementation prompt aligned to project standards."
trigger: /nextjs-tailwind
tags:
  - architecture
  - audit
  - backend
  - data
  - frontend
  - ml
  - nextjs
  - performance
  - prompts
  - security
  - typescript
  - hermes
---

## Goal
Use when "Comprehensive Next.js and Tailwind implementation prompt aligned to project standards." to accomplish the associated tasks and objectives.


## Description

Implement or review Next.js App Router and Tailwind code with emphasis on server-first architecture, strict typing, security, and performance.

## Context

Use this prompt for TypeScript, TSX, JSX, JS, and CSS changes in Next.js + Tailwind projects where architecture, data fetching, and UI behavior must align to standards.

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#nextjs-tailwind)

- Next.js App Router architecture and React Server Components
- Tailwind CSS responsive and semantic styling
- Type-safe data and runtime validation with Zod

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Next.js Architect | Designs server/client boundaries and routing | New features and refactors |
| Styling Reviewer | Enforces Tailwind consistency and semantics | UI and CSS changes |
| Security Reviewer | Validates auth, sanitization, and API route safety | Input and API work |

## Personas

- Next.js Architect: Defaults to server components and minimal client boundaries.
- Styling Reviewer: Ensures responsive, semantic, and maintainable Tailwind patterns.
- Security Reviewer: Applies strict validation and safe handling of external inputs.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


- Prefer Server Components and mark client components only when necessary.
- Plan component hierarchy before implementation.
- Validate external input using strict schemas and explicit error handling.
- Include loading and error states for async boundaries.
- Use Next.js optimization features for images, fonts, and code splitting.

## Phases

> ### Phase 1: Architecture and Type Planning
> ### Phase 2: Implementation and Styling

> **Full content:** `templates/nextjs-tailwind/phases.md`

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

Templates in `templates/nextjs-tailwind/`:
- `phases.md`
