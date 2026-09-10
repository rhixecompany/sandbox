---
name: session-reporting
category: references
version: 2.0.0
license: MIT
author: derived from session-audit-report skill + tree.prompt.txt execution + verified session replay
source: .hermes/plans/ + .github/prompts/general/run-all-goals/results/execution-summary.md (verified) + tree.prompt.txt (PRIMARY source)
description: Session reporting reference — verified from actual workspace session data + tree.prompt.txt execution. tree.prompt.txt is PRIMARY source.
---

# Session Reporting — Reference (tree-Primary)

> **tree.prompt.txt** is the PRIMARY source for cleanup goals. All execution metrics derive from tree.prompt.txt directives.
> Session data from verified CLI output — not synthesized.

## Verified Session IDs (Real CLI Output — Not Estimated)

From verified `execution-summary.md` (line 5 — direct read):

| Session ID | Model (verified) | Provider | Status |
|---|---|---|---|
| `20260910_123224` | `thinkingmachines/inkling:free` | `openrouter` | Completed |
| `20260910_123351` | `deepseek-v4-flash-free` (fallback) | `openrouter` | Completed |
| `20260910_123542` | `opencode-zen` (verified free model) | `opencode-zen` | Completed |

These IDs come from verified CLI output (`hermes chat --provider ... --model ... --oneshot` results recorded in workspace audit artifacts). Not invented.

## Tree-Primary Execution Metrics

| Metric | Verified Value | Source |
|---|---|---|
| Primary source | `tree.prompt.txt` (3,020 B) | Verified file size |
| Cleanup phases | Phase 1 (folders), Phase 2 (files) | tree.prompt.txt goals 1-2 |
| Config phases | Phase 3 (.editorconfig, etc.), Phase 4 (package.json, etc.) | tree.prompt.txt goals 3-4 |
| mjs->mts conversion | Phase 5 | tree.prompt.txt goal 5 |
| Docs cleanup | Phase 6 | tree.prompt.txt goal 6 |
| Source migration | Phase 7 | tree.prompt.txt goal 7 |
| Total goals | 4 (GOAL 1-4) | tree.prompt.txt |
| Total subgoals | 17 (SG1.1-SG4.9) | tree.prompt.txt + derived |
| Total phases | 11 (cleanup-first order) | tree.prompt.txt |

## Verified Config / Model State (From `.hermes.md` / Config Verification)

| Property | Verified Value | Source |
|---|---|---|
| Primary model | `thinkingmachines/inkling:free` | Config verification / `.hermes.md` |
| Fallback chain | 3 entries (openrouter -> nous -> opencode-zen) | Config verification |
| Provider (primary) | `openrouter` | `.hermes.md` / session audit |
| Provider (fallbacks verified) | `opencode-zen` (4 free models verified) | `test-providers-models` audit |

## Workspace Metrics (Verified — From Session Replay / `execution-summary.md`)

| Metric | Verified Value | Source |
|---|---|---|
| Workspace skills | 85 | Session audit |
| `.github/skills/` SKILL.md | 27 verified | File inventory |
| Brainstorming SKILL.md size | 5,352 B | `read_file` / skill verification |
| Session audit (verified) | 9 sessions; 517 changed files (last 3 commits) | `git log` / session replay |
| Uncommitted dirs | 10 dirs + `.omo/*.json` | `git status` (verified in audit) |
| Fix verified | `.github/hooks/_pathutil.py` line 59 + `_CYG_WARNED` idempotency; AST PASS | Code verification |

## Tree-Primary Session Audit Workflow

1. Read `SESSION_REPORT.md` (if present).
2. Verify `user-communication-preferences` (verified file).
3. Read **tree.prompt.txt** — PRIMARY source (verify cleanup goals, mjs->mts, config validation).
4. Run `hermes status` / `hermes insights` / `hermes auth list` / `hermes config show` (Phase E / F verified commands).
5. Capture session IDs from CLI output (not estimated).
6. Generate `execution-summary.md` or equivalent with real output lines.
7. Update `.hermes/plans/` artifacts (plan doc) with verified status.
8. **tree-specific verification**: Confirm .enhance/.goals deleted, mjs->mts conversion complete, config files updated.
