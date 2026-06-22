---
trigger: /projects-init
name: projects-init
title: "Projects Init"
description: >-
  Three-phase workspace initialization: triage MD documentation files, migrate
  prompt files to .github/prompts/, then create skills/scripts and update prompts.
  Eliminates duplicates and consolidates documentation.
version: 1.0.0
tags:
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
- **Phase 3 outputs:** New skills/scripts in `~/.hermes/skills/` + updated prompt frontmatter
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

**Goal:** Inventory all markdown documentation files, identify duplicates, consolidate, delete duplicates.

**Inputs:** `pwd`, `docs/**` (and subdirectories)

**Outputs:** Consolidated markdown documentation with no duplicates

**Steps:**

| Step | Action                                                         | Output             |
| ---- | -------------------------------------------------------------- | ------------------ |
| 1.1  | Run `ls pwd && ls pwd` to list workspace root files            | File list          |
| 1.2  | Run `ls docs/**` recursively to list all documentation files   | Doc file inventory |
| 1.3  | Identify duplicate markdown files (same name, similar content) | Duplicate list     |
| 1.4  | Consolidate: keep canonical version, delete duplicates         | Clean doc set      |
| 1.5  | Report before/after counts                                     | Phase summary      |

**Tasks:**

- **Task 1.1 — List root:** Run `ls` in workspace root, capture all markdown files
- **Task 1.2 — List docs:** Run recursive `ls docs/`, capture all `.md` files
- **Task 1.3 — Find duplicates:** Compare filenames across directories; flag same-name files
- **Task 1.4 — Consolidate:** For each duplicate pair, keep the version with more complete content, delete the other
- **Task 1.5 — Report:** Log file count before → after; document what was deleted

---

## Phase 2: Migrate Prompts

**Goal:** Discover all markdown prompt files, migrate them to `.github/prompts/`, consolidate, delete duplicates.

**Inputs:** `pwd`, `.github/prompts/` (if exists)

**Outputs:** Prompt files consolidated in `.github/prompts/`

**Steps:**

| Step | Action                                               | Output                    |
| ---- | ---------------------------------------------------- | ------------------------- |
| 2.1  | Run `ls pwd` to list root-level prompt files         | Root prompt list          |
| 2.2  | Run `ls .github/prompts/**` to list existing prompts | Existing prompt inventory |
| 2.3  | Migrate root prompt files to `.github/prompts/`      | Migrated prompts          |
| 2.4  | Identify and delete duplicate prompts                | Deduplicated prompts      |
| 2.5  | Report before/after counts                           | Phase summary             |

**Tasks:**

- **Task 2.1 — List root prompts:** Find all `.prompt.md` / `.prompt.txt` files at workspace root
- **Task 2.2 — List existing:** Inventory `.github/prompts/` contents
- **Task 2.3 — Migrate:** Move each root prompt file to `.github/prompts/` (create dir if needed)
- **Task 2.4 — Deduplicate:** Compare for same-name prompts across old/new locations; delete originals
- **Task 2.5 — Report:** Log migration counts and deletions

---

## Phase 3: Create Skills & Update

**Goal:** Scan `.github/prompts/`, identify needed skills and scripts, create them, update prompt frontmatter with correct skill dependencies.

**Inputs:** `.github/prompts/**`

**Outputs:** New skills in `~/.hermes/skills/`, prompts updated with skill references

**Steps:**

| Step | Action                                                                      | Output                 |
| ---- | --------------------------------------------------------------------------- | ---------------------- |
| 3.1  | List all prompts in `.github/prompts/`                                      | Prompt inventory       |
| 3.2  | For each prompt, extract referenced skills/tools from `skills:` frontmatter | Skill requirement list |
| 3.3  | Create any missing skills using `skill-manage`                              | Skills created         |
| 3.4  | Create supporting scripts in `~/.hermes/scripts/`                           | Scripts created        |
| 3.5  | Update prompt frontmatter with correct skill dependency references          | Updated prompts        |

**Tasks:**

- **Task 3.1 — Inventory:** List all `.prompt.md` files in `.github/prompts/`
- **Task 3.2 — Extract skills:** Parse each prompt's YAML frontmatter `skills:` field; aggregate unique skill names
- **Task 3.3 — Create skills:** For each referenced skill that doesn't exist, run `skill_manage(action='create')` with minimal scaffold
- **Task 3.4 — Create scripts:** Write helper scripts to `~/.hermes/scripts/` as needed
- **Task 3.5 — Update prompts:** Ensure each prompt's `dependencies:` and `skills:` lists are accurate and reference real skills

## Actions Summary

1. List and triage all markdown documentation files in `pwd` and `docs/**`; consolidate and delete duplicates
2. List and triage all markdown prompt files in `pwd` and `.github/prompts/`; migrate prompts to `.github/prompts/`; consolidate; delete originals
3. List and triage the migrated `.github/prompts/` collection; create all needed skills and scripts; update all prompts with accurate skill references
