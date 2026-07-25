# Implementation Plan Contract (Workspace Notes)

This reference condenses the plan-update contract used in this workspace.

## Required behaviors

- If a user asks to create or update an implementation plan, check whether prerequisite discovery or inventory artifacts are missing first.
- If a prerequisite artifact is missing, create/update it before finalizing the plan.
- When the target plan file does not exist, create it under `docs/plans/` using the naming convention `[purpose]-[component]-[version].md`.
- Use `plan status: planned` unless the user explicitly asks for a different state.
- Keep the plan scoped to plan content and explicitly identified remediation targets; do not expand into unrelated implementation.

## Required section names

Use these sections in the final plan:

1. Introduction
2. Requirements & Constraints
3. Implementation Steps
4. Alternatives
5. Dependencies
6. Files
7. Testing
8. Risks & Assumptions
9. Related Specifications / Further Reading

## Badge format

- Status badge template: `https://img.shields.io/badge/status-<url_encoded_status>-<color>`
- Status-to-color mapping:
  - Completed → brightgreen
  - In progress → yellow
  - Planned → blue
  - Deprecated → red
  - On Hold → orange

## Practical reminder

For cross-scope script-remediation plans, lead with the inventory/report artifact, then define the wrapper contract, TypeScript consolidation path, package surface updates, and verification matrix.
