---
name: skill-enhancement-plan
title: "Skill Enhancement Implementation Plan"
description: "Implementation plan for enhancing 18 target skills to skill-judge ≥95"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - implementation-plan
  - skill-enhancement
  - skill-quality
  - skill-judge
phases:
  - name: Phase 1 - Scaffold Directories
    description: Create references/, templates/, scripts/ for all 18 skills
    tasks:
      - id: SE-T-1.1
        name: Scaffold core protocol skills (14)
        description: Create directory structure for 14 mandatory protocol skills
        phase: Phase 1 - Scaffold Directories
        assignee: implementer
        status: pending
        dependencies: []
      - id: SE-T-1.2
        name: Scaffold quality gate skills (4)
        description: Create directory structure for 4 judge skills
        phase: Phase 1 - Scaffold Directories
        assignee: implementer
        status: pending
        dependencies: []
  - name: Phase 2 - Enhance Core Protocol Skills
    description: Enhance all 14 mandatory protocol skills
    tasks:
      - id: SE-T-2.1
        name: Enhance using-superpowers
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.2
        name: Enhance brainstorming
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.3
        name: Enhance user-communication-preferences
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.4
        name: Enhance mcp-sequential-thinking
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.5
        name: Enhance mcp-filesystem
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.6
        name: Enhance mcp-ast-grep
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.7
        name: Enhance mcp-memory
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.8
        name: Create plan skill (missing)
        description: Create plan skill from scratch with full structure
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.9
        name: Enhance plans-and-specs
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.10
        name: Enhance create-implementation-plan
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.11
        name: Enhance implementation-plan
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.12
        name: Enhance executing-plans
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.13
        name: Enhance writing-clearly-and-concisely
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
      - id: SE-T-2.14
        name: Enhance subagent-driven-development
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 2 - Enhance Core Protocol Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.1]
  - name: Phase 3 - Enhance Quality Gate Skills
    description: Enhance all 4 judge/validation skills
    tasks:
      - id: SE-T-3.1
        name: Enhance prompts-judge
        description: Complete SKILL.md with rubric, add references/, templates/, scripts/
        phase: Phase 3 - Enhance Quality Gate Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.2]
      - id: SE-T-3.2
        name: Enhance specs-judge
        description: Complete SKILL.md with rubric, add references/, templates/, scripts/
        phase: Phase 3 - Enhance Quality Gate Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.2]
      - id: SE-T-3.3
        name: Enhance plans-judge
        description: Complete SKILL.md with rubric, add references/, templates/, scripts/
        phase: Phase 3 - Enhance Quality Gate Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.2]
      - id: SE-T-3.4
        name: Enhance plan-mode
        description: Complete SKILL.md, add references/, templates/, scripts/
        phase: Phase 3 - Enhance Quality Gate Skills
        assignee: implementer
        status: pending
        dependencies: [SE-T-1.2]
  - name: Phase 4 - Validation
    description: Run skill-judge on all 18 skills
    tasks:
      - id: SE-T-4.1
        name: Run skill-judge on core protocol skills
        description: Validate all 14 core skills score ≥95
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [SE-T-2.1, SE-T-2.2, SE-T-2.3, SE-T-2.4, SE-T-2.5, SE-T-2.6, SE-T-2.7, SE-T-2.8, SE-T-2.9, SE-T-2.10, SE-T-2.11, SE-T-2.12, SE-T-2.13, SE-T-2.14]
      - id: SE-T-4.2
        name: Run skill-judge on quality gate skills
        description: Validate all 4 judge skills score ≥95
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [SE-T-3.1, SE-T-3.2, SE-T-3.3, SE-T-3.4]
      - id: SE-T-4.3
        name: Fix failing skills
        description: Iterate on any skills scoring <95
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [SE-T-4.1, SE-T-4.2]
      - id: SE-T-4.4
        name: Final validation
        description: Confirm all 18 skills ≥95
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [SE-T-4.3]
gates:
  - name: Gate 1 - Directories Scaffolder
    phase: Phase 1 - Scaffold Directories
    criteria:
      - All 18 skills have references/, templates/, scripts/ directories
    check: "find skills -name 'references' -o -name 'templates' -o -name 'scripts' | wc -l"
    pass_condition: "Count = 54 (18 skills × 3 dirs)"
    fail_action: "Create missing directories"
  - name: Gate 2 - Core Skills Enhanced
    phase: Phase 2 - Enhance Core Protocol Skills
    criteria:
      - All 14 core skills have complete SKILL.md
      - All required sections present
      - No placeholder text
    check: "Custom validation script per skill"
    pass_condition: "All 14 skills pass structural validation"
    fail_action: "Fix incomplete skills"
  - name: Gate 3 - Judge Skills Enhanced
    phase: Phase 3 - Enhance Quality Gate Skills
    criteria:
      - All 4 judge skills have complete SKILL.md
      - Rubric with specific criteria
      - No placeholder text
    check: "Custom validation script per skill"
    pass_condition: "All 4 skills pass structural validation"
    fail_action: "Fix incomplete skills"
  - name: Gate 4 - All Skills Score ≥95
    phase: Phase 4 - Validation
    criteria:
      - All 18 skills pass skill-judge with score ≥95
      - Frontmatter ≥18, Structure ≥18, Content ≥16, DRY ≥16, References ≥11
    check: "skill-judge on each skill"
    pass_condition: "All 18 scores ≥95"
    fail_action: "Fix failing skills, re-judge"
