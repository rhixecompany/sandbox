---
author: Hermes Agent
description: Analyze differences between two project versions (branches, commits, or releases) to generate migration instructions for GitHub Copilot. Use when performing technology migrations, major refactoring, or framework version upgrades to create precise instructions that maintain consistency during code evolution.
license: MIT
metadata:
  hermes:
    tags: [imported, migration, code-evolution, copilot, refactoring]
name: generate-custom-instructions-from-codebase
tags:
- imported
- migration
- code-evolution
- copilot
- refactoring
- scripts
title: Generate Custom Instructions From Codebase
version: 1.1.0
---

# Migration and Code Evolution Instructions Generator

## Overview

Analyze differences between two project versions (branches, commits, or releases) to generate migration instructions for GitHub Copilot. Use when performing technology migrations, major refactoring, or framework version upgrades to create precise instructions that maintain consistency during code evolution.

## When to Use

- Technology migrations (e.g., Vue 2 → 3, .NET Framework → .NET Core)
- Major refactoring (architecture changes, pattern updates)
- Framework version upgrades
- Dependency updates with breaking changes
- Pattern changes across codebase

## When NOT to Use

- Simple bug fixes (use `systematic-debugging`)
- Writing new features from scratch (use `create-implementation-plan`)
- Code reviews (use `receiving-code-review`)

## Configuration Variables

```yaml
MIGRATION_TYPE: "Framework Version|Architecture Refactoring|Technology Migration|Dependencies Update|Pattern Changes"
SOURCE_REFERENCE: "branch|commit|tag"
TARGET_REFERENCE: "branch|commit|tag"
ANALYSIS_SCOPE: "Entire project|Specific folder|Modified files only"
CHANGE_FOCUS: "Breaking Changes|New Conventions|Obsolete Patterns|API Changes|Configuration"
AUTOMATION_LEVEL: "Conservative|Balanced|Aggressive"
GENERATE_EXAMPLES: "true|false"
VALIDATION_REQUIRED: "true|false"
```

## Workflow

### Phase 1: Comparative State Analysis

**Structural Changes Detection:**
- Compare folder structure between `${SOURCE_REFERENCE}` and `${TARGET_REFERENCE}`
- Identify moved, renamed, or deleted files
- Analyze changes in configuration files
- Document new dependencies and removed ones

**Code Transformation Analysis:**

```bash
# Framework Version
- Identify API changes between framework versions
- Analyze new features being used
- Document obsolete methods/properties
- Note syntax or convention changes

# Architecture Refactoring
- Analyze architectural pattern changes
- Identify new abstractions introduced
- Document responsibility reorganization
- Note changes in data flows

# Technology Migration
- Analyze replacement of one technology with another
- Identify functional equivalences
- Document API and syntax changes
```

### Phase 2: Generate Transformation Rules

Create structured rules for Copilot:

| Pattern | Before | After | Confidence |
|---------|--------|-------|------------|
| Import style | `import X from 'lib'` | `import { X } from 'lib'` | High |
| Method name | `oldMethod()` | `newMethod()` | High |
| Class component | `class X extends Component` | `function X()` | Medium |
| Lifecycle | `componentDidMount()` | `useEffect(() => {}, [])` | High |

### Phase 3: Generate Copilot Instructions

Output format:
```markdown
---
name: migration-{type}-{date}
description: "Apply {migration-type} patterns. Use when modifying files affected by {migration-type}."
trigger: ["migration", "{type}", "refactor"]
---

# Migration Instructions: {Type}

## Summary
{One paragraph description of the migration}

## Transformation Rules
{List of before/after patterns with examples}

## Files Affected
{List of file patterns or specific files}

## Validation
{How to verify the migration was applied correctly}

## Examples
{Code examples if GENERATE_EXAMPLES=true}
```

### Phase 4: Validate & Test

```bash
# Apply to test files
copilot apply --instructions migration-{type}.md --dry-run

# Verify output
diff expected/ actual/

# Commit if valid
```

## Verification Checklist

- [ ] Source and target references are valid
- [ ] All transformation rules have before/after examples
- [ ] Confidence levels assigned to each rule
- [ ] Dry-run produces expected output
- [ ] No false positives on unaffected files
- [ ] Validation passes if VALIDATION_REQUIRED=true

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `github` | Git operations |
| `copilot-sdk` | Apply instructions |

## Related Skills

- `create-implementation-plan` — Plan migrations
- `systematic-debugging` — Root cause analysis
- `copilot-sdk` — Apply generated instructions

## Usage Examples

```bash
# Generate migration instructions
generate-custom-instructions-from-codebase \
  --source main \
  --target feature/new-framework \
  --type "Framework Version" \
  --output migration-instructions.md

# Apply to specific scope
generate-custom-instructions-from-codebase \
  --source v1.0.0 \
  --target v2.0.0 \
  --scope "src/components" \
  --focus "Breaking Changes"
```

## Error Handling

- **Invalid git refs:** Exits with code 1, prints available refs
- **No changes found:** Warns, exits with code 0 (nothing to migrate)
- **Binary files skipped:** Warns, continues with text files only
- **Dry-run mode:** Uses `--dry-run` flag, outputs plan without writing

## Pitfalls

- **Over-broad rules:** Rules matching too many files cause false positives — scope rules with file patterns
- **Conflicting transformations:** Multiple rules may apply to same code — assign priority and validate order
- **Context loss:** Copilot may not see full file — include surrounding context in examples
- **Version drift:** Generated instructions become stale — regenerate after each major merge

## References

- `references/migration-patterns.md` — Common migration transformation patterns
- `references/copilot-instruction-format.md` — Instruction format specification