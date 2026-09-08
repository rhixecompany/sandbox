---
name: context-files-plan
title: "Context Files Rewrite Implementation Plan"
description: "Implementation plan for rewriting all 7 context files with authority hierarchy"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - implementation-plan
  - context-files
  - soul-md
  - user-md
  - memory-md
  - agents-md
  - claude-md
  - cursorrules
  - hermes-md
phases:
  - name: Phase 1 - Canonical Profile Files
    description: Create canonical files in Hermes profile directory
    tasks:
      - id: CF-T-1.1
        name: Create SOUL.md (canonical)
        description: Create master SOUL.md in /c/Users/Alexa/AppData/Local/hermes/profiles/default/
        phase: Phase 1 - Canonical Profile Files
        assignee: implementer
        status: pending
        dependencies: []
      - id: CF-T-1.2
        name: Create USER.md (canonical)
        description: Create USER.md in profile directory with full preferences
        phase: Phase 1 - Canonical Profile Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-1.1]
      - id: CF-T-1.3
        name: Create MEMORY.md (canonical)
        description: Create MEMORY.md in profile directory with §-delimited facts
        phase: Phase 1 - Canonical Profile Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-1.1]
  - name: Phase 2 - Workspace Pointer Files
    description: Create pointer files in SandBox workspace root
    tasks:
      - id: CF-T-2.1
        name: Create SOUL.md (workspace copy)
        description: Copy canonical SOUL.md to workspace root
        phase: Phase 2 - Workspace Pointer Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-1.1]
      - id: CF-T-2.2
        name: Create USER.md (pointer)
        description: Create pointer USER.md in workspace root
        phase: Phase 2 - Workspace Pointer Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-1.2]
      - id: CF-T-2.3
        name: Create MEMORY.md (pointer)
        description: Create pointer MEMORY.md in workspace root
        phase: Phase 2 - Workspace Pointer Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-1.3]
  - name: Phase 3 - Workspace Root Files
    description: Create AGENTS.md, .hermes.md, CLAUDE.md, .cursorrules
    tasks:
      - id: CF-T-3.1
        name: Create AGENTS.md
        description: Create canonical AGENTS.md in workspace root
        phase: Phase 3 - Workspace Root Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-1.1]
      - id: CF-T-3.2
        name: Create .hermes.md
        description: Create .hermes.md in workspace root
        phase: Phase 3 - Workspace Root Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-1.1]
      - id: CF-T-3.3
        name: Create CLAUDE.md
        description: Create CLAUDE.md stub deferring to AGENTS.md
        phase: Phase 3 - Workspace Root Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-3.1]
      - id: CF-T-3.4
        name: Create .cursorrules
        description: Create .cursorrules stub deferring to AGENTS.md
        phase: Phase 3 - Workspace Root Files
        assignee: implementer
        status: pending
        dependencies: [CF-T-3.1]
  - name: Phase 4 - Validation
    description: Validate all cross-references and consistency
    tasks:
      - id: CF-T-4.1
        name: Validate authority hierarchy
        description: Verify SOUL.md rules not contradicted by other files
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [CF-T-3.4]
      - id: CF-T-4.2
        name: Validate no duplication
        description: Verify each fact appears in exactly one file
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [CF-T-3.4]
      - id: CF-T-4.3
        name: Validate cross-references
        description: Verify all internal links resolve
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [CF-T-3.4]
      - id: CF-T-4.4
        name: Validate profile routing consistency
        description: Verify all routing tables identical across files
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [CF-T-3.4]
      - id: CF-T-4.5
        name: Validate multi-file protocol consistency
        description: Verify protocol references match in all files
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [CF-T-3.4]
      - id: CF-T-4.6
        name: Clean legacy artifacts
        description: Remove any .bak, .old, timestamped backup files
        phase: Phase 4 - Validation
        assignee: implementer
        status: pending
        dependencies: [CF-T-3.4]
