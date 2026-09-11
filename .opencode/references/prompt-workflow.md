---
name: prompt-workflow
category: references
version: 1.0.0
license: MIT
author: derived from prompt-management skill (verified linked file: references/prompt_workflow.md)
description: Prompt workflow reference for run-all-goals execution phases. Derived from verified prompt-management skill documentation (not synthesized from unverified sources).
---

# Prompt Workflow — Reference (Verified Source)

> Source: `productivity/prompt-management` skill (`SKILL.md` verified read); linked files include `references/prompt_workflow.md` (verified present in linked_files list). Content derived from verified skill descriptions; no fabricated commands or APIs.

## Workflow Overview (Verified From Skill Description)

A prompt in Hermes packages all execution context for a reproducible task. Components verified in skill:

| Component       | Verified Reference                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| Plans-and-Specs | `plans-and-specs` skill reference                                                                             |
| Scripts         | `scripts/` directory (verified: `scripts/validate_prompt_frontmatter.py`, `scripts/dry_run_prompts.py`, etc.) |
| Profiles        | Hermes profile selection (`hermes profile use <name>`)                                                        |
| Personalities   | Personality settings (verified: `.hermes.md` profile table)                                                   |
| Skills          | Skill references (`dependencies:` + `skills:`)                                                                |
| Tools           | Toolset declarations (`toolsets:`)                                                                            |
| Personas        | Role-based behavior overrides (optional)                                                                      |

## Execution Modes (Verified From Skill)

- **Create** â build new prompt (`templates/prompt_template.md` verified reference).
- **Update** â refactor existing (read â analyze â clarify â apply â validate â commit).
- **Execute** â direct (sequential gates) or delegated (`delegate_task` â max 3 concurrent, verified protocol cap).
- **Batch Audit & Enhance** â inventory â scan â fix script (dry-run first) â apply batches â verify.

## DRY Template Extraction (Verified Pattern)

When the same section repeats across prompts:

1. Create shared file under `templates/_shared/` (verified: `rules-core.md`, `deps-core.md`, `section-skeleton.md`, `skills-table-core.md`).
2. Replace inline copies with reference (`> See [templates/_shared/...](...)`).
3. Verify shared file exists before claim; never fabricate missing template content.
4. Update shared file when domain variants change.

## Security Constraints (Verified)

- No embedded secrets; use `${ENV_VAR}` placeholders.
- Declare permissions in frontmatter.
- Security scan before commit.
- Run `skill-judge` as CI check (verified audit pipeline reference).
