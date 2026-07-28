---
name: tasksync
title: Task Sync
description: 'Comprehensive prompt for synchronizing tasks, implementations, and updates across projects.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: None
tags:
  - frontend
  - prompts
  - workflow
trigger: /tasksync
dependencies: []
metadata:
  hermes: {}
---
## GoalUse when "Comprehensive TaskSync workflow prompt for persistent task-cycle execution and terminal-based intake." to accomplish the associated tasks and objectives.

## DescriptionExecute tasks continuously without auto-termination, follow TaskSync state rules, and request new tasks after completion using terminal-first intake behavior.

## ContextUse this prompt for sessions requiring ongoing task execution, strict continuation behavior, urgent override handling, and explicit manual termination semantics.

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)- Deterministic task-state management- Terminal-first interaction and fallback handling- Interrupt handling for urgent override and explicit termination

## Subagents| Subagent | Role | When to Use || --- | --- | --- || State Manager | Tracks active/completed/waiting/terminated states | Always || Task Executor | Performs current task with strict focus | Active execution || Intake Handler | Requests and processes next task input | On completion or idle |

## Personas- State Manager: Enforces continuity and prevents unintended session closure.- Task Executor: Completes current task before accepting non-urgent work.- Intake Handler: Uses approved terminal command flow and fallback behavior.

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Never terminate session unless explicit termination command is received.- Do not request new tasks while an active task is incomplete.- Use urgent override only for stop current task, correction, or fix directives.- After task completion, announce approved completion phrase and request next task.- Retry terminal intake failures up to allowed count before chat fallback.

## Phases>

### Phase 1: Initialization and Intake>>

### Phase 2: Focused Task Execution> **Full content:** `templates/tasksync/phases.md`

## Steps1. Activate TaskSync initialization behavior.2. Request and parse task input via terminal-first path.3. Execute active task to completion with concise updates.4. Trigger completion announcement and request next task.5. Continue loop until explicit stop/end/terminate/quit command.

## Tasks- Task 1.1 — Initialize task-state system and execute intake command.- Task 1.2 — Execute active task without accepting non-urgent work.- Task 1.3 — Handle urgent override and termination parity rules.- Task 1.4 — Announce completion and request next task input.- Task 1.5 — Maintain continuous loop and fallback rules.

## Subtasks- Subtask 1.1.1 — Set task counter and active session state.- Subtask 1.2.1 — Provide concise progress while preserving focus on active task.- Subtask 1.3.1 — Apply immediate switch only for authorized override phrases.- Subtask 1.4.1 — Use approved completion phrase exactly.- Subtask 1.5.1 — Retry terminal intake and enter waiting-input if required.

## Actions Summary1. Initialize TaskSync state.2. Execute current task fully.3. Request next task on completion.4. Continue until explicit user termination.

## Template ReferencesTemplates in `templates/tasksync/`:- `phases.md`

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

Comprehensive prompt for synchronizing tasks, implementations, and updates across projects.


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


