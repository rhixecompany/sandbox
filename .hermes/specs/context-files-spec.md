---
name: context-files-spec
title: "Context Files Specification"
description: "Complete rewrite requirements for 7 context files with cross-reference consistency"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - context-files
  - soul-md
  - user-md
  - memory-md
  - agents-md
  - claude-md
  - cursorrules
  - hermes-md
---

# Context Files Specification

## Overview

Defines the complete rewrite requirements for all 7 context files to ensure consistency, authority hierarchy, and zero legacy artifacts.

## Files to Rewrite (7 Total)

### 1. SOUL.md (Master - Agent Identity & Behavior)
**Location**: `/c/Users/Alexa/AppData/Local/hermes/profiles/default/SOUL.md` (canonical)
**Mirror**: `/c/Users/Alexa/Desktop/SandBox/SOUL.md` (workspace copy)
**Authority**: HIGHEST - All other files defer to SOUL.md

**Required Content**:
- [ ] Core Operating Principles (identity, persona, cognitive style)
- [ ] Execution Frameworks (plans, prompts, skills, hooks)
- [ ] Architectural Invariants (plan discipline, prompt integrity, skill bounds, hook guardrails)
- [ ] Standing Rules (13 rules)
- [ ] Memory Hierarchy table
- [ ] 4 Mandatory Rules (non-negotiable)
- [ ] Multi-File Change Protocol (≥5 files) with 14-skill stack
- [ ] Profile routing table
- [ ] Cross-profile sync rules

**Cross-References**:
- → USER.md (operator context)
- → MEMORY.md (agent notes)
- → AGENTS.md (workspace guidance)
- → .hermes.md (project overrides)
- → CLAUDE.md (Claude-specific)
- → .cursorrules (Cursor IDE)

### 2. USER.md (User Profile & Preferences)
**Location**: `/c/Users/Alexa/AppData/Local/hermes/profiles/default/USER.md` (canonical)
**Pointer**: `/c/Users/Alexa/Desktop/SandBox/USER.md` (workspace pointer)

**Required Content**:
- [ ] Identity (name, workspace, profile)
- [ ] Environment Stack (OS, runtimes, tooling)
- [ ] Model configuration (primary, fallback)
- [ ] Execution Preferences (communication, code, skills, hooks, profile routing)
- [ ] Standing Goal (prompt library maintenance)
- [ ] Multi-File Change Protocol (≥5 files)
- [ ] Honcho Memory status
- [ ] Session info (date, model, provider, platform)

**Cross-References**:
- ← SOUL.md (inherits persona rules)
- → MEMORY.md (companion store)
- → .hermes.md (project overrides)

### 3. MEMORY.md (Agent Notes & Environment Facts)
**Location**: `/c/Users/Alexa/AppData/Local/hermes/profiles/default/MEMORY.md` (canonical)
**Pointer**: `/c/Users/Alexa/Desktop/SandBox/MEMORY.md` (workspace pointer)

**Required Content**:
- [ ] §-delimited facts (no H1 headings - MD041 false positive)
- [ ] Environment facts (paths, versions, configs)
- [ ] Lessons learned (procedures, pitfalls)
- [ ] Standing conventions
- [ ] NO task progress, session outcomes, TODO state
- [ ] NO procedures/workflows (those belong in skills)

**Format Rules**:
- § delimiter between entries
- No markdown headings
- Declarative facts only (no imperative instructions)
- Compact, high-signal entries

**Cross-References**:
- ← SOUL.md (memory hierarchy)
- ← USER.md (companion store)

### 4. AGENTS.md (Canonical Workspace Guidance)
**Location**: `/c/Users/Alexa/Desktop/SandBox/AGENTS.md` (workspace root - MASTER)

**Required Content**:
- [ ] Directory map with all paths
- [ ] Quick Rules (numbered, concise)
- [ ] Toolchain commands (lint, typecheck, check, format)
- [ ] Project structure overview
- [ ] Model/Provider state (verified working chain)
- [ ] Subproject references
- [ ] Deferral to SOUL.md for agent behavior

**Cross-References**:
- ← SOUL.md (behavioral authority)
- → .hermes.md (project overrides)
- → CLAUDE.md / .cursorrules (thin stubs)

### 5. .hermes.md (Hermes Project Overrides)
**Location**: `/c/Users/Alexa/Desktop/SandBox/.hermes.md`

