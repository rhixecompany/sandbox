# OpenCode Zen + OpenRouter Provider Setup Report

Generated: 2026-09-14
Sources: OpenRouter free models page, OpenCode Zen docs, web_search

## Provider Inventory (from `hermes auth list`)

| Provider | Credentials | Status |
|----------|-------------|--------|
| openrouter | OPENROUTER_API_KEY (env) | ✅ Active |
| opencode-zen | OPENCODE_ZEN_API_KEY (env) + zen-backup (manual, 401) | ✅ Primary active, backup failed |
| nous | rhixecompany@gmail.com (oauth) | ✅ Active |
| deepseek | DEEPSEEK_API_KEY (env) | ✅ Active |
| ollama-cloud | OLLAMA_API_KEY (env) | ✅ Active |
| openai-codex | device_code (oauth) | ✅ Active |
| minimax | MINIMAX_API_KEY (env) | ✅ Active |
| gemini | GOOGLE_API_KEY (env) | ✅ Active |
| huggingface | HF_TOKEN (env) | ✅ Active |
| copilot | GITHUB_TOKEN + COPILOT_GITHUB_TOKEN | ✅ Active |
| xai | api-key-1 (403), XAI_API_KEY (env) | ⚠️ One credential failed |

## Current Hermes Model Config

- **Default model**: `inkling:free` (OpenRouter)
- **Provider**: openrouter
- **Base URL**: https://openrouter.ai/api/v1
- **API mode**: chat_completions

## OpenCode Zen — Free Models (7 models)

| Model ID | Endpoint | Pricing |
|----------|----------|---------|
| `big-pickle` | `/v1/chat/completions` | Free |
| `mimo-v2.5-free` | `/v1/chat/completions` | Free |
| `ling-3.0-flash-fin-free` | `/v1/chat/completions` | Free |
| `nemotron-3-ultra-free` | `/v1/chat/completions` | Free (NVIDIA trial) |
| `nemotron-3.5-lightning-free` | `/v1/chat/completions` | Free (NVIDIA trial) |
| `muse-spark-1.3-contributor-free` | `/v1/responses` | Free (Meta training) |

Config format: `opencode/<model-id>` (e.g., `opencode/deepseek-v4-flash`)

## OpenRouter — Free Models (17 confirmed :free)

See `docs/openrouter-free-models-report.md` for full table.

Key free models:
- `inclusionai/ling-3.0-flash-sante:free` — 366B params, MoE, health/medicine
- `inclusionai/ling-3.0-flash-fin:free` — 981B params, MoE, finance
- `inclusionai/ling-3.0-flash-vl:free` — 102B params, multimodal
- `nex-agi/nex-n2.5-mini:free` — 86.3B, agentic coding
- `nex-agi/nex-n2.5-pro:free` — 278B, agentic pro
- `nvidia/nemotron-3.5-lightning:free` — 964B, 1M context
- `cohere/north-mini-code:free` — 124B, 256K context, coding
- `thinkingmachines/inkling:free` — 401B, multimodal
- `thinkingmachines/inkling-small:free` — 133B, 1.05M context
- `poolside/laguna-s-2.1:free` — 118B, coding agent
- `poolside/laguna-xs-2.1:free` — 33B, coding agent, FP8
- `dots-studio/dots-3-note-preview:free` — 534B, going away Sep 30 2026
- `deepgram/flux-tts:free` — TTS
- `liquid/lfm-2.5-embedding-350m:free` — embedding
- `liquid/lfm-2.5-2.6b:free` — 2.6B reasoning

## Best Practices for opencode-free + opencode-zen Setup in Hermes

### 1. Provider Order / Fallback Chain
Per test-providers-models skill, set:
```bash
hermes config set model.provider opencode-zen
hermes config set model.default opencode/deepseek-v4-flash-free
hermes config set fallback_providers '["openrouter","nous","deepseek"]'
```

### 2. Config.yaml Rules
- Do NOT edit config.yaml directly — use `hermes config set` (per user-communication-preferences rule 11)
- For emergency fixes only, document as temporary workaround
- Verify after each change with `hermes config check`

### 3. API Key Management
- OpenRouter key is in Hermes credential store (NOT env var in subprocesses) — per test-providers-models pitfall #3
- Store keys in `~/AppData/Local/hermes/.env` — not in repo .env files
- Hermes .env already has 253 keys including all required providers

### 4. Model Selection Strategy
- Primary: `opencode/deepseek-v4-flash-free` (fast, reliable, free)
- Fallback 1: `openrouter/inkling:free` (current default)
- Fallback 2: `nous/nemotron-3-ultra-free` (via opencode-zen)
- Coding: `opencode/mimo-v2.5-free` or `opencode/big-pickle`

### 5. Rate Limit Handling
- OpenRouter free tier: 20 req/min, 50-1000 req/day across 28+ models
- OpenCode Zen free: 200 requests over 5 hours
- Use `rate-limit-bypass` skill for bounded retry with exponential backoff

### 6. Verification
After any config change:
```bash
hermes config check
hermes auth list
hermes mcp test sequential-thinking
```
