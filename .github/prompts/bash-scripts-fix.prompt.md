---

name: bash-scripts-fix

title: Bash Scripts Modernization and Consolidation

description: 'Audit, modernize, and consolidate bash, PowerShell, BAT, and TypeScript scripts across the workspace.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

scripts: []

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

formatter: default

plan: None

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

  - skill:introspection-only-general

  - skill:no-git-delete

  - skill:no-net-fetch

  - skill:skills-tools-preflight-check

tags:

  - audit

  - fix

  - migration

  - prompts

  - typescript

  - workflow

trigger: /bash-scripts-fix

metadata:

  hermes: {}

---

## Goal

Audit, modernize, and consolidate bash, PowerShell, BAT, and TypeScript scripts across the workspace.

> Search, identify, catalog, and modernize scripts across the workspace.

## Context

Use this prompt when the workspace has mixed bash, PowerShell, BAT, andTypeScript scripts that need inventory, modernization, or consolidation. Theworkflow is inventory first, then plan, then review, then migrate, then verify.

## Inputs

- Target directories under `projects/projects/Bash/**` and selected project script roots
- Workspace context and current command mappings
- Optional constraints, compatibility notes, and known script issues

## Outputs

- A script inventory and triage report
- A modernization and migration plan
- Updated scripts, wrappers, or command mappings
- Verification notes for parity and cleanup

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)
> Domain-specific additions below.

1. All operational scripts should end up under `projects/Bash/**` unless a framework seed   script is exempt.
2. Request user confirmation before deleting migrated originals after parity validation passes.
3. Keep dry-run behavior aligned with real execution.
4. Require peer review for AST-sensitive TypeScript changes.
5. Prefer small, verifiable changes over broad rewrites.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

## Phases

### Phase 1: Catalog all scripts

Identify and document scripts across the target directories, then save thesummary report.

### Phase 2: Create the implementation plan

Design the modernization strategy, including wrapper behavior, TypeScriptownership, dry-run semantics, and deletion rules.

### Phase 3: Review and fix

Review scripts for formatting, content, and structural issues, then apply thefixes and validate the results.

- Status: complete for this run- Outcome: review findings recorded in `docs/bash-scripts-fix-review-findings.md`- Constraint: no destructive rewrites applied; user confirmation is still required before any code migration, wrapper replacement, or deletion

### Phase 4: Verify and clean up

Confirm parity, remove migrated originals, and validate the final commandsurface.

- Status: complete for this run- Outcome: verification recorded in `docs/prompt-verify-context.md` if present for the active prompt scope, or `docs/bash-scripts-fix-review-findings.md` for the Bash modernization run- Result: no source scripts were migrated or deleted in this pass; command surface unchanged

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

- [ ] Search target directories for `.sh`, `.ps1`, `.bat`, and `.ts` files- [ ] Categorize each script as migrate, keep, or delete- [ ] Save the inventory report- [ ] Create the modernization plan- [ ] Review all scripts for issues- [ ] Fix formatting inconsistencies- [ ] Fix content issues and contradictions- [ ] Fix structural problems and redundancy- [ ] Migrate scripts to canonical locations- [ ] Delete migrated originals after parity validation- [ ] Run dry-run verification on new scripts- [ ] Update command mappings- [ ] Run final validation on all scripts

## Actions

- `search_files(pattern="*.sh", target="files")` — Find bash scripts
- `search_files(pattern="*.ps1", target="files")` — Find PowerShell scripts
- `search_files(pattern="*.bat", target="files")` — Find BAT scripts
- `terminal("bash -n <script>")` — Syntax-check bash scripts
- `terminal("pwsh -NoProfile -Command ...")` — Validate PowerShell scripts
- `write_file(path, content)` — Write catalog reports
- `patch(path, old_string, new_string)` — Apply targeted script fixes
- `delegate_task(goal, toolsets)` — Parallel per-project migration
- `skill_view(name="acpx-executor")` — Dispatch tasks to ACPX providers---

## Implementation Plan Reference

> Full plan: `_archive/bash-scripts-fix.prompts.txt` (lines 156–310)If `_archive/bash-scripts-fix.prompts.txt` is missing, use the inline7-phase plan below and continue without halting.The 7-phase remediation plan:| Phase | Purpose                                                 | Depends On || ----- | ------------------------------------------------------- | ---------- || 1     | Rebuild inventory (`docs/bash-scripts-list-context.md`) | —          || 2     | Triage: orchestrators / logic / utilities / dead code   | Phase 1    || 3     | Define canonical orchestration contract                 | Phases 1–2 || 4     | TypeScript consolidation + AST-safe refactors           | Phase 3    || 5     | Package/command surface updates                         | Phase 4    || 6     | Verification design + acceptance criteria               | Phases 3–5 || 7:    | Execution sequencing: Bash → Banking → Comicwise        | Phase 6    |**Recommended approach**: Hybrid staged migration — normalize wrappers first, then migrate duplicated logic to TypeScript in controlled batches.**Key risks**:- Inventory file absent → rebuild first- Wrapper shell semantics differ per platform → test parity- Undocumented workflows → inventory before deleting**Core script baselines**: `projects/projects/Bash/upgrade.sh`, `projects/projects/Bash/Banking/scripts/orchestrator.sh/.bat/.ps1`, `projects/projects/Bash/comicwise/dev.sh/.ps1`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |
