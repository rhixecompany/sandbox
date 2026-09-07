---
name: openrouter-docs-extracted
description: Extracted docs from openrouter.ai/docs (authentication + FAQ) via web_extract on 2026-09-07
source_url: https://openrouter.ai/docs/api_reference/authentication
extraction_tool: web_extract
---

# OpenRouter — Documentation Summary (extracted)

## Auth mechanism
- API key via Bearer token (`Authorization: Bearer $OPENROUTER_API_KEY`)
- Also supports cookie-based web auth and OAuth
- Key endpoint: `https://openrouter.ai/api/v1/chat/completions`

## Free tier (`:free` suffix)
- `:free` = model always provided for free, with low rate limits
- Free models: ~20 req/min, low daily cap (rises with credits added)
- `openrouter/free` = automatic free model router

## Rate limits
- Paid: per-credit rate limits; free tier lower
- Rate-limited 429 observed on live auth (57m 53s left at time of capture)

## Best practices (from docs + web research)
- Set `HTTP-Referer` and `X-Title` headers for analytics/rankings
- Use `base_url="https://openrouter.ai/api/v1"` with OpenAI SDK
- If a provider returns error, OpenRouter automatically falls back to next provider
- Protect API keys; OpenRouter is a GitHub secret-scanning partner

## Inference endpoint verified
`https://openrouter.ai/api/v1` (from `hermes config show` + auth file)
