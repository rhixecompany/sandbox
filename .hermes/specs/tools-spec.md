---
name: "tools-spec"
title: "Spec — Tools & Toolsets"
version: 1.0.0
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
- [ ] .hermes/plans/tools-plan.md exists with YAML frontmatter
- [ ] .hermes/specs/tools-spec.md exists with ≥3 sections
- [ ] .hermes/prompts/tools-prompt.md has prompt instructions
- [ ] skills/tools-bundle/SKILL.md has ≥10-line body + frontmatter
- [ ] scripts/tools-execute.py runs without error
- [ ] results/tools-result.md produced
