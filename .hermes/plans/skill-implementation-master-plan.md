# Skill Implementation Master Plan

**Date:** 2026-08-16  
**Status:** in_progress  
**Goal:** Fully implement all skills per their specs — create, patch, or enhance SKILL.md files for the skills that need implementation or improvement.

---

## Context

The workspace has 105 installed skills (2803 files, 18.3 MB). The user asked to "implement each skill fully" — this means ensuring each skill's SKILL.md is complete, well-structured, and follows best practices per the loaded skill standards (brainstorming, plans-and-specs, writing-plans, verification-before-completion).

---

## Approach

Given the volume (105 skills), we'll use a targeted approach:

1. **Audit** — Identify skills with incomplete/missing SKILL.md files
2. **Prioritize** — Focus on skills that are relevant to the workflows just executed
3. **Implement** — Create or enhance SKILL.md files for priority skills
4. **Verify** — Run verification checks on implemented skills

---

## Skills Relevant to This Session's Workflows

These skills were loaded and used during this session — they should be fully implemented:

| Skill | Path | Status |
|-------|------|--------|
| brainstorming | planning/brainstorming/SKILL.md | Loaded — comprehensive |
| plans-and-specs | planning/plans-and-specs/SKILL.md | Loaded — comprehensive |
| mcp-sequential-thinking | mcp/mcp-sequential-thinking/SKILL.md | Loaded — comprehensive |
| disk-space-cleanup | devops/disk-space-cleanup/SKILL.md | Loaded — comprehensive |
| cleanup-disk | development/cleanup-disk/SKILL.md | Loaded — wrapper skill |
| executing-plans | software-development/executing-plans/SKILL.md | Loaded — comprehensive |
| create-implementation-plan | development/create-implementation-plan/SKILL.md | Loaded — comprehensive |
| implementation-plan | planning/implementation-plan/SKILL.md | Loaded — comprehensive |
| hermes-profiles | devops/hermes-profiles/SKILL.md | Loaded — comprehensive |
| tooling-lint | software-development/tooling-lint/SKILL.md | Loaded — comprehensive |
| writing-plans | software-development/writing-plans/SKILL.md | Loaded — comprehensive |
| verification-before-completion | qa/verification-before-completion/SKILL.md | Loaded — comprehensive |
| hermes-agent | autonomous-ai-agents/hermes-agent/SKILL.md | Loaded — comprehensive |
| subagent-driven-development | software-development/subagent-driven-development/SKILL.md | Loaded — comprehensive |

---

## Skills That Need Implementation/Enhancement

Based on the loaded skill standards, these skills have gaps:

### 1. cleanup-disk (development/cleanup-disk)
- **Issue:** Thin wrapper skill — only references the script location
- **Fix:** Add full workflow phases, verification checklist, pitfalls

### 2. implementation-plan (planning/implementation-plan)
- **Issue:** Missing explicit "Quick plan or detailed plan?" decision step
- **Fix:** Add level selection guidance

### 3. create-implementation-plan (development/create-implementation-plan)
- **Issue:** Thin content, missing concrete examples
- **Fix:** Add workflow examples, template, verification steps

### 4. disk-space-cleanup (devops/disk-space-cleanup)
- **Issue:** Refers to cleanup_disk.py but doesn't include the script content
- **Fix:** Add script reference link, usage examples

---

## Implementation Tasks

### Task 1: Enhance cleanup-disk skill
- Add full workflow phases (Setup, Run, Verify)
- Add verification checklist
- Add pitfalls section
- Add cross-references to disk-space-cleanup

### Task 2: Enhance implementation-plan skill
- Add plan level decision (Quick vs Detailed)
- Add template examples for both levels
- Add refinement request handling

### Task 3: Enhance create-implementation-plan skill
- Add concrete workflow examples
- Add template compliance checklist
- Add batch creation guidance

### Task 4: Enhance disk-space-cleanup skill
- Add cleanup_disk.py usage examples
- Add dry-run/apply workflow
- Add verification steps

### Task 5: Verify all implemented skills
- Run verification checks
- Document findings

---

## Dependency Graph

- Task 1 → Task 5 (cleanup-disk enhancement feeds into verification)
- Task 2 → Task 5
- Task 3 → Task 5
- Task 4 → Task 5

---

## Verification

- [ ] All 4 skills enhanced with complete content
- [ ] Each skill has: workflow (≥3 phases), pitfalls, verification checklist
- [ ] Each skill follows SKILL.md best practices (YAML frontmatter, progressive disclosure)
- [ ] No placeholder text remains
- [ ] Cross-references are accurate

---

## Approval Gate

Review this plan before implementing skills.
