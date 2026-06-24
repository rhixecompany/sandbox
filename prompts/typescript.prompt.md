---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "typescript"
title: "TypeScript & Next.js"
description: "Comprehensive TypeScript and Next.js code quality prompt aligned to repository standards."
trigger: /typescript
tags: []
  - hermes
  - typescript
  - nextjs
  - code-quality
  - linting
---

## Goal
Use when "Comprehensive TypeScript and Next.js code quality prompt aligned to repository standards." to accomplish the associated tasks and objectives.


## Description

Produce strict, maintainable TypeScript and Next.js code using server-first patterns, safe configuration access, and validated external input handling.

## Context

Use this prompt for .ts and .tsx updates where code quality, correctness, and architectural consistency are required.

## Skills Required

- Advanced TypeScript typing and API design
- Next.js server/client boundary management
- Runtime validation and error modeling

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Type Architect | Designs strict interfaces and type-safe contracts | Always |
| Next.js Reviewer | Enforces server-component-first architecture | UI and route changes |
| Validation Reviewer | Verifies Zod and runtime safety boundaries | External input paths |

## Personas

- Type Architect: Prefers explicit, safe types over implicit or any-based code.
- Next.js Reviewer: Minimizes client code and enforces clean component boundaries.
- Validation Reviewer: Requires consistent runtime validation and error handling.

## Rules

- Use strict TypeScript patterns and avoid unsafe typing shortcuts.
- Prefer server components and add use client only when justified.
- Route all DB interactions through DAL helpers when applicable.
- Validate external inputs with Zod and consistent error handling.
- Avoid direct process.env access in app logic; use centralized app config.

## Phases

> ### Phase 1: Type and Boundary Design
> ### Phase 2: Implementation with Strict Safety

> **Full content:** `templates/typescript/phases.md`

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

Templates in `templates/typescript/`:
- `phases.md`
