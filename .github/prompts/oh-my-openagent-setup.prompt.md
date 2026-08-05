---
name: oh-my-openagent-setup
title: Oh My OpenAgent Setup
description: 'Install, configure, and verify Oh My OpenAgent (OMO) and the Oh My Hermes workflow layer on top of OpenCode CLI with deterministic, read-only verification.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
  - hermes
  - opencode
  - setup
  - ops
  - workflow
trigger: /oh-my-openagent-setup
formatter: default
dependencies:
  - skill:using-superpowers
  - skill:user-communication-preferences
  - skill:verification-before-completion
  - skill:oh-my-openagent-setup
toolsets:
  - file
  - terminal
scripts:
  - ~/Desktop/SandBox/scripts/omo_doctor.py
skills:
  - using-superpowers
  - user-communication-preferences
  - verification-before-completion
  - oh-my-openagent-setup
plan: None
metadata:
  hermes: {}
---

## Goal

Provision and verify Oh My OpenAgent (OMO, formerly oh-my-opencode) and the Oh My Hermes workflow layer on top of OpenCode CLI + Hermes Agent, with deterministic, non-destructive validation.

## Context

- OpenCode on Windows resolves as `opencode.cmd`.
- Canonical verification script: `scripts/omo_doctor.py`.
- Config lives at `~/.config/opencode/oh-my-openagent.jsonc` or `oh-my-opencode.jsonc`.
- Non-interactive Hermes-driven runs should set `OPENCODE_DISABLE_EMBEDDED_WEB_UI=true`, `OPENCODE_DISABLE_SHARE=true`, and `OPENCODE_DISABLE_AUTOUPDATE=true`.

## Workflow

1. Confirm prerequisites:
   - `opencode --version` is at least 1.4.0.
   - `bun --version` is available.
2. Install OMO:
   - interactive: `bunx oh-my-openagent install`
   - non-interactive: `bunx oh-my-openagent install --no-tui --claude=yes --openai=yes --gemini=yes --copilot=yes`
3. Confirm the config maps the orchestrator/worker/helper roles to the expected models and categories.
4. Authenticate OpenCode:
   - `opencode auth login`
   - `opencode auth list` should show at least one provider.
5. Verify read-only health:
   - `python scripts/omo_doctor.py`
   - `bunx oh-my-openagent doctor`
   - `opencode agents`
6. Optional smoke test:
   - `opencode run "@sisyphus <task> with @oracle review"`
7. If the Oh My Hermes workflow layer is in scope, confirm the plugin copy/sync and Hermes restart requirements before claiming completion.

## Verification Checklist

- [ ] `opencode --version` and `bun --version` are present.
- [ ] OMO install completed or was already present.
- [ ] `opencode auth list` shows at least one provider.
- [ ] `scripts/omo_doctor.py` exits 0.
- [ ] `bunx oh-my-openagent doctor` reports System OK.
- [ ] `opencode agents` lists at least one agent.

## Guardrails

- Read-only verification only; never delete auth or downgrade configs.
- Never print API keys or secrets.
- Do not hardcode a paid provider unless the user has already authenticated it.
