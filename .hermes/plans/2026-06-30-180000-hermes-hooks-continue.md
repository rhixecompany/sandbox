# Hermes Hooks Continue Plan

## Goal
Phase-restart: complete hook remediation after the unconfigure/delete/recreate cycle, then fix conflicting skills/memories/soul/user settings.

## Verified Current State
- Plan: `.hermes/plans/2026-06-30-174800-hermes-hooks-discovery-summary.md`
- Summary: `docs/hermes-hooks-summary.md` exists
- Config: `C:\Users\Alexa\AppData\Local\hermes\config.yaml` currently has 4 registered shell hooks under `hooks:`
- Approval: `.hermes/approvals/2026-06-30-hermes-hooks-unconfigure.md` exists

## Open Blocker
- `hermes config set --help` output shows only flat `key value` assignment.
- If hook registration requires a `hermes hooks ...` CLI command, narrow that exact subcommand now so deletion/recreation can proceed safely.

## Remaining Plan
1. Confirm exact Hermes hook command support for unconfigure/delete/create/configure.
2. Apply the unconfigure step using the approved/verified route.
3. Delete old hook scripts/configs.
4. Recreate hooks with best practices from `hermes-hooks` skill.
5. Re-register/reconfigure only the approved hooks.
6. Diff and fix conflicts across skills/memories/soul/user.

Done when summary is complete, hooks are recreated, and all conflicting docs are fixed with verification commands run.
