---
name: prompt-skill-spec-plan-management-system
title: "Prompt/Skill/Spec/Plan Management System"
description: "Complete prompt, skill, spec, and plan management system with multi-file protocol, structured prompt library, and skill enhancement"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - prompt-management
  - skill-management
  - spec-management
  - plan-management
  - multi-file-protocol
  - automation
---

# Prompt/Skill/Spec/Plan Management System Specification

## Overview

This specification defines a comprehensive system for managing prompts, skills, specs, and plans across the Hermes workspace. The system implements a multi-file change protocol (≥3 files triggers full protocol), structured prompt library with category/trigger organization, and complete skill/spec/plan lifecycle management.

## Requirements

### REQ-001: Multi-File Change Protocol
- **Trigger**: Any operation touching ≥3 files
- **Action**: Load 14 mandatory skills before proceeding
- **Skills**: using-superpowers, brainstorming, user-communication-preferences, mcp-sequential-thinking, mcp-filesystem, mcp-ast-grep, mcp-memory, plan, plans-and-specs, create-implementation-plan, implementation-plan, executing-plans, writing-clearly-and-concisely, subagent-driven-development
- **Output**: Implementation plan → verification → execution → gate validation

### REQ-002: Prompt Library Structure
- **Location**: `/.github/prompts/{category}/{trigger}/`
- **Files**: `{prompt-name}.prompt.md` + 10 companion files
- **Companion files**: specs.md, plans.md, goals.md, subgoals.md, rules.md, phases.md, steps.md, tasks.md, actions.md, gates.md
- **Categories**: development, planning, creative, testing, documentation, debugging, security, devops, mcp, research, productivity, github, qa

### REQ-003: Spec Management
- **Location**: `/.hermes/specs/`
- **Format**: YAML frontmatter + markdown body
- **Fields**: name, title, description, version, author, license, tags, requirements[], acceptance_criteria[]
- **Naming**: `{feature-name}-spec.md`

### REQ-004: Plan Management
- **Location**: `/.hermes/plans/`
- **Format**: YAML frontmatter + markdown body
- **Fields**: name, title, description, version, author, license, tags, phases[], tasks[], gates[], dependencies[]
- **Naming**: `{feature-name}-plan.md`
- **Phases**: Preparation, Execution, Verification, Completion

### REQ-005: Skill Enhancement
- **Target Skills**: 15+ skills requiring enhancement/refactoring
- **Skills List**:
  1. prompts-judge
  2. specs-judge
  3. plans-judge
  4. using-superpowers
  5. brainstorming
  6. user-communication-preferences
  7. mcp-sequential-thinking
  8. mcp-filesystem
  9. mcp-ast-grep
  10. mcp-memory
  11. plan
  12. plan-mode
  13. plans-and-specs
  14. create-implementation-plan
  15. implementation-plan
  16. executing-plans
  17. writing-clearly-and-concisely
  18. subagent-driven-development
- **Enhancement Requirements**:
  - Complete SKILL.md with all required sections
  - References/ directory with supporting docs
  - Templates/ directory with reusable templates
  - Scripts/ directory with validation scripts
  - Verification checklist with measurable gates
  - No placeholder text

### REQ-006: Context File Updates
- **Files to Update**: SOUL.md, USER.md, MEMORY.md, AGENTS.md, CLAUDE.md, .cursorrules, .hermes.md
- **Update Type**: Full rewrite (delete artifacts, recreate fresh)
- **Consistency**: All files must reference each other correctly
- **Authority**: SOUL.md is the master for agent behavior

### REQ-007: Artifact Cleanliness
- **Rule**: Delete ALL existing artifacts before creating new ones
- **Scope**: All spec files, plan files, prompt files, skill files
- **Verification**: Confirm zero legacy artifacts remain
- **No Trust**: Do not trust any previous implementation artifacts

## Acceptance Criteria

### AC-001: Multi-File Protocol Works
- [ ] Loading 14 skills succeeds without errors
- [ ] Plan creation follows protocol
- [ ] Execution follows plan phases
- [ ] Gates validate before completion

### AC-002: Prompt Library Complete
- [ ] All categories exist with proper structure
- [ ] Each prompt has .prompt.md + 10 companion files
- [ ] Files are properly cross-referenced
- [ ] No duplicate or orphaned files

### AC-003: Specs/Plans Functional
- [ ] Specs in .hermes/specs/ are valid and complete
- [ ] Plans in .hermes/plans/ are executable
- [ ] Spec-to-plan traceability exists
- [ ] Verification gates pass

### AC-004: Skills Enhanced
- [ ] All 18 skills have complete SKILL.md
- [ ] References, templates, scripts exist for each
- [ ] Skill judge score ≥95
- [ ] No placeholder text remains

### AC-005: Context Files Consistent
- [ ] All 7 files exist and are current
- [ ] Cross-references are accurate
- [ ] SOUL.md is authoritative
- [ ] No conflicting rules

### AC-006: Zero Legacy Artifacts
- [ ] All old spec/plan/prompt files removed
- [ ] Only new system files exist
- [ ] Git status shows only new files

