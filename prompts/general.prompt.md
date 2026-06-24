---
license: MIT
author: Hermes Agent
version: 1.0.0
name: general
title: General Development Workflow
trigger: /general
description:
    General development workflow for analysis, planning, implementation, and
    verification with context mapping and AI-assisted execution.
tags: []
  - hermes
  - copilot
  - opencode
  - development
  - automation
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

---

> General development workflow with planning, automation, and verification.

## Goal

Handle multi-step development work with a predictable loop: map context, plan,
implement, and verify.

## Context

Use this prompt when a task spans more than one step or needs explicit file
impact analysis before coding. It combines file mapping, planning, direct CLI
execution, and validation.

## Inputs

- Task description
- Optional target area, files, or bug report
- Workspace context and relevant documentation
- Optional constraints, performance targets, or output format requirements

## Outputs

- A dependency-aware context map
- A short execution plan
- Implemented changes or commands
- Verification notes and follow-up actions

## Rules

1. Run `context-map` before implementation.
2. Use Context7 or equivalent docs before changing code.
3. Plan before coding when the scope is multi-step.
4. Keep changes small and verifiable.
5. Use direct CLI execution for implementation and verification.
6. Prefer git rollback over backup files.
7. Keep the workflow deterministic and easy to resume.

## Skills Required

| Skill                         | Purpose                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------- |
| `context-map` (prompt)        | Map impacted files and dependencies before changes (loaded via prompt dependency) |
| `brainstorming`               | Explore approaches before implementation                                          |
| `plans-and-specs`             | Create structured plans and specs                                                 |
| `dispatching-parallel-agents` | Run parallel automation tasks                                                     |
| `subagent-driven-development` | Delegate independent subtasks                                                     |
| `systematic-debugging`        | Isolate and fix issues methodically                                               |
| `simplify`                    | Remove unnecessary complexity                                                     |
| `context7`                    | Query codebase-aware documentation and examples                                   |
| `plan`                        | Write or update a plan before coding                                              |
| `writing-skills`              | Improve prompts and instructions                                                  |
| `acpx-executor`               | Dispatch tasks to ACPX providers                                                  |

## Phases

### Phase 1: Analyze

Map the impacted files, read the relevant docs, and confirm the current state
before changing anything.

### Phase 2: Plan

Use brainstorming and plans-and-specs to define the smallest safe execution
path. Split the work into parallel streams only when the dependencies are clear.

### Phase 3: Execute

Run commands, write code, and manage files directly from the AI client. Use
dispatching-parallel-agents for concurrent work when it reduces risk or
turnaround time.

### Phase 4: Verify

Test changes, validate outputs, and confirm the task is complete.

## Steps

1. Load `context-map` prompt (`.github/prompts/context-map.prompt.md`) and inspect the affected files.
2. Use Context7 docs or equivalent references for the relevant APIs or patterns.
3. Create a compact plan with clear checkpoints.
4. Implement the change with direct CLI/file operations.
5. Verify the result with tests, diffs, or other evidence.
6. Update tickets or docs if required.

## Tasks

- [ ] Map impacted files and dependencies before any code work
- [ ] Apply structured problem-solving to complex issues
- [ ] Create a compact plan before coding
- [ ] Use parallel agents only when the scope is independent
- [ ] Run commands and scripts directly from the terminal
- [ ] Manage files and configuration via CLI
- [ ] Verify all changes pass the required checks

## Actions

1. Map the scope and identify dependencies.
2. Plan the work and split parallel tasks when safe.
3. Execute the change with direct tooling.
4. Verify the result against the original goal.
5. Return the final outcome with the evidence needed to trust it.
