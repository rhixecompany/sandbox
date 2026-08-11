---
name: breakdown-plan-output-format
title: Breakdown Plan — Output Format
description: Output format for the breakdown-plan prompt — project plan and support deliverables.
tags: [breakdown, plan, output-format]
---

# Output Format

> Extracted from `breakdown-plan.prompt.md` (Project Plan deliverables).

## Primary Deliverables

1. **Project Plan**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`
2. **Issue Breakdown**: Stories, bugs, and enablers with full traceability (feature → epic).

## Plan Document Structure

- **Title**: `{Epic Name} — {Feature Name} Breakdown`
- **Epic Description**: Epic summary from PRD.
- **Business Value**:
  - **Primary Goal**: {Main business objective}
  - **Success Metrics**: {KPIs and measurable outcomes}
  - **User Impact**: {How users will benefit}
- **Epic Acceptance Criteria**: High-level requirements checkbox list.
- **Feature**: Issue links to all stories/enablers in this epic.
- **Definition of Done**: All stories completed, e2e testing passed, performance benchmarks met, docs updated, UAT completed.
- **Labels**: `epic`, `{priority-level}`, `{component-name}`.

## Traceability Requirement

Every issue references its parent feature/epic; enablers list "User Stories Enabled" with story issue links.

---

> TODO-to-author: extend with full issue-creation field map if the source PRD schema changes.
