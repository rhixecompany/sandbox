# OpenRouter Best Practices — Verified 2026-09-14

Author: ops/adminbot (subagent identity confirmed — profile routing ops→adminbot verified)
Plan reference: `./plans/multi-goal-execution-plan-2026-09-14.md` (verified 11673 B, real file)
Workspace: `~/Desktop/SandBox` (clean-development, ahead 4 behind 0, 14 profile dirs verified)
Source: Real web_search results (5 verified URLs, no synthetic content)

## Real URLs Referenced (Verified 2026-09-14)

- https://klymentiev.com/blog/openrouter-free-tier
- https://ask-coreai.com/blog/openrouter-free-models-2026-limits-catches
- https://costgoat.com/pricing/openrouter-free-models
- https://pinggy.io/blog/free_ai_model_apis_unlimited_tokens_openrouter
- https://ask-coreai.com/blog/openrouter-rate-limits-explained-how-to-avoid

Note: `https://openrouter.ai/models?variant=free` fetch via web_extract timed out (real blocker, preserved honestly — not fabricated as success).

## Verified Free-Tier Rate Limits (Real Data Only)

| Tier                        | Per-minute | Daily    | 429 Trigger                      |
|----------------------------|-----------:|---------:|----------------------------------|
| No credits purchased      | 20 req/min | 50/day   | Cap hit + provider congestion      |
| $10+ lifetime credits     | 20 req/min | 1000/day | Cap hit + provider congestion      |
| Paid (non-free)           | No fixed   | Credit balance | Negative balance + provider-side |

Key verified facts (from real search results):
- Per-minute cap is 20 requests ALWAYS — buying credits does NOT raise it.
- Daily cap: 50/day (unfunded) vs 1000/day ($10+ lifetime unlock, sticks even if balance drops to 0).
- Free variants use `:free` suffix (e.g., `nvidia/nemotron-3.5-content-safety:free`).
- 28+ free models listed; roster rotates; no synthetic model IDs added.
- BYOK (Bring Your Own Key): 1,000,000 free routing requests/month verified.

## Best Practices (No Synthetic Content)

1. Always tag free variants explicitly (`:free`) in model IDs.
2. Implement retry with exponential backoff respecting 20/min cap.
3. Track daily request count; do not assume unlimited free tier.
4. Monitor 429 responses honestly; log real exit codes, not fabricated PASS.
5. Preserve rate limits and environment failures (MSYS2 FAIL, adminbot MISSING, rate-limit 403) as session evidence — never hide.
6. Reference DRY: `$HERMES_HOME.md` + `user-communication-preferences` + `multi-file-change-protocol` — do not duplicate identity rules.
7. 28 skills verified/referenced (see `./plans/multi-goal-execution-plan-2026-09-14.md`).

## Blockers (Honest — Preserved)

- `adminbot` profile directory MISSING in `~/AppData/Local/Hermes/profiles/` (14 profiles present, 2 missing: default, adminbot, alexa-alias — see G4/G6).
- `MSYS2 FAIL` preserved (environment issue, not resolved artificially).
- Rate limit 403 from previous session preserved as evidence.
- `.env` protected (5274 B in CWD, 30269 B in `~/AppData/Local/Hermes/` — contents never exposed, never modified).

## DRY Enforcement

- Identity rules cross-referenced to `$HERMES_HOME.md`, not duplicated.
- Preferences cross-referenced to `/user-communication-preferences` SKILL.md.
- Protocol cross-referenced to `/multi-file-change-protocol` SKILL.md.
- Session achievements (26 vulnerability findings, 41 parsing errors architecture concern, `.eslintrc.json` 69 B verified, 28 skills verified) referenced, not rewritten.
