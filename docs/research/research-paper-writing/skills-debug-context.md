# Skill Audit: `research-paper-writing`

**Category:** research  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\research\research-paper-writing\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** B  
**Issues:** 0 critical / 0 major / 3 minor  

---

## Frontmatter Check

```yaml
name: research-paper-writing
title: Research Paper Writing Pipeline
description: "Write ML papers for NeurIPS/ICML/ICLR: design→submit."
version: 1.1.0
author: Orchestra Research
license: MIT
dependencies: [semanticscholar, arxiv, habanero, requests, scipy, numpy, matplotlib, SciencePlots]
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Research, Paper Writing, Experiments, ML, AI, NeurIPS, ICML, ICLR, ACL, AAAI, COLM, LaTeX, Citations, Statistical Analysis]
    category: research
    related_skills: [arxiv, ml-paper-writing, subagent-driven-development, plan]
    requires_toolsets: [terminal, files]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |
| MINOR | C1 | Stale pattern: placeholder: TODO/FIXME text present |
| MINOR | C3 | Table pipe count inconsistency: {3, 4, 5} |

## Sections Present

- • `## When To Use This Skill`
- • `## Core Philosophy`
- • `## Phase 0: Project Setup`
- • `## Phase 1: Literature Review`
- • `## Phase 2: Experiment Design`
- • `## Phase 3: Experiment Execution & Monitoring`
- • `## Phase 4: Result Analysis`
- • `## Contribution (one sentence)`
- • `## Experiments Run`
- • `## Figures`
- • `## Failed Experiments (document for honesty)`
- • `## Open Questions`
- • `## Iterative Refinement: Strategy Selection`
- • `## Phase 5: Paper Drafting`
- • `## Phase 6: Self-Review & Revision`
- • `## Phase 7: Submission Preparation`
- • `## Setup`
- • `## Reproduction`
- • `## Citation`
- • `## Phase 8: Post-Acceptance Deliverables`
- • `## Workshop & Short Papers`
- • `## Paper Types Beyond Empirical ML`
- • `## Hermes Agent Integration`
- • `## Experiment: <name>`
- • `## Reviewer Evaluation Criteria`
- • `## Common Issues and Solutions`
- • `## Reference Documents`
- ✅ `## When to Use`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
- Fix `C1`: Stale pattern: placeholder: TODO/FIXME text present
- Fix `C3`: Table pipe count inconsistency: {3, 4, 5}
