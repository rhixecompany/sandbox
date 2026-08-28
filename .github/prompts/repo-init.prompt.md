---
name: repo-init
title: Repo Init
description: Initialize a repository by listing/triaging files across the repo and Hermes root, then dedupe, consolidate, and delete duplicates for consistent state across both locations.
version: 1.0.0
author: Hermes Agent
tags: [repo, initialization, triage, dedupe, consolidation, cleanup]
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
date: '2026-08-25'
---
## Table of Contents

## Goal

## Context

## Phases


# Repo Init

> Comprehensive implementation prompt, plan, scripts, and skill that outlines the steps needed to initialize a repository, including timelines, milestones, and resource allocation.


Initialize a Hermes-managed repository and its accompanying Hermes root (`~/AppData/Local/hermes`) to a consistent, deduplicated state. The end state has exactly one canonical copy of every artifact (prompts, skills, agents, hooks, instructions, plans) — no duplicates, no broken references, no stale wrappers.

## Prerequisites

- Operating from `pwd` inside the target repo and having read/write access to the Hermes root
- 14-skill protocol loaded: `/using-superpowers`, `/brainstorming`, `/user-communication-preferences`, `/mcp-sequential-thinking`, `/mcp-filesystem`, `/mcp-ast-grep`, `/mcp-memory`, `/plan`, `/plans-and-specs`, `/create-implementation-plan`, `/implementation-plan`, `/executing-plans`, `/writing-clearly-and-concisely`, `/subagent-driven-development`
- `repo-management.prompt.md` for rename operations (out of scope here)
- `prompt-builder.prompt.md` for authoring new content (out of scope here)
- `prompts-fix.prompt.md` for cross-platform migration (out of scope here)
- `repo.prompt.md` for workspace-level onboarding (out of scope here)

## Inputs

- The current workspace (`pwd`) and the Hermes root (`~/AppData/Local/hermes`)
- The list of files already known to the user (for context) plus an authoritative fresh scan
- Any user constraints on what counts as a duplicate, what to keep, and what to delete

## Skills Required

Load these skills in order before any triage, dedupe, or delete step. Each skill defines a contract that downstream phases depend on.

- `/using-superpowers`
- `/brainstorming`
- `/user-communication-preferences`
- `/mcp-sequential-thinking`
- `/mcp-filesystem`
- `/mcp-ast-grep`
- `/mcp-memory`
- `/plan`
- `/plans-and-specs`
- `/create-implementation-plan`
- `/implementation-plan`
- `/executing-plans`
- `/writing-clearly-and-concisely`
- `/subagent-driven-development`

> The full skill list is the contract. Do not skip a skill; later phases assume the earlier ones have already shaped context.

## Outputs

- A triaged inventory of files in both the repo and the Hermes root, with purpose and relevance summarized.
- A dedupe/consolidate plan that records the canonical path for every duplicate.
- A delete list scoped to duplicates only — never to unique files.
- An updated workspace and Hermes root where the canonical version of each artifact exists exactly once.

## Steps

### 1. List and Triage

1. Inventory files in the repository and in the Hermes root.
2. For every file, record: path, size, last-modified, owning subsystem, and a one-line purpose.
3. Group files by intended role (prompt, skill, agent, hook, instruction, plan, etc.).
4. Surface the cross-system duplicates (same role in both the repo and the Hermes root) and the within-system duplicates (two or more files serving the same role inside one location).
5. Produce a triage report: `triage.md` (or printed summary) with the file table and a "purpose" column.

### 2. Dedupe and Consolidate

1. For each duplicate cluster, pick the canonical copy using the precedence rules below.
2. Re-point every reference (prompt body, plan, hook, agent card) to the canonical path.
3. Update frontmatter and `metadata.dependencies` blocks to reflect the new canonical paths.
4. Confirm the canonical copy is the most complete and most recently maintained version; if not, merge the missing content into it before deleting the duplicates.

**Canonical precedence (highest wins):**

1. The file under `~/AppData/Local/hermes/skills/...` when the artifact is a skill.
2. The file under `~/AppData/Local/hermes/agents/...` when the artifact is an agent.
3. The file under `.github/prompts/*.prompt.md` for prompts that ship with a project.
4. The file under `.github/instructions/*.instructions.md` for repository-level instructions.
5. The file under `.github/hooks/*` for hooks and hook adapters.
6. The most recently maintained copy when the role matches in two equally-valid locations.

### 3. Delete Duplicates

1. Only delete a file after the canonical copy is verified to exist at the target path and every reference has been rewritten.
2. Never delete a file with no replacement; instead, flag it for human review.
3. Record the delete list (path, reason, kept-alternative) in `dedupe-log.md` before executing.
4. For batch deletes of three or more files, list them and request explicit approval before running.
5. Re-scan after deletion to confirm the canonical version is still present and that no references are broken.

## Rules

- **Verify before delete** — Confirm the canonical copy exists at the target path before removing a source file.
- **One canonical per role** — Every skill, agent, prompt, hook, and instruction must have exactly one canonical path.
- **References first** — Re-point all references before deleting a file; broken links are worse than duplicates.
- **Count before and after** — Record file counts at the start and end of each phase; report deltas.
- **Approval for bulk deletes** — For deletions of three or more files, show the list and wait for explicit user confirmation.
- **Scope discipline** — Stay inside the repo and the Hermes root. Do not touch unrelated paths or hidden directories.

## Verification

- `find` or `search_files` returns zero files matching the dedupe clusters after Phase 3.
- Every reference in surviving files resolves to a real path (`grep` for each deleted path returns no hits in surviving files).
- The triage report and dedupe log are saved at the repo root for audit.
- File count delta is reported and matches the dedupe log.

## Out of Scope

- Renaming files (covered by `repo-management.prompt.md`).
- Authoring new content (covered by `prompt-builder.prompt.md`).
- Cross-platform migration of prompts (covered by `prompts-fix.prompt.md`).
- Workspace-level onboarding (covered by `repo.prompt.md`).
