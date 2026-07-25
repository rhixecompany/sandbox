---
name: introspection-only-general
description: "Constraint flag: restrict agent to introspection-only mode. Read and search files but never create, edit, or delete any files or configuration. Use as a safety constraint during discovery phases."
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - constraint
  - safety
  - introspection
  - read-only
title: Introspection Only General
---

# Introspection Only — General

**Constraint flag**: restrict agent to introspection-only mode.

When this skill is active, the agent may:
- Read and search files
- List directories and inspect structure
- Analyze and report findings

The agent may NOT:
- Create, edit, or delete any files
- Run destructive commands
- Modify configuration
- Execute network operations

## When to Use

- During discovery and inventory phases
- When reviewing unknown code before making changes
- As a safety gate before write operations
- When you must guarantee no side effects

## When NOT to Use

- When you need to create, edit, or delete files
- When configuration changes are required
- When network operations are needed

## Workflow

### Phase 1: Activate

Load this skill at the start of any read-only discovery phase.

### Phase 2: Execute

Perform read/search operations only. No write operations allowed.

### Phase 3: Report

Generate findings report without side effects.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Foundational skill workflow |
| `validate-memories` | Memory validation (read-only) |

## Verification

- [ ] No files were created, edited, or deleted
- [ ] Only read/search operations performed
- [ ] Report generated without side effects

## Pitfalls

- Intent is advisory — the LLM can still attempt writes; rely on tool-level restrictions for enforcement
- Some tools implicitly create state (e.g., `hermes tools list` modifies lock files) — flag these in reports
- Use in conjunction with `no-net-fetch` for fully offline read-only mode
- Not a security boundary — it's a behavioral constraint on the agent

## Verification Checklist

- [ ] All tasks completed
- [ ] Output verified
- [ ] Edge cases handled
- [ ] No writes or modifications occurred
