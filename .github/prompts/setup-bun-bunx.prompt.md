---
name: setup-bun-bunx
title: Setup Bun and Bunx
description: Migrate a repository (and all sub-repos) from npm to bun and from npx to bunx, prune unused dependencies, validate package manifests, and commit and push the changes. Use when consolidating package-manager tooling on bun across a monorepo.
version: 1.0.0
author: Hermes Agent
tags:
  - prompt
  - setup
  - bun
  - bunx
  - package-manager
  - migration
  - monorepo
  - dependencies
  - automation
  - git
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
---
## Table of Contents

## Goal

## Context

## Phases



Migrate the current repository and every sub-repository from `npm` to `bun` and from `npx` / `npx.cmd` to `bunx`. After migration, `bun` becomes the default package manager for the whole workspace (including the Hermes root), unused dependencies are removed, and every affected repository has the new state committed and pushed.

The four high-level outcomes are:

1. Clean up `npm` and `bun` and upgrade `bun` to the latest version.
2. Switch all usage of `npm` to `bun` in this repo and every sub-repo.
3. Switch all usage of `npx` / `npx.cmd` to `bunx` in this repo, every sub-repo, and the Hermes root.
4. Commit the changes in every repo and push them.

## Prerequisites

- `bun` is installed and available on `PATH`. If it is missing, install it first via the official installer (`curl -fsSL https://bun.sh/install | bash`) or the platform package manager.
- `git` is configured with a user name and email, and a credential helper is in place for every remote you intend to push to.
- You have full read/write permission on every target repository (this repo, all sub-repos, and the Hermes root).
- The repositories are clean (no uncommitted changes) before migration starts. Use `git status` to confirm.

## Steps

### 1. Clean up npm and bun, upgrade bun

1. Remove any global `npm` artifacts that conflict with `bun` (e.g. stale `node_modules` caches, leftover `package-lock.json`).
2. Run `bun --version` to confirm `bun` is installed.
3. Upgrade `bun` to the latest stable release:

   ```bash
   bun upgrade
   ```

4. Verify the upgrade with `bun --version` again.

### 2. Switch repo + sub-repos from npm to bun

For the current repo and every sub-repo, in turn:

1. Set up, debug, fix, and validate every needed or optional `package.json`, `*.toml`, and `.npmrc` file.
2. Prefer smaller dependencies and dev dependencies. Replace heavy packages with lighter equivalents when possible.
3. Uninstall every dependency and dev dependency that is no longer used:

   ```bash
   bun remove <unused-package>
   ```

4. Replace the install workflow with `bun install` (and remove the old `node_modules` + lockfile first if present):

   ```bash
   rm -rf node_modules package-lock.json
   bun install
   ```

5. Verify the result by running the project's test, lint, and type-check commands (whatever the package defines).

### 3. Switch npx / npx.cmd to bunx

Across the same set of repos:

1. Search for every invocation of `npx` and `npx.cmd` in scripts, docs, CI config, and `package.json` `scripts` blocks.
2. Replace `npx <tool>` with `bunx <tool>` and `npx.cmd <tool>` with `bunx <tool>`.
3. Re-run the project's install, lint, build, and test commands to confirm nothing regressed.

### 4. Switch Hermes root from npm to bun, npx to bunx

Repeat the same migration against the Hermes root install:

1. Apply the same `package.json` / `.npmrc` / lockfile cleanup.
2. Replace every `npm` invocation with the equivalent `bun` command.
3. Replace every `npx` / `npx.cmd` invocation with `bunx`.
4. Validate by running the Hermes smoke checks (`hermes --version`, `hermes skills list`, etc.).

### 5. Set bun as the default package manager

1. Confirm there are no remaining `npm install`, `npm i`, `npm ci`, `npx`, or `npx.cmd` references in any of the affected repos.
2. Add or update a `packageManager` field in each top-level `package.json` (e.g. `"packageManager": "bun@<version>"`).
3. Document the new default in each repo's README so contributors know to use `bun` / `bunx`.

### 6. Commit and push

For the current repo and every sub-repo, after every step above has been verified:

1. Stage every changed file (use a specific list — do not blanket-add unrelated changes):

   ```bash
   git add -A
   ```

2. Commit with a human-readable message (run it through a humanizer pass so the message reads naturally):

   ```bash
   git commit -m "switch package manager from npm to bun"
   ```

3. Push the commit to the appropriate remote and branch (`origin development`, `origin production`, or the repo's default branch):

   ```bash
   git push -u origin development production
   ```

4. Debug and fix every issue, error, or warning that surfaces during the push. Re-run validation after each fix.

## Verification

Before declaring the migration complete, confirm all of the following:

- `bun --version` reports the latest stable release on every target machine.
- `bun install` succeeds in every affected repo with no warnings.
- No `package-lock.json` or `npm` lockfile artifacts remain in the migrated repos.
- Every `npx` / `npx.cmd` reference has been replaced with `bunx` (search the whole tree to confirm).
- Every repo's tests, linter, and build still pass under `bun`.
- Every commit has been pushed to its intended remote branch and the SHA is verified.
- No issues, errors, or warnings appear in the final `git status` of any repo.

## Related Skills

- `using-superpowers` — Foundational skill workflow.
- `brainstorming` — Clarify unknowns before changing the toolchain.
- `user-communication-preferences` — Keep the user informed during long migrations.
- `mcp-sequential-thinking` — Reason about cross-repo ordering.
- `mcp-filesystem` — Move and edit manifest files.
- `mcp-ast-grep` — Locate every `npx` / `npm` invocation precisely.
- `mcp-memory` — Persist migration state across turns.
- `plan`, `plans-and-specs` — Keep the migration plan discoverable.
- `create-implementation-plan`, `implementation-plan` — Document the rollout.
- `executing-plans` — Drive the migration step by step.
- `writing-clearly-and-concisely` — Keep commit messages human-readable.
- `subagent-driven-development` — Parallelise work across sub-repos.
- `systematic-debugging` — Diagnose and fix every issue that surfaces.
