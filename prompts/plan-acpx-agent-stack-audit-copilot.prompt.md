---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "acpx-stack-audit-copilot"
title: "ACP Agent Stack Audit — GitHub Copilot"
description: "Copilot agent stack audit: inventory GitHub Copilot custom agents, instructions, and prompt files."
trigger: /acpx-stack-audit-copilot
tags:
  - hermes
  - acp
  - audit
  - agents
  - copilot
---

## Goal
Use when ## Description to accomplish the associated tasks and objectives.
## Description

Copilot executor variant. Run command-first audit and reconciliation for Hermes,
Copilot CLI and ACPX.

## Context

> - Primary executor: Copilot CLI.
> - Shell: PowerShell-first commands, runnable from bash.

> **Full content:** `templates/plan-acpx-agent-stack-audit-copilot/context.md`

## Skills Required

- CLI execution.
- Output triage.
- Routing contradiction analysis.
- Config and docs reconciliation.

## Subagents

- `debugger`.
- `technical-writer`.

## Personas

- Executor operator.
- Compatibility auditor.

## Rules

- Prefer runtime evidence over docs.
- Label each route: `working`, `broken`, `unverified`.
- Fix config before docs.
- Keep secrets redacted.

## Phases

> ### Phase 1: Runtime and Liveness
> Set-Location 'C:/Users/Alexa/Desktop/SandBox'

> **Full content:** `templates/plan-acpx-agent-stack-audit-copilot/phases.md`

## Steps

1. Run liveness commands.
2. Run routing scans.
3. Run repo gates.
4. Publish output contract.

## Tasks

- Task 1.1 — Collect runtime and liveness evidence.
- Task 2.1 — Reconcile routing contradictions.
- Task 3.1 — Run repo validation commands.
- Task 4.1 — Publish final matrix and risks.

## Subtasks

- Subtask 1.1.1 — Capture versions and auth listings.
- Subtask 1.1.2 — Execute Copilot/OpenCode/Qwen liveness calls.
- Subtask 2.1.1 — Scan for provider name drift.
- Subtask 2.1.2 — Decide `opencode-acp` route status for Hermes.
- Subtask 3.1.1 — Run format/typecheck/lint strict.
- Subtask 4.1.1 — Emit contract sections in order.

## Actions Summary

1. `Support Matrix`.
2. `Routing Decisions`.
3. `Changes Made`.
4. `Open Risks`.
5. `Validation Run`.


## Template References

Templates in `templates/plan-acpx-agent-stack-audit-copilot/`:
- `context.md`
- `phases.md`
