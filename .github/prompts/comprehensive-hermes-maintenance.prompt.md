---
name: comprehensive-hermes-maintenance
title: Comprehensive Hermes Maintenance
description: "Use when maintaining the Hermes workspace, root scripts, MCP clients, hooks, plugins, agents, configs, Docker, and release state."
trigger: /comprehensive-hermes-maintenance
version: 2.0.0
author: Alexa
status: active
profile: code-architect
priority: high
skills:
  - using-superpowers
  - brainstorming
  - user-communication-preferences
  - mcp-sequential-thinking
  - mcp-filesystem
  - mcp-ast-grep
  - mcp-memory
  - plans-and-specs
  - create-implementation-plan
  - implementation-plan
  - executing-plans
  - writing-clearly-and-concisely
  - subagent-driven-development
  - systematic-debugging
  - scripts-judge
  - hermes-agent
---

# Comprehensive Hermes Maintenance

## Mission

Bring the SandBox workspace and the Hermes installation to a verified, reproducible state. The run covers planning artifacts, root-script quick commands, secret-safe configuration inventory, MCP-client parity, Hermes desktop assets, hooks, agents, Docker resources, duplicate artifacts, and safe Git release.

The workflow is sequential. A phase cannot start until its entry state is captured and its exit gate passes.

## Approved operating boundary

- Workspace: `C:/Users/Alexa/Desktop/SandBox`.
- Hermes home: `C:/Users/Alexa/AppData/Local/hermes`.
- Nested repositories are audited independently.
- Preserve Hermes, OpenCode, Copilot, and Codex. Remove only orphaned, duplicate, disabled, or unconfigured agent assets after reference checks.
- Preserve active or referenced Docker/model/MCP resources. Delete only resources that are both provably unused and present in an explicit allowlist generated from a dry-run.
- Compare `.env*` files by path, class, metadata, and variable names only. Never print, copy, hash, stage, or commit values.
- Modify live Hermes configuration only through `hermes config set` and verify with readback. Do not replace `config.yaml` wholesale.
- Never force-push, bypass hooks, guess credentials, or retry authentication failures indefinitely.

## Required phase order

### M0 — Baseline and inventory | 30–45 minutes

1. Read `SESSION_REPORT.md`, repo guidance, the linked spec, and the linked plan.
2. Select the `code-architect` profile for implementation/debugging work; record actual profile/model.
3. Inventory root and nested Git repositories, Hermes profiles, scripts, `.env*` paths, `config.yaml` paths, MCP clients, hooks, plugins, desktop assets, agents, Docker, and current processes.
4. Capture branch/HEAD/status for every repository and preserve the baseline in `.hermes/reports/` or the Hermes cache.

Gate: inventory is deterministic, path-scoped, and contains no secret values.

### M1 — Design and approval | 45–90 minutes

1. Review at least three approaches:
   - direct command generation;
   - wrapper-based audit projection;
   - per-platform native command registration.
2. Choose the wrapper projection because it avoids running destructive target scripts and gives one testable contract.
3. Update the prompt, spec, master plan, and scripts-judge policy.
4. Record the owner approval and rollback commands in `.hermes/approvals/`.

Gate: requirements, outputs, ownership, timeline, resource allocation, rollback, and acceptance tests agree.

### M2 — Configuration and environment audit | 45–90 minutes

1. Locate every `.env*` and `config.yaml` under the approved roots, excluding Git internals, caches, vendored dependencies, bytecode, and virtual environments.
2. Record file class, size, timestamps, key names, top-level YAML paths, and secret-presence flags only.
3. Compare configuration schemas across Hermes profiles and workspace clients.
4. Treat `.mcp/registry.json` as the workspace MCP source; translate to OpenCode, Copilot, Codex, and VS Code schemas. Treat the Hermes MCP store as a separately managed source.
5. Synchronize only the managed `quick_commands` projection through the Hermes CLI. Preserve provider, model, hook, plugin, channel, and profile-specific settings.

Gate: all reports are secret-safe, parsable, and any schema drift has an explicit classification.

### M3 — Hermes root scripts and quick commands | 60–120 minutes

1. Discover supported regular files directly under the Hermes scripts root: `.py`, `.sh`, `.bash`, `.ps1`, `.ts`, and `.js`.
2. Exclude nested directories, `node_modules`, bytecode, caches, snapshots, backups, and non-script data files.
3. Generate exactly one command per discovered script. Every generated command must invoke the safe wrapper in `audit` mode and target a stable filename or validated inventory index.
4. Preserve non-generated user commands and resolve key collisions deterministically.
5. Read back `quick_commands` from every selected profile and compare counts, target names, command type, wrapper path, and audit arguments.
6. Smoke-test every generated command through the wrapper without executing target business logic.
7. Run the canonical scripts judge with the quick-command gate enabled.

Gate: no missing, stale, duplicate, malformed, out-of-root, untested, or non-wrapper generated entries.

### M4 — Hermes surface remediation | 90–180 minutes

