---
name: comprehensive-hermes-maintenance-plan
title: Comprehensive Hermes Maintenance Implementation Plan
description: "Execute the approved, evidence-first maintenance of the SandBox workspace and Hermes installation with sequential gates."
version: 2.0.0
author: Alexa
license: MIT
tags: [hermes, maintenance, implementation, mcp, scripts, hooks, plugins, agents, docker, release]
status: in_progress
created: 2026-09-05
updated: 2026-09-05
spec: .hermes/specs/comprehensive-hermes-maintenance-spec.md
prompt: .github/prompts/comprehensive-hermes-maintenance.prompt.md
approval: .hermes/approvals/2026-09-05-comprehensive-hermes-maintenance.md
baseline_head: f67b6bfb6281fc6bf77b3f3e37a47c26ea7233dd
baseline_branch: clean-development
---

# Comprehensive Hermes Maintenance Implementation Plan

## Decision

Use one sequential, evidence-first pipeline with a safe wrapper projection for Hermes root-script quick commands. Do not execute old fragment plans independently. Existing plans remain source material; this file owns the current execution order.

Three approaches were considered:

1. Direct command generation — simple, but it would run arbitrary target scripts and cannot provide a uniform safety contract.
2. Native per-platform registration — accurate for each client, but duplicates logic and causes schema drift.
3. Wrapper-based audit projection — one registry generator, one safe audit contract, platform translation at the edges. This is the selected approach because it is testable, idempotent, and does not execute target business logic.

## Verified starting state

Captured at M0 from live state:

- Workspace: `C:/Users/Alexa/Desktop/SandBox`.
- Baseline branch: `clean-development`.
- Baseline HEAD: `f67b6bfb6281fc6bf77b3f3e37a47c26ea7233dd` (`updates`).
- Baseline working tree: one untracked M0 evidence directory created by this run; no staged changes.
- Hermes home: `C:/Users/Alexa/AppData/Local/hermes`.
- Profiles: 14 listed; `code-architect` selected for this implementation pass; `default` gateway was running at inventory time.
- Hermes scripts directory: 237 entries including directories/data; the supported direct-file script count is derived by the generator and excludes nested/cache/vendor/data entries.
- Hermes hooks: directories and hook entry points are present; live `hermes hooks list`/`doctor` output is the source of truth.
- Hermes plugins: installed plugin directories are present; installed/enabled/disabled/unavailable states must remain separate.
- Hermes agents: seven definition files are present; preserve required platform agents and only remove proven orphan/duplicate assets.
- Docker: live inventory was captured read-only; MCP/model/toolkit resources are preserved unless an allowlist proves they are unused.
- Environment/config discovery: paths were located through MCP filesystem search; values are never copied into this plan or reports.
- Prior fragments include `comprehensive-hermes-maintenance-*`, `comprehensive-implementation-*`, the 2026-08-16 MCP plan, the 2026-08-31 plugins/hooks plan, and the 2026-08-24 platform/context plans. Their actionable scope is consolidated here; they are not independent execution targets.

## Milestones and timeline

Estimates are elapsed work time for one primary agent plus up to three read-only review streams. Network/authentication and external dependency failures can extend the schedule.

| Milestone | Phase | Duration | Exit evidence |
|---|---|---:|---|
| M0 | Baseline/inventory | 30–45 min | repository, profile, script, config, env, MCP, Hermes, Docker, and process evidence |
| M1 | Prompt/spec/plan/approval | 45–90 min | validated artifacts and recorded owner approval |
| M2 | Env/config/MCP source audit | 45–90 min | secret-safe inventory and schema-drift report |
| M3 | Quick commands/scripts judge | 60–120 min | registry readback, full wrapper smoke, judge gate |
| M4 | Hermes desktop/hooks/plugins/agents/session assets | 90–180 min | focused diagnostics and regression report |
| M5 | MCP repair/synchronization | 60–120 min | schema parity, live/local probes, runtime tool evidence |
| M6 | Dedupe and cleanup | 30–90 min | reference-aware manifest and Docker post-check |
| M7 | Tests, commit, push | 15–45 min + network | safe staged diff, commit IDs, remote readback |
| M8 | Final verification/handoff | 30–60 min | current report, acceptance matrix, blockers |

## Resource allocation

| Resource | Allocation | Owner | Constraint |
|---|---:|---|---|
| Primary agent | 8–14 hours | controller | sole writer for shared configs and release |
| Read-only inventory agents | up to 3 × 30–60 min | delegated reviewers | no shared mutable writes |
| Code/QA stream | 2–4 hours | implementer + reviewers | spec review before quality review |
| Operations stream | 1–3 hours | admin reviewer | hooks/Docker/Git are approval-gated |
| Hermes CLI/MCP | on demand | controller | use supported interfaces and readback |
| Docker engine | one dry-run + one allowlisted apply | controller | preserve active/reference-required resources |
| Git remotes | one status and one push/readback per eligible repo | release owner | fast-forward, non-forced only |

## Phase execution

### M0 — Baseline and inventory

- Capture live Git status/branches/remotes for root and independently detected subrepositories.
- Capture Hermes profile, MCP, hook, plugin, agent, doctor, process, and Docker state.
- Locate `.env*` and `config.yaml` under the two approved roots through MCP filesystem search.
- Record all baseline output in `.hermes/reports/baseline/` or the Hermes cache without credential values.

Gate: deterministic, secret-safe baseline exists. Completed for this run.

### M1 — Plan and approval

- Update the comprehensive prompt and spec to match the owner-approved scope.
- Update this plan with the live baseline and fragment-consolidation decision.
- Create the approval record with scope, rollback commands, verification, and owner `+1` from the initiating request.
- Load/validate the required skills and use sequential-thinking for phase decisions.

