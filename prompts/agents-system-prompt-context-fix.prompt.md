---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Agents System Prompt Context Fix
name: agents-system-prompt-context-fix
trigger: /agents-system-prompt-context-fix
description: >-
  Create/update agent context files across project and subprojects, then audit
  and enhance VS Code workspace configuration.
tags: []
  - hermes
  - copilot
  - opencode
  - agents
  - context
  - vscode
  - architecture
dependencies:
  - skill:using-superpowers
  - skill:user-communication-preferences
  - skill:plans-and-specs
  - skill:architecture-blueprint-generator
  - skill:folder-structure-blueprint-generator
  - skill:technology-stack-blueprint-generator
  - skill:vscode-workspace-configurator
skills:
  - using-superpowers — Establishes workflow foundation
  - user-communication-preferences — Loads user prefs for execution style
  - plans-and-specs — Creates implementation plan from goal
  - architecture-blueprint-generator — Generates architecture context
  - folder-structure-blueprint-generator — Documents folder structure
  - technology-stack-blueprint-generator — Documents tech stack
  - vscode-workspace-configurator — Audits and enhances VS Code config
---

# Agents System Prompt Context Fix

> Creates and updates agent context files across the project and subprojects, then audits and enhances VS Code workspace configuration.

## Description

This prompt generates comprehensive agent context files (architecture blueprints, folder structures, technology stacks) for the project and all subprojects, then performs a full audit and enhancement of VS Code workspace configuration. It ensures every subproject has proper `AGENTS.md` files and that all VS Code JSON configs are triaged, debugged, and verified.

**Critical rules:**
- Apply to this project AND all subprojects
- Do not stop until plan and specs are fully completed
- All VS Code JSON files must be triaged, audited, debugged, enhanced, and verified

## Context

- **Source reference:** `./agents-system-prompt-context-fix.prompt.txt`
- **Target scope:** Project root `C:\Users\Alexa\Desktop\SandBox` and all subprojects
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI

## Phases

### Phase 1: Generate Agent Context Files

**Goal:** Create/update all agent context files using architecture skills.

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Run `architecture-blueprint-generator` | Architecture context files |
| 1.2 | Run `folder-structure-blueprint-generator` | Folder structure documents |
| 1.3 | Run `technology-stack-blueprint-generator` | Tech stack documents |

### Phase 2: Audit VS Code Configuration

**Goal:** List, triage, audit, debug, enhance, and verify all VS Code JSON files.

| Step | Action | Output |
| --- | --- | --- |
| 2.1 | List all JSON files in `.vscode` and subfolders | File inventory |
| 2.2–2.6 | Triage → Audit → Debug → Enhance → Verify | Verified configs |

### Phase 3: Verify & Implement

**Goal:** Verify the plan and specs, implement, and confirm completion.

| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Verify the plan and specs | Verification report |
| 3.2 | Implement verified plan | Completed implementation |

> **Full phase details:** `templates/agents-system-prompt-context-fix/phases.md`

## Rules

1. **Recursive scope** — Apply to project root and all subprojects containing `.vscode/` or `AGENTS.md`
2. **Sequential execution** — Context files first, then VS Code audit
3. **Completeness** — Do not stop until plan and specs are fully completed

## Actions Summary

1. Generate architecture, folder, and tech stack context files for project and subprojects
2. List, triage, audit, debug, enhance, and verify all VS Code JSON configs
3. Verify plan, implement, verify completion

## Template References

Detailed section content extracted to template files in `templates/agents-system-prompt-context-fix/`:
- `phases.md` — Full Phase breakdown with steps