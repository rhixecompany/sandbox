---
name: session-history-audit
title: Session History Audit
description: Generate comprehensive audit reports across all Hermes sessions by querying the SQLite state database directly. Use when the user asks for multi-session audits, session statistics, or full-history reports.
version: 1.0.0
author: Alexa
license: MIT
tags:
  - session
  - audit
  - history
  - sqlite
  - reporting
---
# Session History Audit

## Overview

Query Hermes' SQLite state database (`~/AppData/Local/hermes/state.db`) directly to generate comprehensive session audit reports. The native `session_search` tool's browse mode caps at 10 results — direct SQL is required for full-history analysis.

## When Use

- User asks for "all sessions", "full history", "session statistics", or "audit across N sessions"
- User wants session counts, model usage breakdowns, or activity timelines
- The native `session_search(limit=N)` browse mode returns fewer results than expected
- Generating SESSION_REPORT.md with scope beyond the last session

## When NOT to Use

- For single-session audit (use `session-audit-report` skill instead)
- For searching session content by keyword (use `session_search(query=...)` discovery mode)
- For reading a specific session's messages (use `session_search(session_id=...)` scroll mode)

## Database Schema

**Location**: `~/AppData/Local/hermes/state.db`

### Tables

| Table | Purpose |
|-------|---------|
| `sessions` | Session metadata (id, title, source, model, timestamps, counts) |
| `messages` | Individual messages per session (role, tool_name, content) |
| `session_model_usage` | Per-model usage per session (tokens, cost, first/last seen) |
| `messages_fts` | Full-text search index over messages |
| `state_meta` | Key-value state |
| `schema_version` | DB schema migration tracking |
| `compression_locks` | Compression state |

### Key Columns in `sessions`

| Column | Type | Description |
|--------|------|-------------|
| `id` | TEXT | Session ID (format: `YYYYMMDD_HHMMSS_hash`) |
| `title` | TEXT | Session title (may be NULL) |
| `source` | TEXT | Origin: `cli`, `tui`, `subagent`, `acp` |
| `model` | TEXT | Full model identifier |
| `started_at` | REAL | Unix timestamp |
| `ended_at` | REAL | Unix timestamp |
| `message_count` | INTEGER | Number of messages |
| `tool_call_count` | INTEGER | Number of tool calls |
| `api_call_count` | INTEGER | Number of API calls |
| `input_tokens` | INTEGER | Input token count |
| `output_tokens` | INTEGER | Output token count |
| `archived` | INTEGER | 0 = active, 1 = archived |
| `cwd` | TEXT | Working directory |

### Key Columns in `messages`

| Column | Type | Description |
|--------|------|-------------|
| `session_id` | TEXT | FK to `sessions.id` |
| `role` | TEXT | `user`, `assistant`, `tool` (also `session_meta`) |
| `content` | TEXT | Message body |
| `tool_name` | TEXT | Tool name on `role='tool'` rows (count directly) |
| `timestamp` | REAL | Unix epoch float |

Tool-usage per session: `SELECT tool_name, COUNT(*) FROM messages WHERE session_id=? AND role='tool' GROUP BY tool_name`. Loaded skills appear as `/slash-name` tokens inside `user` role content: `re.findall(r"(?<!\w)/([A-Za-z][A-Za-z0-9-]+)", content)`.

### Read-Only Connection Pattern

Always open read-only — Hermes may hold a write lock while a session is active:

```python
import sqlite3
con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=5)
con.row_factory = sqlite3.Row
# ... queries ...
con.close()
```

Latest-session queries should filter `WHERE archived != 1 ORDER BY started_at DESC LIMIT 1`.

## Workflow

### Step 1: Query Aggregate Statistics

```sql
SELECT 
    COUNT(*) as total_sessions,
    SUM(message_count) as total_messages,
    SUM(tool_call_count) as total_tools,
    SUM(api_call_count) as total_api_calls,
    SUM(input_tokens) as total_input_tokens,
    SUM(output_tokens) as total_output_tokens
FROM sessions;
```

### Step 2: Query Model Distribution

```sql
SELECT model, COUNT(*) as cnt 
FROM sessions 
GROUP BY model 
ORDER BY cnt DESC;
```

### Step 3: Query Activity by Date

