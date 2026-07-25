---
author: Hermes Agent
description: Audit all active Hermes sessions for resource usage, stale sessions, and cleanup opportunities. Supports automated cleanup with safety checks.
license: MIT
metadata:
  hermes:
    related_skills:
    - hermes-system-maintenance
    - session-audit-report
    - validate-memories
    tags:
    - sessions
    - audit
    - cleanup
    - maintenance
    - resource-management
name: session-audit
tags:
- sessions
- audit
- cleanup
- maintenance
- resource-management
- hermes
title: Session Audit
version: 1.0.0
---

# Session Audit

## Overview

Audit all active and recent Hermes sessions for resource usage (memory, CPU, disk), stale/abandoned sessions, and cleanup opportunities. Generates report with safety-checked cleanup recommendations.

## When to Use

- Periodic system maintenance
- Before major upgrades
- Resource pressure investigation
- Session hygiene

## Workflow

### Phase 1: Audit

```bash
python $LOCALAPPDATA/hermes/scripts/session_audit.py \
  --output docs/session-audit-report.md
```

### Phase 2: Cleanup

```bash
# Dry run
python $LOCALAPPDATA/hermes/scripts/session_audit.py --cleanup --dry-run

# Apply (with safety)
python $LOCALAPPDATA/hermes/scripts/session_audit.py --cleanup --max-age 7d
```

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/session_audit.py`

**Options:**
| Flag | Description |
|------|-------------|
| `--output` | Report output path |
| `--cleanup` | Enable cleanup mode |
| `--dry-run` | Show what would be cleaned |
| `--max-age` | Max session age (default: 7d) |
| `--force` | Bypass safety checks |

## Safety

- Never cleans active sessions
- Preserves sessions with uncommitted work
- Backups before removal
- Configurable age threshold

## Related Skills

- `hermes-system-maintenance` — Full system maintenance
- `session-audit-report` — Session reporting
- `validate-memories` — Memory validation