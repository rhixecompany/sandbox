# Phase 1: Audit Context - update-implementation-plan.prompt.md

## File Overview
- **Source:** .github/prompts/update-implementation-plan.prompt.md
- **Type:** Hermes Copilot Prompt Template
- **Purpose:** Create or update implementation plans with structured sections and status badges
- **Lines:** 109 total
- **Size:** ~4KB

## Front Matter (YAML)
```yaml
trigger: /update-implementation-plan
description: Create or update an implementation plan...
tags: [hermes, copilot, opencode, planning, implementation]
dependencies:
  - skill:writing-plans
  - skill:plans-and-specs
skills:
  - writing-plans — Author structured implementation plans
  - plans-and-specs — Plan and spec management
```

## Content Structure

### Section 1: Title & Goal (Lines 14-20)
- Main title: `# update-implementation-plan`
- Quote block explaining purpose
- Goal section explaining plan creation/update

### Section 2: Context & Inputs (Lines 22-32)
- Usage context for when to invoke
- Input sources (workspace, diffs, specs, existing plans)

### Section 3: Template Variables (Lines 33-42)
- Definition table with 4 variables:
  - `<workspace_root>`: Absolute path
  - `<purpose>`: Slug derived from task
  - `<component>`: Target module
  - `<version>`: Plan version (v1, v2)
- Example: `C:\Users\Alexa\Desktop\Sandbox`

### Section 4: Outputs (Lines 44-47)
- Output path template: `<workspace_root>/plan/<purpose>-<component>-<version>.md`
- Verification note guidance

### Section 5: Rules (Lines 49-65)
- 5 numbered rules for implementation
- Status Mapping table with colors (brightgreen, yellow, blue, red, orange)

### Section 6: Skills Required (Lines 67-72)
- Table mapping skills to purposes

### Section 7: Phases (Lines 74-101)
- Phase 1: Assess
- Phase 2: Write or Update
- Phase 3: Verify
- Each with Goal and Steps

### Section 8: Actions Summary (Lines 103-109)
- 5-item action checklist

## Reference Analysis

### Forward References (Direct Links)
- `<workspace_root>` - variable used in multiple sections
- `<purpose>` - variable for plan file naming
- `<component>` - variable for plan file naming
- `<version>` - variable for plan file naming
- `writing-plans` - skill reference (dependencies)
- `plans-and-specs` - skill reference (dependencies)
- Status values: Planned, In progress, Completed, Deprecated, On Hold
- shields.io badge URL pattern mentioned

### Reverse References (What links to this file)
- Referenced by: `.github/workflows/` (if any automation triggers it)
- Referenced by: Any skill files that invoke `/update-implementation-plan`
- Referenced by: Implementation plan files created by this template

### External Dependencies
- Skill: `writing-plans`
- Skill: `plans-and-specs`
- Service: shields.io (for badge generation)

## Template Variable Usage Map

| Variable | Used In | Lines |
|----------|---------|-------|
| `<workspace_root>` | Output path, examples | 39, 46 |
| `<purpose>` | Output path example, meaning | 40, 46 |
| `<component>` | Output path example, meaning | 41, 46 |
| `<version>` | Output path example, meaning | 42, 46 |

## Configuration & Conventions

### Trigger
- Invoked via: `/update-implementation-plan` command
- Scope: Hermes Copilot environment
- Tags: hermes, copilot, opencode, planning, implementation

### Output Conventions
- Path: `<workspace_root>/plan/<purpose>-<component>-<version>.md`
- Format: Markdown with status badge
- Sections: Standardized (9 main sections)

### Status Badge Convention
- Format: `https://img.shields.io/badge/status-<url_encoded_status>-<color>`
- Color mapping:
  - Completed → brightgreen
  - In progress → yellow
  - Planned → blue
  - Deprecated → red
  - On Hold → orange

## Key Dependencies

### Skills Required
1. `writing-plans` - for authoring structured plans
2. `plans-and-specs` - for namespace management

### External Services
1. shields.io - for status badge generation

## Potential Cross-References

### Related Hermes Files
- Any plan files in `<workspace_root>/plan/` directory
- Skill files: `writing-plans`, `plans-and-specs`
- Related prompts in `.github/prompts/`

### Documentation
- No explicit links to external documentation
- Status badge format references shields.io API

## Summary Statistics

- **Total Lines:** 109
- **Code/Structured Content:** 4 tables + 3 phase sections
- **Variable Count:** 4 unique template variables
- **Dependencies:** 2 skills
- **External Services:** 1 (shields.io)
- **Sections:** 8 major sections + front matter
- **Rules:** 5 numbered rules + phase definitions
