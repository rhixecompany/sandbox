# xAI (Grok) Provider Workflow — Brainstorming

**Date:** 2026-08-16  
**Provider:** xai  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `xai` (direct API) / `xai-oauth` (SuperGrok) |
| Default model | grok-4.3 (OAuth) / varies (API key) |
| Auth type | API key (XAI_API_KEY) OR OAuth (SuperGrok/X Premium+) |
| Env var | `XAI_API_KEY` (direct API) |
| Base URL | xAI API |
| Models | grok-4.3 (1M context), grok-4.3-fast, grok-4.6, voxtral-mini-tts-2603 (TTS) |
| Credential pool | Single key or OAuth token |
| Pool strategy | fill_first |
| Role | Fill-first provider (not in main fallback chain) |
| Direct tools | TTS, image gen, video gen, transcription, X search |

---

## What "Repeat the OpenRouter Workflow" Means for xAI

Adapting the 8-step template to xAI:

1. **Credential verification** — Confirm XAI_API_KEY in .env OR SuperGrok OAuth via `hermes auth xai`
2. **Model selection** — `hermes model` → xAI Grok OAuth → pick grok-4.3 (1M context) or grok-4.6
3. **Config.yaml validation** — Verify model.provider (xai vs xai-oauth), model.default
4. **Fallback chain position** — Not in main fallback chain; fill_first in credential pool
5. **MCP compatibility** — Test MCP servers with xai backing model
6. **Rate limit / quota management** — Document rate limits for Grok models
7. **Direct-to-xAI tools** — TTS (voxtral-mini-tts-2603), image gen, video gen, transcription, X search
8. **Verification** — `hermes doctor`, test chat

---

## Two Auth Paths

### API Key (XAI_API_KEY)
- Direct API access
- Requires XAI_API_KEY in .env
- Provider: `xai` in config.yaml

### SuperGrok OAuth
- Browser-based OAuth (no API key needed)
- Requires SuperGrok or X Premium+ subscription
- Provider: `xai-oauth` in config.yaml
- Same OAuth token auto-reused by direct-to-xAI tools (TTS, image, video, transcription, X search)
- Provider aliases: `xai-oauth`, `grok-oauth`, `x-ai-oauth`, `xai-grok-oauth`

---

## SCAMPER Analysis

### Substitute
- API key path vs OAuth path — different auth mechanisms for same provider
- grok-4.3 vs grok-4.6 vs grok-4.3-fast — model substitution within provider

### Combine
- xAI OAuth token + direct-to-xAI tools (TTS, image, video, transcription, X search) = unified xAI workflow
- xAI as fill_first in credential pool + not in fallback chain = backup capacity without primary reliance

### Adapt
- Adapt 8-step template — xAI-specific: two auth paths, direct-to-xAI tools, provider aliases

### Modify
- Not in main fallback chain — only used when explicitly selected or when credential pool fires
- TTS model (voxtral-mini-tts-2603) is separate from chat models

### Eliminate
- Eliminate if no XAI_API_KEY and no SuperGrok subscription

### Reverse
- xAI as primary for large-context workloads? grok-4.3 has 1M token context — excellent for large codebases

---

## Key Questions

1. Is XAI_API_KEY set, or is SuperGrok OAuth used, or neither?
2. Is xAI used for chat or only TTS?
3. What Grok models are accessible via the current auth method?
4. Should xAI be added to the fallback chain?

---

## Implementation Artifacts Needed

- `.hermes/plans/specs/xai-workflow-spec.md`
- `.hermes/plans/xai-workflow.md` (implementation plan)
- `.hermes/plans/results/xai-*.txt` (execution results)
