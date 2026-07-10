# Approval: Unconfigure Hermes Hooks (Renewed)

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

- Use the supported Hermes config/edit path for hook registration changes.
- Do not modify unrelated config keys.
- Do not delete hook source files in this phase.

## Verification

- Run `hermes hooks list` after unconfigure.
- Confirm the hook registrations are no longer listed.
- Confirm the approval record exists.

## Approval

- Approved by: user via conversation renewal on 2026-07-09
