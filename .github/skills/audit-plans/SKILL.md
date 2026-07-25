---
author: Hermes Agent
description: Consolidate and audit all project plans in .hermes/plans/ directory. Normalizes statuses, detects duplicates/conflicts, merges related plans, and generates master plan index with execution order.
license: MIT
metadata:
  hermes:
    related_skills:
    - plans-and-specs
    - prompt-planning-orchestration
    - project-consolidation
    tags:
    - plans
    - audit
    - consolidation
    - project-management
name: audit-plans
tags:
- plans
- audit
- consolidation
- project-management
- hermes
title: Audit Plans
version: 1.0.0
---

# Audit Plans

## Overview

Consolidate and audit all project plans in `.hermes/plans/` directory. Normalizes statuses, detects duplicates/conflicts, merges related plans, and generates master plan index with execution order.

## When to Use

- Before starting new implementation work
- Periodic plan library maintenance
- Pre-release coordination
- Multi-agent workflow planning

## When NOT to Use

- Creating new plans (use `plans-and-specs` or `prompt-planning-orchestration`)
- Single plan updates (edit directly)

## Workflow

### Phase 1: Inventory

```bash
python $LOCALAPPDATA/hermes/scripts/normalize_plans.py \
  --plans-dir .hermes/plans \
  --output docs/plan-inventory.md
```

### Phase 2: Normalize & Merge

```bash
python $LOCALAPPDATA/hermes/scripts/normalize_plans.py \
  --plans-dir .hermes/plans \
  --normalize-status \
  --merge-related \
  --output .hermes/plans/
```

### Phase 3: Generate Master Index

```bash
python $LOCALAPPDATA/hermes/scripts/normalize_plans.py \
  --plans-dir .hermes/plans \
  --master-index docs/MASTER_PLAN_INDEX.md
```

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/normalize_plans.py`

**Options:**
| Flag | Description |
|------|-------------|
| `--plans-dir` | Plans directory (default: .hermes/plans) |
| `--normalize-status` | Standardize status values |
| `--merge-related` | Auto-merge plans with same target |
| `--master-index` | Generate master plan index |
| `--output` | Output directory |

## Status Normalization

| Input | Normalized |
|-------|------------|
| `in-progress`, `wip`, `working` | `in_progress` |
| `done`, `complete`, `finished` | `completed` |
| `pending`, `todo`, `planned` | `planned` |
| `blocked`, `stuck` | `blocked` |
| `cancelled`, `abandoned` | `cancelled` |

## Master Index Format

```markdown
# Master Plan Index

## Execution Order

| # | Plan | Status | Target | Depends On |
|---|------|--------|--------|------------|
| 1 | hermes-hooks-master-plan.md | completed | hooks | — |
| 2 | ecosystem-audit-plan.md | in_progress | skills | 1 |

## By Category

### Infrastructure
- ...

### Skills
- ...
```

## Related Skills

- `plans-and-specs` — Plan authoring
- `prompt-planning-orchestration` — Complex workflow planning
- `project-consolidation` — Multi-repo project cleanup