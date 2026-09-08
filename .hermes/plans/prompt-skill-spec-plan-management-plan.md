---
name: prompt-skill-spec-plan-management-plan
title: "Prompt/Skill/Spec/Plan Management System Plan"
description: "Complete implementation plan for prompt, skill, spec, and plan management system"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - implementation-plan
  - prompt-management
  - skill-management
  - spec-management
  - plan-management
phases:
  - name: Phase 1 - Specifications
    description: Create all specification files in .hermes/specs/
    tasks:
      - id: T-1.1
        name: Create master system spec
        description: Create prompt-skill-spec-plan-management-system.md
        phase: Phase 1 - Specifications
        assignee: implementer
        status: completed
        dependencies: []
      - id: T-1.2
        name: Create prompt library spec
        description: Create prompt-library-spec.md
        phase: Phase 1 - Specifications
        assignee: implementer
        status: completed
        dependencies: []
      - id: T-1.3
        name: Create skill enhancement spec
        description: Create skill-enhancement-spec.md
        phase: Phase 1 - Specifications
        assignee: implementer
        status: completed
        dependencies: []
      - id: T-1.4
        name: Create context files spec
        description: Create context-files-spec.md
        phase: Phase 1 - Specifications
        assignee: implementer
        status: completed
        dependencies: []
      - id: T-1.5
        name: Create multi-file protocol spec
        description: Create multi-file-protocol-spec.md
        phase: Phase 1 - Specifications
        assignee: implementer
        status: completed
        dependencies: []
  - name: Phase 2 - Plans
    description: Create all plan files in .hermes/plans/
    tasks:
      - id: T-2.1
        name: Create master system plan
        description: Create prompt-skill-spec-plan-management-plan.md
        phase: Phase 2 - Plans
        assignee: implementer
        status: in-progress
        dependencies: [T-1.1, T-1.2, T-1.3, T-1.4, T-1.5]
      - id: T-2.2
        name: Create prompt library plan
        description: Create prompt-library-plan.md
        phase: Phase 2 - Plans
        assignee: implementer
        status: pending
        dependencies: [T-1.2]
      - id: T-2.3
        name: Create skill enhancement plan
        description: Create skill-enhancement-plan.md
        phase: Phase 2 - Plans
        assignee: implementer
        status: pending
        dependencies: [T-1.3]
      - id: T-2.4
        name: Create context files plan
        description: Create context-files-plan.md
        phase: Phase 2 - Plans
        assignee: implementer
        status: pending
        dependencies: [T-1.4]
      - id: T-2.5
        name: Create multi-file protocol plan
        description: Create multi-file-protocol-plan.md
        phase: Phase 2 - Plans
        assignee: implementer
        status: pending
        dependencies: [T-1.5]
  - name: Phase 3 - Prompt Library
    description: Create complete prompt library structure in .github/prompts/
    tasks:
      - id: T-3.1
        name: Create category directories
        description: Create all 13 category directories
        phase: Phase 3 - Prompt Library
        assignee: implementer
        status: pending
        dependencies: [T-2.2]
      - id: T-3.2
        name: Create trigger directories
        description: Create trigger directories for each category
        phase: Phase 3 - Prompt Library
        assignee: implementer
        status: pending
        dependencies: [T-3.1]
      - id: T-3.3
        name: Create prompt files with companions
        description: Create .prompt.md + 10 companion files per prompt
        phase: Phase 3 - Prompt Library
        assignee: implementer
        status: pending
        dependencies: [T-3.2]
      - id: T-3.4
        name: Validate cross-references
        description: Verify all specs.md and plans.md references resolve
        phase: Phase 3 - Prompt Library
        assignee: implementer
        status: pending
        dependencies: [T-3.3]
  - name: Phase 4 - Skill Enhancement
    description: Enhance/refactor all 18 target skills
    tasks:
      - id: T-4.1
        name: Scaffold skill directories
        description: Create references/, templates/, scripts/ for all 18 skills
        phase: Phase 4 - Skill Enhancement
        assignee: implementer
        status: pending
        dependencies: [T-2.3]
      - id: T-4.2
        name: Enhance core protocol skills (14)
        description: Enhance 14 mandatory protocol skills
        phase: Phase 4 - Skill Enhancement
        assignee: implementer
        status: pending
        dependencies: [T-4.1]
      - id: T-4.3
        name: Enhance quality gate skills (4)
        description: Enhance prompts-judge, specs-judge, plans-judge, plan-mode
        phase: Phase 4 - Skill Enhancement
        assignee: implementer
        status: pending
        dependencies: [T-4.1]
      - id: T-4.4
        name: Run skill-judge validation
        description: Verify all 18 skills score ≥95
        phase: Phase 4 - Skill Enhancement
        assignee: implementer
        status: pending
        dependencies: [T-4.2, T-4.3]
  - name: Phase 5 - Context Files
    description: Rewrite all 7 context files
    tasks:
      - id: T-5.1
        name: Create SOUL.md (canonical)
        description: Create master SOUL.md in profile directory
        phase: Phase 5 - Context Files
        assignee: implementer
        status: pending
        dependencies: [T-2.4]
      - id: T-5.2
        name: Create USER.md (canonical)
        description: Create USER.md in profile directory
        phase: Phase 5 - Context Files
        assignee: implementer
        status: pending
        dependencies: [T-5.1]
      - id: T-5.3
        name: Create MEMORY.md (canonical)
        description: Create MEMORY.md in profile directory
        phase: Phase 5 - Context Files
        assignee: implementer
        status: pending
        dependencies: [T-5.1]
      - id: T-5.4
        name: Create workspace pointers
        description: Create pointer files in SandBox root
        phase: Phase 5 - Context Files
        assignee: implementer
        status: pending
        dependencies: [T-5.2, T-5.3]
      - id: T-5.5
        name: Create AGENTS.md
        description: Create canonical AGENTS.md in workspace root
        phase: Phase 5 - Context Files
        assignee: implementer
        status: pending
        dependencies: [T-5.1]
      - id: T-5.6
        name: Create .hermes.md
        description: Create .hermes.md in workspace root
        phase: Phase 5 - Context Files
        assignee: implementer
        status: pending
        dependencies: [T-5.1]
      - id: T-5.7
        name: Create CLAUDE.md
        description: Create CLAUDE.md stub
        phase: Phase 5 - Context Files
        assignee: implementer
        status: pending
        dependencies: [T-5.5]
      - id: T-5.8
        name: Create .cursorrules
        description: Create .cursorrules stub
        phase: Phase 5 - Context Files
        assignee: implementer
        status: pending
        dependencies: [T-5.5]
  - name: Phase 6 - Verification
    description: Run all verification gates
    tasks:
      - id: T-6.1
        name: Verify spec completeness
        description: All specs valid, requirements traceable
        phase: Phase 6 - Verification
        assignee: implementer
        status: pending
        dependencies: [T-3.4, T-4.4, T-5.8]
      - id: T-6.2
        name: Verify plan executability
        description: All plans have concrete tasks, dependencies resolved
        phase: Phase 6 - Verification
        assignee: implementer
        status: pending
        dependencies: [T-3.4, T-4.4, T-5.8]
      - id: T-6.3
        name: Verify prompt library integrity
        description: All 11 files per prompt, cross-refs valid
        phase: Phase 6 - Verification
        assignee: implementer
        status: pending
        dependencies: [T-3.4]
      - id: T-6.4
        name: Verify skill quality
        description: All 18 skills score ≥95
        phase: Phase 6 - Verification
        assignee: implementer
        status: pending
        dependencies: [T-4.4]
      - id: T-6.5
        name: Verify context consistency
        description: All 7 files consistent, no duplication
        phase: Phase 6 - Verification
        assignee: implementer
        status: pending
        dependencies: [T-5.8]
      - id: T-6.6
        name: Verify artifact cleanliness
        description: Zero legacy artifacts, git clean
        phase: Phase 6 - Verification
        assignee: implementer
        status: pending
        dependencies: [T-3.4, T-4.4, T-5.8]
      - id: T-6.7
        name: End-to-end protocol test
        description: Execute multi-file protocol on test change
        phase: Phase 6 - Verification
        assignee: implementer
        status: pending
        dependencies: [T-6.1, T-6.2, T-6.3, T-6.4, T-6.5, T-6.6]