Gate: prompt, spec, plan, and approval agree. Completed after artifact validation.

### M2 — Env/config audit and managed sync design

- Implement a secret-safe inventory for `.env*` and `config.yaml` paths/key names.
- Compare schemas without copying values.
- Validate `.mcp/registry.json`, `opencode.json`, `.github/mcp.json`, `.codex/mcp.json`, and `.vscode/mcp.json`.
- Define Hermes `quick_commands` as the only live Hermes projection managed by this plan.

Gate: parsers pass; no secret values in evidence; intended differences are recorded.

### M3 — Quick-command implementation

- Harden workspace and installed `hermes_quick_commands.py` so generated commands use `python`/the supported interpreter and invoke wrapper audit mode.
- Implement coverage validation, command shape checks, duplicate/stale detection, readback comparison, and full wrapper smoke.
- Update `scripts-judge` SKILL.md, rubric, and judge executable so the Hermes-root gate is mandatory when that root is audited.
- Apply the managed registry through `hermes config set` using the existing CLI helper, then read back each selected profile.

Gate: every supported direct script has one tested wrapper command; judge and profile readback pass.

### M4 — Hermes surface debugging

- Run supported diagnostics for desktop plugins, hooks, scripts, agents, session capture, context files, and system prompts.
- Reproduce each confirmed finding and trace the failing boundary before changing it.
- Apply one focused fix at a time; add/execute a regression check.
- Keep hook allowlist updates behind the recorded approval. Preserve expected-disabled and credential-blocked integrations.

Gate: all confirmed local defects are fixed or precisely blocked; no warning is hidden by enabling optional services.

### M5 — MCP repair and sync

- Fix the known Copilot path and any schema-translation defects in the sync utility.
- Keep dead remote endpoints disabled with reasons; do not delete audit-trail entries without a duplicate/reference decision.
- Replace false-positive HEAD-only validation with JSON-RPC `initialize` POST where supported.
- Test local MCP commands with safe probes and classify missing optional dependencies.
- Synchronize workspace configs one writer at a time; Hermes remains separately managed by its CLI.
- Call at least three currently available MCP tools from this session and record actual results.

Gate: each config parses; enabled-set drift is explicit; live failures have evidence.

### M6 — Dedupe and cleanup

- Produce exact-content hashes and reference scans for candidates.
- Remove only exact, unreferenced, non-secret duplicates after canonical references are updated.
- Generate a Docker/model/MCP/agent allowlist from read-only evidence.
- Apply only allowlisted inactive/unreferenced resources; preserve active and required toolkits.
- Verify post-state and retain the deletion manifest.

Gate: every deletion is reversible where possible and verified; ambiguous resources remain.

### M7 — Release

- Run targeted Python compilation, Bash syntax, JSON/YAML checks, scripts judge, MCP validation, Hermes checks, and relevant root/nested repository tests.
- Secret-scan only the exact staged candidate set.
- Review the diff and stage only verified files. Exclude `.env*`, private keys, tokens, credential-bearing config, caches, virtualenvs, continuation artifacts, and unrelated pre-existing changes.
- Create a human Conventional Commit per eligible repository.
- Push existing `clean-development`, `development`, and `production` branches without force. Retry transient network failures with bounded backoff; stop on authentication, permissions, protected-branch, or non-fast-forward errors.

Gate: commit and remote readback succeed, or an exact blocker is recorded.

### M8 — Final verification

- Re-run inventory and all changed-area gates.
- Update `SESSION_REPORT.md` with actual session ID, profile/model, tools, files, results, and blockers.
- Verify every acceptance criterion in the spec.
- Update this plan status only from evidence.

Gate: no criterion is marked complete from a stale report or an unverified subagent claim.

## File ownership

| Area | Canonical owner |
|---|---|
| Hermes root quick-command registry | `scripts/hermes_quick_commands.py` + Hermes CLI `quick_commands` |
| Workspace MCP source | `.mcp/registry.json` |
| OpenCode translation | `opencode.json` |
| Copilot translation | `.github/mcp.json` |
| Codex translation | `.codex/mcp.json` |
| VS Code translation | `.vscode/mcp.json` |
| Hermes MCP store | `hermes mcp` CLI/internal store; not a workspace-file mirror |
| Environment values | local credential wrappers only; never committed or synchronized |
| Plan/spec/prompt | the three paths declared in frontmatter |

## Rollback and failure handling

- Failed gate: stop, capture command/path/exit code/stderr, then return to root-cause investigation.
- Two failures on one route: change route; do not repeat the same failing command a third time.
- Workspace files: `git restore -- <path>` or `git revert <commit>`.
- Hermes quick commands: restore the captured mapping with `hermes config set`.
- Skill edits: reverse the recorded `skill_manage` patch.
- Hooks: revoke only newly approved allowlist entries if lifecycle checks regress.
- Docker: never assume recovery of deleted volumes/images; preserve ambiguity.
- Git: never force-push or reset another user's work.

## Completion checklist

- [ ] M0 baseline is current and secret-safe.
- [ ] M1 artifacts and approval are validated.
- [ ] M2 env/config inventory and drift report pass.
- [ ] M3 registry/readback/smoke/scripts-judge gates pass.
- [ ] M4 Hermes surface defects are fixed or blocked with evidence.
- [ ] M5 MCP translations and live/runtime checks pass or are classified.
- [ ] M6 dedupe/cleanup changes are allowlisted and verified.
- [ ] M7 tests, safe staging, commits, and pushes are verified.
- [ ] M8 final report and acceptance matrix are current.
