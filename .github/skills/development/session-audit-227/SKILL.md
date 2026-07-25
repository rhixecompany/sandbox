---
name: session-audit-227
title: Session Audit 227
description: Node.js CJS script that generates a comprehensive Markdown audit report of all Hermes sessions from the state database
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - javascript
  - node
  - audit
  - sessions
  - cjs
  - database
---

# Session Audit 227

## Overview

Wrapper skill for the `session-audit-227.cjs` script in `~/AppData/Local/hermes/scripts/`. This Node.js script reads the Hermes SQLite state database (`state.db`) and generates a detailed Markdown audit report (`SESSION_AUDIT_227.md`) with session counts, message/tool/api call totals, token usage, model distribution, source breakdown, daily activity timeline, and top 20 largest sessions.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/session-audit-227.cjs`

**Extension:** `node`

**Usage:**
```bash
node session-audit-227.cjs
```

**Input:** `~/AppData/Local/hermes/state.db` (read-only)
**Output:** `SESSION_AUDIT_227.md` (in cwd)

## When to Use

- To get a comprehensive overview of all Hermes session history
- When analyzing token usage, model preferences, or tool usage patterns
- Before a workspace cleanup to understand session volume
- For reporting and documentation of Hermes usage

## When NOT to Use

- When you need live session data — the DB is read with read-only mode
- For individual session inspection — use `session_search` instead
- When the state.db doesn't exist (new Hermes install)

## Workflow

### Phase 1: Execute from SandBox root
```bash
cd ~/Desktop/SandBox
node $LOCALAPPDATA/hermes/scripts/session-audit-227.cjs
```

### Phase 2: Review
Check `SESSION_AUDIT_227.md` for:
- Overview table with totals
- Source and model breakdowns
- Daily activity timeline
- Top 20 sessions by message count
- Complete session list


### Phase 3: Phase 3

Document results, record any issues found, and verify output matches expected format.


### Phase 4: Final Review

Confirm all changes complete and produce summary report.

## Verification Checklist

- [ ] Script runs without errors (requires state.db to exist)
- [ ] `SESSION_AUDIT_227.md` is generated
- [ ] Overview table has non-zero values if sessions exist
- [ ] Model/source distributions total to 100%
- [ ] All session entries have valid timestamps
- [ ] No data truncation in the report

## Skills Required

| Skill | Purpose |
|-------|--------|
| `script-execution` | Run the script with appropriate runtime |
| `file-operations` | Read and write target files |
| `validation` | Verify output is correct |

## Pitfalls
- Requires `better-sqlite3` npm package — install with `npm install better-sqlite3` if missing
- The state.db path is hardcoded to `~/AppData/Local/hermes/state.db`
- The script opens the DB in read-only mode — won't work if Hermes holds a write lock
- The output file is written to `process.cwd()` — run from the SandBox root for consistent output location
- Large session counts (1000+) will generate a very long Markdown table (all sessions are listed)