---
name: comprehensive-hermes-maintenance-spec
title: "Comprehensive Hermes Maintenance Specification"
description: "Define safe inventory, remediation, synchronization, cleanup, and release gates for the SandBox and Hermes installation."
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, maintenance, config, hooks, plugins, scripts, docker, git, security]
status: draft
plan: .hermes/plans/comprehensive-hermes-maintenance-plan.md
---

# Comprehensive Hermes Maintenance Specification

## Decision state

This specification is **draft** until the owner answers the five clarification questions and approves the destructive-change gate. Safe defaults are used for planning only:

- Scope: SandBox, Hermes home, and nested Git repositories; inventory outside that scope only.
- Configuration: synchronize managed, non-secret projections; preserve profile and project overrides.
- Environment files: compare paths, classes, and variable names only; never copy or expose values.
- Docker: inventory first; delete only resources proven unused and explicitly approved.
- Git: no force-push; push only existing, fast-forwardable branches.

## Goals

1. Inventory the repository, Hermes home, nested repositories, profiles, agents, plugins, desktop assets, hooks, scripts, MCP configuration, environment-file metadata, and Docker resources.
2. Make every supported first-party script directly under the Hermes root `scripts/` directory available through a safe, tested quick-command entry.
3. Synchronize only the managed `quick_commands` projection through the supported Hermes CLI and verify readback.
4. Debug confirmed issues using root-cause investigation, regression checks, and bounded changes.
5. Consolidate exact duplicates without deleting ambiguous, user-owned, credential-bearing, or still-referenced artifacts.
6. Produce an auditable cleanup plan and execute approved Docker cleanup with a dry-run, allowlist, and post-cleanup verification.
7. Release verified repository changes with one logical commit per repository and non-forced pushes only.

## Non-goals

- Copying `.env` values, rotating credentials, or publishing secrets.
- Byte-for-byte synchronization of profile configurations that intentionally differ.
- Executing target scripts merely to test quick-command coverage.
- Deleting a plugin, skill, agent, model, MCP server, volume, image, or file based only on age, naming, or low recent use.
- Force-pushing, rewriting history, deleting branches, or committing generated secrets.

## Functional requirements

### FR-001 — Scoped inventory

The implementation MUST inventory both approved roots and nested Git repositories. It MUST classify paths by purpose, repository, profile, asset family, and generated/runtime status. It MUST exclude caches, vendored dependencies, bytecode, session logs, and `.git` internals from duplicate and source inventories unless a check explicitly targets them.

### FR-002 — Secret-safe environment audit

The implementation MUST locate `.env*` paths under the approved roots and report only absolute path, scope, file class, metadata, and variable names when needed. It MUST NOT print, copy, hash, synchronize, or commit environment values. Credential-bearing runtime files and pre-delete snapshots MUST be flagged for owner review.

### FR-003 — Config inventory and sync boundary

The implementation MUST locate every `config.yaml` in the approved roots, distinguish live configuration from profiles, examples, backups, and snapshots, and preserve unrelated keys. Live Hermes configuration MUST be changed through `hermes config set` or another supported validated CLI path. Direct whole-file replacement is prohibited.

### FR-004 — Complete quick-command coverage

Every supported regular file directly under `C:/Users/Alexa/AppData/Local/hermes/scripts` (`.py`, `.sh`, `.bash`, `.ps1`, `.ts`, `.js`) MUST have exactly one generated quick-command target. Generated entries MUST invoke the safe wrapper in audit mode, not the target script. Existing user commands MUST remain intact unless a collision is reported and resolved deterministically.

### FR-005 — Quick-command validation

The validator MUST check command shape, wrapper path, target/index validity, uniqueness, missing entries, stale entries, and count parity. It MUST read back the live `quick_commands` block and test every generated entry through the wrapper's non-destructive audit path. A malformed registry MUST return a non-zero exit code with an actionable diagnostic.

### FR-006 — Profile parity

The managed quick-command projection MUST be structurally equivalent across every selected active profile. Model, provider, plugin, platform, channel, and user-specific settings MUST remain unchanged. The report MUST list profiles skipped because they are not active, unavailable, or intentionally divergent.

### FR-007 — Scripts-judge enforcement

The canonical installed `scripts-judge` skill and its executable judge MUST treat Hermes quick-command coverage as a hard gate when the audited directory is the Hermes root scripts directory. The judge MUST retain syntax, CLI, error-handling, documentation, and DRY scoring and MUST report registry failures separately from score dimensions.

### FR-008 — Hermes asset diagnostics

