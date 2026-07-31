# Session Audit Report

> Generated: 2026-07-31T20:14:33.389948+00:00 | hermes-home: `C:\Users\Alexa\AppData\Local\hermes`

## Summary

| Metric | Value |
|--------|-------|
| Session files | 7 |
| Active (last 1h) | 0 |
| Stale (> 7d) | 0 |
| DB-referenced (live) | 168 |
| Git dirty (preserve) | True |
| Total size | 3.1 KB |
| Reclaimable (stale) | 0.0 KB |

## Sessions

| File | Events | Session ID | Model | Status | Turns | Size | Modified (UTC) |
|------|--------|-----------|-------|--------|-------|------|----------------|
| e2e-test.jsonl | 1 | e2e-test | unknown | unknown | 0 | 171B | 2026-07-27 22:37 |
| test001.jsonl | 1 | test001 | deepseek-v4-flash-free | unknown | 0 | 213B | 2026-07-27 22:36 |
| errors.jsonl | 9 | unknown | — | unknown | 0 | 1290B | 2026-07-27 22:36 |
| v.jsonl | 3 | v | unknown | unknown | 0 | 639B | 2026-07-24 19:50 |
| verify.jsonl | 2 | verify | unknown | unknown | 0 | 436B | 2026-07-24 19:46 |
| test.jsonl | 1 | test | unknown | unknown | 0 | 216B | 2026-07-24 19:37 |
| verify-skip.jsonl | 1 | verify-skip | unknown | unknown | 0 | 174B | 2026-07-23 21:54 |

## Cleanup Recommendations

No stale sessions found. Nothing to clean.

## Safety Checks

- Active-session guard: **ON** (1h recency window)
- DB-liveness check: sessions referenced in `state.db` are never cleaned: **enabled**
- Files are backed up to `<hermes>/session-audit-backup-<ts>/` before removal
