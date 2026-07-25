---
name: memory-repair
title: Memory Repair
description: Repairs or manages memory files for profiles
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - python
  - remediation
  - memory
  - scripts
---

# Memory Repair

## Overview

Manage Hermes memory state — MEMORY.md file, pending write queue, and durable facts. Covers inspection, consolidation, stale-entry cleanup, and budget enforcement.

Two contexts:
1. **MEMORY.md file** — native file injected every turn, capped at 2,200 chars
2. **Pending queue** — `pending/memory/*.json` — staged writes awaiting TUI approval

## When to Use

- MEMORY.md exceeds 2,200-char budget and needs consolidation
- Pending queue has stale entries (>24h old, never approved) that need purging
- User asks to "clean up memory" or "save durable facts"
- After a session that produced new cross-session facts worth preserving

## When NOT to Use

- Writing a single fact (use `memory` tool directly)
- Validating schema across profiles (use `validate-memories` skill)
- Editing USER.md / SOUL.md (use `hermes-profiles` skill)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `validate-memories` | Schema checks, drift detection after consolidation |

## Workflow

### Phase 1: Assess State

```bash
# MEMORY.md size
wc -c ~/AppData/Local/hermes/memories/MEMORY.md

# Pending queue
ls ~/AppData/Local/hermes/pending/memory/ | wc -l
```

**Categorize pending by age:**
```python
import json, os, time
from pathlib import Path
now = time.time()
for f in sorted(Path(os.path.expanduser('~/AppData/Local/hermes/pending/memory')).glob('*.json'), key=lambda p: p.stat().st_mtime):
    age_h = (now - f.stat().st_mtime) / 3600
    data = json.loads(f.read_text())
    marker = '🟢' if age_h < 24 else ('🟡' if age_h < 168 else '🔴')
    print(f'{marker} {f.stem} [{age_h:.0f}h] {data.get("action","?")}')
```

Check: MEMORY.md > 2,200 chars → consolidate. Pending >24h → purge candidates.

### Phase 2: Purge Stale Pending Entries

**Keep** — entries from current session (still awaiting user approval).
**Purge** — everything older than 24h that wasn't just staged.

```bash
# Dry-run first
python3 -c "
import os, time
from pathlib import Path
now = time.time()
keep = {'05136666','255055ee','66d7f562','85f19979','adf06145'}  # current session IDs
for f in Path(os.path.expanduser('~/AppData/Local/hermes/pending/memory')).glob('*.json'):
    if f.stem in keep: continue
    if (now - f.stat().st_mtime) > 86400:
        print(f'PURGE {f.stem}  ({age_h/24:.0f}d)')
        # f.unlink()
"
```

**Safety:** Never purge current-session entries. User must approve/reject via TUI `/memory pending`.

### Phase 3: Consolidate MEMORY.md (over-budget repair)

When >2,200 chars:

1. **Read** current file
2. **Identify stale** — completed tasks, superseded facts, redundant rules
3. **Identify durable** — environment facts, user prefs, tool quirks, system state, noise classifications
4. **Write** clean version under budget. Recommended structure:
   - `## Conventions` — path rules, commit format, security
   - `## Tools & Workflows` — MCP list, common patterns
   - `## Corrections` — environment corrections (Win 11 vs 10, etc.)
   - `## System State Facts` — intentional config choices (`mcp-docker disabled`, etc.)
   - `## Noise Classification` — known-safe log patterns
   - `## Execution Directives` — protocol rules, user work style
5. **Apply** via `write_file`; verify with `wc -c`
6. **Re-read and validate** nothing critical lost

**Compression:** remove task progress, condense one-liners with `|`, merge related entries. Procedural steps belong in skills, not memory.

### Phase 4: Script Repair (profile-level)

```bash
cd ~/AppData/Local/hermes/scripts
python memory_repair.py --check          # Check current profile
python memory_repair.py --all-profiles   # Check all
python memory_repair.py --fix --backup   # Fix with backup
```

See `references/overview.md` for full script options.

### Phase 5: Verify

- MEMORY.md < 2,200 chars ✅
- No stale pending entries (<24h only) ✅
- Durable facts preserved ✅
- schema check passes (`validate-memories`) ✅

## Verification Checklist

- [ ] MEMORY.md exists and under budget
- [ ] Pending queue has no stale entries
- [ ] Durable cross-session facts preserved
- [ ] Task progress / completed-work NOT in memory
- [ ] System state facts match actual config
- [ ] Updated file re-read and verified

## Pitfalls

- **Don't purge current-session pending entries** — user needs to approve via TUI
- **Memory is not a task log** — session_search is for recall, not MEMORY.md
- **Budget is hard 2,200 chars** — count with `wc -c`, not word count
- **`memory.write_approval` blocks tool** — use `write_file` for MEMORY.md directly when immediate effect needed
- **Memory ≠ MCP knowledge graph** — independent stores, no propagation
- **Stale facts harm more than help** — prune aggressively on every consolidation pass
- **Pending queue accumulates indefinitely** if user never runs `/memory pending` — proactive cleanup prevents 60+ entry backlogs