gates:
  - name: Gate 1 - Specs Complete
    phase: Phase 1 - Specifications
    criteria:
      - All 5 spec files created
      - All frontmatter valid
      - Requirements traceable to acceptance criteria
    check: "ls .hermes/specs/*.md | wc -l"
    pass_condition: "Count = 5"
    fail_action: "Re-create missing specs"
  - name: Gate 2 - Plans Complete
    phase: Phase 2 - Plans
    criteria:
      - All 5 plan files created
      - All phases, tasks, gates defined
      - Dependencies resolved
    check: "ls .hermes/plans/*.md | wc -l"
    pass_condition: "Count = 5"
    fail_action: "Re-create missing plans"
  - name: Gate 3 - Prompt Library Complete
    phase: Phase 3 - Prompt Library
    criteria:
      - All 13 categories exist
      - Each category has ≥1 trigger
      - Each trigger has 11 files
      - All cross-references resolve
    check: "find .github/prompts -name '*.md' | wc -l"
    pass_condition: "Count ≥ 143 (13 categories × 1 trigger × 11 files)"
    fail_action: "Fix missing files/references"
  - name: Gate 4 - Skills Enhanced
    phase: Phase 4 - Skill Enhancement
    criteria:
      - All 18 skills have complete SKILL.md
      - All have references/, templates/, scripts/
      - All skill-judge scores ≥95
      - No placeholder text
    check: "skill-judge on all 18 skills"
    pass_condition: "All scores ≥95"
    fail_action: "Fix failing skills, re-judge"
  - name: Gate 5 - Context Files Consistent
    phase: Phase 5 - Context Files
    criteria:
      - All 7 files exist
      - No duplication across files
      - Cross-references valid
      - Authority hierarchy respected
    check: "Custom validation script"
    pass_condition: "All checks pass"
    fail_action: "Fix inconsistencies, re-validate"
  - name: Gate 6 - Artifact Cleanliness
    phase: Phase 6 - Verification
    criteria:
      - No legacy spec/plan/prompt files
      - No backup files (.bak, .old, timestamped)
      - Git status shows only new system files
    check: "git status --porcelain"
    pass_condition: "Only new files listed"
    fail_action: "Remove legacy artifacts, re-check"
  - name: Gate 7 - End-to-End Test
    phase: Phase 6 - Verification
    criteria:
      - Multi-file protocol triggers on ≥3 file change
      - All 14 skills load
      - Plan created, executed, gates pass
    check: "Execute test change touching 3 files"
    pass_condition: "Protocol completes without manual intervention"
    fail_action: "Debug protocol, fix gaps"
