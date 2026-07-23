---
name: "prompts-strict-template"
description: "Enforce strict prompt markdown template for this repository"
applyTo: "**/*.prompt.md"
---

# Prompts Strict Template

Apply these rules when creating or editing files that match `**/*.prompt.md`.

## Scope

- Applies only to `**/*.prompt.md`.
- Do not apply these rules to files outside `**/*.prompt.md`.

## Required Top-Level Structure

Every prompt markdown file must contain these top-level sections in this exact order:

1. `## Description`
2. `## Context`
3. `## Skills Required`
4. `## Subagents`
5. `## Personas`
6. `## Rules`
7. `## Phases`
8. `## Steps`
9. `## Tasks`
10. `## Subtasks`
11. `## Actions Summary`

## Phase Formatting Rules

- `## Phases` must include one or more `### Phase N: Name` subsections.
- Each phase subsection must include a markdown table with this header:
  - `| Field | Details |`
- Each phase table must include these rows:
  - Goal
  - Inputs
  - Outputs
  - Validation

## Task Numbering Rules

- `## Tasks` entries must use numbered task labels in this format:
  - `- Task N.x — ...`
- `## Subtasks` entries must use hierarchical numbering in this format:
  - `- Subtask N.x.y — ...`

## Source Intent Rules

- Preserve existing prompt intent and wording as much as possible.
- If a same-name `.txt` file exists alongside a `.prompt.md` file, treat the `.txt` file as source intent and keep `.txt` files read-only.
- Do not remove meaningful sections; only normalize structure and formatting.

## Validation Rules

Before finalizing edits in `**/*.prompt.md`, ensure the following:

- Confirm all 11 required top-level sections exist and are non-empty.
- Confirm at least one phase table is present under `## Phases`.
- Confirm `## Tasks` and `## Subtasks` numbering format is valid.
- Resolve markdown lint or diagnostics issues introduced by the change.
