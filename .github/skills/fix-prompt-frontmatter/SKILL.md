---
author: Hermes Agent
description: Audit and repair prompt frontmatter for schema compliance, required fields, tag formatting, and version consistency. Auto-fixes common issues with backup and verification.
license: MIT
metadata:
  hermes:
    related_skills:
    - validate-prompts
    - fix-prompts
    - audit-prompts
    - boost-prompts
    tags:
    - prompts
    - frontmatter
    - yaml
    - repair
    - schema
name: fix-prompt-frontmatter
tags:
- prompts
- frontmatter
- yaml
- repair
- schema
- compliance
title: Fix Prompt Frontmatter
version: 1.1.0
---

# Fix Prompt Frontmatter

## Overview

Repair prompt frontmatter corruption and schema violations: missing required fields, malformed YAML arrays, duplicate metadata blocks, tag format normalization, and version field consistency.

## When to Use

- After bulk prompt operations
- Frontmatter corruption from bad merges
- Schema migration (old → new frontmatter)

## When NOT to Use

- Content/structure fixes (use `fix-prompts`)
- Quality enhancement (use `boost-prompts`)

## Workflow

### Phase 1: Audit

```bash
python $LOCALAPPDATA/hermes/scripts/fix_copilot_frontmatter.py \
  --scan --workspace . \
  --output docs/frontmatter-issues.md
```

### Phase 2: Fix

```bash
# Dry run
python $LOCALAPPDATA/hermes/scripts/fix_copilot_frontmatter.py \
  --workspace . --dry-run

# Apply fixes
python $LOCALAPPDATA/hermes/scripts/fix_copilot_frontmatter.py \
  --workspace . --fix --backup
```

### Phase 3: Verify

```bash
python $LOCALAPPDATA/hermes/scripts/validate_prompts.py \
  --workspace . --threshold 90
```

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/fix_copilot_frontmatter.py`

**Options:**
| Flag | Description |
|------|-------------|
| `--scan` | List issues without fixing |
| `--fix` | Apply fixes |
| `--backup` | Create `.bak` files |
| `--normalize-tags` | Convert tags to lowercase kebab-case |
| `--dedupe-metadata` | Remove duplicate metadata blocks |

## Common Fixes

| Issue | Fix |
|-------|-----|
| `tags: - foo - bar` (inline) | Convert to YAML array |
| Duplicate `metadata:` blocks | Merge, keep first |
| Missing `trigger:` | Derive from filename |
| Tags not kebab-case | Normalize |
| Missing `version:` | Add `1.0.0` |
| Missing `scripts:` | Add `scripts: []` |
| Missing `skills:` | Infer from `dependencies:` `skill:` entries, or add `skills: []` |
| Missing `formatter:` | Add `formatter: default` |
| Missing `plan:` | Match against `hermes/plans/` by name similarity, or add `plan: ""` |
| Missing `toolset`/`toolsets:` | Add reasonable defaults based on prompt domain (e.g. `terminal`, `file`, `web`) |

## Related Skills

- `validate-prompts` — Schema validation
- `fix-prompts` — Structural fixes
- `boost-prompts` — Quality enhancement

## Reference Files

- `references/batch-field-retrofit.md` — Python batch fix pattern for adding frontmatter fields across 200+ prompts