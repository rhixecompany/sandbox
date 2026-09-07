---
name: breakdown-plan-estimate
title: Breakdown Plan — Priority and Value Matrix
description: Estimate and priority matrix for breakdown-plan — story points and value mapping.
tags: [breakdown, plan, estimate, priority]
---

# Priority and Value Matrix

> Extracted from `breakdown-plan.prompt.md` (section 4).

## Story Estimate Format

| Field | Value |
|| ----- | ----- ||
| Issue | #{story-issue-number} — {Story title} |
| Estimate | {Story points or effort estimate} |
| Priority | P1 (must) / P2 (should) / P3 (could) |
| Value | {Business value or user impact note} |

## Enabler Estimate Format

- **Title**: Technical Enabler: {Enabler Title}
- **Description**: Technical work required to support user stories.
- **Technical Requirements**: checkbox list.
- **Implementation Tasks**: #{task-issue-number} — {Implementation detail / Infrastructure setup}.
- **User Stories Enabled**: #{story-issue-number} — {Story title} (one per line).
- **Acceptance Criteria**: {Technical validation 1}, {Technical validation 2}, Performance benchmarks met.

## Matrix Columns

1. **Priority** (P1/P2/P3)
2. **Estimate** (story points)
3. **Dependencies** (issue links)
4. **Value**: Business value or risk reduction

> Sorting rule: P1 first, then by value score, then by estimate (smallest first).

---

> TODO-to-author: add weighting formula if the team adopts a scored value model.
