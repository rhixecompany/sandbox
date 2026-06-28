---
author: Hermes Agent
description: Use when creating, viewing, transitioning, or managing Jira tickets,
  sprints, and epics via CLI or MCP with complex workflows.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: jira
tags: null
title: Jira
version: 1.0.0

---
# Jira

Use this skill when working with Jira tickets, sprints, epics, or project workflows via CLI or MCP.

## Overview

This skill provides guidance for creating, viewing, transitioning, and managing Jira objects. It focuses on CLI-driven workflows, linking issues and epics, and updating project status safely.

## When to Use

- Creating or updating Jira tickets, sprints, or epics
- Transitioning issues through workflow states
- Managing Jira labels, components, or priorities
- Linking issues to epics or related work
- Generating reports or extracting ticket data

## When NOT to Use

- Non-Jira issue tracker operations
- Real-time collaborative ticket triage that requires discussion before updates
- External project management tools that are not Jira

## Skills Required

| Skill | Purpose |
|-------|---------|
| work-on-ticket | Ticket-level work tracking and updates |
| task-management | Task planning and follow-up discipline |

## Workflow

### Phase 1: Identify the Ticket

1. Confirm the project key and issue type.
2. Identify whether the work is new, linked, or blocked.
3. Confirm the target transition and acceptance information.

### Phase 2: Manage the Ticket

1. Update fields with available ticket data.
2. Add concise comments describing changes.
3. Attach evidence or context when relevant.
4. Maintain metadata, labels, and priority settings.

### Phase 3: Transition State

1. Locate the current workflow status.
2. Select the correct transition action.
3. Update status only after required fields are set.
4. Confirm the resulting workflow state before proceeding.

### Phase 4: Track and Report

1. Verify ticket progress against completion criteria.
2. Record triage findings and next actions.
3. Prepare analytical data or metrics if requested.
4. Preserve ticket context for review.

## Verification Checklist

- [ ] Ticket fields complete and validated
- [ ] Comments and links added where needed
- [ ] Status transition completed successfully
- [ ] Project key and issue type confirmed
- [ ] No conflicting ticket updates retired

## Pitfalls

- Update only confirmed and inspected ticket metadata.
- Avoid moving tickets to closed states without review.
- Confirm assignees or watchers when ownership changes.
