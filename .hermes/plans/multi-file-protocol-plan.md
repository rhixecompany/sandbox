---
name: multi-file-protocol-plan
title: "Multi-File Protocol Implementation Plan"
description: "Implementation plan for the multi-file change protocol with 14-skill stack"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - implementation-plan
  - multi-file-protocol
  - skill-protocol
  - workflow
  - governance
phases:
  - name: Phase 1 - Protocol Encoding
    description: Encode protocol in SOUL.md and context files
    tasks:
      - id: MP-T-1.1
        name: Verify SOUL.md has protocol
        description: Ensure SOUL.md contains canonical 14-skill protocol
        phase: Phase 1 - Protocol Encoding
        assignee: implementer
        status: pending
        dependencies: []
      - id: MP-T-1.2
        name: Verify USER.md references protocol
        description: Ensure USER.md references multi-file protocol
        phase: Phase 1 - Protocol Encoding
        assignee: implementer
        status: pending
        dependencies: []
      - id: MP-T-1.3
        name: Verify AGENTS.md quick rules
        description: Ensure AGENTS.md quick rules include protocol
        phase: Phase 1 - Protocol Encoding
        assignee: implementer
        status: pending
        dependencies: []
      - id: MP-T-1.4
        name: Verify .hermes.md references protocol
        description: Ensure .hermes.md references SOUL.md protocol
        phase: Phase 1 - Protocol Encoding
        assignee: implementer
        status: pending
        dependencies: []
  - name: Phase 2 - Skill Integration
    description: Ensure all 14 protocol skills are loadable and integrated
    tasks:
      - id: MP-T-2.1
        name: Verify all 14 skills exist
        description: Confirm all 14 mandatory skills available in skill system
        phase: Phase 2 - Skill Integration
        assignee: implementer
        status: pending
        dependencies: []
      - id: MP-T-2.2
        name: Test skill loading sequence
        description: Load all 14 skills in sequence, verify no errors
        phase: Phase 2 - Skill Integration
        assignee: implementer
        status: pending
        dependencies: [MP-T-2.1]
      - id: MP-T-2.3
        name: Test skill interoperability
        description: Verify skills work together in multi-skill workflow
        phase: Phase 2 - Skill Integration
        assignee: implementer
        status: pending
        dependencies: [MP-T-2.2]
  - name: Phase 3 - Protocol Automation
    description: Implement automated protocol triggering
    tasks:
      - id: MP-T-3.1
        name: Add file count check to using-superpowers
        description: Modify using-superpowers to auto-detect ≥3 file changes
        phase: Phase 3 - Protocol Automation
        assignee: implementer
        status: pending
        dependencies: [MP-T-2.3]
      - id: MP-T-3.2
        name: Add auto-skill-load to using-superpowers
        description: Auto-load 14 skills when protocol triggered
        phase: Phase 3 - Protocol Automation
        assignee: implementer
        status: pending
        dependencies: [MP-T-3.1]
      - id: MP-T-3.3
        name: Add plan creation enforcement
        description: Enforce plan creation before any multi-file execution
        phase: Phase 3 - Protocol Automation
        assignee: implementer
        status: pending
        dependencies: [MP-T-3.2]
  - name: Phase 4 - Validation & Testing
    description: Test protocol end-to-end
    tasks:
      - id: MP-T-4.1
        name: Create test change (3 files)
        description: Create a test request that modifies exactly 3 files
        phase: Phase 4 - Validation & Testing
        assignee: implementer
        status: pending
        dependencies: [MP-T-3.3]
      - id: MP-T-4.2
        name: Execute protocol on test
        description: Run full protocol on test change
        phase: Phase 4 - Validation & Testing
        assignee: implementer
        status: pending
        dependencies: [MP-T-4.1]
      - id: MP-T-4.3
        name: Verify all gates pass
        description: Confirm all verification gates pass
        phase: Phase 4 - Validation & Testing
        assignee: implementer
        status: pending
        dependencies: [MP-T-4.2]
      - id: MP-T-4.4
        name: Test failure scenarios
        description: Test protocol with missing skills, failed gates
        phase: Phase 4 - Validation & Testing
        assignee: implementer
        status: pending
        dependencies: [MP-T-4.3]
