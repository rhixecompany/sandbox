# Gemini Provider Workflow — Brainstorming

**Date:** 2026-08-16  
**Provider:** gemini  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `gemini` |
| Default model | gemini-2.5-flash |
| Auth type | API key |
| Env vars | `GOOGLE_API_KEY` or `GEMINI_API_KEY` |
| Base URL | `https://generativelanguage.googleapis.com/v1beta` |
| Credential pool | Single API key |
| Pool strategy | fill_first |
| Role | 3rd in fallback chain |
| TTS model | gemini-2.5-flash-preview-tts |

---

## What "Repeat the OpenRouter Workflow" Means for Gemini

Adapting the 8-step OpenRouter template to Gemini:

1. **Credential verification** — Confirm GOOGLE_API_KEY or GEMINI_API_KEY in .env
2. **Model selection** — `hermes model` → gemini → pick gemini-2.5-flash
3. **Config.yaml validation** — Verify model.provider, model.default_model
4. **Fallback chain position** — 3rd in chain (after opencode-zen, openrouter)
5. **MCP compatibility** — Test MCP servers with gemini backing model
6. **Free tier quota management** — CRITICAL: free tier can be exhausted after handful of agent turns
7. **Auxiliary model offload** — Gemini Flash recommended for cheap auxiliary tasks
8. **Verification** — `hermes doctor` (NOTE: known false positive bug #26623), test chat

---

## Known Issues

1. **hermes doctor false positive** (GitHub #26623): doctor may report "invalid API key" even when key works. The main chat works fine — cosmetic CLI bug.
2. **Free tier exhaustion**: Free tier quotas are low for agentic workloads. A single complex session can exhaust quota.
3. **Tier detection bug** (GitHub #21399): probe_gemini_tier() may report "paid" for free-tier keys when rate-limit headers are absent.

---

## SCAMPER Analysis

### Substitute
- Gemini via OpenRouter (Option 3 from OpenClaw Launch guide) — routes through OpenRouter, no separate Google billing
- Gemini OAuth (Google subscription) — but Google bans accounts for third-party app usage via OAuth; API key method is safer

### Combine
- Gemini Flash for auxiliary tasks + Gemini Pro for main tasks = cost optimization
- Gemini API key + OpenRouter fallback = dual-path reliability

### Adapt
- Adapt 8-step OpenRouter template — Gemini-specific: free tier awareness, doctor false positive workaround

### Modify
- 3rd in fallback chain — consider promoting if free tier is sufficient
- Explicit auxiliary.<task>.provider config for Gemini Flash offload

### Eliminate
- Eliminate free tier reliance for production agent workloads (move to paid or OpenRouter-routed)

### Reverse
- Gemini as primary for cost-sensitive workloads? Free tier + OpenRouter routing = very cheap

---

## Key Questions

1. Is the current Gemini API key on free tier or paid tier?
2. Has the free tier been exhausted in previous sessions?
3. Should gemini be promoted in the fallback chain?
4. Is the doctor false positive causing any real issues?

---

## Implementation Artifacts Needed

- `.hermes/plans/specs/gemini-workflow-spec.md`
- `.hermes/plans/gemini-workflow.md` (implementation plan)
- `.hermes/plans/results/gemini-*.txt` (execution results)
