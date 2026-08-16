---
name: openrouter-client-py
title: "openrouter-client-py — Spec"
description: "Spec for openrouter-client-py — Python client wrapper for OpenRouter chat completions API"
version: 1.0.0
status: in_progress
created: 2026-08-16
tags: [spec, package, openrouter, python]
requirements:
  - R1: Package uses pyproject.toml with setuptools build backend
  - R2: Provides async chat_send function and OpenRouterClient class
  - R3: Has type hints and pyright-compatible annotations
  - R4: Has SPEC.md and PLAN.md
  - R5: Has bun package.json for monorepo metadata
acceptance_criteria:
  - AC1: pyproject.toml is valid with correct dependencies
  - AC2: pyright passes on source files (or failures are documented)
  - AC3: pytest passes (if tests exist)
  - AC4: package.json with bun packageManager exists
  - AC5: SPEC.md status is in_progress or done
  - AC6: PLAN.md exists with actionable phases
---

# openrouter-client-py — Spec

## Purpose

Python client wrapper for OpenRouter's chat completions API. Provides async `send_chat` convenience function and a reusable `OpenRouterClient` class with configuration-driven initialization.

## Stack

- Python 3.11+, setuptools
- Dependency: openrouter>=1.0.0
- Optional test dep: pytest>=7.0
- Quality: ruff, pyright

## Requirements

See frontmatter.

## Acceptance Criteria

See frontmatter.
