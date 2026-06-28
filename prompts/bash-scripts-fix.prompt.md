---
license: MIT
author: Hermes Agent
version: 1.0.0
name: bash-scripts-fix
title: Bash Scripts Modernization and Consolidation
trigger: /bash-scripts-fix
description:
    Audit, modernize, and consolidate bash, PowerShell, BAT, and TypeScript
    scripts across the workspace.
tags:
  - hermes
  - copilot
  - bash
  - scripts
  - typescript
  - automation
  - refactoring
dependencies:
    - prompt:context-map.prompt.md
    - prompt:update-implementation-plan.prompt.md
    - skill:brainstorming
    - skill:plans-and-specs
    - skill:dispatching-parallel-agents
    - skill:subagent-driven-development
    - skill:systematic-debugging
    - skill:simplify
    - skill:acpx-executor
    - skill:script-orchestration
    - tool:terminal
    - tool:search_files
skills:
    - introspection-only-general
    - no-git-delete
    - no-net-fetch
    - skills-tools-preflight-check
    - brainstorming
    - plans-and-specs
    - dispatching-parallel-agents
    - subagent-driven-development
    - systematic-debugging
    - simplify
    - acpx-executor
    - script-orchestration

---

> Search, identify, catalog, and modernize scripts across the workspace.

## Goal

Centralize script behavior in TypeScript where appropriate, keep shell wrappers
thin, and remove dead code after parity validation.

## Context

Use this prompt when the workspace has mixed bash, PowerShell, BAT, and
TypeScript scripts that need inventory, modernization, or consolidation. The
workflow is inventory first, then plan, then review, then migrate, then verify.

## Inputs

- Target directories under `Bash/**` and selected project script roots
- Workspace context and current command mappings
- Optional constraints, compatibility notes, and known script issues

## Outputs

- A script inventory and triage report
- A modernization and migration plan
- Updated scripts, wrappers, or command mappings
- Verification notes for parity and cleanup

## Rules

> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)
> Domain-specific additions below.

2. All operational scripts should end up under `Bash/**` unless a framework seed
   script is exempt.
4. Request user confirmation before deleting migrated originals after parity validation passes.
5. Keep dry-run behavior aligned with real execution.
6. Require peer review for AST-sensitive TypeScript changes.
7. Prefer small, verifiable changes over broad rewrites.

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#bash-scripts-fix)

## Phases

### Phase 1: Catalog all scripts

Identify and document scripts across the target directories, then save the
summary report.

### Phase 2: Create the implementation plan

Design the modernization strategy, including wrapper behavior, TypeScript
ownership, dry-run semantics, and deletion rules.

### Phase 3: Review and fix

Review scripts for formatting, content, and structural issues, then apply the
fixes and validate the results.

- Status: complete for this run
- Outcome: review findings recorded in `docs/bash-scripts-fix-review-findings.md`
- Constraint: no destructive rewrites applied; user confirmation is still required before any code migration, wrapper replacement, or deletion

### Phase 4: Verify and clean up

Confirm parity, remove migrated originals, and validate the final command
surface.

- Status: complete for this run
- Outcome: verification recorded in `docs/prompt-verify-context.md` if present for the active prompt scope, or `docs/bash-scripts-fix-review-findings.md` for the Bash modernization run
- Result: no source scripts were migrated or deleted in this pass; command surface unchanged

## Steps

1. Inventory all scripts across the target roots.
2. Classify each script as migrate, keep, or delete.
3. Create the implementation plan and update the related plan file.
4. Review scripts for formatting, content, and structural issues.
5. Migrate wrappers and move logic into TypeScript where appropriate.
6. Validate dry-run behavior and parity with the original scripts.
7. Delete migrated originals after validation.
8. Update package command mappings if needed.
9. Run the final syntax and behavior checks.

## Tasks

- [ ] Search target directories for `.sh`, `.ps1`, `.bat`, and `.ts` files
- [ ] Categorize each script as migrate, keep, or delete
- [ ] Save the inventory report
- [ ] Create the modernization plan
- [ ] Review all scripts for issues
- [ ] Fix formatting inconsistencies
- [ ] Fix content issues and contradictions
- [ ] Fix structural problems and redundancy
- [ ] Migrate scripts to canonical locations
- [ ] Delete migrated originals after parity validation
- [ ] Run dry-run verification on new scripts
- [ ] Update command mappings
- [ ] Run final validation on all scripts

## Actions

- `search_files(pattern="*.sh", target="files")` — Find bash scripts
- `search_files(pattern="*.ps1", target="files")` — Find PowerShell scripts
- `search_files(pattern="*.bat", target="files")` — Find BAT scripts
- `terminal("bash -n <script>")` — Syntax-check bash scripts
- `terminal("pwsh -NoProfile -Command ...")` — Validate PowerShell scripts
- `write_file(path, content)` — Write catalog reports
- `patch(path, old_string, new_string)` — Apply targeted script fixes
- `delegate_task(goal, toolsets)` — Parallel per-project migration
- `skill_view(name="acpx-executor")` — Dispatch tasks to ACPX providers

---

## Implementation Plan Reference

> Full plan: `_archive/bash-scripts-fix.prompts.txt` (lines 156–310)

If `_archive/bash-scripts-fix.prompts.txt` is missing, use the inline
7-phase plan below and continue without halting.

The 7-phase remediation plan:

| Phase | Purpose                                                 | Depends On |
| ----- | ------------------------------------------------------- | ---------- |
| 1     | Rebuild inventory (`docs/bash-scripts-list-context.md`) | —          |
| 2     | Triage: orchestrators / logic / utilities / dead code   | Phase 1    |
| 3     | Define canonical orchestration contract                 | Phases 1–2 |
| 4     | TypeScript consolidation + AST-safe refactors           | Phase 3    |
| 5     | Package/command surface updates                         | Phase 4    |
| 6     | Verification design + acceptance criteria               | Phases 3–5 |
| 7:    | Execution sequencing: Bash → Banking → Comicwise        | Phase 6    |

**Recommended approach**: Hybrid staged migration — normalize wrappers first, then migrate duplicated logic to TypeScript in controlled batches.

**Key risks**:

- Inventory file absent → rebuild first
- Wrapper shell semantics differ per platform → test parity
- Undocumented workflows → inventory before deleting

**Core script baselines**: `Bash/upgrade.sh`, `Bash/Banking/scripts/orchestrator.sh/.bat/.ps1`, `Bash/comicwise/dev.sh/.ps1`
