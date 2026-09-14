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

- `Summarize the package capability matrix and return a normalized JSON record with provider, context, max_output, capabilities, status, result, and notes.`
- `ops`
- `copilot`
- `1200`
- `- openrouter-client (typescript, bun)
  summary: TypeScript/Bun OpenRouter wrapper with TypeScript wrapper, OpenRouter SDK client, chat completions, streaming
  capabilities: TypeScript wrapper, OpenRouter SDK client, chat completions, streaming, custom headers, max_tokens, temperature control, typed client
  files: PLAN.md, README.md, SPEC.md, package.json, src/chat.ts, src/client.ts, src/types.ts, test/chat.test.ts … (+1 more)
- openrouter-client-py (python, python)
  summary: Python OpenRouter wrapper with Python wrapper, OpenRouter client, chat completions, streaming
  capabilities: Python wrapper, OpenRouter client, chat completions, streaming, custom headers, max_tokens, temperature control, dataclasses
  files: .pytest_cache/README.md, PLAN.md, README.md, SPEC.md, pyproject.toml, src/openrouter_client_py.egg-info/SOURCES.txt, src/openrouter_client_py.egg-info/dependency_links.txt, src/openrouter_client_py.egg-info/requires.txt … (+6 more)`
- `- TypeScript wrapper
- OpenRouter SDK client
- chat completions
- streaming
- custom headers
- max_tokens
- temperature control
- typed client
- Python wrapper
- OpenRouter client
- dataclasses`
- `deepseek-v4-flash-free`

## Request body

Summarize the package capability matrix and return a normalized JSON record with provider, context, max_output, capabilities, status, result, and notes.

## Context

Profile: `ops`

Provider: `copilot`

Max output: `1200`

Model hint: `deepseek-v4-flash-free`

Package context:

- openrouter-client (typescript, bun)
  summary: TypeScript/Bun OpenRouter wrapper with TypeScript wrapper, OpenRouter SDK client, chat completions, streaming
  capabilities: TypeScript wrapper, OpenRouter SDK client, chat completions, streaming, custom headers, max_tokens, temperature control, typed client
  files: PLAN.md, README.md, SPEC.md, package.json, src/chat.ts, src/client.ts, src/types.ts, test/chat.test.ts … (+1 more)
- openrouter-client-py (python, python)
  summary: Python OpenRouter wrapper with Python wrapper, OpenRouter client, chat completions, streaming
  capabilities: Python wrapper, OpenRouter client, chat completions, streaming, custom headers, max_tokens, temperature control, dataclasses
  files: .pytest_cache/README.md, PLAN.md, README.md, SPEC.md, pyproject.toml, src/openrouter_client_py.egg-info/SOURCES.txt, src/openrouter_client_py.egg-info/dependency_links.txt, src/openrouter_client_py.egg-info/requires.txt … (+6 more)

Package capabilities:

- TypeScript wrapper
- OpenRouter SDK client
- chat completions
- streaming
- custom headers
- max_tokens
- temperature control
- typed client
- Python wrapper
- OpenRouter client
- dataclasses

## Final instruction

Return only JSON unless the runner explicitly asks for a short markdown summary.
