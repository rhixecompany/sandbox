---
name: hermes-breakdown
title: "Hermes Breakdown — Epic → Feature → Story → Test"
description: "Umbrella for project breakdown: epic→feature→story→test decomposition and implementation planning. Consolidates all hermes-breakdown-* sub-skills."
version: 2.0.0
author: Alexa
license: MIT
tags: [imported]
metadata:
  hermes:
    tags: [imported]
---
# Hermitian Breakdown — Epic → Feature → Story → Test

Umbrella skill for end-to-end product decomposition and implementation planning. Consolidates all former `hermes-breakdown-*` sub-skills into a single authoritative reference.

## Decomposition Chain

```
Epic → Feature → Story → Task → Test
```

| Level | Output | Skill Reference |
|-------|--------|----------------|
| Epic | Epic PRD (`epic.md`) | absorbed from `hermes-breakdown-epic-pm` |
| Feature | Feature PRD (`prd.md`) | absorbed from `hermes-breakdown-feature-prd` |
| Plan | Implementation plan (`implementation-plan.md`) | `create-implementation-plan` |
| Test | Test strategy & QA checklist | absorbed from `hermes-breakdown-test` |

## When to Use

- Creating an Epic / Feature decomposition for a new initiative
- Generating implementation plans from design PRDs
- Running the test strategy and QA checklist for a feature
- Full product decomposition from vision to executable tasks

## Workflow

### Phase 1: Epic Definition
Define the epic: business goals, success metrics, scope boundaries, stakeholders.
Output: `epic.md`

### Phase 2: Feature Breakdown
Decompose epic into features: user stories, acceptance criteria, dependencies.
Output: `prd.md` per feature

### Phase 3: Implementation Planning
Generate phased implementation plans with atomic tasks, file references, and verification criteria.
Output: `implementation-plan.md` (uses `create-implementation-plan` skill)

### Phase 4: Test Strategy
Define test approach: unit, integration, e2e, acceptance criteria.
Output: `test-strategy.md`

## Related Skills

- `create-implementation-plan` — hands-on plan authoring (keep as standalone)
- `writing-plans` — plan formatting patterns
- `executing-plans` — plan execution patterns
- `plans-and-specs` — broader planning umbrella

## Absorbed Skills

These former sub-skills are now consolidated into this umbrella:

| Former Skill | What Was Absorbed |
|---|---|
| `hermes-breakdown-epic-pm` | Epic PRD template and PM guidance |
| `hermes-breakdown-feature-prd` | Feature PRD template |
| `hermes-breakdown-plan` | Implementation plan generation workflow |
| `hermes-breakdown-test` | Test strategy and QA checklist |

---

## Skills Required

| Skill | Purpose | When Needed |
|-------|---------|-------------|
| `create-implementation-plan` | Generate implementation plans | Phase 3: Implementation Planning |
| `writing-plans` | Plan formatting & structure | All phases |
| `executing-plans` | Plan execution patterns | Post-planning execution |
| `plans-and-specs` | Broader planning context | Phase 1-2: Epic/Feature definition |

---

## Pitfalls

| Pitfall | Severity | Mitigation |
|---------|----------|------------|
| Skipping Epic definition | High | Always start with Phase 1 — no Epic = no shared vision |
| Features not traced to Epic | High | Every feature must link to Epic goal/metric |
| Stories without acceptance criteria | Medium | Define AC in Phase 2 before planning |
| Plans without verification criteria | High | Phase 3 output must include testable criteria |
| Test strategy as afterthought | Medium | Phase 4 runs in parallel, not after implementation |
| Over-decomposing to trivial tasks | Low | Stop at "Task" level — 1-2 day units |
| Not updating Epic when scope changes | Medium | Epic is living document — revise and re-communicate |

---

## Verification Checklist

- [ ] Frontmatter complete: name, title, description, version, author, license, tags
- [ ] Skills Required table present
- [ ] Phased workflow with 4 clear phases (Epic → Feature → Plan → Test)
- [ ] Pitfalls table with ≥5 entries covering critical/high/medium
- [ ] Verification checklist present
- [ ] Reference files exist in `references/`, `templates/`
- [ ] No placeholder text (`[Add ... here]`)
- [ ] Concrete outputs per phase (epic.md, prd.md, implementation-plan.md, test-strategy.md)
- [ ] Cross-references consistent

---

## References

- `references/epic-template.md` — Epic PRD template with goals, metrics, scope, stakeholders
- `references/feature-prd-template.md` — Feature PRD template with stories, AC, dependencies
- `templates/test-strategy-template.md` — Test strategy template (unit, integration, e2e, acceptance)
