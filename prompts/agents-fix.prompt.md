---
license: MIT
author: Hermes Agent
version: 1.0.0
name: agents-fix
title: Agents Sync and Deduplication
trigger: /agents-fix
description: Sync and deduplicate agent definitions across Hermes, and Copilot
    with dependency mapping and schema validation.
tags:
  - hermes
  - copilot
  - agents
  - sync
dependencies:
    - prompt:context-map.prompt.md
    - prompt:update-implementation-plan.prompt.md
    - skill:brainstorming
    - skill:plans-and-specs
    - skill:dispatching-parallel-agents
    - skill:subagent-driven-development
    - skill:systematic-debugging
    - skill:simplify
    - skill:acpx-executor
    - skill:copilot-cli-quickstart
    - tool:terminal
    - tool:search_files
skills:
    - introspection-only-general
    - no-git-delete
    - no-net-fetch
    - skills-tools-preflight-check
    - brainstorming
    - plans-and-specs
    - dispatching-parallel-agents
    - subagent-driven-development
    - systematic-debugging
    - simplify
    - acpx-executor
    - copilot-cli-quickstart
---

## Goal

Sync agent definitions across Hermes and Copilot without losing schema fidelity or registration details.

## Context

Use this prompt when agent definitions, agent-style prompts, or platform
registrations drift across the three ecosystems. The workflow is discovery
first, then mapping, then sync, then verification.

## Inputs

- The agent files and registrations in each platform
- Workspace context and platform configuration
- Optional user constraints, platform targets, or migration rules

## Outputs

- A cross-reference table for equivalent agents
- A sync plan with deduplication notes
- Updated files or config entries
- A verification report showing what changed

## Rules

> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)
> Domain-specific additions below.

2. Detect the file format before modifying anything.
4. Preserve registrations unless the user explicitly requests a rename or
   removal.

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#agents-fix)

## Phases

### Phase 1: Discovery

Discover agent files across Hermes, and Copilot. Record names,
triggers, descriptions, and registration state.

### Phase 2: Cross-reference mapping

Build a mapping table that links equivalent agents across platforms and
highlights gaps.

### Phase 3: Sync and deduplicate

Apply the minimal set of changes needed to align the agent definitions.

### Phase 4: Verification

Verify that each platform still matches its expected schema and that no agents
were lost.

## Steps

1. Load the planning and debugging skills.
2. Discover agents on Hermes, and Copilot.
3. Build a three-way cross-reference table.
4. Identify gaps, inconsistencies, and duplicates.
5. Apply sync corrections platform by platform.
6. Run platform-specific validation after each change.
7. Produce a consolidated registry with platform mappings.

## Tasks

- [ ] Discover all agents in Hermes, and Copilot scopes
- [ ] Build a three-way agent cross-reference table
- [ ] Flag agents present on one platform but missing on another
- [ ] Flag agents with different names that serve the same purpose
- [ ] Sync missing agents to each platform
- [ ] Deduplicate redundant agent entries
- [ ] Validate all modified files
- [ ] Generate a consolidated agent registry

## Actions

- `search_files(pattern="*.md", target="files")` — Locate agent definition files
- `read_file(path)` — Read agent definitions for comparison
- `patch(path, old_string, new_string)` — Apply targeted fixes
- `write_file(path, content)` — Create new agent files where needed
- `delegate_task(goal, toolsets)` — Parallel discovery across platforms
- `skill_view(name="acpx-executor")` — Dispatch tasks to ACPX providers
