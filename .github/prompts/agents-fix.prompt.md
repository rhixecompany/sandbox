---
name: agents-fix
title: Agents Sync and Deduplication
description: 'Sync and deduplicate agent definitions across Hermes, and Copilot with dependency mapping and schema validation.'
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
plan: None
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
metadata:
  hermes: {}
---
## GoalSync agent definitions across Hermes and Copilot without losing schema fidelity or registration details.

## ContextUse this prompt when agent definitions, agent-style prompts, or platformregistrations drift across the three ecosystems. The workflow is discoveryfirst, then mapping, then sync, then verification.

## Inputs- The agent files and registrations in each platform- Workspace context and platform configuration- Optional user constraints, platform targets, or migration rules

## Outputs- A cross-reference table for equivalent agents- A sync plan with deduplication notes- Updated files or config entries- A verification report showing what changed

## Rules> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)> Domain-specific additions below.1. Detect the file format before modifying anything.2. Preserve registrations unless the user explicitly requests a rename or   removal.

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

## Phases

### Phase 1: DiscoveryDiscover agent files across Hermes, and Copilot. Record names,triggers, descriptions, and registration state.

### Phase 2: Cross-reference mappingBuild a mapping table that links equivalent agents across platforms andhighlights gaps.

### Phase 3: Sync and deduplicateApply the minimal set of changes needed to align the agent definitions.

### Phase 4: VerificationVerify that each platform still matches its expected schema and that no agentswere lost.

## Steps1. Load the planning and debugging skills.2. Discover agents on Hermes, and Copilot.3. Build a three-way cross-reference table.4. Identify gaps, inconsistencies, and duplicates.5. Apply sync corrections platform by platform.6. Run platform-specific validation after each change.7. Produce a consolidated registry with platform mappings.

## Tasks- [ ] Discover all agents in Hermes, and Copilot scopes- [ ] Build a three-way agent cross-reference table- [ ] Flag agents present on one platform but missing on another- [ ] Flag agents with different names that serve the same purpose- [ ] Sync missing agents to each platform- [ ] Deduplicate redundant agent entries- [ ] Validate all modified files- [ ] Generate a consolidated agent registry

## Actions- `search_files(pattern="*.md", target="files")` — Locate agent definition files- `read_file(path)` — Read agent definitions for comparison- `patch(path, old_string, new_string)` — Apply targeted fixes- `write_file(path, content)` — Create new agent files where needed- `delegate_task(goal, toolsets)` — Parallel discovery across platforms- `skill_view(name="acpx-executor")` — Dispatch tasks to ACPX providers

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |


## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes


## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.


## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.


## Phases

### Phase 1: Intake
- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute
- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify
- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off
- Return final artifact or findings clearly.
- Stop once the requested result is delivered.


## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.


## Verification Checklist

| # | Gate | Criterion |
|---|------|-----------|
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |


## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

Sync and deduplicate agent definitions across Hermes, and Copilot with dependency mapping and schema validation.


## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |


## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |



## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions


