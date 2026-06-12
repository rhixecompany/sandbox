# Bash Scripts Modernization and Consolidation

Generated: 2026-06-12
Prompt: `Prompts/bash-scripts-fix.prompts.md`
Inputs: `docs/bash-scripts-list-context.md`, live `Bash/` scan

## Goal

Move duplicated script logic into TypeScript where appropriate, keep shell wrappers thin, and avoid deleting anything without explicit confirmation.

## Scope

- Active scripts only.
- Orchestrators `Bash/upgrade.*` and `Bash/orchestrator-unified.*` are keepers.
- Primary wrapper families:
  - `Bash/Banking/scripts/*`
  - `Bash/comicwise/*`
  - `Bash/scripts/*`

## Phases

### Phase A: Banking wrappers

- Target logic/owner mapping for PowerShell/BAT/sh wrappers.
- Identify canonical TS entrypoint for each wrapper.
- Confirm dry-run parity before switching runtime.

### Phase B: Comicwise wrappers

- Same wrapper-contract pass as Banking.
- Restrict edits to documented wrapper surface only.

### Phase C: Root utilities with TS equivalents

- Limit to scripts with TS counterparts under `Bash/src/*`.
- Operator-visible behavior must remain unchanged during migration.

## Verification Checklist

- `bash -n <script>` for bash wrappers
- PowerShell parse validation where applicable
- TypeScript build/syntax check for TS targets
- Dry-run parity validation before any migration or deletion
