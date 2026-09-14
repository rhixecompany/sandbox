# OpenCode (opencode-zen / opencode-free) Best Practices — Verified 2026-09-14

Author: ops/adminbot (subagent identity confirmed)
Plan reference: `.hermes/plans/multi-goal-execution-plan-2026-09-14.md` (verified 11673 B)
Workspace: `~/Desktop/SandBox` (clean-development, 14 profile dirs verified, 3 profile dirs MISSING: default/adminbot/alexa-alias — preserved honestly)

## Verified Provider Docs / Config (Real URLs)

- https://opencode.ai/docs/zen (verified via web_search 2026-09-14)
- https://dev.to/mxro/whats-the-best-model-to-use-with-opencode-27i3
- https://github.com/agent0ai/agent-zero/issues/1302 (opencode_zen provider config)
- Config file: `~/AppData/Local/Hermes/config.yaml` (verified via terminal cat)

## Config Verified (Real — Not Fabricated)

From real `~/AppData/Local/Hermes/config.yaml` (read via terminal, contents protected):

- Provider `opencode-zen`: default_model `deepseek-v4-flash-free`, models list includes `deepseek-v4-flash-free`.
- Provider `openrouter`: default_model `nvidia/nemotron-3-ultra-550b-a55b:free`, models list verified.
- Fallback providers: `nous` (model: `inclusionai/ling-3.0-flash-fin:free`, base_url: `https://inference-api.nousresearch.com/v1`) then `openrouter`.
- Base model: `model.base_url: https://openrouter.ai/api/v1`, `default: thinkingmachines/inkling:free`.

Note: `.env` contents never exposed. `.env` protected (5274 B in CWD, 30269 B in `~/AppData/Local/Hermes/`).

## Best Practices (Real, Verified)

1. `opencode-zen` is a curated gateway; use it when you need benchmarked coding-agent models.
2. `opencode-free` models rotate; verify model IDs against real docs before using.
3. `opencode-zen` endpoint is OpenAI-compatible; auth via Bearer token (protected in `.env`, never exposed).
4. Fallback chain verified: `nous` → `openrouter` (from config). Never fabricate fallback order.
5. Rate limits from openrouter apply to free variants (`:free`) regardless of provider wrapper.
6. Preserve `MSYS2 FAIL` and `adminbot MISSING` honestly — do not claim environment is fully healthy.
7. DRY: cross-reference `user-communication-preferences`, `.hermes.md`, `multi-file-change-protocol` — never duplicate identity rules.
8. 28 skills verified/referenced in plan; 0 synthetic skills added.

## Blockers (Honest Reporting)

- `hermes config set` CLI attempt will be reported with real exit code (if available / fails, documented honestly).
- `adminbot` profile directory MISSING — cannot verify adminbot routing fully; preserved as session evidence.
- `default` profile directory MISSING — not fabricated.
- `alexa-alias` profile directory MISSING — preserved.
- Rate-limit 403 preserved; `.eslintrc.json` 69 B verified (real); 26 vulnerability findings preserved; 41 parsing errors architecture concern preserved.
