---
name: comprehensive-hermes-maintenance-spec
title: Comprehensive Hermes Maintenance Specification
description: "Define testable safety, synchronization, remediation, cleanup, and release requirements for the SandBox and Hermes installation."
version: 2.1.0
author: Alexa
license: MIT
tags: [hermes, maintenance, scripts, config, mcp, hooks, plugins, agents, docker, git, security]
status: approved
owner: Alexa
plan: .hermes/plans/comprehensive-hermes-maintenance-plan.md
prompt: .github/prompts/comprehensive-hermes-maintenance.prompt.md
approval: .hermes/approvals/2026-09-05-comprehensive-hermes-maintenance.md
---

# Comprehensive Hermes Maintenance Specification

## Goal
Build a deterministic inventory and remediation pipeline for the SandBox workspace and Hermes root installation, covering scripts, configs, secrets metadata, MCP servers, hooks, plugins, desktop assets, agents, Docker resources, and process state.

## Functional requirements

### FR-001 — Scoped inventory

Inventory both approved roots and every independently detected nested Git repository. Classify paths by repository, asset family, source/generated/runtime state, and purpose. Exclude Git internals, caches, bytecode, virtual environments, vendored dependencies, and session logs from source/dedupe counts unless the check explicitly targets them.

### FR-002 — Secret-safe environment audit

Locate every `.env*` file under the approved roots. Report only absolute path, scope, class, size/mtime metadata, variable names, and a boolean indicating whether a value-bearing assignment exists. Do not print, copy, hash, synchronize, stage, or commit values. Mark credential-bearing runtime files for review.

### FR-003 — Config inventory

Locate every `config.yaml` under the approved roots, including profile directories and snapshots. Classify live, profile, example, backup, snapshot, and generated files. Report key paths and schema differences without values. The audit must never overwrite a whole live config.

### FR-004 — Hermes CLI configuration boundary

Use `hermes config set` for live Hermes changes. The only managed projection in this run is `quick_commands`. Before and after writes, read back the exact block and verify unrelated config keys remain structurally unchanged.

### FR-005 — Complete root-script registry

Define a supported Hermes root script as a regular file directly under `C:/Users/Alexa/AppData/Local/hermes/scripts` with suffix `.py`, `.sh`, `.bash`, `.ps1`, `.ts`, or `.js`. Each supported file must map to exactly one generated command. Nested directories, `node_modules`, caches, bytecode, data files, backups, and snapshots are excluded.

### FR-006 — Safe command contract

Generated commands must invoke the installed or workspace wrapper in `audit` mode, with a stable filename or validated inventory index. They must not invoke target business logic. The wrapper must check existence and safe syntax where the host supports it and return a non-zero result for invalid or missing targets.

### FR-007 — Registry verification and smoke

The validator must detect missing, stale, duplicate, malformed, out-of-root, non-wrapper, wrong-mode, and untested entries. It must read the live Hermes `quick_commands` block and test every generated entry through the wrapper's audit path. It must emit machine-readable counts and fail non-zero on any gate violation.

### FR-008 — Profile parity

For each selected profile, the managed quick-command projection must be structurally equivalent. Provider, model, plugin, hook, channel, platform, user, and other unrelated settings must remain unchanged. Unavailable or intentionally divergent profiles must be listed with a reason.

### FR-009 — Scripts-judge enforcement

The canonical installed `scripts-judge` skill and judge script must retain its five score dimensions and add a hard Hermes-root quick-command gate. The gate must validate coverage, command shape, wrapper/audit mode, target uniqueness, live readback input, and wrapper smoke results. Registry failures must be reported separately from score totals.

### FR-010 — Hermes surface diagnostics

Run supported checks and targeted static analysis for desktop, desktop plugins, hooks, scripts, agents, session start/end capture, context files, and system prompts. Classify each finding as confirmed, suspected, expected-disabled, credential-blocked, external dependency, or not reproducible. Every fix needs a focused regression check.

### FR-011 — Hook safety

Check hook registration, command paths, executable state, allowlist status, payload contracts, Windows path handling, and synthetic lifecycle behavior. Allowlist mutations require an approval record. Synthetic tests must not leave fake session rows, generated credentials, or working-tree changes.

### FR-012 — Plugin and agent safety

Separate installed, enabled, disabled, unavailable, and credential-blocked states. Do not enable optional integrations to hide warnings. Preserve the four required agent platforms. A removable agent/tool must be orphaned, duplicated, disabled, or unconfigured and must have no active reference.

### FR-013 — MCP translation and health

Treat `.mcp/registry.json` as the workspace source of truth for platform translations. Preserve Hermes' separate internal MCP store. Validate OpenCode `mcp`, Copilot/Codex `mcpServers`, and VS Code `servers` schemas. Use JSON-RPC `initialize` POST probes for remote servers where supported, safe help/version probes for local commands, and record authentication/optional-dependency blockers separately.

### FR-014 — Dedupe and consolidation

Group exact candidate duplicates by content hash and semantic role. Check references before removal. Keep one canonical file, update references first, and write a before/after manifest. Never remove secrets, caches, runtime logs, virtual environments, active source, or ambiguous files.

### FR-015 — Docker and model cleanup

