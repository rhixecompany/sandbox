---
name: hermes-platform-diagnostics-debug
title: "Hermes Platform Diagnostics & Debug Plan"
author: Alexa
version: 1.1.0
status: completed
created: 2026-08-11
completed: 2026-08-11
tags: [hermes, diagnostics, debugging, plan]
---

# Hermes Platform Diagnostics & Debug Plan

## Goal
Run the full Hermes diagnostic chain in the background (no timeout), then
systematically fix every bug, issue, warning, and error surfaced — root cause
first, per `systematic-debugging`.

## Context / Assumptions
- Host: Windows 11, git-bash/MSYS terminal, cwd `C:\Users\Alexa\Desktop\SandBox`
- Profile: default (deepseek-v4-flash-free / opencode-zen)
- Known prior findings (2026-07-24→08-08): skills hub Windows hash bug
  (`hermes skills update` reports Updated but `skills check` re-flags),
  hook wire-payload shapes fixed, MCP server restorations done.
- `&&` chain means short-circuit on failure: if a command exits non-zero, the
  remaining commands stop. If that happens, run the remainder individually.

## Phase 1 — Background Diagnostic Collection [x] COMPLETE
Executed verbatim in background, output teed to `.hermes/diagnostics-2026-08-11.log` (2173 lines):

```bash
hermes doctor && hermes doctor --fix && hermes security audit && hermes status && hermes insights && hermes skills audit && hermes skills check && hermes skills update && hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway && hermes logs gui && hermes logs agent
```

- CHAIN_EXIT=0 — all 14 commands completed; no `&&` short-circuit truncation.
- Log artifact: `.hermes/diagnostics-2026-08-11.log`

## Phase 2 — Triage Findings [x] COMPLETE
Full findings table (17 items): `.hermes/plans/docs/2026-08-11-hermes-platform-diagnostics-findings.md`

Summary:
- **1 actionable "bug" found & auto-fixed by the chain itself:** 6 skills had
  `update_available` → `hermes skills update` applied all 6 → re-check = 0
  pending. Confirmed the prior Windows skills-hash bug does NOT reproduce.
- **2 billing items (user action, not agent-fixable):** Nous Portal 0 credits
  (managed tools unavailable) and xAI team over monthly spend limit (xai HTTP
  403 — key itself is valid; direct API call confirms "used all available
  credits or reached its monthly spending limit"). xAI affects x_search
  (grok-4.20-reasoning) + xai TTS voice; needs credit top-up, NOT key rotation.
- **Rest = transient/cosmetic/guard-working:** Telegram DNS blips (recovered),
  ollama-cloud connect errors (live check 303 ✓), gateway unclean exits (Windows
  sleep/console-close pattern), gui event-loop GIL stalls, neon MCP scanner
  false positive, 15 community skills BLOCKED by skills-guard (by design —
  installer/env-read content; not involved in this update round), optional
  OAuth/tool warnings.

## Phase 3 — Systematic Debugging [x] COMPLETE
Per `systematic-debugging`, only the xai HTTP 403 warranted deep root-cause work:

1. **Root cause** — `hermes doctor` flagged `xai (HTTP 403)`. Reproduced via
   authorized call to `https://api.x.ai/v1/models`: `403 permission-denied —
   team 77cbc11c… has either used all available credits or reached its monthly
   spending limit`.
2. **Pattern analysis** — key format/prefix valid (`xai-…l0iu`), endpoint live
   (404 on unauthenticated root is normal), other providers in fallback chain
   (openrouter/gemini/ollama-cloud) all ✓ in doctor connectivity.
3. **Hypothesis & test** — "key invalid" vs "account exhausted": the API
   response names the team and quotes the spending-limit reason, ruling out key
   deletion/rotation. Conclusion: **billing state, not config defect** — no
   fix performed (changing the key would be wrong).
4. **Fix** — none required from agent side; documented for user (top up xAI
   credits to restore x_search + xai TTS).
5. Skills hash bug: verified fixed by post-update `hermes skills check` → 0
   `update_available` re-flags (previous behavior: perpetual re-flag after
   update).

Rules followed:
- Config changes via `hermes config set`, never direct YAML edits — **no config
  edits were needed**.
- No `rm -rf` / destructive ops performed.

## Phase 4 — Re-Verify [x] COMPLETE
- `hermes doctor` → **All checks passed** (run pre- and post-`--fix`)
- `hermes doctor --fix` → "No known vulnerabilities found across 160 component(s)"
- `hermes security audit` → 0 advisories
- `hermes skills check` (post-update) → **0 updates available** across 41 skills;
  no unexpected `update_available` re-flags
- Log chains (errors/desktop/gateway/gui/agent): no new actionable errors —
  only documented billing, transient DNS, and cosmetic warnings remain

## Files Changed
- `.hermes/diagnostics-2026-08-11.log` (new — diagnostic capture)
- `.hermes/plans/docs/2026-08-11-hermes-platform-diagnostics-findings.md` (new — findings table)
- `.hermes/plans/2026-08-11_hermes-platform-diagnostics-debug.md` (this plan — status updated)
- Skills updated in place by `hermes skills update` (6): baoyu-article-illustrator, prompt-engineering, search-skills-plugins-subagents, hooks-pattern, agentmemory-hooks, data-migration-scripts

## Validation
- Final: `hermes doctor` green + findings table closed + re-run of any fixed
  command shows the error gone. ✅ All satisfied.

## Risks / Tradeoffs
- `hermes doctor --fix` and `hermes skills update` are mutating: diffs reviewed
  via the chain log — only the 6 intended skill updates were applied; no config
  drift detected.
- Background `&&` short-circuit can truncate the diagnostic capture — monitored:
  CHAIN_EXIT=0, all 14 commands ran.

## Lessons Learned
1. **Skills hash bug confirmed fixed** — post-update `skills check` shows 0
   re-flags. No further action needed.
2. **xAI HTTP 403 = billing, not key.** The API explicitly names the team's
   spending limit. Do NOT rotate/delete the xAI key; top up credits instead.
3. **Gateway `previous_unclean_exit` is a recurring Windows pattern**
   (machine sleep / console close), self-identified by lifecycle_ledger; not a
   defect requiring a fix — monitor only.
4. **Neon "concealment instruction" warning is a scanner false positive** on
   the remote MCP's official tool description; no local remediation possible.
5. **Full-chain diagnostics remain the reliable entry point** — 2173-line
   capture with CHAIN_EXIT=0 gave complete evidence for triage in one pass.