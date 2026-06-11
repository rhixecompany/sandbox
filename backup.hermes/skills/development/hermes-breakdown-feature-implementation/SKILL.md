---
name: hermes-breakdown-feature-implementation
title: Hermes Breakdown Feature Implementation
description: "Generate a Feature Implementation Plan (implementation-plan.md) following monorepo conventions. Includes testing and dry-run verification workflows for shell/powershell/bat scripts and TypeScript migration templates."
version: 1.1.0
metadata:
  last_patched: 2026-05-26

author: Alexa
license: MIT
metadata:
  hermes:
    tags: [implementation, development, monorepo, scripts, dry-run]
    related_skills: [hermes-breakdown-plan]
---

# Hermes: Breakdown Feature Implementation

## When to Use

- When working with skills\development\hermes breakdown feature implementation\skill.md tools or services
- When automating or managing skills\development\hermes breakdown feature implementation\skill.md tasks
- When troubleshooting skills\development\hermes breakdown feature implementation\skill.md configurations
- **Triggers**: "Skills\development\hermes Breakdown Feature Implementation\skill.md"## Overview
Use this skill when you need a detailed technical implementation plan for a feature with an emphasis on safely refactoring and testing shell/Powershell/batch scripts into thin orchestrators and TypeScript modules. Produces implementation-plan.md with architecture diagrams, ERD, API specs, frontend component hierarchy, migration notes, and a testing/debugging workflow for scripts under ./Bash.

This skill now includes templates and helper scripts for:
- adding DRY_RUN_SUPPORT markers and --dry-run handling
- a failing-first verification harness (verify-dryrun)
- TypeScript migration templates and a ts-morph helper for AST-safe transforms

## Inputs
- Feature PRD path (required)

## Outputs
- /docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md
- Optional: templates and helper scripts placed under the skill's references/templates/scripts for reuse

## Usage
delegate_task({"goal":"Build implementation plan for feature X","context":"feature_prd=/docs/.../prd.md","toolsets":["file"]})

When executing in a repository context, resolve relative paths in this skill against the skill directory and prefer writing support files under the skill's references/templates/scripts so they are reproducible.

## Verification
- implementation-plan.md exists and contains architecture, ERD, API specs, and migration steps.
- verify-dryrun script exists and returns non-zero when side-effecting scripts are missing DRY_RUN_SUPPORT marker.

## Patterns & Enforcement (new)
- Safety-first: any script that performs side-effects must include DRY_RUN_SUPPORT=true marker and accept a --dry-run flag. CI (verify-dryrun) should fail when markers are missing — failing-first is intentional to force TDD-style fixes.
- Branching policy: default to creating failing-first local branches named `feat/bash-dryrun-markers` unless user instructs otherwise. Always ask for explicit consent before pushing remote branches or opening PRs.
- Migration strategy: keep shell orchestrators thin; move logic to TypeScript modules with tests. Use ts-morph for AST-safe automated transformations rather than brittle text replace.

## Templates & Support Files
This skill ships with convenience files in the skill package. Use skill_manage(file write) to add or update them in the skill. Current support files (pointers):
- references/verify-dryrun.md — short reproduction recipe & verification semantics
- templates/ts-morph-helper.ts — starter ts-morph helper to perform AST-safe edits
- templates/ts-module-template.ts — example TypeScript module to receive migrated logic
- scripts/verify-dryrun.sh — canonical verification harness skeleton

When you update these support files, also update the implementation plan so the repo-level equivalents are placed under docs/ways-of-work/plan/... and Bash/tests/verify-dryrun.sh is created.

## Pitfalls (captured from recent session)
- Do not conflate transient MCP filesystem errors with permanent configuration bugs. The retry + stepwise parent-directory creation pattern is the correct remediation for parent-missing write failures.
- Do not add destructive behavior in the same PR that modifies verification harness; favor a failing-first PR that only adds DRY_RUN_SUPPORT markers so CI reflects the required follow-up work.
- When editing PowerShell scripts, prefer non-interactive confirmation flags (e.g., --yes or -Confirm:$false) for CI; avoid Read-Host prompts unless behind an interactive gate.

## User preferences (embedded)
- The user prefers concise, action-first responses and requires explicit approval before destructive operations and remote pushes. Include a short verification checklist with every proposed change and request one-word confirmation for pushes/commits.

## Example steps (short)
1. Search & catalogue scripts (Bash/scripts/**, Bash/**, repo-wide).
2. Create failing-first branch `feat/bash-dryrun-markers` and add DRY_RUN_SUPPORT markers only.
3. Add TypeScript templates and ts-morph helper to skill references and repo templates directory.
4. Create verify-dryrun.sh under Bash/tests and a GitHub Actions job to run it on pull_request for Bash/**.
5. Iterate: implement dry-run behavior in scripts, run verify-dryrun until green, then open PR to merge.

## Where to add session-specific evidence
Add run logs, transient workarounds, or error transcripts under `references/<topic>.md`. Keep them short (1-2 pages) and focused on reproduction.

---

References: see references/ directory for quick templates and verification recipes.



