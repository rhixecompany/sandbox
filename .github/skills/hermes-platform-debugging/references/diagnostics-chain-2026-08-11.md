# Full Hermes Diagnostic Chain — Session Evidence 2026-08-11

Plan: `.hermes/plans/2026-08-11_hermes-platform-diagnostics-debug.md` (executed
end-to-end per `executing-plans` with auto-advance). 2173-line log captured
with `CHAIN_EXIT=0` — all 14 commands ran, no `&&` truncation.

## Chain
```bash
hermes doctor && hermes doctor --fix && hermes security audit && hermes status \
&& hermes insights && hermes skills audit && hermes skills check && hermes skills update \
&& hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway \
&& hermes logs gui && hermes logs agent
```

## Findings by category

| # | Category | Finding | Disposition |
|---|----------|---------|-------------|
| 1 | Fixed | 6 hub skills `update_available` (baoyu-article-illustrator, prompt-engineering, search-skills-plugins-subagents, hooks-pattern, agentmemory-hooks, data-migration-scripts) | `hermes skills update` applied all 6; re-check = 0 pending |
| 2 | Regression cleared | Windows skills-hash bug (update reports Updated but check re-flags) | `.as_posix()` fixes landed; no re-flag on re-check |
| 3 | Billing (user) | `hermes doctor`: `xai (HTTP 403)`; direct probe of `/v1/models` with stored key → `403 permission-denied — team 77cbc11c… has either used all available credits or reached its monthly spending limit` | Key valid; top up xAI credits to restore `x_search` (grok-4.20-reasoning) + xai TTS — do NOT rotate key |
| 4 | Billing (user) | Nous Portal "no usable paid credits" → managed web/image/TTS/STT/browser/Modal tools unavailable | Add credits at portal.nousresearch.com/billing |
| 5 | Transient | Telegram `getaddrinfo failed` + fallback IP failures (08-09 14:49, 08-11 19:00–19:04); agent.log bootstrap delete-webhook timeout | Recovered via DNS-over-HTTPS fallback + reconnect loop |
| 6 | Transient | desktop.log ollama-cloud (nemotron-3-ultra) 3× APIConnectionError; live curl later = HTTP 303 | Fallback chain worked as designed |
| 7 | Operational | lifecycle_ledger `previous_unclean_exit` (pid 10392, prior 20888/7352/16016); exitCode 3221225786 = STATUS_CONTROL_C_EXIT | Windows sleep/console-close signature; current gateway healthy → monitor only |
| 8 | Cosmetic | gui.log event loop stalled 5.1–22.2s ×10 (GIL pressure) | Perf note under heavy parallel load |
| 9 | Cosmetic | Optional OAuth/tool warnings (MiniMax, xAI OAuth, Qwen, discord/feishu/homeassistant/image_gen deps) | No action |
| 10 | False positive | neon `prepare_database_migration` "concealment instruction" (recurs since 08-09) | Remote official Neon MCP `<use_case>` tool description; scanner heuristic, no local fix |
| 11 | Guard working | 15 community skills BLOCKED by skills-guard (antigravity-cli, grok, pinggy-tunnel, watchers, stocks, fitness-nutrition, mcp-oauth-remote-gateway, axolotl, unsloth, shop, godmode, unbroker, rest-graphql-debug, hyperliquid, subagent-driven-development) | Installer/env-read content verdicts; none involved in this update round |
| 12 | Cosmetic | Skill 'rollback' /rollback collision; hardline block on prior compound grep command | Benign; use `/skill rollback` |

## Lessons
- `CHAIN_EXIT=${PIPESTATUS[0]}` on a teed `&&` chain is the only reliable
  way to know every command ran — never infer from the visible tail.
- Triage a big diagnostic log with `read_file` pagination, not one giant
  `cat`/`grep` dump in a single terminal call (stream caps/timeouts).
- Skills-hub acceptance gate = post-update `hermes skills check` showing
  `0 update(s) available`, not the "Updated N" print.
- write_file resolves RELATIVE paths against the terminal session's persisted
  cwd (the last `cd`), not the session start cwd — after `cd`-ing into
  `~/AppData/Local/hermes/logs`, a relative write lands under that directory.
  Use absolute paths for file writes after any `cd` in the same session.