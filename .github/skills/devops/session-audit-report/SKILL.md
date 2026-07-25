---
author: Hermes Agent
description: At session start, audit the last session and generate SESSION_REPORT.md
  in cwd. Priority rule — never skipped. Summarizes tools, skills, insights from the
  previous session.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: session-audit-report
tags:
- session
- audit
- report
- hermes
title: Session Audit & Report Generation
version: 1.0.0

---
# Session Audit & Report

## Overview

Generate a session summary report at the beginning of every session.

> **For full-history audits** (all sessions, not just the last one), use the `session-history-audit` skill instead. It queries the SQLite database directly since `session_search` browse mode caps at 10 results.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-setup` | Configure Hermes home and session paths |

- **Always** — at session start, before any other work
- Triggered automatically by SOUL.md Core Rule 9
- **Part of mandatory 5-skill startup** — Must be loaded alongside `/using-superpowers`, `/user-communication-preferences`, `/hermes-profiles`, `/validate-memories`. Verify all 5 loaded before proceeding.

## Workflow

### Step 0: Verify Mandatory 5-Skill Startup

Before generating the session report, confirm all 5 mandatory skills are loaded:
- `/using-superpowers` ✓
- `/user-communication-preferences` ✓
- `/session-audit-report` ✓ (this skill)
- `/hermes-profiles` ✓
- `/validate-memories` ✓

If any missing → load immediately via skill tool.

### Step 1: Find Last Session

```
session_search(limit=3, sort=newest)
```

If no results → write placeholder report, stop.

### Step 2: Extract Session Data

```
session_search(session_id=<id>, around_message_id=<match_id>, window=30)
```

Extract from messages:
- Tools used (count calls per tool)
- Skills loaded/invoked
- User corrections, preferences, insights
- Tasks completed, blocked items, errors resolved

Prefer MCP-first recall paths:
- Use `session_search` for durable session history.
- Use `memory` for cross-session facts, user preferences, and project context.
- Use local JSONL under `C:/Users/Alexa/AppData/Local/hermes/logs/sessions` only as fallback.

### Step 3: Write Report

Write `SESSION_REPORT.md` in current working directory with this structure:

- After writing, immediately re-read the file and verify it contains the current session id, title, when, model, source, and a changelog row for every file changed in this session.
- If runtime model/provider metadata differs from the report or prior context, add an explicit correction in `Key Insights & Corrections` instead of leaving the mismatch implicit.

- After writing, immediately re-read the file and verify it contains the current session id, title, when, model, source, and a changelog row for every file changed in this session.
- If runtime model/provider metadata differs from the report or prior context, add an explicit correction in `Key Insights & Corrections` instead of leaving the mismatch implicit.

```markdown
# SESSION_REPORT.md

> Generated: <ISO_DATE> | cwd: `<path>`

## Last Session Summary
| Field | Value |
|-------|-------|
| Session ID | ... |
| Title | ... |
| When | ... |
| Model | ... |
| Source | ... |

## Tools Used
| Tool | Calls | Purpose |
|------|-------|---------|
| read_file | 8 | Read 4 profile files |
| write_file | 4 | Update profile files |
| ... | ... | ... |

## Skills Loaded
| Skill | Trigger |
|-------|---------|
| profile-maintenance | User invoked /profile-maintenance |
| ... | ... |

## Key Insights & Corrections
1. Finding 1
2. Finding 2

## Open Items
| Item | Status |
|------|--------|
| ... | ... |

## Errors Resolved
| Error | Fix |
|-------|-----|
| ... | ... |

## Session Changelog
| File | Action |
|------|--------|
| `path/to/file` | What changed |
```

**Key:** The "Session Changelog" section is critical — it lists every file modified/written during the session. This is the most useful section for the next session to understand what state changed.

### Step 4: Placeholder (No Prior Session)

If `session_search` returns no results:

```markdown
# SESSION_REPORT.md

