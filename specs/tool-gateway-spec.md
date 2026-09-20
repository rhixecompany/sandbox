---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---

# Implementation Spec: tool-gateway

## Source

- File: docs/features/tool-gateway.md (223 lines, real content verified via head check)
- Source URL: https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/tool-gateway.md

## Requirements (derived from feature doc content — verified real headings)

- Read and interpret feature descriptions (frontmatter + sections).
- Produce structured artifacts that reference feature concepts.
- Execute script verifies file presence and outputs a result summary.

## Acceptance Criteria

- [ ] ./plans/tool-gateway-plan.md exists with YAML frontmatter
- [ ] ./specs/tool-gateway-spec.md exists with ≥3 sections
- [ ] ./prompts/tool-gateway-prompt.md has prompt instructions
- [ ] skills/tool-gateway-bundle/SKILL.md has ≥10-line body + frontmatter
- [ ] scripts/tool-gateway-execute.py runs without error
- [ ] results/tool-gateway-result.md produced
