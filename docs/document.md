# Document Pipeline

This file describes the docs pipeline for this workspace.

## What it covers

- Scope files at `docs/scope/`
- Specs at `docs/specs/`
- Plans at `.hermes/plans/`
- Audit reports at `docs/specs/` or `.hermes/plans/`
- Project docs at `docs/project-docs/`

## Pipeline order

| Phase | Command | Output |
|---|---|---|
| 1 | `/scope` | `docs/scope/*.md` |
| 2 | `/architect` | `docs/specs/*.md` |
| 3 | `/audit` | `docs/specs/*-audit.md` |
| 4 | `/develop` | `docs/*.md` + `docs/project-docs/` |
| 5 | `/document` | `docs/document.md` (this file) |

## Verification checklist

- [ ] Scope file exists and has At a glance table
- [ ] Architect spec exists with build plan
- [ ] Audit evidence uses real exit codes/file sizes
- [ ] `.env` untouched; no secrets exposed
- [ ] 0 synthetic session IDs, capabilities, rankings, artifacts
