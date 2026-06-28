---
license: MIT
author: Hermes Agent
trigger: /sync-hermes-copilot-codex
name: sync-hermes-copilot-codex
title: Sync Hermes Copilot Codex
version: 1.1.0
description: >-
  Sync skills, plugins, and hooks across Hermes, Copilot, and Codex agents;
  create personalities and profiles from instruction/agent definitions.
tags:
  - hermes
  - copilot
  - opencode
  - sync
  - skills
  - plugins
  - hooks
  - personalities
  - profiles
  # Copilot-format deps (Hermes uses skills:)
dependencies:
  - skill:using-superpowers
  - skill:user-communication-preferences
  - skill:plans-and-specs
skills:
  - using-superpowers
  - user-communication-preferences
  - plans-and-specs
metadata:
  hermes:
    related_skills:
      - using-superpowers
      - user-communication-preferences
      - plans-and-specs
---

# Sync Hermes Copilot Codex

> Synchronizes skills, plugins, and hooks across three AI agents (Hermes, Copilot, Codex) and creates corresponding personalities/profiles from their instruction/agent definitions.

## Description

This prompt performs a bidirectional sync of skills, plugins, and hooks across Hermes Agent, GitHub Copilot, and OpenCode Codex. It scans `.github/agents/` and `.github/instructions/` to create corresponding personalities and profiles, identifies all three agent root directories, and synchronizes assets between them. Execution is sequential with "only then" constraints between phases.

**Critical rules:**

- For each instruction file → create a corresponding personality
- For each agent file → create a corresponding profile
- Identify all three AI agent root folders before syncing
- Do not stop until plan and specs are fully completed

## Context

- **Source:** `sync-hermes-copilot-codex.prompt.md` (canonical; legacy `.txt` consolidated)
- **Target scope:** Hermes (`~/AppData/Local/hermes/`), Copilot (`~/.copilot/`), Codex (`~/.codex/`)
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI

## Skills Required

| Skill                            | Purpose                               |
| -------------------------------- | ------------------------------------- |
| `using-superpowers`              | Establishes workflow foundation       |
| `user-communication-preferences` | Loads user prefs for execution style  |
| `plans-and-specs`                | Creates implementation plan from goal |

## Rules

1. **Sequential execution** — Phases must complete in order ("only then" constraint)
2. **Bidirectional sync** — Skills, plugins, and hooks flow in both directions
3. **Completeness** — Do not stop until plan and specs are fully completed

## Phases

> ### Phase 1: Inventory Instructions & Agents
> **Goal:** List and triage all instructions and agents, creating personalities an

> **Full content:** `templates/sync-hermes-copilot-codex/phases.md`

## Actions Summary

1. Inventory instructions and agents; create personalities and profiles
2. Identify Hermes, Copilot, and Codex root folders
3. Sync skills, plugins, and hooks bidirectionally across all three agents
4. Verify plan, implement, verify completion

## Verification Checklist

- [ ] All instructions scanned and personalities created
- [ ] All agents scanned and profiles created
- [ ] Hermes root identified
- [ ] Copilot root identified
- [ ] Codex root identified
- [ ] Skills synced bidirectionally
- [ ] Plugins synced bidirectionally
- [ ] Hooks synced bidirectionally
- [ ] Plan and specs verified complete


## Template References

Detailed templates in `templates/sync-hermes-copilot-codex/`:
- `phases.md`
