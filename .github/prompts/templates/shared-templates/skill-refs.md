---
name: shared-skill-refs
title: Shared Skill References
description: Standard table of Hermes skills referenced across prompts. Copy this table into any prompt that needs to invoke a known skill bundle.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [shared, skills, references, prompts]
---
## Goal

<!-- Shared template — see file body for goal content -->

## Context

<!-- Shared template — see file body for context content -->

## Workflow

<!-- Shared template — see file body for workflow content -->

## Verification

<!-- Shared template — see file body for verification content -->


# Shared Skill References

## When to use

Include this table when your prompt needs to invoke one or more Hermes skills by name. The user can use these names directly in their invocation.

## Tier 1: Always-on (load by default for any task)

| Skill | When to load |
|---|---|
| `using-superpowers` | Foundational workflow — load first, every conversation |
| `user-communication-preferences` | Concise, action-first, DRY responses |
| `hermes-agent` | Configuring, extending, or troubleshooting Hermes itself |

## Tier 2: Domain-specific (load per task type)

| Skill | Task type |
|---|---|
| `code-architect` / `code-architect` profile | Implementation, refactoring, debugging |
| `research-analyst` / `research-analyst` profile | Research, literature review, synthesis |
| `creative-director` / `creative-director` profile | Design, content, brainstorming |
| `exec-assistant` / `exec-assistant` profile | Planning, coordination, admin |
| `patient-tutor` / `patient-tutor` profile | Teaching, explanations |
| `adminbot` / `adminbot` profile | DevOps, infra, system ops |

## Tier 3: Multi-file change protocol (load 14 skills for ≥5 file changes)

| # | Skill | Purpose |
|---|---|---|
| 1 | `using-superpowers` | Workflow foundation |
| 2 | `brainstorming` | Structured ideation |
| 3 | `user-communication-preferences` | Communication style |
| 4 | `mcp-sequential-thinking` | Chain-of-thought |
| 5 | `mcp-filesystem` | MCP fs ops |
| 6 | `mcp-ast-grep` | MCP AST search |
| 7 | `mcp-memory` | MCP knowledge graph |
| 8 | `plan` | Plan mode |
| 9 | `plans-and-specs` | Spec + plan docs |
| 10 | `create-implementation-plan` | Create plans |
| 11 | `implementation-plan` | Modify plans |
| 12 | `executing-plans` | Execute plans |
| 13 | `writing-clearly-and-concisely` | Editing workflow |
| 14 | `subagent-driven-development` | Parallel subagent exec |

## Usage in prompts

Reference like this in the prompt body:

```markdown
Skills loaded: using-superpowers, brainstorming, code-architect
```

Or for the full multi-file protocol:

```markdown
/mcp-filesystem /mcp-ast-grep /mcp-memory /plan /plans-and-specs
/create-implementation-plan /implementation-plan /executing-plans
/writing-clearly-and-concisely /subagent-driven-development
```

## References

- `../_index.md` — templates index
- Hermes docs: https://hermes-agent.nousresearch.com/docs