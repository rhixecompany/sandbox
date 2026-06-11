---
name: simplify-codemap
description: "src/skills/simplify/"
version: 1.0.0
author: Alexa
---
     1|# src/skills/simplify/
     2|
     3|## Responsibility
     4|
     5|- Provide a behavior-preserving refactoring skill contract that constrains code cleanup to clarity-focused, low-risk changes.
     6|- Define explicit quality gates (understand-before-edit, behavior parity, incremental simplification, rollback-friendly diffs) for any simplification task.
     7|- Ship only metadata; no local runtime state machine is kept in this directory.
     8|
     9|## Design
    10|
    11|- Contract layer: `SKILL.md` is the executable prompt specification with explicit phases:
    12|  - pre-change understanding
    13|  - simplification candidate selection
    14|  - incremental transformation and verification
    15|  - final review checklist.
    16|- Documentation layer: `README.md` explains intent, source provenance, and plugin install behavior.
    17|- Policy model is declarative (`description`, allowed usage, checklist) consumed by the OpenCode skill executor, without helper scripts or plugin code dependencies.
    18|
    19|## Flow
    20|
    21|- Agent discovery resolves `src/skills/simplify` as a custom skill entrypoint, then reads `SKILL.md` at runtime.
    22|- Runtime behavior is gated by `src/cli/custom-skills.ts` (`allowedAgents: ['oracle']`) and by skill permissions computed in `getSkillPermissionsForAgent()`.
    23|- In practice the workflow is read-only and context-driven: simplify instructions require understanding of callers, edge cases, and tests before mutation, then apply local, scoped refactors with validation.
    24|- Consumers (Fixer/Oracle/Reviewer tasks) rely on this contract as operational constraints, not as executable TypeScript.
    25|
    26|## Integration
    27|
    28|- Installed by plugin installer (`installCustomSkills`) using `src/cli/install.ts` via `installCustomSkill()`.
    29|- Permission surface is enforced by hook layer in `src/hooks/filter-available-skills/index.ts` (`permissionRules`).
    30|- Release integrity: `scripts/verify-release-artifact.ts` checks for `src/skills/simplify/SKILL.md` in package tarballs.
    31|- Operationally paired with codemap/fixer flows in `src/index.ts` orchestrations for post-feature readability hardening.
    32|