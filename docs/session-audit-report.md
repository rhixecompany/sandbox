# Session Audit Report

> Generated: 2026-08-05T03:15:39.503871+00:00 | hermes-home: `C:\Users\Alexa\AppData\Local\hermes`

## Summary

| Metric | Value |
|--------|-------|
| Session files | 15 |
| Active (last 1h) | 1 |
| Stale (> 7d) | 6 |
| DB-referenced (live) | 95 |
| Git dirty (preserve) | True |
| Total size | 18.1 KB |
| Reclaimable (stale) | 1.8 KB |

## Sessions

| File | Events | Session ID | Model | Status | Turns | Size | Modified (UTC) |
|------|--------|-----------|-------|--------|-------|------|----------------|
| 20260629_091442_414845a4.jsonl | 12 | 20260629_091442_414845a4 | unknown | unknown | 0 | 2684B | 2026-08-05 02:40 |
| 20260804_210522_d570c6.jsonl | 3 | 20260804_210522_d570c6 | unknown | unknown | 0 | 643B | 2026-08-04 20:08 |
| 20260804_210134_c4829e.jsonl | 2 | 20260804_210134_c4829e | unknown | unknown | 0 | 419B | 2026-08-04 20:01 |
| 20260804_205704_2520bb.jsonl | 2 | 20260804_205704_2520bb | unknown | unknown | 0 | 419B | 2026-08-04 19:57 |
| 20260804_180634_5f3894.jsonl | 4 | 20260804_180634_5f3894 | unknown | unknown | 0 | 877B | 2026-08-04 17:22 |
| 20260801_153510_9247ec.jsonl | 5 | 20260801_153510_9247ec | unknown | unknown | 0 | 1091B | 2026-08-01 16:14 |
| test-session.jsonl | 10 | test-session | unknown | unknown | 0 | 2053B | 2026-08-01 14:41 |
| 20260801_072826_c72170.jsonl | 3 | 20260801_072826_c72170 | unknown | unknown | 0 | 702B | 2026-08-01 08:37 |
| errors.jsonl | 52 | test-session | — | unknown | 0 | 7813B | 2026-08-01 08:13 |
| e2e-test.jsonl | 1 | e2e-test | unknown | unknown | 0 | 171B | 2026-07-27 22:37 |
| test001.jsonl | 1 | test001 | deepseek-v4-flash-free | unknown | 0 | 213B | 2026-07-27 22:36 |
| v.jsonl | 3 | v | unknown | unknown | 0 | 639B | 2026-07-24 19:50 |
| verify.jsonl | 2 | verify | unknown | unknown | 0 | 436B | 2026-07-24 19:46 |
| test.jsonl | 1 | test | unknown | unknown | 0 | 216B | 2026-07-24 19:37 |
| verify-skip.jsonl | 1 | verify-skip | unknown | unknown | 0 | 174B | 2026-07-23 21:54 |

## Cleanup Recommendations

`6` stale session file(s) older than 7 days:
- `e2e-test.jsonl` (171B, last modified 2026-07-27 22:37)
- `test001.jsonl` (213B, last modified 2026-07-27 22:36)
- `v.jsonl` (639B, last modified 2026-07-24 19:50)
- `verify.jsonl` (436B, last modified 2026-07-24 19:46)
- `test.jsonl` (216B, last modified 2026-07-24 19:37)
- `verify-skip.jsonl` (174B, last modified 2026-07-23 21:54)

## Safety Checks

- Active-session guard: **ON** (1h recency window)
- DB-liveness check: sessions referenced in `state.db` are never cleaned: **enabled**
- Files are backed up to `<hermes>/session-audit-backup-<ts>/` before removal