dependencies:
  - skill-enhancement-spec.md
  - prompt-skill-spec-plan-management-system.md
---

# Skill Enhancement Implementation Plan

## Overview

Enhances 18 target skills to achieve skill-judge score ≥95 with full structural compliance (SKILL.md + references/ + templates/ + scripts/).

## Target Skills

### Core Protocol Skills (14 - Mandatory)
1. using-superpowers
2. brainstorming
3. user-communication-preferences
4. mcp-sequential-thinking
5. mcp-filesystem
6. mcp-ast-grep
7. mcp-memory
8. plan (CREATE - missing)
9. plans-and-specs
10. create-implementation-plan
11. implementation-plan
12. executing-plans
13. writing-clearly-and-concisely
14. subagent-driven-development

### Quality Gate Skills (4)
15. prompts-judge
16. specs-judge
17. plans-judge
18. plan-mode

## Enhancement Requirements Per Skill

### SKILL.md Structure (All Skills)
- Complete YAML frontmatter
- Description with overview
- When to Use / When NOT to Use
- Skills Required table
- Workflow with ≥3 phases
- Pitfalls (≥3 items)
- Best Practices
- Verification Checklist (≥5 items)
- References to linked files

### References/ Directory (All Skills)
- overview.md - Skill overview and architecture
- ≥2 domain-specific reference files
- Cross-references to related skills

### Templates/ Directory (All Skills)
- ≥1 reusable template
- Follows project conventions
- Documented in SKILL.md

### Scripts/ Directory (All Skills)
- ≥1 validation/utility script
- Executable and tested
- Documented in SKILL.md

## Special Requirements

### plan skill (CREATE FROM SCRATCH)
This skill doesn't exist - must be created:
- Location: `planning/plan/`
- Based on plan-mode patterns
- Plan file format specification
- Phase templates
- Gate definitions

### Judge Skills (prompts-judge, specs-judge, plans-judge)
- Detailed rubric with specific criteria
- Scoring calibration examples
- Remediation patterns
- Integration with multi-file protocol

## Verification Process

1. Structural validation (all sections present)
2. skill-judge scoring
3. Fix iterations until ≥95
4. Cross-skill consistency check
5. Multi-file protocol integration test

## Dependencies
- skill-judge skill available
- All skill directories accessible
- MCP servers for validation