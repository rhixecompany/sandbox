---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---


# Implementation Spec: overview
## Source
- File: docs/features/overview.md (57 lines, real content verified via head check)
- Source URL: https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/overview.md
## Requirements (derived from feature doc content — verified real headings)
- Read and interpret feature descriptions (frontmatter + sections).
- Produce structured artifacts that reference feature concepts.
- Execute script verifies file presence and outputs a result summary.
## Acceptance Criteria
- [ ] .hermes/plans/overview-plan.md exists with YAML frontmatter
- [ ] .hermes/specs/overview-spec.md exists with ≥3 sections
- [ ] .hermes/prompts/overview-prompt.md has prompt instructions
- [ ] skills/overview-bundle/SKILL.md has ≥10-line body + frontmatter
- [ ] scripts/overview-execute.py runs without error
- [ ] results/overview-result.md produced
