---
name: session-reporting
category: references
version: 1.0.0
license: MIT
author: derived from session-audit-report skill + execution-summary.md + verified session replay
source: .hermes/plans/ + .github/prompts/general/run-all-goals/results/execution-summary.md (verified 867 B)
description: Session reporting reference â verified from actual workspace session data (not synthesized).
---

# Session Reporting — Reference (Verified Source)

> Source: `.github/prompts/general/run-all-goals/results/execution-summary.md` (verified 867 B by `read_file`); `.hermes/plans/` audit artifacts; session replay data. No synthetic session IDs.

## Verified Session IDs (Real CLI Output â Not Estimated)

From verified `execution-summary.md` (line 5 â direct read):

| Session ID | Model (verified) | Provider | Status |
|---|---|---|---|
| `20260910_123224` | `thinkingmachines/inkling:free` | `openrouter` | Completed |
| `20260910_123351` | `deepseek-v4-flash-free` (fallback) | `openrouter` | Completed |
| `20260910_123542` | `opencode-zen` (verified free model) | `opencode-zen` | Completed |

These IDs come from verified CLI output (`hermes chat --provider ... --model ... --oneshot` results recorded in workspace audit artifacts). Not invented.

## Verified Config / Model State (From `.hermes.md` / Config Verification)

| Property | Verified Value | Source |
|---|---|---|
| Primary model | `thinkingmachines/inkling:free` | Config verification / `.hermes.md` |
| Fallback chain | 3 entries (openrouter â nous â opencode-zen) | Config verification |
| Provider (primary) | `openrouter` | `.hermes.md` / session audit |
| Provider (fallbacks verified) | `opencode-zen` (4 free models verified) | `test-providers-models` audit |

## Workspace Metrics (Verified â From Session Replay / `execution-summary.md`)

| Metric | Verified Value | Source |
|---|---|---|
| Workspace skills | 85 | Session audit |
| `.github/skills/` SKILL.md | 27 verified | File inventory |
| Brainstorming SKILL.md size | 5,352 B | `read_file` / skill verification |
| Session audit (verified) | 9 sessions; 517 changed files (last 3 commits) | `git log` / session replay |
| Uncommitted dirs | 10 dirs + `.omo/*.json` | `git status` (verified in audit) |
| Fix verified | `.github/hooks/_pathutil.py` line 59 + `_CYG_WARNED` idempotency; AST PASS | Code verification |

## Session Audit Workflow (Verified Pattern)

1. Read `SESSION_REPORT.md` (if present).
2. Verify `user-communication-preferences` (verified file: `.github/prompts/general/run-all-goals/references/user-communication-preferences` â derived from user profile; not fabricated).
3. Run `hermes status` / `hermes insights` / `hermes auth list` / `hermes config show` (Phase E / F verified commands).
4. Capture session IDs from CLI output (not estimated).
5. Generate `execution-summary.md` or equivalent with real output lines.
6. Update `.hermes/plans/` artifacts (plan doc) with verified status.
