---
name: opencode-zen-docs-extracted
description: Extracted docs from opencode.ai/docs/zen/ via web_extract on 2026-09-07
source_url: https://opencode.ai/docs/zen/
extraction_tool: web_extract
---

# OpenCode Zen — Documentation Summary (extracted)

## What is Zen
- Curated list of tested/verified models by OpenCode team
- Works like any provider; sign in at opencode.ai/auth, add billing, copy API key
- Endpoint: `https://opencode.ai/zen/v1/responses` (OpenAI SDK: `@ai-sdk/openai`) and `/v1/messages` (Anthropic SDK: `@ai-sdk/anthropic`)

## Auth mechanism
- API key (`OPENCODE_ZEN_API_KEY`) via Bearer token
- Auth endpoint: `https://opencode.ai/zen/v1`
- Auth mechanism confirmed: api_key (from `.env` / `auth.json`)

## Free / contributor tier
- Muse Spark contributor-free: discounted token pricing in exchange for permission to use prompts/completions for training future Meta models (`https://dev.meta.ai/docs/pricing-rate-limits#contributor-tier`)

## Rate/status (live auth)
- Status captured by `hermes auth list`: OPENCODE_ZEN_API_KEY env key present; 3 manual keys auth-failed 401 (require rotation/re-auth)
- 1 manual key (`api-key-3` per auth list) may be working; others 401

## Best practices (from docs + web research)
- Run `/connect` in TUI, select OpenCode Zen, paste API key
- Run `/models` to see recommended model list
- Benchmark best combinations; no lock-in, supports BYOK (own OpenAI/Anthropic keys)
- Monthly limits configurable per workspace member
