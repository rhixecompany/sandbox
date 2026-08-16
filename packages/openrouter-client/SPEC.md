---
name: openrouter-client
title: "openrouter-client — Spec"
description: "Spec for openrouter-client — TypeScript wrapper for OpenRouter chat completions API"
version: 1.0.0
status: in_progress
created: 2026-08-16
tags: [spec, package, openrouter, typescript]
requirements:
  - R1: Package uses Bun as package manager
  - R2: Provides typed client wrapper for OpenRouter chat completions API
  - R3: Exports send_chat function and OpenRouterClient class
  - R4: Has typecheck passing (tsc --noEmit)
  - R5: Has SPEC.md and PLAN.md
acceptance_criteria:
  - AC1: package.json has "packageManager": "bun@1.3.14"
  - AC2: tsc --noEmit passes with zero errors
  - AC3: bun test passes (if tests exist)
  - AC4: SPEC.md status is in_progress or done
  - AC5: PLAN.md exists with actionable phases
---

# openrouter-client — Spec

## Purpose

TypeScript client wrapper for OpenRouter's chat completions API using @openrouter/sdk. Provides a simple `send_chat` function and a reusable `OpenRouterClient` class with config-driven initialization.

## Stack

- TypeScript 5.x, Bun 1.3.14
- Dependency: @openrouter/sdk ^1.0.0
- Dev: @types/bun, typescript

## Requirements

See frontmatter.

## Acceptance Criteria

See frontmatter.
