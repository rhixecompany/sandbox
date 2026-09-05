# Audit Skills Judge Fix — Phases

> Full operational phases for `prompts/audit-skills-judge-fix.prompt.md`.

## Phase 1: Skills Audit & Inventory

- Inventory all skills under `C:\Users\Alexa\AppData\Local\hermes\skills`.
- Gate: inventory artifacts exist and paths are valid.

## Phase 2: Categorize Skills

- Categorize skills from the inventory.
- Gate: 0 empty categories; mapping saved.

## Phase 3: Deduplicate & Consolidate

- Identify duplicates and consolidate mappings.
- Gate: duplicates resolved and report written.

## Phase 4: Judge Skills

- Judge all skills against quality criteria.
- Gate: all skills scored and results written.

## Phase 5: Remediate Skills

- Apply remediation to failing/weak skills.
- Gate: no skill remains below 80.

## Phase 6: Consolidate Umbrella Skills

- Merge umbrella skill content where appropriate.
- Gate: consolidation report written.

## Phase 7: Final Verification

- Final cross-check of all prior phase artifacts.
- Gate: final report shows pass with zero unresolved issues.

## Completion

- Append progress after each phase.
- Append evidence to `docs/orchestrator-verification.md` after each phase.
