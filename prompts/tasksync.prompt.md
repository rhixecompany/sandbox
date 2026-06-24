---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "tasksync"
title: "Task Sync"
description: "Comprehensive prompt for synchronizing tasks, implementations, and updates across projects."
trigger: /tasksync
tags: []
  - hermes
  - tasks
  - sync
  - project-management
---

## Goal
Use when "Comprehensive TaskSync workflow prompt for persistent task-cycle execution and terminal-based intake." to accomplish the associated tasks and objectives.


## Description

Execute tasks continuously without auto-termination, follow TaskSync state rules, and request new tasks after completion using terminal-first intake behavior.

## Context

Use this prompt for sessions requiring ongoing task execution, strict continuation behavior, urgent override handling, and explicit manual termination semantics.

## Skills Required

- Deterministic task-state management
- Terminal-first interaction and fallback handling
- Interrupt handling for urgent override and explicit termination

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| State Manager | Tracks active/completed/waiting/terminated states | Always |
| Task Executor | Performs current task with strict focus | Active execution |
| Intake Handler | Requests and processes next task input | On completion or idle |

## Personas

- State Manager: Enforces continuity and prevents unintended session closure.
- Task Executor: Completes current task before accepting non-urgent work.
- Intake Handler: Uses approved terminal command flow and fallback behavior.

## Rules

- Never terminate session unless explicit termination command is received.
- Do not request new tasks while an active task is incomplete.
- Use urgent override only for stop current task, correction, or fix directives.
- After task completion, announce approved completion phrase and request next task.
- Retry terminal intake failures up to allowed count before chat fallback.

## Phases

> ### Phase 1: Initialization and Intake
> ### Phase 2: Focused Task Execution

> **Full content:** `templates/tasksync/phases.md`

## Steps

1. Activate TaskSync initialization behavior.
2. Request and parse task input via terminal-first path.
3. Execute active task to completion with concise updates.
4. Trigger completion announcement and request next task.
5. Continue loop until explicit stop/end/terminate/quit command.

## Tasks

- Task 1.1 — Initialize task-state system and execute intake command.
- Task 1.2 — Execute active task without accepting non-urgent work.
- Task 1.3 — Handle urgent override and termination parity rules.
- Task 1.4 — Announce completion and request next task input.
- Task 1.5 — Maintain continuous loop and fallback rules.

## Subtasks

- Subtask 1.1.1 — Set task counter and active session state.
- Subtask 1.2.1 — Provide concise progress while preserving focus on active task.
- Subtask 1.3.1 — Apply immediate switch only for authorized override phrases.
- Subtask 1.4.1 — Use approved completion phrase exactly.
- Subtask 1.5.1 — Retry terminal intake and enter waiting-input if required.

## Actions Summary

1. Initialize TaskSync state.
2. Execute current task fully.
3. Request next task on completion.
4. Continue until explicit user termination.


## Template References

Templates in `templates/tasksync/`:
- `phases.md`
