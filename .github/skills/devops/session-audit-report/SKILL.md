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

### Step 3: Write Report

Write `SESSION_REPORT.md` in current working directory with this structure:

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

## Verification Checklist

- [ ] Last session found via session_search
- [ ] Session data extracted (tools, skills, insights)
- [ ] SESSION_REPORT.md written with all sections
- [ ] Session Changelog lists all modified files
- [ ] Report is concise (no prose walls)

## Pitfalls

- **Don't skip this.** It's a priority rule. Even if the user jumps straight into a task, generate the report first.
- **Don't make it long.** Crisp tables and bullets only. No prose walls.
- **Don't fabricate.** If session data is sparse, report what's there — don't invent insights.
