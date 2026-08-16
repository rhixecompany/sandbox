---
name: validate-then-sync
title: Validate-then-sync Vault Keys (working keys only)
description: Live-validate vault keys against provider URLs, then sync only working keys to agent .env stores.
version: 1.0.0
tags: [credentials, validation, env-sync, api-keys, mcp]
---

# Validate-then-sync Vault Keys

Companion to SKILL.md's validate-then-sync section. Captures the live endpoint
map and extraction rules proven in the 2026-08-12 rotation session (23 vault
files, 26/29 keys validated OK).

## The two scripts

Both live in `$LOCALAPPDATA/hermes/scripts/` (NOT in the skill dir — they read
the real vault and write the real `.env`, so they stay with the agent scripts):

| Script | Phase | Behaviour |
|--------|-------|-----------|
| `vault_key_validate.py` | validate | Extracts every key from `~/Desktop/Github/*.txt`, hits each provider's LIVE endpoint concurrently, prints masked status table. `--json` writes `%TEMP%\hermes-vault-working-keys.json`. Never writes agent files. |
| `vault_key_sync.py` | sync | Reads the working-keys JSON, idempotently writes ONLY those vars into Hermes root `.env` + workspace `.env`. Dry-run default; `--apply` writes with `.bak.<ts>` backup. Post-apply dry-run must show "no changes needed". |

Sequence: `python vault_key_validate.py --json` → review masked table →
`python vault_key_sync.py` (dry) → `python vault_key_sync.py --apply` →
re-run `vault_key_validate.py` and `vault_key_sync.py` (dry) to confirm.

## Verified endpoint map (proven live 2026-08-12)

Use THESE exact URLs. Invented REST URLs produce false failures.

| Var(s) | Endpoint | Method/Auth | Notes |
|--------|----------|-------------|-------|
| GITHUB_PAT_* / GITHUB_TOKEN | `https://api.github.com/user` | GET `Authorization: Bearer` + UA | 200 → `login=` |
| OPENAI_API_KEY_* | `https://api.openai.com/v1/models` | GET Bearer | 200 even when no `gpt` id matches (models list may lack `gpt` prefix) |
| GROQ_API_KEY | `https://api.groq.com/openai/v1/models` | GET Bearer | |
| XAI_API_KEY | `https://api.x.ai/v1/models` | GET Bearer | 403 = credit block, key valid |
| HF_TOKEN | `https://huggingface.co/api/whoami-v2` | GET Bearer | 200 → user + type |
| OPENROUTER_API_KEY | `https://openrouter.ai/api/v1/auth/key` | GET Bearer | 200 → label + limit |
| TAVILY_API_KEY | `https://api.tavily.com/search` | POST body `{"api_key": key, "query": "test", "max_results": 1}` | |
| NEON_API_KEY | `https://mcp.neon.tech/mcp` | POST JSON-RPC initialize, Bearer | REST `api.neon.tech` does NOT resolve on this network |
| SENTRY_AUTH_TOKEN | `https://sentry.io/api/0/` | GET Bearer | |
| TAILSCALE_API_KEY | `https://api.tailscale.com/api/v2/tailnet/-/devices` | GET Bearer | 200 → devices count |
| TAILSCALE_AUTH_KEY | (not API-testable) | — | `tskey-auth-` pre-auth key; 401 vs API is expected, use with `tailscale up --auth-key` |
| CONTEXT7_API_KEY | `https://mcp.context7.com/mcp` | POST JSON-RPC initialize, `x-api-key` + Bearer | REST `context7.com` times out |
| HONCHO_API_KEY | `https://mcp.honcho.dev/` | POST JSON-RPC initialize, Bearer | REST `/v1/workspaces` → 404 (route mismatch) |
| HOSTINGER_API_TOKEN | `https://api.hostinger.com/api/v1/` | GET Bearer | Cloudflare 530/1016 = provider origin outage, not key failure |
| OPENCODE_ZEN_API_KEY | `https://opencode.ai/zen/v1/models` | GET Bearer | |
| OLLAMA_API_KEY | `https://api.ollama.com/v1/models` | GET Bearer | fallback `https://ollama.com/api/tags` |
| ACEDATA_API_KEY | `https://api.acedata.cloud/v1/models` | GET Bearer | root path 404s; `/v1/models` works |
| SMITHERY_LEGACY_UUID | `https://mcp.smithery.ai/<namespace>` (e.g. `alexanderrhixe30`) | POST JSON-RPC initialize, Bearer + `x-api-key` | legacy `mcp.smithery.run/{uuid}` path returns 404 "Invalid credentials or namespace not found" |
| ALIBABA_ACCESS_KEY_ID/SECRET | `https://sts.aliyuncs.com/` | signed GET `Action=GetCallerIdentity` (RPC v1.0 HMAC-SHA1, params sorted + percent-encoded) | 200 → `Arn` shows account |

## MCP gateway gotchas

- All cloud MCP gateways require `Accept: application/json, text/event-stream`
  on JSON-RPC initialize; otherwise `406 Not Acceptable` ("Client must accept
  both application/json and text/event-stream").
- SSE-flavoured 200 responses arrive as `event: message\ndata: {...}` — parse
  defensively (search for `"serverInfo"` / `"name"` rather than strict JSON).
- Smithery: `mcp.smithery.ai/<namespace>` works; the old `mcp.smithery.run/{uuid}` path is dead.

## Extraction rules (proven)

- Labeled files (`OLD:`, `NEW:`, `new3:`, `personal_access_token:`) → explicit
  prefix hint per label. The generic "first token ≥20 chars" fallback silently
  grabs the WRONG token when a file holds multiple token types (e.g.
  `rhixecompany_github_access_token.txt` has both `github_pat_11AX…` and
  `ghp_oranUN…`; the var `GITHUB_PAT_RHIXE_PERSONAL` must be pinned to `ghp_or`).
- Verify before apply: compare masked extract() output vs the DEPLOYED .env
  fingerprint for each var — a validator bug that extracts the wrong token
  would otherwise overwrite a good deployed key with a wrong one.
- Alibaba: two tokens in one file → `idx0` (AccessKeyId, `LTAI…`) and `idx1`
  (secret, `rkZ5…`); validated together via the signed STS call.

## Status-code triage (do NOT purge these)

| Code | Meaning | Action |
|------|---------|--------|
| xAI 403 permission-denied | valid key, team out of credits / monthly spend cap | keep; top up credits |
| Hostinger 530 error 1016 | Cloudflare origin DNS on provider side | keep; retry later |
| Tailscale tskey-auth- 401 | pre-auth key type, wrong endpoint by design | keep |
| MCP 406 Not Acceptable | missing Accept header | add `Accept: application/json, text/event-stream` and retest |
| OpenAI 500 on /v1/models | transient server error | retry once; a prior 200 overrides a later 500 |

## Sync discipline

- Only vars in the working-keys JSON get written. XAI (credit-blocked) and
  Hostinger (outage) stay as-is in Hermes and are NOT propagated to the
  workspace `.env` — "working keys only" means exactly that.
- OpenCode `~/.local/share/opencode/auth.json` (openai/openrouter/opencode),
  Codex `~/.codex/auth.json` (OAuth device-flow, `OPENAI_API_KEY: null` by
  design) and Codex config.toml Neon MCP token were all validated 200 already —
  no writes needed. Only hermes root `.env` + workspace `.env` were touched.
- After apply, delete the workspace `.env.bak.*` (NOT gitignored → leaks
  secrets into `git status`); keep the hermes-side backups.
