---
author: Alexa
description: Use when working with Create Implementation Plan. Supports creating single
  plans and batch creating multiple plans from templates or specifications.
license: MIT
metadata:
  hermes:
    tags:
    - tools
name: create-implementation-plan
tags:
- tools
title: Create Implementation Plan
version: 1.1.0

---

# Create Implementation Plan

## Goal

Provide comprehensive guidance for Create Implementation Plan workflows. **Supports creating single plans and batch creating multiple plans from templates or specifications.**

## Subgoals

1. **Preparation** — Understand prerequisites and setup
2. **Execution** — Follow structured workflow with error handling
3. **Verification** — Confirm output meets requirements
4. **Batch Creation** — Generate multiple plans from templates or specifications

## Personas

| Persona | When to Use |
|---------|-------------|
| **Developer** | Technical implementation and coding tasks |
| **Admin** | System operations and maintenance |
| **User** | Day-to-day operations and usage |

## Personality & Tone

- **Tone**: Professional, concise
- **Style**: Step-by-step instructions with examples
- **Avoid**: Unclear prerequisites, missing error handling
- **Encourage**: Verification checkpoints, resumability

## Profile Selection

| Task Type | Recommended Profile |
|-----------|---------------------|
| General purpose | `default` |
| Code changes | `code-architect` |
| System operations | `adminbot` |

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## When to Use

When working with Create Implementation Plan in Hermes workflows.

## When NOT to Use

When this skill is not relevant to your task.

## Workflow

### Phase 0: Batch Discovery (Batch/Folder Modes Only)

**Entry check:** If `.hermes/plans/batch-create-discovery.md` exists → skip to Phase 1.

1. **Discover targets** — Resolve plan creation specs from:
   - `--batch spec1.md spec2.md ...` explicit specification files
   - `--folder specs/` recursive scan for specification files
   - `--template <path>` template plan to use as base
2. **Validate targets** — Filter existing files, validate specification format
3. **Write discovery artifact** → `.hermes/plans/batch-create-discovery.md` with spec list

### Phase 1: Preparation

- Understand the context and requirements
- Verify prerequisites are met
- **Batch mode:** Load template plan and specification files in parallel using `execute_code`

### Phase 2: Execution

- Follow step-by-step instructions
- Handle errors gracefully
- **Batch mode:** Generate multiple plans from template + specs using `execute_code` with a bulk creation script. Each spec produces one plan file.

### Phase 3: Verification

- Confirm output meets requirements
- Document results
- **Batch mode:** Verify all generated plans against template compliance checklist. Aggregate results to `.hermes/plans/batch-create-verification.md`.

## Pitfalls

- **Thin content**: This skill may lack concrete examples. Add code examples and real-world use cases.
- **Missing error handling**: Always include error handling patterns in workflow phases.
- **No resumability**: Add entry/exit checks at each phase for long-running workflows.
- **Batch template drift**: When creating many plans from one template, ensure template updates propagate to all generated plans. Use `update-implementation-plan` for bulk updates.

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text