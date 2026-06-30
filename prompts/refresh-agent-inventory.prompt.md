---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "refresh-agent-inventory"
title: "Refresh Agent Inventory"
description: >
  Refresh workspace customization inventory and patch stale AGENTS or copilot
  instruction references.
trigger: refresh-agent-inventory
tags:
  - agents
  - ai-assistant
  - ml
  - prompts
  - skills
  - typescript
  - hermes
  - agents
  - inventory
  - audit
mode: ask
metadata:
  hermes:
    related_skills: []
    tags:
    - refresh-agent-inventory.prompt

---
metadata:
  hermes:
    related_skills: []
    tags:
    - refresh-agent-inventory.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - refresh-agent-inventory.prompt

## Goal
Use when ## Description to accomplish the associated tasks and objectives.


## Description

Refresh the workspace customization inventory by reconciling discovered assets
against the canonical report, then propose precise edits for stale AGENTS and
copilot instruction references.

## Context

- Workspace is monorepo-style with root and subproject overrides.
- Canonical report path:
  - reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
- Primary customization files:
  - AGENTS.md
  - .github/copilot-instructions.md

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#refresh-agent-inventory)

- customization-audit
- context-map

## Subagents

- Explore (optional): read-only discovery of inventory, duplicates, and stale
  references.

## Personas

- Maintainer persona: prioritize deterministic, low-risk edits.
- Auditor persona: prioritize verifiable findings with file evidence.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


- Follow nearest-file precedence for AGENTS and instructions.
- Link to existing documents instead of embedding long copied content.
- Keep edits minimal and scoped to customization files.
- If no changes are needed, output a no-op report with evidence.

## Phases

### Phase 1: Discover and compare

| Field      | Details                                                                    |
| ---------- | -------------------------------------------------------------------------- |
| Goal       | Build a current inventory snapshot and compare it to the canonical report. |
| Inputs     | Workspace files, report file, AGENTS.md, .github/copilot-instructions.md.  |
| Outputs    | Drift list with concrete path-level evidence.                              |
| Validation | Every drift item cites at least one path and one mismatch type.            |

### Phase 2: Propose and apply scoped updates

| Field      | Details                                                                  |
| ---------- | ------------------------------------------------------------------------ |
| Goal       | Produce minimal customization-file updates that remove drift.            |
| Inputs     | Phase 1 drift list and current customization file contents.              |
| Outputs    | Patch-ready update plan and optional applied edits.                      |
| Validation | Updated references are path-valid and do not introduce duplicate assets. |

## Steps

1. Discover AGENTS.md files and customization assets under .github.
2. Read the canonical inventory report and compare counts and references.
3. Identify stale lists, missing paths, and duplicate-purpose customizations.
4. Prepare minimal edits for AGENTS.md and .github/copilot-instructions.md if
   needed.
5. Summarize outcomes as a remediation report.

## Tasks

- Task 1.1 — Discover AGENTS and customization asset files.
- Task 1.2 — Compare discovered inventory with report-backed counts and
  references.
- Task 2.1 — Draft minimal updates for stale customization references.
- Task 2.2 — Validate paths and precedence logic after updates.
- Task 2.3 — Publish remediation summary with risk notes.

## Subtasks

- Subtask 1.1.1 — Enumerate AGENTS files by workspace path.
- Subtask 1.2.1 — Record count deltas for instructions, prompts, and skills.
- Subtask 2.1.1 — Patch stale override lists and refresh commands.
- Subtask 2.2.1 — Verify no broken links or invalid paths in changed files.
- Subtask 2.3.1 — Report fixed items, remaining risks, and next actions.

## Actions Summary

- Discover current customization inventory.
- Compare against canonical report and precedence rules.
- Apply or propose minimal customization-file fixes.
- Deliver a concise remediation report with evidence.


## Template References

Templates in `templates/refresh-agent-inventory/`:
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
