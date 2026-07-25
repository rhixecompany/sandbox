---
author: Hermes Agent
description: Comprehensive prompt quality audit and enhancement pipeline. Audits frontmatter, structure, content quality, and safety; then applies automated fixes for frontmatter corruption, missing sections, heading hierarchy, and boilerplate. Supports batch processing with configurable quality thresholds.
license: MIT
metadata:
  hermes:
    related_skills:
    - audit-prompts
    - prompt-builder
    - boost-prompt
    - convert-plaintext-to-md
    - ai-prompt-engineering-safety-review
    tags:
    - prompts
    - quality
    - audit
    - enhancement
    - batch
name: boost-prompts
tags:
- prompts
- quality
- audit
- enhancement
- batch
- pipeline
title: Boost Prompts Pipeline
version: 1.0.0
---

# Boost Prompts Pipeline

## Overview

End-to-end prompt quality pipeline: audit → fix → enhance → verify. Combines structural audit, safety review, and quality boosting in a single workflow with configurable thresholds and batch processing.

## When to Use

- Full prompt library refresh
- Pre-release quality gate
- Migrating legacy prompts to current standard
- Periodic library maintenance

## When NOT to Use

- Single prompt fixes (use individual skills)
- TXT→MD conversion only (use `convert-plaintext-to-md`)
- Safety review only (use `ai-prompt-engineering-safety-review`)

## Pipeline Stages

### Stage 1: Structural Audit (`audit_prompts.py`)

```bash
python $LOCALAPPDATA/hermes/scripts/audit_prompts.py \
  --workspace . \
  --threshold 70 \
  --output docs/prompt-audit-report.md
```

**Outputs:** Per-file scores (7 criteria), pass/fail summary, broken refs, duplicate triggers.

### Stage 2: Safety Review (`ai_prompt_engineering_safety_review.py`)

```bash
python $LOCALAPPDATA/hermes/scripts/ai_prompt_engineering_safety_review.py \
  --input docs/prompt-audit-report.md \
  --output docs/prompt-safety-report.md
```

**Checks:** Credential handling, approval workflows, destructive ops, fabricated verification, backup/rollback instructions.

### Stage 3: Automated Fixes (`fix_prompts.py`)

```bash
# Fix all auto-fixable issues
python $LOCALAPPDATA/hermes/scripts/fix_prompts.py --all

# Fix specific categories
python $LOCALAPPDATA/hermes/scripts/fix_prompts.py --frontmatter --sections --headings

# Fix specific files
python $LOCALAPPDATA/hermes/scripts/fix_prompts.py --files "prompts/a.prompt.md,prompts/b.prompt.md"
```

**Fix categories:**
- `frontmatter` — YAML corruption, missing fields, inline arrays
- `sections` — Missing required sections (Goal, Phases, etc.)
- `headings` — Skipped levels, inconsistent hierarchy
- `boilerplate` — Unreplaced template text
- `code-blocks` — Missing language tags
- `refs` — Broken relative paths

### Stage 4: Quality Boost (`boost_prompt.py`)

```bash
# Boost all prompts
python $LOCALAPPDATA/hermes/scripts/boost_prompt.py --all --threshold 85

# Boost specific files
python $LOCALAPPDATA/hermes/scripts/boost_prompt.py --files "prompts/a.prompt.md"
```

**Enhancements:** Rule strengthening, frontmatter enrichment, section reorganization, redundancy removal, instruction ratio optimization.

### Stage 5: Re-verification

```bash
python $LOCALAPPDATA/hermes/scripts/audit_prompts.py \
  --workspace . \
  --threshold 85 \
  --output docs/prompt-final-report.md
```

## Script Reference

| Script | Purpose | Location |
|--------|---------|----------|
| `audit_prompts.py` | Structural quality audit | `~/AppData/Local/hermes/scripts/` |
| `ai_prompt_engineering_safety_review.py` | Safety compliance check | `~/AppData/Local/hermes/scripts/` |
| `fix_prompts.py` | Automated structural fixes | `~/AppData/Local/hermes/scripts/` |
| `boost_prompt.py` | Quality enhancement | `~/AppData/Local/hermes/scripts/` |
| `normalize_prompt_actions.py` | Action section normalization | `~/AppData/Local/hermes/scripts/` |
| `validate_prompts.py` | Frontmatter/schema validation | `~/AppData/Local/hermes/scripts/` |
| `prompt_inventory.py` | Library inventory & catalog | `~/AppData/Local/hermes/scripts/` |

## Pitfalls

- **Bundled scripts may be missing or mis-targeted** — `boost_prompt.py` (the Stage 4 enhance step) is **ABSENT** from `~/AppData/Local/hermes/scripts/`. `audit_prompts.py` / `fix_prompts.py` are **hardcoded** to `C:/Users/Alexa/Desktop/SandBox/Prompts/` (and `.github/prompts/`) and ignore `--workspace`, so against the live `~/AppData/Local/hermes/prompts/` library they audit **0 files**. Do NOT assume the pipeline scripts run as written. Drive enhancement via a **read-only analysis pass** (score each prompt against the criteria below, emit concrete file-specific suggestions) or a **deterministic Python frontmatter repair** — see `prompt-library-maintenance` and its `references/prompt-repair-technique.md`. Never fabricate an "enhanced" result when the script is absent; report the gap and offer the manual path.
- **Enhancement mutates working prompts** — Apply boosts only after the library passes schema/integrity verification (e.g. 211/211 clean via `verify_prompt_library.py`). Prefer read-only suggestion reports first; gate actual edits behind user confirmation so a verified-clean library isn't regressed.
- **False-positive safety/structure flags** — A safety scan that matches the literal words "System Prompt" inside a heading/title is a FALSE POSITIVE, not an injection attempt. A gated `rm -rf` (with verify/confirm/approval nearby) is intentional cleanup, not a defect. Heading-less "You are ..." persona prompts are valid Copilot-style prompts. Apply the false-positive filters in `prompt-library-maintenance` before filing issues.

## Configuration

```yaml
# boost_pipeline_config.yaml
audit:
  threshold: 70
  pattern: "**/*.prompt.md"
safety:
  strict: true
  fail_on_critical: true
fixes:
  categories: [frontmatter, sections, headings, boilerplate, code-blocks, refs]
boost:
  target_threshold: 85
  enhance_rules: true
  normalize_structure: true
  remove_redundancy: true
```

## Related Skills

- `audit-prompts` — Standalone audit
- `prompt-builder` — Scaffold new prompts
- `convert-plaintext-to-md` — TXT→MD conversion
- `prompt-management` — Library operations