---
name: sync-hermes-copilot-codex
title: "Sync Hermes Copilot Codex"
description: "Bidirectional sync of skills, plugins, hooks, prompts, and instructions across Hermes, GitHub Copilot, and OpenAI Codex environments with verification."
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
  - ai-assistant
  - data
  - prompts
  - skills
  - typescript
  - workflow
trigger: /sync-hermes-copilot-codex
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
scripts: []
skills: []
plan: ''
---

# Sync Hermes Copilot Codex

## Context

- **Hermes root:** `C:\Users\Alexa\AppData\Local\hermes`
- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Rules

1. Execute phases in order; do not reorder.
2. Each phase must pass its gate before advancing.
3. Conflicts should be resolved or documented, not silently dropped.

## Phases

Full phase instructions live in `templates/sync-hermes-copilot-codex/phases.md`.

| Order | Phase | Gate |
| --- | --- | --- |
| 1 | Inventory Instructions & Agents | inventories complete; personality/profile mappings created |
| 2 | Identify Agent Roots | all 3 roots confirmed; paths documented |
| 3 | Bidirectional Sync | sync report written; conflicts resolved or documented |
| 4 | Verify Completion | verification report written; all critical assets in sync |

## Verification Checklist

- [ ] Phase 1 completed and verified
- [ ] Phase 2 completed and verified
- [ ] Phase 3 completed and verified
- [ ] Phase 4 completed and verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`
