---
name: comprehensive-hermes-maintenance-plan
title: "Comprehensive Hermes Maintenance Implementation Plan"
description: "Inventory, remediate, synchronize, deduplicate, clean, and release the SandBox and Hermes installation with explicit safety gates."
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, maintenance, implementation, remediation, cleanup, docker, release]
status: awaiting_owner_decisions
created: 2026-09-05
spec: .hermes/specs/comprehensive-hermes-maintenance-spec.md
---

# Comprehensive Hermes Maintenance Implementation Plan

## Executive decision

Use a **safe projection + evidence-first maintenance pipeline**:

1. Inventory and classify before changing anything.
2. Generate quick commands from the Hermes root script inventory, but execute only the wrapper's audit mode.
3. Synchronize only the managed configuration projection through the Hermes CLI.
4. Treat hooks, credentials, Docker resources, file deletion, and Git release as approval-gated operations.
5. Verify every phase from live state, not from prior report headers.

This replaces the narrower quick-command plan once the owner approves the scope and destructive-change decisions. The existing quick-command artifacts remain reference inputs until consolidation is verified.

## Current evidence baseline

Captured during discovery on 2026-09-05:

- Workspace: `C:/Users/Alexa/Desktop/SandBox`; current branch `clean-development`; working tree has 37 entries.
- Hermes source repository: `C:/Users/Alexa/AppData/Local/hermes/hermes-agent`; branch `main`; working tree has 2 entries.
- Other discovered nested repositories: project directories are mostly on `development`; `rhixecompany-comics` has 8 dirty entries; the remaining checked project repositories were clean at inventory time.
- Hermes root scripts: 220 supported files directly under `C:/Users/Alexa/AppData/Local/hermes/scripts`.
- Live quick-command readback: 227 commands; validator found no issues; wrapper smoke tested 220 generated targets with zero failures.
- Hooks: 8 configured entries; scripts exist and are executable, but the current doctor reports all 8 as not allowlisted because the live command form and allowlist records are out of sync.
- Plugins: 15 bundled/plugin directories plus user/git-sourced entries are installed; enabled, disabled, and not-enabled states must remain distinct.
- Docker: 3 images, 0 containers, 0 local volumes, and 0 build-cache bytes; all reported image bytes are reclaimable, but MCP-toolkit ownership still needs an owner decision.
- Hermes doctor: core checks passed with warnings for portal authentication, an xAI authorization failure, missing optional tool dependencies, and one web-workspace vulnerability.
- Hermes verification: failed because 40 workspace files fail the current Prettier check; this is a separate repository-gate remediation item, not a reason to rewrite live Hermes configuration blindly.
- A live Hermes config contains credential-bearing material; no secret values are copied into reports, synchronized, or committed.

## Clarifications and approval gates

The five owner answers requested at session start control the following:

| Decision | Blocks |
|---|---|
| Modification scope | file edits outside the two approved roots and nested repositories |
| Config/env policy | profile synchronization and any environment-file action |
| Docker cleanup boundary | deletion of images, build cache, containers, volumes, models, or MCP toolkit data |
| Git policy | commits, branch creation, and pushes |
| `scripts-judge` scope | installed canonical skill edit versus every duplicate |

Before any destructive phase, create `.hermes/approvals/<timestamp>-comprehensive-hermes-maintenance.md` with scope, rollback, verification, and an explicit owner `+1`. No approval means inventory/report-only for that phase.

## Phases, milestones, and timeline

Estimates assume one primary agent, three read-only review streams, and no credential or network provisioning delay. They are elapsed engineering estimates, not calendar promises.

### Phase 0 — Live baseline and safety snapshot | 45–75 minutes

| Task | Owner | Output | Gate |
|---|---|---|---|
| Re-read guidance, report, profile, and current Git state | Primary | baseline manifest | no secret values emitted |
| Inventory MCP, hooks, plugins, desktop, agents, scripts, configs, env paths | Primary + reviewer | inventory JSON/MD | scope rules recorded |
| Capture live quick-command readback and Docker dry-run | Primary | baseline reports | no mutation |
| Scan current modifications and ignored secret paths | Primary | release risk list | no `.env` staged |

**M1 exit:** deterministic inventory exists and blockers are classified.

### Phase 1 — Design and owner review | 45–90 minutes

| Task | Owner | Output | Gate |
|---|---|---|---|
| Finalize prompt/spec/plan against discovered facts | Primary | four plan artifacts | spec criteria are testable |
| Review three implementation options and choose wrapper projection | Primary + reviewer | decision record | direct-target execution rejected |
| Create destructive approval request | Primary | approval file | owner `+1` required before apply |

**M2 exit:** plan/spec/prompt agree on scope; destructive actions remain paused until approved.

### Phase 2 — Safe implementation | 2–4 hours

| Task | Owner | Output | Gate |
|---|---|---|---|
| Harden workspace and installed quick-command helpers | Code stream | tested scripts | Python/Bash syntax passes |
| Add inventory/dedupe/Docker dry-run orchestration | Ops stream | reusable scripts | default is read-only |
| Patch canonical `scripts-judge` coverage gate | QA stream | skill + judge update | judge accepts live registry input |
| Create/update maintenance skill | Primary | installed skill and references | validator passes |

**M3 exit:** local tests and safe reports pass; no live config or deletion yet.

### Phase 3 — Config and asset remediation | 2–5 hours

| Task | Owner | Output | Gate |
|---|---|---|---|
| Apply managed quick-command projection via Hermes CLI | Primary | readback report | structural parity, unrelated config unchanged |
| Repair hook allowlist only if approved | Admin stream | allowlist/readback report | `hermes hooks doctor` issue count drops |
| Fix confirmed plugin/desktop/agent defects one class at a time | Code stream | regression evidence | no optional integrations enabled to hide warnings |
| Classify external blockers | Primary | blocker register | auth/dependency issues remain explicit |

