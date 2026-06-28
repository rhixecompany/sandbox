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

## When to use

- During discovery and inventory phases
- When reviewing unknown code before making changes
- As a safety gate before write operations

## Verification

- [ ] No files were created, edited, or deleted
- [ ] Only read/search operations performed
- [ ] Report generated without side effects
