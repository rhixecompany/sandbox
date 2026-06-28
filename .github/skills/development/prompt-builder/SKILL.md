---
author: Hermes Agent
description: Use when scaffolding new prompt files, generating prompt templates, or
  building structured prompt libraries from specifications.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: prompt-builder
tags:
- prompts
- scaffolding
- templates
- library
title: Prompt Builder
version: 1.0.0

---
# Prompt Builder

## Description

Scaffold, generate, and build structured prompt files and prompt libraries from specifications. Works with the 9-section and 11-section templates from `enforce-markdown`, supports Hermes/Copilot/OpenCode cross-platform formats, and produces ready-to-use prompt artifacts.

## When to Use

- Scaffolding new prompt files from specifications
- Building prompt libraries from a set of requirements
- Converting feature specs into prompt definitions
- Generating starter prompts for new workflows
- Batch-creating prompts from a manifest or registry

## When NOT to Use

- Improving existing prompt content (use `prompt-engineering`)
- Auditing prompt quality (use `enhance-markdown`)
- Executing prompts (use `acpx-executor` or direct delegation)

## Goal

Generate well-structured, ready-to-use prompt files from specifications — with correct frontmatter, section ordering, and cross-platform compatibility.

## Inputs

- Prompt name, trigger, description
- Feature specifications or requirements
- Target platform (Hermes, Copilot, OpenCode, or cross-platform)
- Template choice (9-section for internal, 11-section for cross-system)

## Outputs

- Structured `.prompt.md` file with valid YAML frontmatter
- Cross-references to required skills and dependencies
- Validation report confirming structural compliance

## Rules

1. **Always include YAML frontmatter** — title, trigger, description, tags minimum
2. **Always include context-map dependency** when prompt is part of a pipeline
3. **Use 9-section template** for internal workflow prompts
4. **Use 11-section template** for cross-system commands
5. **Name section: `## Actions`** (not `Actions Summary`)
6. **Every Task must have at least one Action** — no orphaned checkboxes
7. **Validate before writing** — check structural compliance before file write

## Workflow

### Phase 1: Gather Requirements

- Collect prompt name, trigger, description
- Identify target platform(s)
- Determine template type (9-section vs 11-section)
- List required skills, dependencies, subagents

### Phase 2: Select Template

- 9-section: Goal, Context, Inputs, Outputs, Rules, Phases, Steps, Tasks, Actions
- 11-section: Adds YAML frontmatter fields, Description, Context sections with Steps/Tasks/Subtasks nesting
- Prefer 11-section when `trigger:` needs OpenCode compatibility

### Phase 3: Populate Sections

- Fill frontmatter (title first, then trigger, description, tags, dependencies)
- Write Goal as single paragraph (not blockquote)
- Extract Rules from requirements (behavioral guardrails)
- Build Phases from workflow stages
- Derive Steps from Phases
- Derive Tasks from Steps (each Task = one checkbox)
- List Actions with tool/command references

### Phase 4: Validate and Write

- Run structural validation (frontmatter, section ordering, heading levels)
- Check cross-references resolve
- Write to target path
- Report file path and size

## Skills Required

- `enhance-markdown` — Template application and structure rules
- `writing-plans` — Structuring specifications
- `systematic-debugging` — Validating structural compliance
- `simplify` — Keeping output crisp

## Verification Checklist

- [ ] Prompt name, trigger, description collected
- [ ] Target platform confirmed (Hermes/Copilot/OpenCode)
- [ ] Template type selected (9-section vs 11-section)
- [ ] YAML frontmatter valid
- [ ] Section ordering correct
- [ ] Cross-references resolve
- [ ] File written to target path

## Pitfalls

- Start from a template, not blank
- Reuse existing prompt patterns over inventing new structures
- Always cross-link to `context-map` when part of a pipeline
- Keep Actions specific (named tools, not generic descriptions)
- Use Subtasks section only when Tasks need further decomposition
