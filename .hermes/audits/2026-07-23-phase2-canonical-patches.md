# Phase 2 — Canonical Path Normalization Audit

Date: 2026-07-23
Scope: `.github/prompts/agents/*.agent.md` and `.github/prompts/instructions/*.instructions.md`

## Summary

No stale references to legacy `.github/agents/` or `.github/instructions/` were found inside the canonical prompt files. Zero files required changes.

## Findings

- **Canonical agents clean:** Scanned all `*.agent.md` files under `.github/prompts/agents/`. No occurrences of legacy paths.
- **Canonical instructions clean:** Scanned all `*.instructions.md` files under `.github/prompts/instructions/`. No occurrences of legacy paths.

## Outside Scope / Context Only

Legacy path references still exist in non-canonical locations and were intentionally left untouched per task scope:

- `.github/prompts/index.md` — documentation note forbidding legacy paths.
- `.hermes/plans/*` and other `.hermes/archived-*` files — historical plan/docs references.

## Changed Files

_None._
