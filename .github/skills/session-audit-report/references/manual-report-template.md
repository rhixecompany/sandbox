# Manual Session Report Template

Use when `scripts/generate_session_report.py` fails or produces corrupt output.

## Template

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

## When to Use

- `generate_session_report.py` fails with MSYS path bleed (Errno 2)
- Script returns corrupt session IDs (e.g., `"v"` from `v.jsonl`)
- JSONL logs are multi-line and `json.loads(line)` fails
- Any case where automated script output is unreliable

## Fallback Procedure

1. Run `session_search(limit=3, sort="newest")` to find last session
2. Run `session_search(session_id=..., around_message_id=..., window=30)` for detail
3. Extract tools, skills, insights, open items, errors, changelog manually
4. Write `SESSION_REPORT.md` using this template
5. Re-read and verify all required sections present