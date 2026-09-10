---
name: run-all-goals
title: "Run All Goals — Unified Pipeline Skill"
description: >
  Execute the unified run-all-goals pipeline: comprehensive implementation
  covering context audit, plugins/hooks, MCP sync, config sync, diagnostic
  repair, model tests, agent sync, cleanup, and verification at score >= 99.
version: 2.0.0
author: Alexa (via OWL)
license: MIT
tags: [implementation, execution, unified, score-99, audit]
metadata:
  hermes:
    related_skills:
    - using-superpowers
    - brainstorming
    - subagent-driven-development
    - prompt-management
    - executing-plans
tags: [implementation, execution, audit, verification]
---

# Run All Goals — Unified Pipeline Skill

## Overview
Execute the comprehensive run-all-goals pipeline merging three source files into a single execution plan with 4 goals, 17 subgoals, and 11 phases.

## Workflow

### Phase 1: Audit
- Read all 3 source files
- Verify workspace inventory
- Load all 14 mandatory skills + judge skills

### Phase 2: Plan
- Create implementation plan (.hermes/plans/run-all-goals-implementation.md)
- Create shared templates (_shared/)
- Create reference docs (references/)
- Create scripts (scripts/)

### Phase 3: Execute
- SG1.1 through SG4.9: All subgoals
- GOAL 1-4: All goals
- 11 phases with verified gates

### Phase 4: Verify
- Run judge skills (specs-judge, plans-judge, prompts-judge, skill-judge)
- Target score >= 99 on all
- Run verify_run_all_goals.py
- Generate execution summary

## Skills Required
| Skill | Purpose |
|---|---|
| using-superpowers | Foundational workflow |
| brainstorming | Idea generation |
| user-communication-preferences | Alexa's style |
| mcp-sequential-thinking | Chain-of-thought |
| systematic-debugging | Root cause |
| subagent-driven-development | 2-stage review |
| hermes-diagnostic-repair | Diagnostic |
| log-analysis-and-triage | Log analysis |
| plans-and-specs | Plans |
| create-implementation-plan | Plan creation |
| implementation-plan | Detailed plans |
| executing-plans | Multi-phase execution |
| writing-clearly-and-concisely | Clarity |
| prompt-management | Prompt workflow |
| skill-judge | Judge scoring |
| prompts-judge | Prompt scoring |
| plans-judge | Plans scoring |
| specs-judge | Specs scoring |

## Verification Checklist
- [ ] All 3 source files read; sizes verified
- [ ] All 14 mandatory skills loaded
- [ ] All 11 phases have verified gates
- [ ] All judge skills score >= 99
- [ ] Agent sync: 5 AI agents identical
- [ ] Cleanup complete
- [ ] Config files updated
- [ ] Git push succeeded
- [ ] No placeholders in any artifact
- [ ] Execution summary generated

## Best Practices
- Use MCP servers first
- DRY: shared components in _shared/
- Concise, action-first responses
- Verify with tools, not memory
- Score >= 99 on all judge skills
