---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---

# Implementation Spec: memory

## Source

- File: docs/features/memory.md (464 lines, real content verified via head check)
- Source URL: https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/memory.md

## Requirements (derived from feature doc content — verified real headings)

- Read and interpret feature descriptions (frontmatter + sections).
- Produce structured artifacts that reference feature concepts.
- Execute script verifies file presence and outputs a result summary.

## Acceptance Criteria

- [ ] ./plans/memory-plan.md exists with YAML frontmatter
- [ ] ./specs/memory-spec.md exists with ≥3 sections
- [ ] ./prompts/memory-prompt.md has prompt instructions
- [ ] skills/memory-bundle/SKILL.md has ≥10-line body + frontmatter
- [ ] scripts/memory-execute.py runs without error
- [ ] results/memory-result.md produced
