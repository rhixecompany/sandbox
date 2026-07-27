---
name: agents-fix
title: Agents Sync and Deduplication
description: Sync and deduplicate agent definitions across Hermes, and Copilot with dependency
  mapping and schema validation.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
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
formatter: default
plan: ''
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
  - skill:introspection-only-general
  - skill:no-git-delete
  - skill:no-net-fetch
  - skill:skills-tools-preflight-check
tags:
  - agents
  - ai-assistant
  - configuration
  - fix
  - ml
  - prompts
  - typescript
  - workflow
trigger: /agents-fix
---

## GoalSync agent definitions across Hermes and Copilot without losing schema fidelity or registration details.## ContextUse this prompt when agent definitions, agent-style prompts, or platformregistrations drift across the three ecosystems. The workflow is discoveryfirst, then mapping, then sync, then verification.## Inputs- The agent files and registrations in each platform- Workspace context and platform configuration- Optional user constraints, platform targets, or migration rules## Outputs- A cross-reference table for equivalent agents- A sync plan with deduplication notes- Updated files or config entries- A verification report showing what changed## Rules> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)> Domain-specific additions below.1. Detect the file format before modifying anything.2. Preserve registrations unless the user explicitly requests a rename or   removal.## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)## Phases### Phase 1: DiscoveryDiscover agent files across Hermes, and Copilot. Record names,triggers, descriptions, and registration state.### Phase 2: Cross-reference mappingBuild a mapping table that links equivalent agents across platforms andhighlights gaps.### Phase 3: Sync and deduplicateApply the minimal set of changes needed to align the agent definitions.### Phase 4: VerificationVerify that each platform still matches its expected schema and that no agentswere lost.## Steps1. Load the planning and debugging skills.2. Discover agents on Hermes, and Copilot.3. Build a three-way cross-reference table.4. Identify gaps, inconsistencies, and duplicates.5. Apply sync corrections platform by platform.6. Run platform-specific validation after each change.7. Produce a consolidated registry with platform mappings.## Tasks- [ ] Discover all agents in Hermes, and Copilot scopes- [ ] Build a three-way agent cross-reference table- [ ] Flag agents present on one platform but missing on another- [ ] Flag agents with different names that serve the same purpose- [ ] Sync missing agents to each platform- [ ] Deduplicate redundant agent entries- [ ] Validate all modified files- [ ] Generate a consolidated agent registry## Actions- `search_files(pattern="*.md", target="files")` — Locate agent definition files- `read_file(path)` — Read agent definitions for comparison- `patch(path, old_string, new_string)` — Apply targeted fixes- `write_file(path, content)` — Create new agent files where needed- `delegate_task(goal, toolsets)` — Parallel discovery across platforms- `skill_view(name="acpx-executor")` — Dispatch tasks to ACPX providers