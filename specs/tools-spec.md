---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---


# Implementation Spec: tools
## Source
- File: docs/features/tools.md (261 lines, real content verified via head check)
- Source URL: https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/tools.md
## Requirements (derived from feature doc content — verified real headings)
- Read and interpret feature descriptions (frontmatter + sections).
- Produce structured artifacts that reference feature concepts.
- Execute script verifies file presence and outputs a result summary.
## Acceptance Criteria
- [ ] ./plans/tools-plan.md exists with YAML frontmatter
- [ ] ./specs/tools-spec.md exists with ≥3 sections
- [ ] ./prompts/tools-prompt.md has prompt instructions
- [ ] skills/tools-bundle/SKILL.md has ≥10-line body + frontmatter
- [ ] scripts/tools-execute.py runs without error
- [ ] results/tools-result.md produced