gates:
  - name: Gate 1 - Protocol Encoded
    phase: Phase 1 - Protocol Encoding
    criteria:
      - SOUL.md has complete 14-skill protocol
      - USER.md references protocol
      - AGENTS.md quick rules include protocol
      - .hermes.md references protocol
    check: "grep -r '14-skill\\|multi-file.*protocol' SOUL.md USER.md AGENTS.md .hermes.md"
    pass_condition: "All 4 files contain protocol references"
    fail_action: "Add missing protocol references"
  - name: Gate 2 - Skills Loadable
    phase: Phase 2 - Skill Integration
    criteria:
      - All 14 skills load without error
      - Skills interoperate correctly
    check: "Load all 14 skills via skill_view"
    pass_condition: "Zero load errors"
    fail_action: "Fix missing/broken skills"
  - name: Gate 3 - Automation Working
    phase: Phase 3 - Protocol Automation
    criteria:
      - File count detection works
      - Auto-skill-load triggers
      - Plan creation enforced
    check: "Trigger protocol with 3-file change"
    pass_condition: "Protocol executes automatically"
    fail_action: "Fix automation gaps"
  - name: Gate 4 - End-to-End Test Passes
    phase: Phase 4 - Validation & Testing
    criteria:
      - Test change completes via protocol
      - All gates pass
      - Failure scenarios handled
    check: "Full protocol execution on test"
    pass_condition: "Zero manual interventions needed"
    fail_action: "Debug and fix protocol gaps"
dependencies:
  - multi-file-protocol-spec.md
  - prompt-skill-spec-plan-management-system.md
  - context-files-plan.md (for SOUL.md/USER.md/AGENTS.md updates)
---

# Multi-File Protocol Implementation Plan

## Overview

Implements the mandatory multi-file change protocol that triggers on ≥3 file modifications, requiring 14-skill stack loading, plan creation, and gate validation.

## Protocol Trigger

**AUTOMATIC**: Any user request modifying ≥3 files (create/modify/delete)

## 14 Mandatory Skills

1. using-superpowers
2. brainstorming
3. user-communication-preferences
4. mcp-sequential-thinking
5. mcp-filesystem
6. mcp-ast-grep
7. mcp-memory
8. plan
9. plans-and-specs
10. create-implementation-plan
11. implementation-plan
12. executing-plans
13. writing-clearly-and-concisely
14. subagent-driven-development

## Protocol Flow

```
User Request (≥3 files)
        ↓
using-superpowers detects file count
        ↓
Auto-load all 14 skills
        ↓
create-implementation-plan creates plan
        ↓
User approves plan
        ↓
executing-plans OR subagent-driven-development executes
        ↓
All verification gates pass
        ↓
COMPLETE
```

## Integration Points

### SOUL.md (Canonical)
- Standing Rules #13: Multi-File Change Protocol
- Architectural Invariants: Plan Discipline
- 4 Mandatory Rules reference

### USER.md (Preferences)
- Multi-File Change Protocol section
- Standing Goal references protocol

### AGENTS.md (Workspace)
- Quick Rules include protocol
- Directory map shows .hermes/plans/, .hermes/specs/

### .hermes.md (Overrides)
- References SOUL.md for canonical protocol
- Multi-File Change Protocol section

### Skills
- using-superpowers: Auto-detection + skill loading
- create-implementation-plan: Plan creation
- executing-plans: Plan execution with gates
- subagent-driven-development: Parallel execution

## Verification Gates

4 gates ensuring protocol is encoded, skills load, automation works, and end-to-end test passes.

## Dependencies

- context-files-plan.md (for SOUL.md, USER.md, AGENTS.md updates)
- skill-enhancement-plan.md (for plan skill creation)
- All 14 skills enhanced to ≥95