1. Run Hermes diagnostics for hooks, plugins, desktop assets, scripts, agents, session start/end capture, context files, and system prompts.
2. Classify each finding as confirmed, suspected, expected-disabled, credential-blocked, external dependency, or not reproducible.
3. Debug one root cause at a time. Reproduce first, trace the data flow, write a regression check, apply the smallest fix, and rerun the focused check.
4. Keep hook allowlist changes approval-gated. Synthetic hook tests must be isolated and must not leave fake session artifacts.
5. Verify startup and end capture contain session ID, profile, model, cwd, Git baseline, changelog, and error state where available.

Gate: each confirmed defect is fixed with evidence or recorded as an external blocker; optional integrations are not enabled just to suppress warnings.

### M5 — MCP repair and synchronization | 60–120 minutes

1. Validate the source registry and all platform translations structurally.
2. Repair path/schema defects in sync scripts before synchronizing files.
3. Probe remote MCP servers with JSON-RPC `initialize` POST where the endpoint supports it; do not treat a HEAD-only failure as proof of a dead server.
4. Test local commands with safe help/version probes and classify missing optional dependencies separately from broken configuration.
5. Keep dead endpoints disabled with an audit note; do not erase their history without an exact, unreferenced duplicate decision.
6. Confirm at least three live MCP tool calls in the current Hermes session and record server-specific results.

Gate: enabled sets and translations are consistent, known live servers are not false-positive failures, and every remaining failure has evidence.

### M6 — Dedupe and cleanup | 30–90 minutes

1. Hash exact candidate files only after excluding secrets, caches, virtual environments, runtime logs, and referenced source files.
2. Build a reference-aware allowlist. Keep one canonical path; update references before removing a duplicate.
3. Inventory Docker images, containers, build cache, volumes, networks, local models, and MCP toolkit resources.
4. Apply deletion only for explicit allowlisted resources that are inactive, unreferenced, and not ambiguous. Verify `docker system df` and targeted listings afterward.
5. Do not remove the four preserved agent platforms or any resource referenced by their active configuration.

Gate: every deletion has a before/after record, reason, canonical replacement or usage proof, and post-change readback.

### M7 — Release | 15–45 minutes plus network time

1. Run targeted tests and repository quality gates on the files actually changed.
2. Scan the staged set for `.env`, private keys, tokens, credential-bearing config, caches, virtual environments, and runtime continuations.
3. Review the final diff and generate a human Conventional Commit message.
4. Commit one logical change per eligible repository. Do not use blind `git add -A` when it would stage unrelated or secret files.
5. Push existing `clean-development`, `development`, and `production` branches only when the remote is fast-forwardable. Use non-forced pushes and bounded retries for transient failures.

Gate: commit IDs and remote branch readback prove the release; auth, permissions, or non-fast-forward errors remain explicit blockers.

### M8 — Final verification and handoff | 30–60 minutes

1. Rerun the focused inventory, config, quick-command, MCP, Hermes-surface, Docker, and Git checks.
2. Update `SESSION_REPORT.md` from actual state, including every file changed in this run.
3. Mark each plan/spec requirement from evidence, not intention.
4. Report completed work, preserved resources, deletions, commits, pushes, and blockers.

Gate: every acceptance criterion is PASS or has a precise blocker with command, path, exit code, and recovery path.

## Resource allocation

- Primary implementation agent: orchestration, shared-config writes, release review.
- Up to three read-only subagents: independent inventory/risk review for scripts, Hermes surface, and MCP/cleanup.
- One sequential code stream: helper scripts and regression tests.
- One sequential operations stream: hooks, profiles, Docker, and Git readback.
- Shared config files have one writer at a time; reviewers never mutate them.
- Network calls use the existing environment only. No credential provisioning is assumed.

## Failure policy

- Stop at a failed gate and capture command, path, exit code, and relevant stderr.
- After two failures on one route, choose a different verified route; never repeat blindly.
- Authentication, permissions, missing binaries, non-fast-forward pushes, and locked Windows files are external blockers unless evidence proves a local fix.
- Never claim success from a tool return code alone; read back the target state.

## Required deliverables

- `.github/prompts/comprehensive-hermes-maintenance.prompt.md`
- `.hermes/specs/comprehensive-hermes-maintenance-spec.md`
- `.hermes/plans/comprehensive-hermes-maintenance-plan.md`
- `.hermes/approvals/2026-09-05-comprehensive-hermes-maintenance.md`
- Secret-safe inventory, validation, cleanup, and release reports under `.hermes/reports/`
- Updated Hermes workspace scripts and installed maintenance/QA skills

## Output contract

Return a compact evidence table with:

- scope and baseline;
- files and skills changed;
- script/quick-command counts and smoke results;
- config/env parity findings without values;
- Hermes/MCP/plugin/hook/agent results;
- Docker/agent cleanup results;
- tests, commit IDs, push readback;
- unresolved blockers and exact recovery steps.
