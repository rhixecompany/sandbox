---
name: multi-file-protocol-spec
title: "Multi-File Change Protocol Specification"
description: "Protocol for changes touching ≥3 files requiring 14-skill stack"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - multi-file-protocol
  - skill-protocol
  - workflow
  - governance
---

# Multi-File Change Protocol Specification

## Overview

Defines the mandatory protocol for any user request that will modify 3 or more files. This protocol ensures structured, verified, and traceable multi-file changes.

## Trigger Condition

**AUTOMATIC TRIGGER**: When a user request will modify ≥3 files
- Creating new files counts
- Modifying existing files counts
- Deleting files counts
- Any combination ≥3 files

## Protocol Requirements

### REQ-MFP-001: Mandatory Skill Loading
Before ANY response or action, load all 14 skills:
1. `/using-superpowers` - Foundational workflow
2. `/brainstorming` - Structured idea generation
3. `/user-communication-preferences` - Alexa's execution style
4. `/mcp-sequential-thinking` - Structured reasoning
5. `/mcp-filesystem` - File operations
6. `/mcp-ast-grep` - Code search/replace
7. `/mcp-memory` - Persistent memory access
8. `/plan` - Write markdown plan to `.hermes/plans/`
9. `/plans-and-specs` - Draft implementation plans
10. `/create-implementation-plan` - Create detailed plans
11. `/implementation-plan` - Modify existing plans
12. `/executing-plans` - Execute written plans
13. `/writing-clearly-and-concisely` - Clear communication
14. `/subagent-driven-development` - Parallel subagent delegation

### REQ-MFP-002: Protocol Execution Steps
1. **Load Skills** - Verify all 14 skills loaded successfully
2. **Create Plan** - Use `/create-implementation-plan` to create detailed plan
3. **Verify Plan** - Present plan to user for approval
4. **Execute** - Use `/executing-plans` or `/subagent-driven-development`
5. **Verify Gates** - All verification gates must pass before completion

### REQ-MFP-003: Plan Structure
Plan must include:
- [ ] Plan name, version, description
- [ ] Phases with entry/exit criteria
- [ ] Tasks with assignees and dependencies
- [ ] Gates with pass/fail criteria
- [ ] Rollback procedures
- [ ] Resource requirements

### REQ-MFP-004: Execution Guardrails
- **Linear Execution**: Validate Step N before Step N+1
- **Checkpoint Rule**: Pause on failure/ambiguity, request approval
- **Fallback Trigger**: After 2 failures, generate alternative plan
- **State Alignment**: Update state after each phase
- **Checkpointing**: Save progress to plan document

### REQ-MFP-005: Subagent Delegation Rules
- Use `delegate_task` for parallel/isolated work
- Inject FULL context to subagents
- Fresh subagent per task
- Two-stage review: Spec Compliance → Code Quality
- Never skip reviews

### REQ-MFP-006: Verification Gates
Every plan must have gates:
- **Pre-flight**: Environment, dependencies, token budget
- **Phase Gates**: Each phase has entry/exit criteria
- **Quality Gates**: Spec compliance, code quality
- **Completion Gate**: All ACs met, no regressions
- **Rollback Gate**: Failure triggers documented rollback

## Acceptance Criteria

### AC-MFP-001: Protocol Activation
- [ ] Protocol triggers automatically on ≥3 file changes
- [ ] All 14 skills load without error
- [ ] No action taken before skills loaded

### AC-MFP-002: Plan Quality
- [ ] Plan created via skill (not ad-hoc)
- [ ] All required sections present
- [ ] Gates defined with measurable criteria

### AC-MFP-003: Execution Discipline
- [ ] Linear execution followed
- [ ] Checkpoints honored
- [ ] Fallback triggered on repeated failure

### AC-MFP-004: Subagent Quality
- [ ] Fresh subagent per task
- [ ] Two-stage review completed
- [ ] No scope creep

### AC-MFP-005: Gate Compliance
- [ ] All gates pass before completion claim
- [ ] Failed gates trigger remediation
- [ ] Rollback executed if needed

## Verification Gates

### Gate 1: Skill Load Verification
```bash
# All 14 skills must load successfully
hermes skill load using-superpowers
hermes skill load brainstorming
# ... all 14
```

### Gate 2: Plan Validation
- Plan file exists in `.hermes/plans/`
- Frontmatter complete
- Phases, tasks, gates defined
- Dependencies resolved

### Gate 3: Execution Verification
- Each phase completes with verification
- Progress logged to plan artifact
- No skipped phases

### Gate 4: Quality Review
- Spec compliance review PASS
- Code quality review APPROVED
- Integration review PASS

### Gate 5: Completion Verification
- All acceptance criteria met
- All artifacts created
- No legacy artifacts remain
- Git status clean

## Integration Points

### With Specs
- Plan references spec in `.hermes/specs/`
- Spec requirements trace to plan tasks
- Spec acceptance criteria = plan gates

### With Prompts
- Prompt companion files reference plan
- Prompt `plans.md` → `.hermes/plans/`
- Prompt `gates.md` = plan gates

### With Skills
- Protocol skills enhanced per skill-enhancement-spec
- Judge skills validate protocol compliance
- Skill library hygiene maintained

### With Context Files
- SOUL.md contains canonical protocol
- USER.md references protocol
- AGENTS.md quick-rules include protocol

## Dependencies
- 14 mandatory skills available
- MCP servers: filesystem, ast-grep, memory, sequential-thinking
- Git for rollback
- skill-judge for validation

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Skills not loading | Medium | High | Pre-load verification; fallback to native |
| Plan approval bypassed | Low | High | Hard gate - no execution without approval |
| Subagent context loss | Medium | Medium | Full context injection; progress artifacts |
| Gate skipping | Low | High | Automated gate enforcement in executing-plans |
| Protocol not triggered | Medium | High | Automated file count check in using-superpowers |

## Enforcement

This protocol is ENCODED in SOUL.md as a Standing Rule and Architectural Invariant. Any agent operating in this workspace MUST follow it. Non-compliance is a critical failure requiring immediate remediation.