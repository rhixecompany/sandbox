---
name: hermes-root-scripts-quick-commands-plan
title: "Hermes Root Scripts Quick-Command Implementation Plan"
description: "Implement and verify complete, safe quick-command coverage for Hermes root scripts with scoped profile configuration synchronization."
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, scripts, quick-commands, config, implementation]
status: in_progress
created: 2026-09-04
spec: .hermes/specs/hermes-root-scripts-quick-commands-spec.md
---

# Hermes Root Scripts Quick-Command Implementation Plan

## Objective

Replace the incomplete 7-command registry with deterministic coverage for every first-party script directly under the Hermes scripts root, while making configuration drift and environment scope observable and safe.

## Scope and assumptions

- Immediate Hermes script root only: `.py`, `.sh`, `.bash`, `.ps1`, `.ts`, `.js`.
- `node_modules`, nested directories, snapshots, and backups are excluded.
- A quick command is a safe audit entry point, not permission to execute arbitrary script logic.
- Existing user-defined commands remain unchanged unless their key conflicts with a discovered script; conflicts are reported and preserved.
- Project and Hermes `.env` files are separate scopes. Only names/metadata are compared.

## Phases and tasks

### Phase 1 — Discovery | Day 1 AM | 2 hours

| Task | Deliverable | Owner | Duration |
|---|---|---|---:|
| Read live guidance/state | Startup evidence | Agent | 20m |
| Inventory scripts/config/env paths | Baseline JSON | Agent | 45m |
| Inspect quick-command schema and judge | Compatibility notes | Agent | 35m |
| Capture baseline judge/config results | Baseline report | Agent | 20m |

**Milestone M1:** deterministic inventory and known baseline blockers.

### Phase 2 — Specification and design | Day 1 PM | 2 hours

| Task | Deliverable | Owner | Duration |
|---|---|---|---:|
| Define safe wrapper protocol | Spec FR-001–FR-007 | Agent | 40m |
| Define registry naming/collision rules | Design section | Agent | 25m |
| Define scoped profile/env sync | Risk decision | Agent | 25m |
| Define verification/rollback gates | Plan gates | Agent + User | 30m |

**Milestone M2:** approved spec, plan, and prompt.

### Phase 3 — Implementation | Day 2 AM | 4–6 hours

| Task | Deliverable | Owner | Duration |
|---|---|---|---:|
| Implement registry auditor | `scripts/hermes_quick_commands.py` | Agent | 2h |
| Update implementation orchestrator | `scripts/comprehensive-implementation.py` | Agent | 1h |
| Install/copy tested wrapper to Hermes root | Hermes root script | Agent | 30m |
| Update scripts-judge docs and checker | Skill + judge changes | Agent | 1–2h |

**Milestone M3:** local registry generation and smoke tests pass.

### Phase 4 — Live config synchronization | Day 2 PM | 1–2 hours

| Task | Deliverable | Owner | Duration |
|---|---|---|---:|
| Apply canonical block through CLI | Root config readback | Agent | 20m |
| Apply same block to active profiles | Profile readbacks | Agent | 40m |
| Compare only quick-command structures | Sync report | Agent | 20m |

**Milestone M4:** all active profiles have equivalent quick-command blocks.

### Phase 5 — Verification and closure | Day 2 PM | 2 hours

| Task | Deliverable | Owner | Duration |
|---|---|---|---:|
| Run every safe wrapper audit | Smoke-test report | Agent | 30m |
| Run env path/key-name inventory | Scope report | Agent | 20m |
| Run scripts-judge registry gate | Judge report | Agent | 30m |
| Run repo gates and update evidence | Final report | Agent | 40m |

**Milestone M5:** all acceptance criteria verified; plan marked complete only with evidence.

## Timeline

| Day | Gate | Exit criteria |
|---|---|---|
| Day 1 AM | G1 discovery | Inventory and baseline captured |
| Day 1 PM | G2 design | Spec/prompt/plan agree on safe scope |
| Day 2 AM | G3 implementation | Local wrapper, generator, and tests pass |
| Day 2 PM | G4 configuration | Root + active profiles agree structurally |
| Day 2 EOD | G5 closure | Judge, env audit, and repo gates pass |

## Resource allocation

| Resource | Allocation | Use |
|---|---:|---|
| Primary agent | 8–12h | Discovery, implementation, config, verification |
| Read-only review subagents | 2 × 30m | Schema/design and risk review |
| Hermes CLI | 1 active profile + 14 config targets | Supported config writes/readbacks |
| MCP filesystem | As available | Inventory and scoped file operations |
| MCP AST-grep | As available | Entry-point/schema discovery |
| Sequential-thinking MCP | As available | Decision trace; native fallback if unavailable |
| CI/tooling | 1 verification run | lint, typecheck, check, format |

## Verification gates

- **G1:** script/config/env inventory has explicit inclusion and exclusion rules.
- **G2:** spec has testable criteria and rejects secret copying.
- **G3:** wrapper generation and all local smoke tests pass.
- **G4:** `hermes config get quick_commands --json` readback is structurally equivalent for root and active profiles.
- **G5:** scripts-judge registry coverage, env audit, and repo gates pass.

## Rollback

1. Stop on the first failed gate.
2. Restore the prior quick-command map from the captured in-memory/readback artifact using `hermes config set --force quick_commands ...`.
3. Do not restore or copy `.env` values; no environment mutation is part of this plan.
4. Re-run config readback and `hermes config check`.

## Status log

- [x] Startup audit and memory validation completed.
- [x] Baseline quick-command and scripts-judge gaps captured.
- [x] Prompt and specification created.
- [ ] Registry auditor implementation.
- [ ] Live config synchronization.
- [ ] Scripts-judge update.
- [ ] Final verification.
