---
name: phase4-reconstruct
title: Phase 4 Reconstruct
description: Node.js CJS script that checks existence and size of target files (scripts, docs, prompts) in the SandBox workspace
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - javascript
  - node
  - verification
  - cjs
  - project-health
---

# Phase 4 Reconstruct

## Overview

Wrapper skill for the `phase4-reconstruct.cjs` script in `~/AppData/Local/hermes/scripts/`. This Node.js script checks whether 10 specific target files exist in the SandBox workspace and reports their size if they do. It's designed as a post-reconstruction verification step.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/phase4-reconstruct.cjs`

**Extension:** `node`

**Usage:**
```bash
node phase4-reconstruct.cjs
```

**Workspace root:** `~/Desktop/SandBox`

**Targets checked:** batch_skill_judge.py, batch_remediate.py, benchmark_models.py, test_models.py, dedupe-report.md, remediation_report.md, consolidation-report.md, final-verification.md, and two prompt templates.

## When to Use

- After running reconstruction or remediation pipelines to verify artifact creation
- As a health check to confirm expected files exist after workspace operations
- When debugging missing files after batch operations

## When NOT to Use

- For general file discovery — use `search_files(target='files')`
- When you need detailed file content validation — the script only checks existence and size

## Workflow

### Phase 1: Execute
```bash
cd ~/Desktop/SandBox
node $LOCALAPPDATA/hermes/scripts/phase4-reconstruct.cjs
```

### Phase 2: Review
Output shows `TARGET_COUNT {n}` and `TARGET {path} :: {note}` for each target.


### Phase 3: Phase 3

Document results, record any issues found, and verify output matches expected format.


### Phase 4: Final Review

Confirm all changes complete and produce summary report.

## Verification Checklist

- [ ] Script runs without Node.js errors
- [ ] TARGET_COUNT matches expected number (10)
- [ ] Expected existing files show `exists {size}B`
- [ ] Missing files show `missing`
- [ ] Stats are correctly parsed (no `stat-error` entries)

## Skills Required

| Skill | Purpose |
|-------|--------|
| `script-execution` | Run the script with appropriate runtime |
| `file-operations` | Read and write target files |
| `validation` | Verify output is correct |

## Pitfalls
- The root path is hardcoded to `C:/Users/Alexa/Desktop/SandBox`
- Stat errors on existing files are reported as `stat-error` rather than a specific message
- Does not validate file content — only checks existence and file size
- The target list is hardcoded and includes specific prompt template paths