Inventory containers, images, build cache, volumes, networks, local models, and MCP toolkit resources read-only. Generate an allowlist from proven inactive/unreferenced resources. Apply only the allowlist. Preserve active, referenced, ambiguous, toolkit, model, and credential-sensitive resources unless separately approved. Verify every deletion with post-state listings and `docker system df`.

### FR-016 — Repository release

Run relevant tests and secret scans per repository. Review the staged set. Create one human Conventional Commit per eligible repository. Exclude `.env*`, private keys, tokens, credential-bearing configs, caches, virtual environments, raw runtime continuation files, and unrelated pre-existing changes. Push only existing branches with fast-forward, non-forced updates and verify remote readback.

### FR-017 — Evidence and resumability

Every phase writes secret-safe JSON/Markdown evidence with timestamp, scope, command, exit status, counts, and blockers. Re-running a phase is idempotent or reuses a verified artifact. A phase is not complete because a previous report says it is complete; live state is authoritative.

## Acceptance criteria

| ID | Pass condition |
|---|---|
| AC-01 | Approved roots, independent nested repositories, profiles, scripts, configs, env paths, MCP, hooks, plugins, agents, Docker, and process state are inventoried. |
| AC-02 | Reports contain no secret values and no secret-bearing files are staged. |
| AC-03 | Live `quick_commands` readback covers every supported Hermes root script exactly once. |
| AC-04 | Every generated entry invokes the safe wrapper in audit mode and all generated entries pass wrapper smoke. |
| AC-05 | Canonical scripts-judge preserves five dimensions and passes its quick-command hard gate. |
| AC-06 | Confirmed Hermes-surface defects are fixed with evidence or recorded with an exact external blocker. |
| AC-07 | MCP files pass schema checks, enabled-server policy is explicit, and live failures are not false-positive HEAD-only results. |
| AC-08 | Environment/config schema synchronization preserves secrets and intentional profile/platform differences. |
| AC-09 | Any removed file/resource has an exact identity, proof of non-use, reason, and post-change verification. |
| AC-10 | Root and changed nested repositories pass applicable gates; commits and pushes are non-forced and read back successfully. |
| AC-11 | Prompt, spec, plan, scripts, skill changes, reports, decisions, and blockers are listed in the final handoff. |

## Verification matrix

| Area | Primary check | Evidence |
|---|---|---|
| Planning | frontmatter, traceability, approval | prompt/spec/plan/approval |
| Environment | key-name-only scan | env/config inventory |
| Scripts | inventory, registry verify, smoke, judge | quick-command report + judge |
| Hermes | doctor/list/capabilities + focused tests | Hermes surface report |
| Hooks | list/doctor + isolated lifecycle test | hook report |
| MCP | schema, sync, JSON-RPC/local probes, live tools | MCP report |
| Dedupe | hashes and references | dedupe manifest |
| Docker | dry-run, allowlist, apply, post-check | Docker report |
| Release | tests, secret scan, status, push readback | release report |

## Rollback

- Workspace: `git restore -- <path>` or `git revert <commit>` after review.
- Hermes `quick_commands`: restore the captured managed projection with `hermes config set`; never replace the full YAML file.
- Skills: reverse the recorded `skill_manage` patch or restore the previous skill content from Git/skill metadata.
- Hooks: remove only newly added approved allowlist entries if the focused lifecycle check regresses.
- Docker: deleted data is not assumed recoverable; preserve ambiguity and require allowlists.
- Git: stop on auth, permission, protected-branch, or non-fast-forward errors; do not force a recovery.

## Traceability

| Requirement | Plan milestone | Verification |
|---|---|---|
| FR-001–FR-004 | M0–M2 | inventory/config reports |
| FR-005–FR-009 | M3 | quick-command + judge reports |
| FR-010–FR-012 | M4 | Hermes surface report |
| FR-013 | M5 | MCP report + live calls |
| FR-014–FR-015 | M6 | dedupe/Docker reports |
| FR-016–FR-017 | M7–M8 | release/final reports |

## Non-Functional Requirements

### NFR1: Performance
- Quick command generation: < 30 seconds
- Smoke test for 265 scripts: < 60 seconds
- Environment sync: < 10 seconds
- Docker cleanup: < 5 minutes

### NFR2: Reliability
- All operations must be idempotent
- Rollback must be possible for all changes
- No data loss during cleanup

### NFR3: Maintainability
- All scripts must have quick_commands
- All skills must follow SKILL.md format
- All plans must follow .hermes/plans/ format
- Documentation must be updated with changes

### NFR4: Security
- No secrets in output or config.yaml
- .env files must not be committed
- Credential pool strategies must be maintained

## Verification
- Run specs-judge with threshold 98 on all specs in .hermes/specs/
- Run plans-judge with threshold 98 on all plans in .hermes/plans/
- Run prompts-judge with threshold 98 on all prompts in .github/prompts/
- All judge skills must score ≥ 98
- Run hermes doctor and confirm 0 issues
- Run hermes security audit and confirm clean
- Verify all MCP servers pass hermes mcp test
- Confirm git push succeeds on all three branches

## Linked Plan
../plans/comprehensive-hermes-maintenance-plan.md
