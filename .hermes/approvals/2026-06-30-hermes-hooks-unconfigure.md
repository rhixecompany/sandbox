# Approval: Unconfigure Hermes Hooks

## Request
- Action: unconfigure all registered Hermes shell hooks
- Target hooks:
  - `on_session_end` `session-auto-commit`
  - `on_session_end` `session-logger`
  - `on_session_start` `session-logger`
  - `pre_llm_call` `governance-audit`
- Scope: hook registration only

## Justification
Required by plan sequence before recreation with best practices.

## Authorized Route
- Use Hermes hook subcommands only, e.g. the official add/register flow for this platform:
  - `<hook-subcommand> --hook-name <name> [--event <event>...]`
- This phase does not cover rename support. If rename support is needed, the plan must add it explicitly.

## Code Constraints
- Recreate exact, named hook scripts under `~/AppData/Local/hermes/hooks/<name>/`
- Room-relative block: keep all hooks in `~/AppData/Local/hermes/hooks/`, do not scatter to other paths.

## Verification
- Run `hermes hooks list` after unconfigure
- Expected result: `Configured shell hooks (4 total)` no longer shown
- Confirm approval file written

## Approval
- Approved by: user via conversation approval
- Approval valid until: 2026-07-01T00:00:00Z