Hooks, plugins, desktop assets, desktop plugins, and agent definitions MUST be checked using supported Hermes diagnostics and targeted static checks. Each finding MUST be labeled confirmed, suspected, expected-disabled, credential-blocked, or not reproducible. Fixes MUST include a regression check and avoid enabling optional integrations merely to silence warnings.

### FR-009 — Hook safety

Hook command paths, executable state, allowlist status, script mtime drift, payload contracts, and synthetic test behavior MUST be verified. Allowlist changes are security-sensitive and require an explicit approval record before application. Synthetic hook tests MUST not create fake session artifacts or commit working-tree changes.

### FR-010 — Plugin and desktop safety

Plugin and desktop audits MUST separate installed/enabled state from availability. Missing optional credentials, disabled-by-design plugins, and unsupported platform features MUST not be misclassified as defects. The audit MUST record plugin capability drift and desktop build/readiness failures without launching destructive or interactive flows.

### FR-011 — Dedupe and consolidation

Potential duplicates MUST be grouped by content hash plus semantic role. Only exact, unreferenced, non-secret duplicates may be removed. Consolidation MUST update references first, preserve one canonical path, and produce a before/after manifest. Untracked reports and generated caches MUST not be committed merely because they exist.

### FR-012 — Docker cleanup

Docker cleanup MUST begin with a read-only inventory of containers, images, build cache, volumes, networks, models, and MCP toolkit resources. The apply phase MUST use an explicit allowlist generated from the approved dry-run. Resources with active references, ambiguous ownership, credential state, or MCP/toolkit purpose MUST be preserved until separately approved. Post-cleanup `docker system df` and targeted listings MUST verify the result.

### FR-013 — Repository release

Before release, each changed repository MUST pass its relevant tests and a secret scan. The root repository and changed nested repositories MUST be reviewed independently. The implementation MUST create one human-written Conventional Commit per repository, never include `.env` or credential files, never force-push, and push only branches that exist and are fast-forwardable.

### FR-014 — Evidence and resumability

Every phase MUST write machine-readable evidence under `.hermes/reports/` or a documented Hermes cache path. Reports MUST include timestamps, scope, command, exit status, counts, and unresolved blockers without secret values. Re-running a phase MUST be idempotent or detect and reuse its verified artifact.

## Acceptance criteria

| ID | Pass condition |
|---|---|
| AC-01 | Inventory covers both roots, all selected profiles, all nested repositories, and the requested asset families. |
| AC-02 | Environment and credential reports contain paths/metadata only; no secret values appear in tracked output or terminal summaries. |
| AC-03 | Live `quick_commands` readback covers every inventoried Hermes root script exactly once; generated entries use the wrapper audit mode. |
| AC-04 | Wrapper smoke tests pass for every generated entry without executing target business logic. |
| AC-05 | Canonical scripts-judge reports a passing quick-command gate and preserves its five score dimensions. |
| AC-06 | Confirmed hook/plugin/desktop/agent defects either have verified fixes or an explicit external blocker. |
| AC-07 | Dedupe report proves every removed file was an exact, unreferenced duplicate and retains a canonical replacement. |
| AC-08 | Docker deletion, if approved, is limited to allowlisted unused resources and is verified after execution. |
| AC-09 | Root and changed nested repositories pass applicable gates; pushes are non-forced and branch-scoped. |
| AC-10 | Prompt, spec, plan, scripts, skill changes, reports, and blockers are listed in the final handoff. |

## Verification matrix

| Area | Primary check | Evidence |
|---|---|---|
| Scripts | safe wrapper inventory, registry validation, smoke | quick-command JSON + judge report |
| Config | Hermes CLI readback and structural diff | profile sync report |
| Environment | path/key-name-only scan | redacted env inventory |
| Hooks | `hermes hooks doctor` plus approved synthetic tests | hook diagnostic report |
| Plugins | `hermes plugins list/capabilities/doctor` | plugin report |
| Desktop | supported build-only/readiness checks | desktop report |
| Agents | definition and profile routing checks | agent inventory |
| Dedupe | hashes, references, canonical mapping | dedupe manifest |
| Docker | dry-run inventory, allowlist, post-check | Docker report |
| Release | tests, secret scan, status, push readback | release report |

## Rollback

- Workspace files: use Git restore/revert for tracked edits; do not create backup copies.
- Live config: restore only the captured managed `quick_commands` projection through `hermes config set`; never replace the whole file.
- Skills: use `skill_manage` patch reversal from the recorded old text.
- Hooks: revoke newly added allowlist entries if approved changes misbehave.
- Docker: do not promise recovery for deleted images/volumes; therefore require an explicit allowlist and preserve all ambiguous resources.
- Git: stop on non-fast-forward or protected branches; do not force a recovery push.
