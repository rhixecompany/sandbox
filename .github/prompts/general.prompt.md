---
name: general
title: General Development Workflow
description: 'General development workflow for analysis, planning, implementation, and verification with context mapping and AI-assisted execution.'
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
  - context-map
  - brainstorming
  - plans-and-specs
  - dispatching-parallel-agents
  - subagent-driven-development
  - systematic-debugging
  - simplify
  - context7
  - plan
  - writing-skills
  - acpx-executor
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
  - skill:context7
  - skill:plan
  - skill:writing-skills
  - skill:acpx-executor
  - tool:terminal
  - tool:search_files
  - tool:web_search
  - tool:delegate_task
  - skill:introspection-only-general
  - skill:no-git-delete
  - skill:no-net-fetch
  - skill:skills-tools-preflight-check
  - skill:context-map
tags:
  - documentation
  - planning
  - prompts
  - typescript
  - workflow
trigger: /general
metadata:
  hermes: {}
---
## Goal

General development workflow for analysis, planning, implementation, and verification with context mapping and AI-assisted execution.

> General development workflow with planning, automation, and verification.

## GoalHandle multi-step development work with a predictable loop: map context, plan,implement, and verify.

## ContextUse this prompt when a task spans more than one step or needs explicit fileimpact analysis before coding. It combines file mapping, planning, direct CLIexecution, and validation.

## Inputs- Task description- Optional target area, files, or bug report- Workspace context and relevant documentation- Optional constraints, performance targets, or output format requirements

## Outputs- A dependency-aware context map- A short execution plan- Implemented changes or commands- Verification notes and follow-up actions

## Rules> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)> Domain-specific additions below.1. Use Context7 or equivalent docs before changing code.2. Plan before coding when the scope is multi-step.3. Keep changes small and verifiable.4. Use direct CLI execution for implementation and verification.5. Keep the workflow deterministic and easy to resume.

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

## Phases

### Phase 1: AnalyzeMap the impacted files, read the relevant docs, and confirm the current statebefore changing anything.

### Phase 2: PlanUse brainstorming and plans-and-specs to define the smallest safe executionpath. Split the work into parallel streams only when the dependencies are clear.

### Phase 3: ExecuteRun commands, write code, and manage files directly from the AI client. Usedispatching-parallel-agents for concurrent work when it reduces risk orturnaround time.

### Phase 4: VerifyTest changes, validate outputs, and confirm the task is complete.

## Steps1. Load `context-map` prompt (`prompts/context-map.prompt.md`) and inspect the affected files.2. Use Context7 docs or equivalent references for the relevant APIs or patterns.3. Create a compact plan with clear checkpoints.4. Implement the change with direct CLI/file operations.5. Verify the result with tests, diffs, or other evidence.6. Update tickets or docs if required.

## Tasks- [ ] Map impacted files and dependencies before any code work- [ ] Apply structured problem-solving to complex issues- [ ] Create a compact plan before coding- [ ] Use parallel agents only when the scope is independent- [ ] Run commands and scripts directly from the terminal- [ ] Manage files and configuration via CLI- [ ] Verify all changes pass the required checks

## Actions1. Map the scope and identify dependencies.2. Plan the work and split parallel tasks when safe.3. Execute the change with direct tooling.4. Verify the result against the original goal.5. Return the final outcome with the evidence needed to trust it.

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


