# 0001 · Hermes Hooks Upgrade and Verification

**Status**: Proposed
**Date**: 2026-09-20
**Feature link**: docs/scope/scope.md feature 8 (`Hermes hooks update, repair, and verification`)
**Build approach**: Tracer Bullet (per feature 8 in scope.md)
**Workflow tier**: Beta (`/check verify`, `/test` required)

## Summary

Update, repair, enhance, test, debug, and verify all hermes hooks in `$HERMES_HOME/hooks/` and workspace `.hermes/hooks/` so they work reliably for new sessions and multiple AI agent profiles (hermes, agent, copilot, opencode, default, adminbot, ops). The audit (see `plan/hermes-hooks-2026-09-20.md`) found 17 hook files with real sizes (991 B to 20810 B). No stale references were found in the basic scan, but full `/check` and `/debug` verification is required.

## Requirements (acceptance criteria seeds from scope feature 8)

- AC-1: Every hook category (session, agent, browser, provider, governance, secrets, tool-guardian) passes `/check`.
- AC-2: Any `/check` failure is documented, fixed, and re-verified via `/debug`.
- AC-3: `/test all hermes hooks` confirms working behavior for new sessions.
- AC-4: Multi-agent profiles (default, adminbot, ops, etc.) can use hooks without errors.
- AC-5: Best practices applied: clean syntax, correct paths, permission checks, session state tracking.

## Decision

No new provider or library needed; the build uses existing hook scripts (`lib.py`, `lib.sh`, `capture_common.py`, shell scripts) and improves them. The only design decision is the order: Tracer Bullet slices mean each hook category is verified end to end before the next (audit → repair → enhance → verify → debug → test → complete).

## Implementation skills (relevant community skills from AGENTS.md)

- audit (QA / gap fill)
- architect (spec capture for broken/enhanced hooks)
- develop (build fixes/enhancements)
- check (verification)
- test (confirmation)
- debug (root cause analysis when `/check` fails)
- sync (post-change reconciliation with AGENTS.md)

## Build plan (Tracer Bullet slices)

1. Audit slice (`/audit /hermes-hooks`): full scan of all hook files, read `README.md`, identify broken/stale references, missing permissions.
2. Repair slice (`/architect` + `/develop` for broken hooks): fix syntax errors, update paths, restore references.
3. Enhance slice (`/develop`): add agent identity checks (hermes, agent, copilot, opencode) and new session initialization.
4. Verify slice (`/check all hermes hooks`): confirm each category passes.
5. Debug slice (`/debug all hermes hooks`): investigate failures, apply fixes, re-verify.
6. Test slice (`/test all hermes hooks`): confirm working behavior for new sessions and multi-agent profiles.

## Consequences

- Positive: hooks become reliable for new sessions and multi-agent use.
- Risk: modifying session hooks (`session_start_capture.py`, `session-logger/`) could break session tracking if the fix introduces a new error. Mitigated by `/check` and `/test` gates before calling `done`.

## References

Sources (no web fetch used): workspace `AGENTS.md`, `docs/scope/scope.md`, hook `README.md`, `multi-file-change-protocol` skill (for DRY/protocol rules), `systematic-debugging` skill (for 4-phase root cause fix).

No links group (no web verified links added).

## Build approach note

Tracer Bullet: build and verify each hook category end to end before moving to the next. This aligns with the user's choice (confirmed in scope feature 8).