## Technical Architecture

### Directory Structure
```
.github/prompts/
├── development/
│   ├── create-feature/
│   │   ├── create-feature.prompt.md
│   │   ├── specs.md
│   │   ├── plans.md
│   │   ├── goals.md
│   │   ├── subgoals.md
│   │   ├── rules.md
│   │   ├── phases.md
│   │   ├── steps.md
│   │   ├── tasks.md
│   │   ├── actions.md
│   │   └── gates.md
│   └── ...
├── planning/
├── creative/
├── testing/
├── documentation/
├── debugging/
├── security/
├── devops/
├── mcp/
├── research/
├── productivity/
├── github/
└── qa/

.hermes/
├── specs/
│   ├── prompt-skill-spec-plan-management-system.md
│   ├── prompt-library-spec.md
│   ├── skill-enhancement-spec.md
│   ├── context-files-spec.md
│   └── multi-file-protocol-spec.md
└── plans/
    ├── prompt-skill-spec-plan-management-plan.md
    ├── prompt-library-plan.md
    ├── skill-enhancement-plan.md
    ├── context-files-plan.md
    └── multi-file-protocol-plan.md
```

### File Format Standards

#### Spec File Format
```yaml
---
name: {feature-name}-spec
title: "{Feature Name} Specification"
description: "Brief description"
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [tag1, tag2]
requirements:
  - REQ-001: Requirement description
acceptance_criteria:
  - AC-001: Criteria description
---
# {Feature Name} Specification
...
```

#### Plan File Format
```yaml
---
name: {feature-name}-plan
title: "{Feature Name} Plan"
description: "Brief description"
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [tag1, tag2]
phases:
  - phase: Preparation
    tasks: [...]
  - phase: Execution
    tasks: [...]
gates:
  - gate: Spec Validation
    criteria: [...]
dependencies:
  - {other-plan}
---
# {Feature Name} Plan
...
```

#### Prompt File Format
```yaml
---
name: {category}/{trigger}/{prompt-name}
title: "{Prompt Name}"
description: "Brief description"
version: 1.0.0
author: Hermes Agent
license: MIT
category: {category}
trigger: {trigger}
tags: [tag1, tag2]
skills_required: [skill1, skill2]
tools_required: [tool1, tool2]
companion_files:
  - specs.md
  - plans.md
  - goals.md
  - subgoals.md
  - rules.md
  - phases.md
  - steps.md
  - tasks.md
  - actions.md
  - gates.md
---
# {Prompt Name}
...
```

#### Companion File Purposes
| File | Purpose |
|------|---------|
| specs.md | Links to .hermes/specs/ specification |
| plans.md | Links to .hermes/plans/ implementation plan |
| goals.md | High-level goals and success metrics |
| subgoals.md | Decomposed sub-goals with owners |
| rules.md | Business rules, constraints, invariants |
| phases.md | Phase definitions with entry/exit criteria |
| steps.md | Detailed step-by-step instructions |
| tasks.md | Individual tasks with assignees |
| actions.md | Specific actions/commands to execute |
| gates.md | Verification gates with pass/fail criteria |

## Verification Gates

### Gate 1: Spec Completeness
- All required fields present
- Requirements traceable to acceptance criteria
- No TBD or placeholder content

### Gate 2: Plan Executability
- All phases have concrete tasks
- Dependencies resolved
- Resource requirements specified

### Gate 3: Prompt Library Integrity
- All 11 files present per prompt
- Cross-references valid
- No circular dependencies

### Gate 4: Skill Quality
- Skill judge score ≥95
- All sections complete
- References and templates exist

### Gate 5: Context Consistency
- All 7 files reference each other correctly
- SOUL.md rules propagated
- No duplicate or conflicting rules

### Gate 6: Artifact Cleanliness
- No legacy files remain
- Only new system files present
- Git history clean

## Dependencies

- Hermes Agent with 14 mandatory skills loaded
- MCP servers: filesystem, ast-grep, memory, sequential-thinking
- Git for version control
- Bash/MSYS2 for script execution

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Legacy artifact contamination | High | High | Delete all before create; verify with git status |
| Skill enhancement scope creep | Medium | Medium | Fixed skill list; no additions during execution |
| Context file conflicts | Medium | High | Single source of truth (SOUL.md); cross-validate |
| Multi-file protocol failures | Low | High | Automated verification at each gate |
| MCP server unavailability | Low | Medium | Fallback to native tools; retry with backoff |

## Timeline

- Phase 1 (Specs): 30 min - Create all spec files
- Phase 2 (Plans): 30 min - Create all plan files
- Phase 3 (Prompt Library): 60 min - Create all prompt structures
- Phase 4 (Skills): 90 min - Enhance all 18 skills
- Phase 5 (Context Files): 30 min - Rewrite all 7 context files
- Phase 6 (Verification): 30 min - Run all gates
- **Total**: ~4.5 hours

## Success Metrics

- All 6 acceptance criteria pass
- Zero legacy artifacts
- All 18 skills score ≥95
- All 7 context files consistent
- Multi-file protocol executes without manual intervention