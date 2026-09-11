---
name: agent-provider-matrix-prompt
title: Agent / Provider Matrix Prompt
description: "Noninteractive prompt template for running the same request across every Hermes profile and authorized provider while preserving package-derived context and normalized output fields."
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - terminal
  - file
  - memory
trigger: /agent-provider-matrix
tags:
  - hermes
  - providers
  - profiles
  - matrix
  - prompts
  - execution
---

## Actions

- Do not ask clarifying questions.
- Use the provided context exactly as given.
- Return strict JSON first, then a short human summary if requested.
- Keep the response within the requested `max_output` budget.

# Agent / Provider Matrix Prompt

## Goal

Run the same user request across one Hermes profile and one authorized provider, using the package inventory as capability context, and return a normalized result.

## Required output fields

Return a JSON object with these keys:

- `profile`
- `provider`
- `package_context`
- `max_output`
- `capabilities`
- `model`
- `status`
- `result`
- `notes`
- `assumptions`

## Response rules

- Mention the provider explicitly.
- Mention the effective profile explicitly.
- Include a concise context summary derived from the package inventory.
- Include the requested max-output budget as an integer.
- List capabilities as an array of strings.
- If a default was assumed, explain it in `assumptions`.
- If the provider run fails, return the error text in `notes` and set `status` to `error`.

## Runtime placeholders

The runner fills these placeholders before calling Hermes:

- `{{REQUEST}}`
- `{{PROFILE}}`
- `{{PROVIDER}}`
- `{{MAX_OUTPUT}}`
- `{{PACKAGE_CONTEXT}}`
- `{{PACKAGE_CAPABILITIES}}`
- `{{MODEL_HINT}}`

## Request body

{{REQUEST}}

## Context

Profile: `{{PROFILE}}`

Provider: `{{PROVIDER}}`

Max output: `{{MAX_OUTPUT}}`

Model hint: `{{MODEL_HINT}}`

Package context:

{{PACKAGE_CONTEXT}}

Package capabilities:

{{PACKAGE_CAPABILITIES}}

## Final instruction

Return only JSON unless the runner explicitly asks for a short markdown summary.