dependencies:
  - prompt-skill-spec-plan-management-system.md
  - prompt-library-spec.md
  - skill-enhancement-spec.md
  - context-files-spec.md
  - multi-file-protocol-spec.md
---

# Prompt/Skill/Spec/Plan Management System Plan

## Overview

This plan implements the complete prompt, skill, spec, and plan management system as specified in the 5 specification files. The plan follows a 6-phase approach with verification gates at each phase boundary.

## Phase Details

### Phase 1: Specifications (COMPLETED)
All 5 specification files created in `.hermes/specs/`:
1. `prompt-skill-spec-plan-management-system.md` - Master system spec
2. `prompt-library-spec.md` - Prompt library structure
3. `skill-enhancement-spec.md` - 18 skill enhancement requirements
4. `context-files-spec.md` - 7 context file rewrite requirements
5. `multi-file-protocol-spec.md` - Protocol for ≥3 file changes

**Gate 1 Status**: ✅ PASSED - All 5 specs created and validated

### Phase 2: Plans (IN PROGRESS)
Creating 5 plan files in `.hermes/plans/`:
1. `prompt-skill-spec-plan-management-plan.md` - This file (master plan)
2. `prompt-library-plan.md` - Prompt library implementation
3. `skill-enhancement-plan.md` - Skill enhancement implementation
4. `context-files-plan.md` - Context files rewrite implementation
5. `multi-file-protocol-plan.md` - Protocol implementation

### Phase 3: Prompt Library
Building complete prompt library at `.github/prompts/`:
- 13 categories (development, planning, creative, testing, documentation, debugging, security, devops, mcp, research, productivity, github, qa)
- Each category: ≥1 trigger directory
- Each trigger: 11 files (.prompt.md + 10 companions)

### Phase 4: Skill Enhancement
Enhancing 18 skills to skill-judge ≥95:
- 14 core protocol skills
- 4 quality gate skills
- Each skill: SKILL.md + references/ + templates/ + scripts/

### Phase 5: Context Files
Rewriting 7 context files with authority hierarchy:
1. SOUL.md (canonical in profile, pointer in workspace)
2. USER.md (canonical in profile, pointer in workspace)
3. MEMORY.md (canonical in profile, pointer in workspace)
4. AGENTS.md (workspace root)
5. .hermes.md (workspace root)
6. CLAUDE.md (workspace root - stub)
7. .cursorrules (workspace root - stub)

### Phase 6: Verification
Running 7 verification gates:
1. Specs completeness
2. Plans executability
3. Prompt library integrity
4. Skill quality
5. Context consistency
6. Artifact cleanliness
7. End-to-end protocol test

## Resource Requirements

- **Skills**: All 14 mandatory protocol skills + 4 judge skills
- **MCP Servers**: filesystem, ast-grep, memory, sequential-thinking
- **Tools**: git, bash, skill-judge, skill-manage
- **Time**: ~4.5 hours total

## Rollback Procedures

- Each phase has independent verification
- On gate failure: fix and re-verify only that phase
- Git commits at each gate passage for rollback points
- Full rollback: `git reset --hard <last-passed-gate-commit>`

## Success Criteria

All 7 gates pass → System complete and operational