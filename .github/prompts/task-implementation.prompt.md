---
name: task-implementation
title: Task Implementation
description: Implements plan-driven tasks in order with progressive change logging, continuous execution tracking, explicit divergence and blocker recording, and complete working outcomes.
trigger: /task-implementation
version: 1.0.0
author: Hermes Agent
tags:
- tool
- automation
- planning
- documentation
- workflow
- backend
- devops
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: markdown
license: MIT
---
## Table of Contents

## Goal

## Context

## Phases

# Table of Contents

- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Plan Intake and Context Preparation](#phase-1:-plan-intake-and-context-preparation)
  - [Phase 2: Ordered Task Implementation](#phase-2:-ordered-task-implementation)
- [Steps](#steps)
- [Tasks](#tasks)
- [Subtasks](#subtasks)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Plan Intake and Context Preparation](#phase-1:-plan-intake-and-context-preparation)
- [Phase 2: Ordered Task Implementation](#phase-2:-ordered-task-implementation)
- [Steps](#steps)
- [Tasks](#tasks)
- [Subtasks](#subtasks)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Use when "Comprehensive prompt for implementing tracked task plans with progressive change logging." to accomplish the associated tasks and objectives.

## Description

Implement plan-driven tasks in order, update execution tracking continuously, and produce complete working outcomes with explicit divergence and blocker recording.


Use this prompt for execution workflows based on tracked plan/detail files and paired change logs, especially under .copilot-tracking conventions.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Plan-driven implementation and dependency sequencing
- Change tracking and release-note discipline
- Validation-oriented iterative execution

## Subagents

| Subagent | Role | When to Use || --

- | --- | --- || Plan Interpreter | Parses plan and details requirements before coding | Always || Implementer | Executes tasks in order with working code | Always || Change Recorder | Maintains incremental changes file updates | After each task |

## Personas

- Plan Interpreter: Refuses implementation before full task detail comprehension.
- Implementer: Delivers complete, working outcomes for each task.
- Change Recorder: Maintains release-ready traceability for every change.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Read full plan and corresponding changes file before implementing.
- Execute tasks in order and associate each change with a specific task.
- Read full details section before each task implementation.
- Update plan checklist status and changes file after each completed task.
- Record blockers and divergences explicitly when required.


### Phase 1: Plan Intake and Context Preparation

### Phase 2: Ordered Task Implementation

## Steps

1. Read full plan, details, and changes tracking files.
2. Sequence tasks and verify prerequisites.
3. Implement one task completely at a time.
4. Validate implementation and update tracking artifacts.
5. Continue until all tasks are complete or explicitly blocked.

## Tasks

- Task 1.1 — Load and verify complete plan, details, and changes context.
- Task 1.2 — Implement next unchecked task using full details guidance.
- Task 1.3 — Validate implementation before advancing.
- Task 1.4 — Update plan status and append changes tracking entries.
- Task 1.5 — Complete all phases and finalize release summary.

## Subtasks

- Subtask 1.1.1 — Confirm all referenced files are located and understood.
- Subtask 1.2.1 — Implement with existing workspace conventions and safety checks.
- Subtask 1.3.1 — Resolve discovered defects before marking task complete.
- Subtask 1.4.1 — Record divergence or blockers in required format when needed.
- Subtask 1.5.1 — Populate release summary only after all phases are complete.

## Actions Summary

1. Analyze full plan context first.
2. Implement tasks in strict order.
3. Validate after each task.
4. Maintain accurate progressive change tracking.

## Template References

Templates in `templates/task-implementation/`:- `phases.md`

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
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

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`create-implementation-plan.prompt.md`](create-implementation-plan.prompt.md)
- [`tooling-implementation.prompt.md`](tooling-implementation.prompt.md)
- [`update-implementation-plan.prompt.md`](update-implementation-plan.prompt.md)