**M4 exit:** all applied changes have a live readback and regression check.

### Phase 4 — Dedupe and approved Docker cleanup | 1–3 hours

| Task | Owner | Output | Gate |
|---|---|---|---|
| Hash and reference-check report artifacts/config copies | Primary | dedupe manifest | only exact, unreferenced duplicates eligible |
| Consolidate reports and remove approved duplicates | Primary | canonical report set | before/after manifest verifies references |
| Generate Docker allowlist from dry-run | Admin stream | deletion manifest | explicit owner approval |
| Delete approved unused resources | Admin stream | Docker post-check | no ambiguous MCP/model resource removed |

**M5 exit:** storage cleanup is verified; preserved resources are listed.

### Phase 5 — Repository gates and release | 1–3 hours

| Task | Owner | Output | Gate |
|---|---|---|---|
| Run root lint/typecheck/check/format and targeted tests | QA stream | gate report | failures fixed or recorded |
| Run relevant tests in changed nested repositories | Repo owners | per-repo report | no unrelated repo changes |
| Secret scan staged set; inspect diff | Primary | release checklist | no env/credential files staged |
| Commit once per changed repository and push existing branches | Release owner | commit/push readback | non-force, fast-forward only |

**M6 exit:** release is backed by command output and branch readback.

### Phase 6 — Handoff and durable evidence | 30–60 minutes

- Mark plan/spec status from actual evidence.
- Update `SESSION_REPORT.md` with the exact changelog and unresolved blockers.
- Record final paths, counts, tests, Docker result, and push result.
- Do not mark `completed` while any acceptance criterion is only inferred.

## Work allocation

| Resource | Allocation | Responsibility |
|---|---:|---|
| Primary agent | 8–14 hours | orchestration, implementation, config projection, verification |
| Read-only inventory subagents | 3 × 30–60 minutes | independent inventory and risk review |
| Code/QA stream | 2–4 hours | helper, judge, regression checks |
| Admin/ops stream | 1–3 hours | hooks, Docker, release preflight |
| Hermes CLI/MCP | on demand | supported config, filesystem, AST, diagnostics |
| Docker engine | one read-only + one approved apply pass | resource cleanup |
| Git remotes | one status/readback pass per changed repo | release only |

## Implementation files

### Existing files to update

- `.github/prompts/comprehensive-hermes-maintenance.prompt.md`
- `scripts/comprehensive-implementation.py`
- `scripts/hermes_quick_commands.py`
- `scripts/apply_quick_commands.py`
- Installed canonical `scripts-judge/SKILL.md` and `scripts/judge.py` (via `skill_manage`)

### New files

- `.hermes/specs/comprehensive-hermes-maintenance-spec.md`
- `.hermes/plans/comprehensive-hermes-maintenance-plan.md`
- `scripts/hermes_maintenance.py`
- `scripts/docker_cleanup.py`
- Installed `hermes-comprehensive-maintenance/SKILL.md` plus substantive references/templates as needed

### Evidence files

Reports belong under `.hermes/reports/` only when they are deterministic, secret-safe, useful for release review, and not duplicate snapshots. Runtime-only inventories belong under the Hermes cache and are not committed.

## Verification commands

```text
python scripts/hermes_maintenance.py inventory --repo C:/Users/Alexa/Desktop/SandBox --hermes-home C:/Users/Alexa/AppData/Local/hermes
python scripts/hermes_maintenance.py dedupe-report --repo C:/Users/Alexa/Desktop/SandBox
python scripts/docker_cleanup.py inventory
python C:/Users/Alexa/AppData/Local/hermes/scripts/hermes_quick_commands.py verify-registry --registry <readback-json> --wrapper C:/Users/Alexa/AppData/Local/hermes/scripts/hq.py
python C:/Users/Alexa/AppData/Local/hermes/scripts/hermes_quick_commands.py smoke --registry <readback-json>
python C:/Users/Alexa/AppData/Local/hermes/skills/qa/scripts-judge/scripts/judge.py --scripts-dir C:/Users/Alexa/AppData/Local/hermes/scripts --quick-commands-json <readback-json>
hermes config check
hermes hooks doctor
hermes plugins list --plain --no-bundled
bun run lint
bun run typecheck
bun run check
bun run format
```

Target scripts are never executed by the quick-command smoke gate. `bun run format` is a mutation and must be run only as a separately reviewed remediation step.

## Failure handling

- Failed phase gate: stop, capture command/path/exit code, and return to root-cause investigation.
- Two failures on the same route: choose an alternative route; do not repeat the same command blindly.
- Missing credential or protected remote: classify as external blocker; do not fabricate success.
- Ambiguous duplicate or resource: preserve it and add a review item.
- Non-fast-forward push: stop; do not force-push.

## Completion checklist

- [ ] Owner clarification decisions recorded.
- [ ] Prompt/spec/plan/skill/scripts validated.
- [ ] Inventory and blocker register current.
- [ ] Quick-command coverage/readback/smoke/judge gates pass.
- [ ] Config scope limited to managed projection.
- [ ] Environment values never exposed or synchronized.
- [ ] Confirmed Hermes issues fixed or explicitly blocked.
- [ ] Dedupe decisions backed by hashes and references.
- [ ] Docker cleanup approved and verified, or explicitly left as dry-run.
- [ ] Repository tests and secret scan pass.
- [ ] Commits and non-forced pushes verified.
- [ ] Session report and final evidence updated.
