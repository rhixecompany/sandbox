# Description

> Extracted from `projects-init.prompt.md`.

## Description

This prompt initialises a new or stale workspace by running a three-phase cleanup and consolidation pipeline. Phase 1 discovers and deduplicates all markdown documentation files. Phase 2 discovers prompt files, migrates them to `.github/prompts/`, and consolidates. Phase 3 indexes the new prompt directory, creates any needed skills and helper scripts, and updates all prompts to reference the skills they need.

**Critical rules (must appear within the first 15% of execution):**

- **Only then constraint** — Each phase completes fully before the next begins. No overlapping phases.
- **Delete only after verification** — Before deleting any file, confirm the canonical copy exists in the target location.
- **Count before and after** — Record file counts at each phase start and end; report deltas.
