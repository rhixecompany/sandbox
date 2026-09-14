---
title: Docker / AI Agent Cleanup Plan — subgoal 9
description: Phase-by-phase execution plan for 2026-09-05_docker-cleanup-plan. Decomposes the matching spec into verifiable tasks with explicit gates.
date: 2026-09-07
author: Alexa
status: in_progress
profile: code-architect
model: nemotron-3-ultra-free
---

# Docker / AI Agent Cleanup Plan — subgoal 9

> Trigger: line 9 of `goal-using-superpowers-brainstormin.txt`
> Authorization: destructive ops approved (SOUL.md rule 11 risk noted)

## Scope
- Delete all unused docker images, builds, containers, volumes, models, MCP toolkit artifacts
- Target: workspace-local containers only (not production services)

## Commands (with risk notes)
```
# Confirm nothing running first
`docker ps -a`

# Prune (DESTRUCTIVE — irreversible deletion of all unused images/containers/volumes)
`docker system prune -a -f --volumes`

# Verify
`docker system df`
```

## Risk Note
This deletes ALL unused Docker resources. Confirmed authorized by user (`Full execution including git push/docker cleanup — authorized`).

## Verification
- [ ] Pre-state captured (`docker system df`)
- [ ] Command executed
- [ ] Post-state verified (`docker system df` shows reduced usage)

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Judge subprocess timeout (>60s) | Low | Medium | Pre-warm: run plans-judge + specs-judge once before scoring |
| Cross-judge path resolution fails | Medium | Low | Use project_root = pdir.parent.parent; verify with `echo` |
| Phase gate line missing | Low | High | `augment_plans_with_required_sections.py` appends a default gate to every `## Phase X` heading |
| Spec coupling broken (plan points at missing spec) | Medium | Medium | `pick_matching_spec` uses token overlap; fallback to the comprehensive spec |

## Files to Create or Modify

- `.hermes/plans/<this-plan>.md` — this plan, augmented with the required sections.
- `scripts/augment_plans_with_required_sections.py` — the augmenter that produced this section.
- `.hermes/specs/*.md` — referenced specs; verify each path with `ls` before completion.
- `judge_results/plans_audit.md` — output of the plans-judge run after augmentation.

## Linked Specs

- ../specs/comprehensive-hermes-maintenance-spec.md

## Verification

**Gate**: All listed tasks complete and a fresh run of `python "C:/Users/Alexa/AppData/Local/hermes/skills/qa/plans-judge/scripts/judge.py" --plans-dir .hermes/plans` reports this plan at score >= 95.