```sql
SELECT date(started_at, 'unixepoch') as d, COUNT(*) as cnt 
FROM sessions 
GROUP BY d 
ORDER BY d ASC;
```

### Step 4: Query Largest Sessions

```sql
SELECT id, title, message_count, tool_call_count, source, model
FROM sessions 
WHERE title IS NOT NULL 
ORDER BY message_count DESC 
LIMIT 20;
```

### Step 5: List All Sessions (for full enumeration)

```sql
SELECT id, title, source, model, started_at, message_count, tool_call_count
FROM sessions 
ORDER BY started_at ASC;
```

### Step 6: Generate Report

Write `SESSION_REPORT.md` in cwd with:
- Overview table (totals)
- Source breakdown
- Model distribution
- Daily activity timeline
- Busiest days
- Top N largest sessions
- Session themes by period (if discernible from titles)
- Notable patterns

## Execution Method

Use `terminal` with Python (NOT execute_code — `hermes_tools` does not export `session_search`):

```python
import sqlite3, os
from datetime import datetime

db = sqlite3.connect(os.path.expanduser(os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes/state.db"))
cursor = db.cursor()
cursor.execute("SELECT ... FROM sessions ...")
# Process results
db.close()
```

## Scripting Notes

- Default implementation can use `terminal` + Python stdlib `sqlite3`; Node-based runs should use `better-sqlite3` only if already available in the workspace env, otherwise fall back to Python.
- Common fallback failure: `Cannot find module 'better-sqlite3'`. Treat that as environment state, not a durable constraint; recover with Python `sqlite3`.
- Long report outputs should be written to a file rather than streamed inline to avoid truncation.

## Output Convention

- Preferred output file: `SESSION_AUDIT_227.md` in the workspace root when the user explicitly requests an audit of all sessions.
- Include headline totals: total sessions, total messages, source breakdown, model distribution, first seen, last seen, top sessions, and full session table.


## When to Use

- Use when _(describe scenario 1)_
- Use when _(describe scenario 2)_
- Use when _(describe scenario 3)_


## Pitfalls

- **Test artifacts pollute JSONL-based report generation.** `logs/sessions/` can contain hook-testing files (`e2e-test.jsonl`, `test001.jsonl`, `errors.jsonl`, `v.jsonl`) that are NOT real sessions. `generate_session_report.py` picks the most recently modified file and can emit corrupt output (Session ID `e2e-test`, model `unknown`). When this happens, fall back to manual report writing via `session_search(limit=3, sort=newest)` — do not trust the script's placeholder output.
- **`on_session_end` at hermes root may be a stale text file.** The real session-end capture is config.yaml `hooks.on_session_end` → `hooks/session-logger/log-session-end.sh` (stdin JSON payload → `logs/sessions/<id>.jsonl`). Verify the hook with a crafted payload and check the JSONL row.
- **State.db session count is authoritative, not cited totals.** Query `state.db` directly for session counts (175 as of 2026-07-31); user-cited numbers like "227" can be stale.
- **session_search browse mode caps at 10**: Always use direct SQL for full-history queries
- **session_search not in execute_code**: The `hermes_tools` module does not export `session_search`; use `terminal` with Python instead
- **Timestamps are Unix floats**: Use `datetime.fromtimestamp()` for formatting. A raw float passed into a table row crashes with `TypeError: sequence item 1: expected str instance, float found` — always coerce before rendering.
- **User-cited session/item counts are approximate**: When the user cites a total count (e.g., '227 sessions'), verify it first with SQL/`find`. Report actual vs. cited counts before gating work on that number.
- **Model names vary**: Same model may appear under slightly different names (e.g., `nemotron-3-ultra:free` vs `nemotron-3-ultra-free`); normalize by splitting on `/` and taking the last segment
- **NULL titles are common**: Many sessions have NULL titles; filter with `WHERE title IS NOT NULL` when analyzing by title
- **Windows path**: Use `os.path.expanduser('~/AppData/Local/hermes/state.db')` for cross-compatibility
- **Report size**: Full session tables can exceed output caps. Always write to file and summarize totals inline.

## Verification

- [ ] Total session count matches expected (ask user if they cited a number)
- [ ] Report written to SESSION_REPORT.md in cwd
- [ ] All aggregate stats included
- [ ] Date range covers full history
- [ ] Model distribution accurate

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has >=3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md under 250 lines
- [ ] No placeholder text

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
