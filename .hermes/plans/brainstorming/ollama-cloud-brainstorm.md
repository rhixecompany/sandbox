# Ollama-Cloud Provider Workflow — Brainstorming

**Date:** 2026-08-16  
**Provider:** ollama-cloud  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `ollama-cloud` |
| Default model | nemotron-3-ultra |
| Auth type | API key |
| Env var | `OLLAMA_API_KEY` |
| Base URL | Ollama Cloud API (`https://ollama.com/v1`) |
| Credential pool | Single API key |
| Pool strategy | fill_first |
| Role | 4th/last in fallback chain |
| Model discovery | Dynamic from `ollama.com/v1/models`, cached 1 hour |

---

## What "Repeat the OpenRouter Workflow" Means for Ollama-Cloud

Adapting the 8-step template to Ollama-Cloud:

1. **Credential verification** — Confirm OLLAMA_API_KEY in .env
2. **Model selection** — `hermes model` → ollama-cloud → pick from dynamically discovered models (gpt-oss:120b, glm-4.6:cloud, qwen3-coder:480b-cloud, nemotron-3-super, nemotron-3-ultra)
3. **Config.yaml validation** — Verify model.provider, model.default_model
4. **Fallback chain position** — Last in chain (after opencode-zen, openrouter, gemini)
5. **MCP compatibility** — Test MCP servers with ollama-cloud backing model
6. **Context window compliance** — Verify models meet 64K minimum context (critical for Hermes)
7. **Rate limit / quota management** — Document pricing model and limits
8. **Verification** — `hermes doctor`, test chat

---

## Model Discovery

- Model catalog fetched dynamically from `ollama.com/v1/models`
- Cache TTL: 1 hour
- `model:tag` notation preserved (e.g., `qwen3-coder:480b-cloud`) — don't use dashes
- Available models: gpt-oss:120b, glm-4.6:cloud, glm-5.1, qwen3-coder:480b-cloud, kimi-k2.5, minimax-n2.7, mistral-large, and more

---

## SCAMPER Analysis

### Substitute
- Ollama Cloud vs local Ollama: cloud requires API key but no GPU; local is free but needs GPU
- Substitute models within Ollama Cloud catalog freely

### Combine
- Ollama Cloud as last-resort fallback + local Ollama for offline = hybrid reliability

### Adapt
- Adapt 8-step template — Ollama-Cloud-specific: dynamic model discovery, model:tag notation

### Modify
- Last in fallback chain — only used when all others fail
- Model discovery is dynamic — models can change between sessions

### Eliminate
- Eliminate if OLLAMA_API_KEY is invalid or no free tier available

### Reverse
- Ollama Cloud as primary for privacy-focused workloads? No — it's cloud, not local

---

## Key Questions

1. Is the OLLAMA_API_KEY currently valid?
2. What is the pricing model — free tier, paid, or trial?
3. Are all discovered models ≥ 64K context?
4. Is Ollama Cloud used for anything other than last-resort fallback?

---

## Implementation Artifacts Needed

- `.hermes/plans/specs/ollama-cloud-workflow-spec.md`
- `.hermes/plans/ollama-cloud-workflow.md` (implementation plan)
- `.hermes/plans/results/ollama-cloud-*.txt` (execution results)
