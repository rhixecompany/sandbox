---
name: shared-skills-table-core
title: Shared Template — Skills Table (Core)
description: Per-domain skills reference table used by prompt files for discovery, sync, and repair workflows
version: 1.0.0
tags: [template, shared, skills, table, prompts]
---

# Skills Table (Core)

Per-domain skills referenced by prompt workflows. Prompts link here via
[`templates/_shared/skills-table-core.md#<prompt-name>`](skills-table-core.md#<prompt-name>).

## prompts-fix

| Skill | Purpose |
| ----- | ------- |
| `subagent-driven-development` | Implement → spec-review → quality-review pipeline (serial within task) |
| `dispatching-parallel-agents` | Parallel fan-out of independent discovery/sync work |
| `systematic-debugging` | Four-phase root cause debugging when sync diverges |
| `simplify` | Collapse duplicate prompt/skill definitions after dedup |
| `acpx-executor` | Dispatch tasks to ACPX providers for cross-platform execution |
| `hermes-agent` | Configure, extend, or contribute to Hermes Agent itself |
| `copilot-cli-quickstart` | Onboard GitHub Copilot CLI for Copilot-side sync |
| `brainstorming` | Divergent ideation before a sync plan is settled |
| `plans-and-specs` | Author the implementation plan and spec for the sync |

## prompts-strict-template

| Skill | Purpose |
| ----- | ------- |
| `enhance-markdown` | Audit, normalize, and enhance markdown formatting |
| `skill-judge` | Score structure/compliance of generated prompt files |
| `writing-skills` | Author clear, compliant prompt prose |
| `using-superpowers` | Establishes the skill workflow and tool precedence |
| `hermes-skills` | Discover, install, and manage prompt/skill definitions |