gates:
  - name: Gate 1 - Canonical Files Created
    phase: Phase 1 - Canonical Profile Files
    criteria:
      - SOUL.md exists in profile dir with all required sections
      - USER.md exists in profile dir with full preferences
      - MEMORY.md exists in profile dir with §-delimited format
    check: "ls ~/AppData/Local/hermes/profiles/default/*.md"
    pass_condition: "All 3 files present and valid"
    fail_action: "Re-create missing/invalid files"
  - name: Gate 2 - Pointer Files Created
    phase: Phase 2 - Workspace Pointer Files
    criteria:
      - SOUL.md copy in workspace root
      - USER.md pointer in workspace root
      - MEMORY.md pointer in workspace root
    check: "ls ~/Desktop/SandBox/*.md"
    pass_condition: "All 3 pointer files present"
    fail_action: "Create missing pointers"
  - name: Gate 3 - Workspace Root Files Created
    phase: Phase 3 - Workspace Root Files
    criteria:
      - AGENTS.md exists with directory map and quick rules
      - .hermes.md exists with profile/MCP/hook tables
      - CLAUDE.md exists as minimal stub
      - .cursorrules exists as minimal stub
    check: "ls ~/Desktop/SandBox/AGENTS.md ~/Desktop/SandBox/.hermes.md ~/Desktop/SandBox/CLAUDE.md ~/Desktop/SandBox/.cursorrules"
    pass_condition: "All 4 files present"
    fail_action: "Create missing files"
  - name: Gate 4 - Consistency Validated
    phase: Phase 4 - Validation
    criteria:
      - Zero duplication across files
      - All cross-references resolve
      - Authority hierarchy respected
      - Profile routing identical
      - Protocol references match
      - No legacy artifacts
    check: "Custom validation script"
    pass_condition: "All checks pass"
    fail_action: "Fix inconsistencies, re-validate"
dependencies:
  - context-files-spec.md
  - prompt-skill-spec-plan-management-system.md
---

# Context Files Rewrite Implementation Plan

## Overview

Rewrites all 7 context files following the authority hierarchy with zero duplication and full cross-reference consistency.

## Authority Hierarchy (Enforced)

```
SOUL.md (HIGHEST - Agent Identity & Behavior)
    ↓
USER.md (Operator Context & Preferences)
    ↓
MEMORY.md (Session Facts & Lessons)
    ↓
AGENTS.md (Workspace Guidance)
    ↓
.hermes.md (Project Overrides)
    ↓
CLAUDE.md / .cursorrules (IDE-Specific Stubs)
```

## File Locations

### Canonical (Profile Directory)
- `/c/Users/Alexa/AppData/Local/hermes/profiles/default/SOUL.md`
- `/c/Users/Alexa/AppData/Local/hermes/profiles/default/USER.md`
- `/c/Users/Alexa/AppData/Local/hermes/profiles/default/MEMORY.md`

### Workspace Root (SandBox)
- `/c/Users/Alexa/Desktop/SandBox/SOUL.md` (copy of canonical)
- `/c/Users/Alexa/Desktop/SandBox/USER.md` (pointer to canonical)
- `/c/Users/Alexa/Desktop/SandBox/MEMORY.md` (pointer to canonical)
- `/c/Users/Alexa/Desktop/SandBox/AGENTS.md` (master workspace guidance)
- `/c/Users/Alexa/Desktop/SandBox/.hermes.md` (project overrides)
- `/c/Users/Alexa/Desktop/SandBox/CLAUDE.md` (Claude stub)
- `/c/Users/Alexa/Desktop/SandBox/.cursorrules` (Cursor stub)

## Content Requirements

### SOUL.md (Master)
All sections from context-files-spec.md REQ-CF-001:
- Core Operating Principles
- Persona, Cognitive Style
- Execution Frameworks (Plans, Prompts, Skills, Hooks)
- Architectural Invariants
- Standing Rules (13)
- Memory Hierarchy
- 4 Mandatory Rules
- Multi-File Change Protocol (14-skill stack)
- Profile Routing Table

### USER.md (Preferences)
- Identity, Environment Stack, Model Config
- Execution Preferences (communication, code, skills, hooks, profile routing)
- Standing Goal (prompt library maintenance)
- Multi-File Protocol Reference
- Honcho Memory Status
- Session Info

### MEMORY.md (Facts)
- §-delimited facts only
- No headings (MD041 compliance)
- Environment facts, lessons, conventions
- NO task progress, session outcomes, TODOs
- NO procedures/workflows

### AGENTS.md (Workspace)
- Directory map
- Quick Rules (numbered)
- Toolchain commands
- Project structure
- Verified model chain
- Subproject references
- Deferral to SOUL.md

### .hermes.md (Overrides)
- Profile table
- MCP/hook/plugin commands
- Live provider/model commands
- Session startup (5 skills)
- Profile routing table
- Multi-file protocol reference
- File hierarchy table
- MCP servers & tools priority table

### CLAUDE.md (Stub)
- Thin deferral to AGENTS.md
- MCP tool preferences
- Multi-file protocol reference

### .cursorrules (Stub)
- Thin deferral to AGENTS.md
- Code style preferences
- Multi-file protocol reference

## Verification Gates

4 gates with measurable pass/fail criteria. All must pass before Skill Enhancement phase can complete.