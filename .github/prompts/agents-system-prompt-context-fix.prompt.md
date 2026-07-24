---
name: agents-system-prompt-context-fix
title: "Agents System Prompt Context Fix"
description: 'Fix and verify Hermes/Copilot/Codex agent system prompt context by '
  'generating project context artifacts, auditing VS Code configs, and verifying completion.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
- agents
- system-prompt
- context
- verification
- vscode
trigger: /agents-system-prompt-context-fix
formatter: default
dependencies:
- skill:using-superpowers
- skill:user-communication-preferences
- skill:verification-before-completion
metadata:
  hermes:
    related_skills:
    - using-superpowers
    - user-communication-preferences
    - verification-before-completion
toolsets:
- file
- terminal
scripts: []
skills: []
plan: ''
---

# Agents System Prompt Context Fix

## Context

- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Rules

1. Execute phases in order.
2. Each phase must pass its gate before advancing.
3. If a referenced path is missing, pause and report the exact missing path instead of fabricating work.

## Phases

Full phase instructions live in `templates/agents-system-prompt-context-fix/phases.md`.

| Order | Phase | Gate |
| --- | --- | --- |
| 1 | Generate Agent Context Files | context docs generated for root and each subproject |
| 2 | Audit VS Code Configuration | all VS Code JSON configs triaged and verified |
| 3 | Verify & Implement | verification report written and issues closed |

## Verification Checklist

- [ ] Phase 1 completed and verified
- [ ] Phase 2 completed and verified
- [ ] Phase 3 completed and verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`
