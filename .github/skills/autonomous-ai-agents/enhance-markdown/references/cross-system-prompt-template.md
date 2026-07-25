# Cross-System Prompt Template (Hermes + Copilot + OpenCode)

## When to Use

Use this 11-section template when the output `.md` prompt needs to work across all three AI systems:
- **Hermes** — loads as a skill with triggered commands
- **Copilot** — reads as a structured markdown prompt with clear sections
- **OpenCode** — uses YAML frontmatter as command metadata

Prefer the 9-section template (from `SKILL.md` Phase 3) for simpler prompts that don't need frontmatter or cross-system metadata. Use this 11-section template for prompts that will be invoked as OpenCode commands or shared across multiple agents.

## Template Structure

```markdown
---
trigger: /<command-name>
description: >-
  <one-line description of what this prompt does>
tags:
  [hermes, copilot, opencode, <tag1>, <tag2>, ...]
dependencies:
  - skill:<skill-name>
  - subagent:<subagent-name>
skills:
  - <skill-name> — <why it's needed>
  - <skill-name2> — <why it's needed>
---

# <title>

> <purpose statement — one sentence>

## Description

<What this prompt does, when to use it, and what it delivers. 2-4 paragraphs covering scope and key outcomes.>

**Critical rules (must appear within the first 15% of execution):**
- <rule 1 — most important behavioral constraint>
- <rule 2>
- <rule 3>

## Context

- **Source reference:** `<path to source if applicable>`
- **Target scope:** `<what files/dirs this prompt operates on>`
- **Phase 1 outputs:** `<paths>`
- **Phase 2 outputs:** `<paths>`
- **Execution environment:** `<OS, shell, tools required>`

## Skills Required

| Skill | Purpose |
| --- | --- |
| `<skill-name>` | Brief justification |

## Subagents

| Subagent | Role | Phase |
| --- | --- | --- |
| `<name>` | `<what they do>` | `<which phases>` |

## Personas

### @<persona-name> _(<phases>)_

<Description of this persona's ownership and responsibilities.>

**Constraints:**
- <constraint 1>
- <constraint 2>

## Rules

1. **<Rule name>** — <description>
2. **<Rule name>** — <description>

## Phases

### Phase 1: <Phase Name>

**Goal:** <one-liner>

**Inputs:** <what goes in>

**Outputs:** <what comes out>

**Steps:**

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | <what to do> | <result> |
| 1.2 | <what to do> | <result> |

**Tasks:**

- **Task 1.1 — <name>:** <description>
  - Subtask: <atomic operation>
  - Subtask: <atomic operation>
- **Task 1.2 — <name>:** <description>
  - Subtask: <atomic operation>

---

### Phase 2: <Phase Name>

_(same structure as Phase 1)_
_(repeat for all phases)_

## Actions Summary

1. <ordered action>
2. <ordered action>
3. <ordered action>
```

## Frontmatter Fields

| Field | Required | Description |
| --- | --- | --- |
| `trigger` | Yes | The `/command` that invokes this prompt (OpenCode) |
| `description` | Yes | One-line summary — used in listings |
| `tags` | Yes | Always include `hermes`, `copilot`, `opencode` plus domain tags |
| `dependencies` | No | Skills and subagents this prompt relies on |
| `skills` | No | Skill slugs with brief justifications |

## Section Detection Rules (from refactor_txt_markdown.md)

| Section | Always include? | Notes |
| --- | --- | --- |
| Description | **Yes** | Core — always present |
| Context | **Yes** | Core — always present |
| Skills Required | **Yes** | Core — always present (may list 0 if none needed) |
| Subagents | If delegation is involved | Included if the prompt delegates to other agents |
| Personas | If role-based work | Included if the prompt defines distinct roles |
| Rules | **Yes** | Core — always present |
| Phases | If 2+ sequential stages | Each phase has Goal/Inputs/Outputs/Steps/Tasks |
| Actions Summary | **Yes** | Core — always present |

## Key Differences from 9-Section Template

| Aspect | 9-section (detail sections) | 11-section (full structure) |
| --- | --- | --- |
| Context/Description | Absent | Present at top of document |
| Steps/Tasks/Subtasks | Top-level sections next to each other | Nested inside each Phase |
| YAML frontmatter | Not specified | Required for OpenCode compatibility |
| Cross-system tags | Not specified | Required (`hermes, copilot, opencode`) |
| Best for | Internal workflow prompts | Shared prompts invoked as commands |

## Example (minimal)

```markdown
---
trigger: /my-command
description: Does X, Y, and Z in three phases with verification.
tags: [hermes, copilot, opencode, automation]
dependencies:
  - skill:systematic-debugging
skills:
  - systematic-debugging — Find and fix issues
---

# my-command

> Does X, Y, and Z with phased execution and verification.

## Description

This prompt ... [describe what it does and when to use it]

**Critical rules:**
- Batch size is exactly 7 files
- Verify after each phase

[... remaining sections follow the template above]
```
