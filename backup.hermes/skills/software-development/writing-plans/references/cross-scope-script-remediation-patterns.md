# Cross-scope Script Remediation Plan Patterns

Condensed lessons from a phased remediation-planning session spanning Bash, Banking, and Comicwise script trees.

## What worked

- Start with a prerequisite inventory artifact before finalizing the plan.
- Keep the plan itself focused on planning content and explicitly identified remediation targets.
- Use a phase-gated structure where each phase has:
  - a short purpose statement
  - concrete completion criteria
  - outputs that feed the next phase
- Add an execution checklist early so later implementation batches stay bounded.
- Make wrapper/runner contract decisions before package-script cleanup.
- Delay wrapper deletion until dry-run and normal-mode parity is verified.
- Define verification by script family and file type, not a single generic test command.

## Phase order pattern

1. Inventory / prerequisite artifact
2. Triage and classify candidates
3. Canonical wrapper contract
4. TypeScript consolidation / AST-safe refactors
5. Package and command-surface cleanup
6. Verification matrix and acceptance criteria
7. Rollout sequencing and regression checkpoints

## Pitfalls to avoid

- Mixing implementation details into the plan beyond explicitly identified remediation targets.
- Letting package/command cleanup happen before the canonical runner contract is clear.
- Writing verification only at a high level without mapping it to each script family.
- Deleting compatibility wrappers before parity is demonstrated.
- Forgetting to mirror phase status in the plan when the workstream advances.
