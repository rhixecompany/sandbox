---
name: prompts-fix
...
title: prompts Sync and Deduplication
...
description: Sync and deduplicate prompt files across Hermes and Copilot with dependency mapping
  and platform-specific validation.
...
version: 1.0.0
...
license: MIT
...
author: Hermes Agent
...
toolsets: - file
- terminal
scripts: []
skills: - subagent-driven-development
- brainstorming
- plans-and-specs
- dispatching-parallel-agents
- systematic-debugging
- simplify
- acpx-executor
- hermes-agent
- copilot-cli-quickstart
formatter: default
...
plan: ''
dependencies: - prompt:context-map.prompt.md
- prompt:update-implementation-plan.prompt.md
- prompt:skills-fix.prompt.md
- skill:brainstorming
- skill:plans-and-specs
- skill:dispatching-parallel-agents
- skill:subagent-driven-development
- skill:systematic-debugging
- skill:simplify
- skill:acpx-executor
- skill:hermes-agent
- skill:copilot-cli-quickstart
tags: - ai-assistant
- fix
- ml
- prompts
- specification
- typescript
- workflow
trigger: /prompts-fix
...
---

## Goal

Sync prompt files across Hermes and Copilot without losing trigger names or platform-specific behavior.

## Context

Use this prompt when prompt definitions, prompt-style prompts, or platform registrations drift across the three ecosystems. The workflow is discovery first, then mapping, then sync, then verification.

## Inputs

- The prompt files and prompt definitions in each platform
- Workspace context and platform registration files
- Optional user constraints, platform targets, or migration rules

## Outputs

- A cross-reference table for equivalent prompts
- A sync plan with deduplication notes
- Updated prompt files or config files
- A verification report showing what changed
- A consolidated prompt registry at `docs/prompt-registry.md`

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)
> Domain-specific additions below.

1. Detect the file format before modifying anything.
2. Preserve trigger names unless the user explicitly requests a rename.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

## Phases

### Phase 1: Discovery

Discover prompt files across Hermes, and Copilot. Record trigger, description, and registration state.

### Phase 2: Cross-reference mapping

Build a mapping table that links equivalent prompts across platforms and highlights gaps.

### Phase 3: Sync and deduplicate

Apply the minimal set of changes needed to align the prompt definitions.
Write the consolidated platform mapping to `docs/prompt-registry.md` (relative to the
workspace) so execution produces a real, inspectable artifact rather than an in-memory result.

### Phase 4: Verification

Verify that each platform still matches its expected schema and that no prompts were lost.

## Steps

1. Load the planning and debugging skills.
2. Discover prompts on Hermes, and Copilot.
3. Build a three-way cross-reference table.
4. Identify gaps, inconsistencies, and duplicates.
5. Apply sync corrections platform by platform.
6. Run platform-specific validation after each change.
7. Produce a consolidated registry with platform mappings.

## Tasks

- [ ] Discover all prompts in Hermes, and Copilot scopes
- [ ] Build a three-way prompt cross-reference table
- [ ] Flag prompts present on one platform but missing on another
- [ ] Flag prompts with different names that serve the same purpose
- [ ] Sync missing prompts to each platform
- [ ] Deduplicate redundant prompt entries
- [ ] Validate all modified prompt files
- [ ] Generate a consolidated prompt registry

## Actions

- `search_files(pattern="*.prompt.md", target="files")` — Locate prompt and prompt files
- `read_file(path)` — Read prompt definitions for comparison
- `patch(path, old_string, new_string)` — Apply targeted fixes
- `write_file(path, content)` — Create new prompt files where needed
- `delegate_task(goal, toolsets)` — Parallel discovery across platforms
- `skill_view(name="acpx-executor")` — Dispatch tasks to ACPX providers
- `delegate_task(goal="Discover and map all *.prompt.md across Hermes and Copilot scopes", toolsets=["file","terminal"])` — Dispatch parallel sub-agents for Phase 1/2 discovery; consult the `dispatching-parallel-agents` skill for fan-out patterns.
