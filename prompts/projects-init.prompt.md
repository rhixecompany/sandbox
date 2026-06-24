---
license: MIT
author: Hermes Agent
trigger: /projects-init
name: projects-init
title: "Projects Init"
description: >-
  Three-phase workspace initialization: triage MD documentation files, migrate
  prompt files to .github/prompts/, then create skills/scripts and update prompts.
  Eliminates duplicates and consolidates documentation.
version: 1.0.0
tags: []
  [
    hermes,
    projects,
    init,
    docs,
    prompts,
    skills,
    migrate,
    consolidate,
    deduplicate,
  ]
dependencies:
  - skill:enhance-markdown
  - skill:hermes-skills
  - skill:skill-creator
skills:
  - enhance-markdown
  - hermes-skills
  - skill-creator
metadata:
  hermes:
    tags: [projects, init, docs, prompts, migrate, consolidate]
    related_skills: [enhance-markdown, hermes-skills, skill-creator]
---

# Projects Init

> Initialize a workspace: triage docs, migrate prompts, create skills. Three sequential phases — each must finish before the next begins.

## Description

This prompt initialises a new or stale workspace by running a three-phase cleanup and consolidation pipeline. Phase 1 discovers and deduplicates all markdown documentation files. Phase 2 discovers prompt files, migrates them to `.github/prompts/`, and consolidates. Phase 3 indexes the new prompt directory, creates any needed skills and helper scripts, and updates all prompts to reference the skills they need.

**Critical rules (must appear within the first 15% of execution):**

- **Only then constraint** — Each phase completes fully before the next begins. No overlapping phases.
- **Delete only after verification** — Before deleting any file, confirm the canonical copy exists in the target location.
- **Count before and after** — Record file counts at each phase start and end; report deltas.

## Context

- **Source reference:** `projects-init.prompt.txt` (raw specification)
- **Target scope:** `pwd` (workspace root), `docs/`, `.github/prompts/`
- **Phase 1 outputs:** Consolidated markdown documentation inventory + deleted duplicates
- **Phase 2 outputs:** Prompt files migrated to `.github/prompts/` + deleted originals
- **Phase 3 outputs:** New skills/scripts in `~/AppData/Local/hermes/skills/` + updated prompt frontmatter
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI

## Skills Required

| Skill              | Purpose                                                 |
| ------------------ | ------------------------------------------------------- |
| `enhance-markdown` | Audit, enhance, convert, and consolidate markdown files |
| `hermes-skills`    | List, create, install, and manage skills                |
| `skill-creator`    | Scaffold new skills with validated frontmatter          |

## Rules

1. **Strict sequential execution** — Phase 1 → Phase 2 → Phase 3. Each phase must complete (including verification) before the next starts.
2. **Verify before delete** — Always confirm the canonical copy exists at the target path before removing a source file.
3. **Count and report** — Log file counts before and after each phase. Report deltas in the phase summary.
4. **No destructive operations without confirmation** — For `rm` operations over 3+ files, show the list and ask before executing.

## Phases

## Phase 1: Triage Documentation

> **Goal:** Inventory all markdown documentation files, identify duplicates, conso
> **Inputs:** `pwd`, `docs/**` (and subdirectories)

> **Full content:** `templates/projects-init/phase_1_triage_documentat.md`

## Phase 2: Migrate Prompts

> **Goal:** Discover all markdown prompt files, migrate them to `.github/prompts/`
> **Inputs:** `pwd`, `.github/prompts/` (if exists)

> **Full content:** `templates/projects-init/phase_2_migrate_prompts.md`

## Phase 3: Create Skills & Update

> **Goal:** Scan `.github/prompts/`, identify needed skills and scripts, create th
> **Inputs:** `.github/prompts/**`

> **Full content:** `templates/projects-init/phase_3_create_skills__up.md`

## Actions Summary

1. List and triage all markdown documentation files in `pwd` and `docs/**`; consolidate and delete duplicates
2. List and triage all markdown prompt files in `pwd` and `.github/prompts/`; migrate prompts to `.github/prompts/`; consolidate; delete originals
3. List and triage the migrated `.github/prompts/` collection; create all needed skills and scripts; update all prompts with accurate skill references


## Template References

Detailed templates in `templates/projects-init/`:


## Template References

Templates in `templates/projects-init/`:
- `actions_summary.md`
- `context.md`
- `description.md`
- `phase_1_triage_documentat.md`
- `phase_2_migrate_prompts.md`
- `phase_3_create_skills__up.md`
- `rules.md`
- `skills_required.md`
