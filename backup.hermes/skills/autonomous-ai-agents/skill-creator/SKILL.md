---
name: skill-creator
title: Skill Creator
description: Use when authoring, scaffolding, and validating in-repo SKILL.md files and skill assets.
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags:
      - imported
      - priority
    related_skills: []
---## Goal
authoring, scaffolding, and validating in-repo SKILL.md files and skill assets. to accomplish the associated tasks and objectives.


# Skill Creator

## Linked Files

- `references/frontmatter-corruption-repair.md` — Detection and repair patterns for garbled frontmatter in migrated skill files (double/triple blocks, `1|` prefix corruption)
- `references/prompt-normalization-hermes-structure.md` — Canonical Hermes-friendly shape for migrated prompt files
- `references/prompt-library-standardization.md` — Session-backed workflow for class-level prompt library normalization and legacy prompt preservation

## When to Use

- Creating new skills from scratch
- Editing or improving existing skills
- Running evals to test skills
- Benchmarking skill performance
- Optimizing skill descriptions
- Measuring skill effectiveness

## When NOT to Use

- Using existing skills
- Non-skill development
- Quick one-off tasks
- Real-time skill testing

## Workflow

### Phase 1: Plan Skill

- Identify skill purpose
- Define use cases
- Plan skill structure
- Outline workflow

### Phase 2: Create Skill

- Write skill description
- Define when to use
- Create workflow phases
- Add tools and references

### Phase 3: Test & Evaluate

- Run evals on skill
- Test with real scenarios
- Measure performance
- Identify issues

### Phase 4: Optimize & Deploy

- Improve based on feedback
- Optimize description for triggering
- Benchmark performance
- Deploy skill

## Tools & References

- **Related Skills**: writing-skills, skill-judge
- **Skill Format**: SKILL.md structure
- **Evals**: Performance testing framework
- **Benchmarking**: Variance analysis and metrics

## Best Practices

- Start with clear purpose
- Test thoroughly before deploying
- Get feedback from users
- Measure performance metrics
- Optimize descriptions for discovery
- Document skill behavior
- Maintain and update skills

### Prompt Refactor & Repository Prompt Hygiene

- When refactoring repository prompt files (Prompts/*.md, .github/prompts/*.md), prefer a DRY YAML frontmatter that tools (Hermes, Copilot, OpenCode) can parse programmatically. See `references/prompt-frontmatter-template.md` for the canonical template.
- Use git status and a focused checkpoint commit if needed before editing prompts. Do not create timestamped backup copies.
- Use a "preview-first" flow: produce a sample refactor for the first file and obtain sign-off before batch changes.
- If a search_files or tooling JSON parse error occurs while enumerating files, fallback to narrower globs, pagination (offset), or per-file reads instead of retrying identical wide searches (this avoids idempotent-no-progress traps).
- Do NOT perform git commits, destructive moves, or start/modify live MCP servers without explicit separate approval; scaffold metadata/stubs only unless asked to run servers.

## Overview

Skill authoring tool for creating, testing, and deploying SKILL.md files. Covers the complete skill lifecycle from planning through optimization, with evals and benchmarking for quality assurance.

## Verification Checklist

- [ ] Skill has clear purpose, use cases, and structured workflow
- [ ] Skill is tested with real scenarios and passes evaluations
- [ ] Description is optimized for triggering on relevant queries
- [ ] Prompt refactors follow DRY YAML frontmatter and git-backed rollback
- [ ] Skill performance is benchmarked and tracked over time
