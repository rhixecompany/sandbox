# boost-prompt — Context Catalog

Generated: 2026-05-25 | Source file: .github/prompts/boost-prompt.prompt.md

## Purpose & Trigger

- **Trigger**: `/boost-prompt`
- **Purpose Slug**: `boost-prompt`
- **Description**: Interactive prompt refinement workflow: interrogates scope, deliverables, and constraints, then copies final markdown to clipboard using Joyride.
- **Tags**: hermes, copilot, opencode, prompt-engineering, refinement, joyride
- **Special Requirements**: Joyride VS Code extension (for clipboard operations)

## File Inventory

| # | Path | Type | Status | Size |
| --- | ---- | ---- | ------ | ---- |
| 1 | .github/prompts/boost-prompt.prompt.md | Markdown (Hermes Prompt) | Active | 3.9 KB |

## Frontmatter Summary

```yaml
trigger: /boost-prompt
description: >-
  Interactive prompt refinement workflow: interrogates scope, deliverables, and constraints, 
  then copies final markdown to clipboard using Joyride.
tags:
  [hermes, copilot, opencode, prompt-engineering, refinement, joyride]
dependencies:
  - skill:prompt-engineering
  - skill:writing-plans
skills:
  - prompt-engineering — Research-backed prompt optimization patterns
  - writing-plans — Structured prompt authoring
```

**Validation**: ✓ All required fields present

## Dependencies Declared

### Direct Dependencies

| Type | Name | Purpose | Status |
| --- | ---- | ---- | ------ |
| Skill | `prompt-engineering` | Research-backed prompt optimization patterns | External (not verified) |
| Skill | `writing-plans` | Structured prompt authoring and organization | External (not verified) |
| Tool (implicit) | `joyride_request_human_input` | Interrogate user for clarification | Referenced in Phase 1 |
| Tool (implicit) | Joyride/VS Code clipboard API | Copy final markdown to clipboard | Referenced in Phase 3 |

### Reference Sources

- **Joyride integration**: Described in Phase 3, step 1 — uses vscode clipboard API
- **Human input**: Phase 1 step 2 references `joyride_request_human_input` for interrogation
- No @agent references
- No /trigger references to other prompts

## Reverse Dependencies & Cross-File References

### Forward References TO This Prompt

**In docs/**:
- `docs/boost-prompt-context.md` — (this file)
- `docs/boost-prompt-issues-context.md` — Issues catalog
- `docs/boost-prompt-verify-context.md` — Verification report

**In .opencode/**:
- No direct references in `.opencode/` configuration files

**In backups/**:
- `docs/prompt-backups/20260525-162517Z/Prompts/bash-scripts-fix.prompts.md` — Listed as available prompt
- `docs/prompt-backups/20260525-162517Z/Prompts/general.prompts.md` — Listed as available prompt
- `docs/prompt-backups/20260525-162517Z/Prompts/repo.prompts.md` — Listed as available prompt

## Content Structure Audit

### Sections Present

| Section | Lines | Status |
| --- | ---- | ------ |
| YAML Frontmatter | 13 | ✓ Complete |
| Goal | 2 | ✓ Present |
| Context | 4 | ✓ Present (with critical rules) |
| Inputs | 3 | ✓ Present |
| Outputs | 3 | ✓ Present |
| Rules | 6 | ✓ Present (includes "No code" rule) |
| Skills Required | 4 | ✓ Present |
| Phases (4 phases) | 82 | ✓ Complete |
| Actions Summary | 6 | ✓ Present |

### Phase Breakdown

- **Phase 1: Interrogate** (lines 62-70) — Understand scope, objectives, deliverables, constraints
- **Phase 2: Refine** (lines 71-80) — Produce improved, well-structured prompt
- **Phase 3: Deliver** (lines 81-95) — Deliver prompt to user and system clipboard via Joyride
- **Phase 4: Iterate** (lines 96-104) — Confirm satisfaction and handle revisions

## Unique Characteristics

### Critical Safety Rule (Lines 27-30)

```
Critical rules (must appear within the first 15% of execution):
- DO NOT WRITE ANY CODE — this is a prompt refinement workflow only
- Always ask clarifying questions before finalizing the prompt
- Copy the final markdown to clipboard using Joyride after each revision
```

**Location**: Line 27 explicitly in Context section  
**Visibility**: High — positioned early for compliance  
**Purpose**: Prevent users from misusing prompt as code generation tool

### Joyride Integration (Phase 3)

The prompt requires Joyride VS Code extension:
- **Phase 3, Step 1**: Code snippet using `(vscode/env.clipboard.writeText "...")`
- **Clojure syntax**: Uses Joyride's Clojure-based API
- **Dependency**: Assumes Joyride is installed and accessible

## Content Quality Notes

- **Consistency**: High — follows template patterns
- **Completeness**: All outputs described in phases
- **Clarity**: Clear workflow from interrogation through iteration
- **Markdown**: Proper tables and code block formatting
- **Line count**: 112 lines total (compact, focused)
- **Safety**: Emphasizes "no code" rule prominently

## Cross-File Consistency

### Comparison with Related Prompts

Similar structured prompts in directory:
- `context-map.prompt.md` — Follows same 4-phase pattern ✓
- `ai-prompt-engineering-safety-review.prompt.md` — Follows same pattern ✓

**Consistency Score**: Excellent — matches established template

## External Dependencies Check

| Dependency | Type | Verified | Status |
| --- | --- | --- | --- |
| skill:prompt-engineering | Skill | No | Not found in audit |
| skill:writing-plans | Skill | No | Not found in audit |
| Joyride VS Code extension | Tool | No | Assumed installed by user |
| joyride_request_human_input | Function | No | Assumed available in Joyride |

## Dependency Map

```
boost-prompt.prompt.md
├── skill:prompt-engineering (external)
├── skill:writing-plans (external)
└── Joyride (VS Code extension, external)
    └── joyride_request_human_input
    └── vscode.env.clipboard API
```

## Historical References

Prompt is referenced in:
- Historical prompts inventory (prompt-backups dated 2026-05-25)
- Described as: "Use when the prompt needs a stronger structure and clearer intent."

## Status Summary

| Aspect | Finding |
| --- | --- |
| Frontmatter | ✓ Valid |
| Structure | ✓ Complete |
| Dependencies | ✓ Declared (2 skills) |
| External Tools | ⚠ Joyride references (unverified) |
| Critical Rules | ✓ Present and visible |
| Internal References | ✓ Self-contained |
| Cross-file Refs | ✓ Appears in 3 backup indexes |
| Markdown Format | ✓ Proper |
| Content Flow | ✓ Clear |

## Recommendations for Next Phase

1. Verify that `skill:prompt-engineering` and `skill:writing-plans` exist
2. Document Joyride version requirements and installation steps
3. Create a guide for using Joyride clipboard API with this prompt
4. Add example interrogation questions for Phase 1
5. Add example prompts before/after refinement
6. Document fallback procedure if Joyride is unavailable
