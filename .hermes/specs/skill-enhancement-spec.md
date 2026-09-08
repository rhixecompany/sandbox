---
name: skill-enhancement-spec
title: "Skill Enhancement Specification"
description: "Complete enhancement/refactoring requirements for 18 target skills"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - skill-enhancement
  - skill-quality
  - skill-judge
  - refactoring
---

# Skill Enhancement Specification

## Overview

Defines the complete enhancement requirements for 18 target skills to achieve skill-judge score ≥95 with full structural compliance.

## Target Skills (18 Total)

### Core Protocol Skills (14 - Mandatory for Multi-File Protocol)
1. **using-superpowers** - Foundational workflow
2. **brainstorming** - Structured ideation
3. **user-communication-preferences** - Alexa's execution style
4. **mcp-sequential-thinking** - Structured reasoning
5. **mcp-filesystem** - File operations
6. **mcp-ast-grep** - Code search/replace
7. **mcp-memory** - Persistent memory access
8. **plan** - Write markdown plan to .hermes/plans/
9. **plans-and-specs** - Draft implementation plans
10. **create-implementation-plan** - Create detailed plans
11. **implementation-plan** - Modify existing plans
11. **executing-plans** - Execute written plans
12. **writing-clearly-and-concisely** - Clear communication
13. **subagent-driven-development** - Parallel subagent delegation

### Quality Gate Skills (4 - Judge/Validation)
14. **prompts-judge** - Audit prompt quality
15. **specs-judge** - Audit spec quality
16. **plans-judge** - Audit plan quality
17. **plan-mode** - Plan mode execution

## Requirements

### REQ-SE-001: SKILL.md Structural Completeness
Each skill must have:
- [ ] Complete YAML frontmatter (name, title, description, version, author, license, tags, metadata)
- [ ] Description section with overview
- [ ] When to Use / When NOT to Use
- [ ] Skills Required table
- [ ] Workflow with ≥3 phases
- [ ] Pitfalls section (≥3 items)
- [ ] Best Practices section
- [ ] Verification Checklist (≥5 items)
- [ ] References to all linked files

### REQ-SE-002: References Directory
Each skill must have `references/` directory with:
- [ ] `overview.md` - Skill overview and architecture
- [ ] At least 2 domain-specific reference files
- [ ] Cross-references to related skills

### REQ-SE-003: Templates Directory
Each skill must have `templates/` directory with:
- [ ] At least 1 reusable template
- [ ] Template follows project conventions
- [ ] Template documented in SKILL.md

### REQ-SE-004: Scripts Directory
Each skill must have `scripts/` directory with:
- [ ] At least 1 validation/utility script
- [ ] Script is executable and tested
- [ ] Script documented in SKILL.md

### REQ-SE-005: Skill Judge Compliance
Each skill must pass skill-judge with:
- [ ] Frontmatter score ≥18/20
- [ ] Structure score ≥18/20
- [ ] Content score ≥16/20
- [ ] DRY score ≥16/20
- [ ] References score ≥11/15
- [ ] **Total ≥95/100**

### REQ-SE-006: No Placeholder Text
- [ ] No "TODO", "FIXME", "TBD", "placeholder"
- [ ] No "None identified yet" in pitfalls
- [ ] All sections have real content
- [ ] All examples are functional

### REQ-SE-007: Cross-Skill Consistency
- [ ] Shared patterns extracted to common references
- [ ] No duplicate workflows across skills
- [ ] Skill dependencies documented
- [ ] Profile routing consistent

## Acceptance Criteria

### AC-SE-001: All 18 Skills Enhanced
- [ ] All 18 target skills meet REQ-SE-001 through REQ-SE-006
- [ ] All skill-judge scores ≥95
- [ ] No skill has placeholder content

### AC-SE-002: Structural Consistency
- [ ] All SKILL.md files follow same structure
- [ ] All have references/, templates/, scripts/ directories
- [ ] Naming conventions consistent

### AC-SE-003: Integration Validated
- [ ] Multi-file protocol loads all 14 core skills
- [ ] Quality gates (judge skills) validate correctly
- [ ] Profile routing works for all task types

## Skill-Specific Requirements

### using-superpowers
- Add session startup protocol reference
- Add profile routing table
- Add MCP precedence rules
- Add skill library hygiene reference

### brainstorming
- Add ideation techniques reference
- Add decision documentation template
- Add feasibility matrix reference

### user-communication-preferences
- Add preferences.md reference with templates
- Add destructive command approval phrasing
- Add DRY violation examples

### mcp-sequential-thinking
- Add complex reasoning examples
- Add branching/revision patterns
- Add test cases for verification

### mcp-filesystem
- Add all 14 tool examples
- Add directory tree patterns
- Add error handling patterns

### mcp-ast-grep
- Add YAML rule examples
- Add rewrite patterns
- Add scan_code rule catalog

### mcp-memory
- Add knowledge graph patterns
- Add entity/relation templates
- Add search strategies

### plan
- Create from scratch (missing skill)
- Add plan file format spec
- Add phase templates
- Add gate definitions

### plans-and-specs
- Move detailed patterns to references/
- Add cross-platform patterns
- Add verification-before-completion integration

### create-implementation-plan
- Add batch creation workflow
- Add template compliance checklist
- Add spec-to-plan mapping

### implementation-plan
- Add detailed plan template
- Add dependency tracking
- Add risk/mitigation table

### executing-plans
- Add Phase 0 inventory verification
- Add approval gates for destructive changes
- Add batch execution patterns

### writing-clearly-and-concisely
- Ensure all 6 references exist
- Add editing checklist template
- Add before/after examples

### subagent-driven-development
- Add context budget discipline reference
- Add gates taxonomy reference
- Add red flags checklist

### prompts-judge / specs-judge / plans-judge
- Add rubric with specific criteria
- Add scoring calibration examples
- Add remediation patterns

### plan-mode
- Add plan-only execution workflow
- Add dry-run validation
- Add plan modification patterns

## Verification Gates

### Gate 1: Individual Skill Validation
- Run skill-judge on each skill
- Score ≥95 required
- Fix all Critical/High issues

### Gate 2: Cross-Skill Validation
- Load all 14 protocol skills together
- Verify no conflicts
- Test multi-skill workflow

### Gate 3: Integration Testing
- Execute multi-file protocol end-to-end
- Verify all gates pass
- Confirm context file consistency

## Dependencies
- skill-judge skill available
- All 18 skill directories exist
- MCP servers for validation

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Skill missing (plan) | High | High | Create from scratch first |
| Judge score < 95 | Medium | High | Iterative fix-verify loop |
| Placeholder text remains | Medium | Medium | Automated grep validation |
| Directory structure missing | Low | High | Scaffold all dirs first |