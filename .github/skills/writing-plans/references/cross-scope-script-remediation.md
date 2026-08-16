# Cross-Scope Script Remediation Notes

This reference captures workspace-specific lessons from cross-scope Bash/Banking/Comicwise remediation planning.

## Planning order that worked

1. Create or validate the inventory/context artifact first.
2. Write or update the plan file in `docs/plans/` using the `[purpose]-[component]-[version].md` naming pattern.
3. Keep the plan scoped to planning content and explicitly identified remediation targets.
4. Define the wrapper contract before planning TypeScript consolidation.
5. Add package/command updates only after the consolidation path is clear.
6. Finish with verification criteria and rollout sequencing.

## Useful constraints to carry forward

- Prefer wrapper-thin / TypeScript-core architecture when a repo already has a stable TS runner pattern.
- Keep shell, PowerShell, and BAT wrappers focused on orchestration, argument forwarding, and exit-code propagation.
- Treat dry-run as a first-class behavioral contract, not an optional note.
- Use AST-safe refactors (`ts-morph`) when the plan implies structural TypeScript edits.
- Keep remediation batches bounded; in this workspace, a max of 7 modified files per batch was used as the planning guardrail.

## Common plan sections for this class of work

- Introduction
- Requirements & Constraints
- Implementation Steps
- Alternatives
- Dependencies
- Files
- Testing
- Risks & Assumptions
- Related Specifications / Further Reading

## Reminder

For workspace implementation plans, mention the prerequisite inventory/report artifact explicitly so later phases do not start from a missing baseline.
