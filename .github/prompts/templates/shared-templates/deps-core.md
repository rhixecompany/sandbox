---
name: shared-deps-core
title: Shared Template — Dependencies Core
description: Standard core dependencies table for prompt files
version: 1.0.0
tags: [template, shared, dependencies]
---
## Goal

<!-- Shared template — see file body for goal content -->

## Context

<!-- Shared template — see file body for context content -->

## Workflow

<!-- Shared template — see file body for workflow content -->

## Verification

<!-- Shared template — see file body for verification content -->


# Core Dependencies (Shared Across Fix Prompts)

These dependencies appear in most fix/sync prompts. Each prompt adds
domain-specific deps.

## Dependency Block (YAML frontmatter)

```yaml
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
    - tool:terminal
    - tool:search_files
```

## Constraint Flags (skills: field in frontmatter)

```yaml
skills:
    - introspection-only-general
    - no-git-delete
    - no-net-fetch
    - skills-tools-preflight-check
```

## Per-Field Notes

| Dep prefix | Type | Purpose |
|| -------- | ------ | --------- ||
| `prompt:` | Other prompt | Reference another prompt file for context |
| `skill:` | Hermes skill | Load a reusable skill module |
| `tool:` | MCP tool | Declare a required MCP tool |