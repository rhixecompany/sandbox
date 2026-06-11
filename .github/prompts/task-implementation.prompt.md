---
name: "task-implementation"
description: "Comprehensive prompt for implementing tracked task plans with progressive change logging."
---## Goal
Use when "Comprehensive prompt for implementing tracked task plans with progressive change logging." to accomplish the associated tasks and objectives.


## Description

Implement plan-driven tasks in order, update execution tracking continuously, and produce complete working outcomes with explicit divergence and blocker recording.

## Context

Use this prompt for execution workflows based on tracked plan/detail files and paired change logs, especially under .copilot-tracking conventions.

## Skills Required

- Plan-driven implementation and dependency sequencing
- Change tracking and release-note discipline
- Validation-oriented iterative execution

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Plan Interpreter | Parses plan and details requirements before coding | Always |
| Implementer | Executes tasks in order with working code | Always |
| Change Recorder | Maintains incremental changes file updates | After each task |

## Personas

- Plan Interpreter: Refuses implementation before full task detail comprehension.
- Implementer: Delivers complete, working outcomes for each task.
- Change Recorder: Maintains release-ready traceability for every change.

## Rules

- Read full plan and corresponding changes file before implementing.
- Execute tasks in order and associate each change with a specific task.
- Read full details section before each task implementation.
- Update plan checklist status and changes file after each completed task.
- Record blockers and divergences explicitly when required.

## Phases

### Phase 1: Plan Intake and Context Preparation

| Field | Details |
| --- | --- |
| Goal | Fully understand plan scope, details, and tracking expectations before edits. |
| Inputs | Plan files, details files, changes files, referenced source files. |
| Outputs | Sequenced execution roadmap and dependency confirmation. |
| Validation | No task starts without verified plan-details context and file references. |

### Phase 2: Ordered Task Implementation

| Field | Details |
| --- | --- |
| Goal | Implement each task fully with working, validated behavior. |
| Inputs | Task-specific details, existing code patterns, dependencies. |
| Outputs | Completed task implementation and updated checklist status. |
| Validation | Task requirements are met and validated before moving forward. |

### Phase 3: Progressive Tracking and Release Readiness

| Field | Details |
| --- | --- |
| Goal | Keep changes file synchronized and release-ready throughout execution. |
| Inputs | Implemented task deltas, divergence/blocker events, validation outcomes. |
| Outputs | Accurate Added/Modified/Removed tracking and final release summary. |
| Validation | Changes log reflects true state and includes required blockers/divergence notes. |

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