No previous session found.
```

## Output

- File: `SESSION_REPORT.md` in cwd (always overwritten at session start)
- No return value — file is the deliverable

## Implementation

This skill provides Markdown formatting/rules, not a runnable script by itself. Use `scripts/generate_session_report.py` as a best-effort helper, but verify the output.

```text
devops/session-audit-report/scripts/generate_session_report.py
```

Example usage:

```bash
python scripts/generate_session_report.py --cwd "C:\\Users\\Alexa\\Desktop\\SandBox"
```

If the script emits placeholder/unknown fields despite a recent session existing, fall back to `session_search(limit=3, sort=newest)` plus a targeted `session_search(session_id=..., around_message_id=..., window=30)` scroll, then overwrite `SESSION_REPORT.md` manually with the real session ID, model, tools, and outcomes.

If no prior session is found, the script writes a minimal placeholder report.

## MCP Memory Integration

Session lifecycle hooks now mirror events to MCP memory for durable cross-session recall:
- `session-logger` writes session start/end/LLM events and mirrors them to MCP memory.
- `governance-audit` writes governance audits and mirrors them to MCP memory.
- `session-auto-commit` records auto-commit decisions and mirrors them to MCP memory.

Use `memory` to query these entities/sessions later instead of relying solely on JSONL files.

## Verification Checklist

- [ ] Last session found via session_search
- [ ] `scripts/generate_session_report.py` ran successfully
- [ ] SESSION_REPORT.md exists and contains required sections
- [ ] Session Changelog lists all modified files

## Pitfalls

- **Don't skip this.** It's a priority rule. Even if the user jumps straight into a task, generate the report first.
- **Don't make it long.** Crisp tables and bullets only. No prose walls.
- **Don't fabricate.** If session data is sparse, report what's there — don't invent insights.
- **Log files may not be one JSON object per line.** In this Windows install, `logs/sessions/*.jsonl` often contains pretty-printed multi-line JSON objects separated by whitespace. Use `json.JSONDecoder().raw_decode` to extract objects from arbitrary offsets; do not rely on `json.loads(line)`.
- **Windows MSYS path bleed (generate_session_report.py).** On Windows Git Bash (MSYS), `python /c/.../generate_session_report.py` may fail with `Errno 2` because the MSYS `/c/` prefix leaks into Python's path normalization. The script lives at `<hermes_skills>/devops/session-audit-report/scripts/generate_session_report.py`. If it fails: (1) verify the file exists with `ls -la`, (2) pass the absolute Windows-style path (not MSYS `/c/`). If it still fails, fall back to writing the report manually using the template in `references/manual-report-template.md` — this is the correct belt-and-suspenders path; the report is mandatory even when the script is down.
- **Prompt metadata corruption detection.** If prior session involved bulk prompt file edits, add a "Corruption Watch" section to the report checking for `promptmetadata` artifacts in `prompts/*.prompt.md` and YAML frontmatter array flattening. Run `grep -r "promptmetadata" prompts/ && echo "CORRUPTION FOUND"`.
- **Windows MSYS path bleed (generate_session_report.py).** On Windows Git Bash (MSYS), `python /c/.../generate_session_report.py` may fail with `Errno 2` because the MSYS `/c/` prefix leaks into Python's path normalization. The script lives at `<hermes_skills>/devops/session-audit-report/scripts/generate_session_report.py`. If it fails: (1) verify the file exists with `ls -la`, (2) pass the absolute Windows-style path (not MSYS `/c/`). If it still fails, fall back to writing the report manually using the template in `references/manual-report-template.md` — this is the correct belt-and-suspenders path; the report is mandatory even when the script is down.
- **Prompt metadata corruption detection.** If prior session involved bulk prompt file edits, add a "Corruption Watch" section to the report checking for `promptmetadata` artifacts in `prompts/*.prompt.md` and YAML frontmatter array flattening. Run `grep -r "promptmetadata" prompts/ && echo "CORRUPTION FOUND"`.