**Required Content**:
- [ ] Profile table with models/providers
- [ ] MCP servers (run command to list)
- [ ] Hooks (run command to list)
- [ ] Plugins (run command to list)
- [ ] Live provider/model state commands
- [ ] Session startup reference (5 mandatory skills)
- [ ] Profile routing table
- [ ] Multi-File Change Protocol reference
- [ ] File hierarchy table
- [ ] MCP servers & tools priority table

**Cross-References**:
- ← SOUL.md (project-level overrides)
- → AGENTS.md (general guidance)

### 6. CLAUDE.md (Claude-Specific Guidance)
**Location**: `/c/Users/Alexa/Desktop/SandBox/CLAUDE.md`

**Required Content**:
- [ ] Thin stub deferring to AGENTS.md
- [ ] MCP tool preferences
- [ ] Multi-file protocol reference
- [ ] Toolchain routing

**Format**: Minimal - only Claude-specific deviations

### 7. .cursorrules (Cursor IDE Rules)
**Location**: `/c/Users/Alexa/Desktop/SandBox/.cursorrules`

**Required Content**:
- [ ] Thin stub deferring to AGENTS.md
- [ ] Code style preferences
- [ ] Multi-file protocol reference
- [ ] Toolchain routing

**Format**: Minimal - only Cursor-specific deviations

## Requirements

### REQ-CF-001: Authority Hierarchy
```
SOUL.md (HIGHEST)
    ↓
USER.md (operator context)
    ↓
MEMORY.md (session facts)
    ↓
AGENTS.md (workspace guidance)
    ↓
.hermes.md (project overrides)
    ↓
CLAUDE.md / .cursorrules (IDE-specific)
```

### REQ-CF-002: No Duplication (DRY)
- Each fact appears in EXACTLY ONE file
- Other files use cross-references (links, not copies)
- Violation: Same rule in SOUL.md AND USER.md

### REQ-CF-003: No Legacy Artifacts
- Delete ALL existing versions before creating new
- Verify with git status only new files
- No backup files (.bak, .old, timestamped)

### REQ-CF-004: Consistency Checks
- All profile routing tables identical
- All multi-file protocol references identical
- All mandatory rules identical
- Model/provider info current

### REQ-CF-005: Format Standards
- SOUL.md: Full markdown with sections
- USER.md: YAML frontmatter + markdown sections
- MEMORY.md: §-delimited, no headings
- AGENTS.md: Markdown with directory map
- .hermes.md: Markdown with tables
- CLAUDE.md / .cursorrules: Minimal stubs

## Acceptance Criteria

### AC-CF-001: All 7 Files Exist and Current
- [ ] All 7 files present in correct locations
- [ ] All canonical/pointer pairs correct
- [ ] No missing files

### AC-CF-002: Zero Duplication
- [ ] No fact repeated across files
- [ ] All cross-references use links
- [ ] Grep confirms unique content

### AC-CF-003: Authority Respected
- [ ] SOUL.md rules not contradicted
- [ ] USER.md preferences not overridden
- [ ] AGENTS.md guidance consistent

### AC-CF-004: Cross-References Valid
- [ ] All internal links resolve
- [ ] Profile routing consistent
- [ ] Protocol references match

### AC-CF-005: Legacy Clean
- [ ] No .bak, .old, timestamped files
- [ ] Git shows only new versions
- [ ] No artifact pollution

## Verification Gates

### Gate 1: File Existence
- All 7 files present
- Canonical/pointer pairs correct

### Gate 2: Content Validation
- Required sections present
- No placeholder text
- Format standards met

### Gate 3: Cross-Reference Check
- All links resolve
- Routing tables identical
- Protocol references match

### Gate 4: Duplication Scan
- Grep for repeated content
- Verify DRY compliance
- Confirm unique facts per file

### Gate 5: Legacy Artifact Check
- No backup files
- Git status clean
- Only intended files modified

## Dependencies
- SOUL.md created first (authority source)
- USER.md/MEMORY.md in profile directory
- Workspace files in SandBox root

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Authority conflicts | High | High | Create SOUL.md first, others reference |
| Duplication creep | Medium | High | Automated grep validation |
| Pointer drift | Medium | Medium | Verify pointers after each write |
| Format inconsistency | Low | Medium | Template-driven creation |