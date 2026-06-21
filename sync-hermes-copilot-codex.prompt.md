---
trigger: /sync-hermes-copilot-codex
description: >-
  Sync skills, plugins, and hooks across Hermes, Copilot, and Codex agents;
  create personalities and profiles from instruction/agent definitions.
tags:
  [
    hermes,
    copilot,
    opencode,
    sync,
    skills,
    plugins,
    hooks,
    personalities,
    profiles,
  ]
dependencies:
  - skill:using-superpowers
  - skill:user-communication-preferences
  - skill:plans-and-specs
skills:
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

- **Source reference:** `./sync-hermes-copilot-codex.prompt.txt`
- **Target scope:** Hermes (`~/AppData/Local/hermes/`), Copilot (`.github/`), Codex (`.opencode/` or `~/.codex/`)
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

### Phase 1: Inventory Instructions & Agents

**Goal:** List and triage all instructions and agents, creating personalities and profiles.

**Inputs:** `.github/agents/` and `.github/instructions/` directories

**Outputs:** Personalities and profiles created for each instruction/agent

**Steps:**

| Step | Action                                                   | Output                |
| ---- | -------------------------------------------------------- | --------------------- |
| 1.1  | List all files in `.github/instructions/`                | Instruction inventory |
| 1.2  | For each instruction, create a corresponding personality | Personalities created |
| 1.3  | List all files in `.github/agents/`                      | Agent inventory       |
| 1.4  | For each agent, create a corresponding profile           | Profiles created      |

**Tasks:**

- **Task 1.1–1.2 — Instructions → Personalities:** Scan instructions, create matching personalities
- **Task 1.3–1.4 → Agents → Profiles:** Scan agents, create matching profiles

---

### Phase 2: Identify Root Folders

**Goal:** Locate all three AI agent root directories.

**Inputs:** Filesystem scan

**Outputs:** Identified root paths for Hermes, Copilot, and Codex

**Steps:**

| Step | Action                                                        | Output       |
| ---- | ------------------------------------------------------------- | ------------ |
| 2.1  | Identify Hermes root folder (`~/AppData/Local/hermes/`)       | Hermes path  |
| 2.2  | Identify Copilot root folder (`.github/` or VS Code settings) | Copilot path |
| 2.3  | Identify Codex root folder (`~/.codex/` or `.opencode/`)      | Codex path   |

---

### Phase 3: Sync Assets

**Goal:** Synchronize skills, plugins, and hooks across all three agents.

**Inputs:** Identified root paths from Phase 2

**Outputs:** Synced skills, plugins, and hooks

**Steps:**

| Step | Action                               | Output         |
| ---- | ------------------------------------ | -------------- |
| 3.1  | Sync skills across all three agents  | Skills synced  |
| 3.2  | Sync plugins across all three agents | Plugins synced |
| 3.3  | Sync hooks across all three agents   | Hooks synced   |

**Tasks:**

- **Task 3.1 — Skills Sync:** Bidirectional sync of skill directories
- **Task 3.2 — Plugins Sync:** Bidirectional sync of plugin directories
- **Task 3.3 — Hooks Sync:** Bidirectional sync of hook directories

---

### Phase 4: Verify & Implement

**Goal:** Verify the plan and specs, implement, and confirm completion.

**Inputs:** All previous phase outputs

**Outputs:** Verified and complete plan

**Steps:**

| Step | Action                              | Output                  |
| ---- | ----------------------------------- | ----------------------- |
| 4.1  | Verify the plan and specs           | Verification report     |
| 4.2  | Implement the plan and specs        | Implementation complete |
| 4.3  | Verify plan and specs are completed | Completion confirmation |

## Actions Summary

1. Inventory instructions and agents; create personalities and profiles
2. Identify Hermes, Copilot, and Codex root folders
3. Sync skills, plugins, and hooks bidirectionally across all three agents
4. Verify plan, implement, verify completion
