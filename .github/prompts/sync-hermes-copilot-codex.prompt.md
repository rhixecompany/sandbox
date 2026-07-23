---
name: sync-hermes-copilot-codex
...
title: Sync Hermes Copilot Codex
...
description: Sync canonical Hermes assets to Copilot/Codex forms where appropriate, resolving drift
  without overwriting intentional forks. Covers skills, plugins, hooks, profiles,
  instructions, and agents.
...
version: 1.0.0
...
license: MIT
...
author: Hermes Agent
...
toolsets: - terminal
- file
scripts: []
skills: - using-superpowers
- user-communication-preferences
- executing-plans
- verification-before-completion
formatter: default
...
plan: ''
dependencies: - skill:using-superpowers
- skill:user-communication-preferences
- skill:executing-plans
- skill:verification-before-completion
tags: - sync
- copilot
- codex
- hermes
- cross-platform
- prompt
trigger: /sync-hermes-copilot-codex
...
---

# Sync Hermes Copilot Codex

> Repair references before writing sync actions. Privacy-scrub before comparing or copying files.

## Sources of Truth

- Hermes skills/profiles/plugins in `%LOCALAPPDATA%\hermes\`
- Copilot artifacts in `.github/instructions/` and `.github/agents/`
- Codex-related artifacts tracked explicitly in this repo

## Known Source Sets in This Repo

- `.github/instructions/*.instructions.md`
- `.github/agents/*.agent.md`

## Rules

1. Do not overwrite customized copies without explicit authorization.
2. Strip secrets before diff/copy.
3. Verify sync operation with file counts and parse checks only.
4. Append progress after each phase.

## Phase 1: Inventory Roots & Derived Assets

1. Count:
   - `.github/instructions/*.instructions.md`
   - `.github/agents/*.agent.md`
2. Inspect duplicates by filename similarity across roots/derived locations.
3. Identify root templates vs copies by inspection of first lines and metadata.

**Verification:** inventory list written to `docs/sync-hermes-copilot-codex-inventory.md`.

---

## Phase 2: Identify Drift and Safe Sync Candidates

1. Diff candidate pairs by checksum and filename.
2. Exclude intentionally customized copies.
3. Flag files with shared frontmatter template as highest-priority sync candidates.
4. Do not touch secrets/categories unrelated to prompt/sync scope.

**Verification:** drift list documented with reason for each candidate.

---

## Phase 3: Sync Corrective Diffs

1. Update canonical source first.
2. Propagate only when authorization is explicit in prompt context or affirmation.
3. Preserve custom sections in derived copies.
4. Use `patch` for narrow changes; do not use bulk replace.

**Verification:** sample pre/post checksums logged.

---

## Phase 4: Verify File Counts and Parse State

1. Re-count target files.
2. Spot-check frontmatter parse on a sample of affected files:
   - start must be `---`
   - no empty required fields used by this repo's templates
3. Append summary to `docs/sync-hermes-copilot-codex-report.md`.

**Verification:** user-communication-preferences checklist complete; progress artifact updated.
