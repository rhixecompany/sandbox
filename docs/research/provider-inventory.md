# Provider Inventory (Live Hermes Config — 2026-07-27)

## Active Profile: default
- **Primary**: deepseek-v4-flash-free via opencode-zen
- **Fallback**: nemotron-3-ultra-free via opencode-zen

## Authorized Providers & Credentials

| Provider | Credentials | Status | Notes |
|----------|-------------|--------|-------|
| **copilot** | 3 (GITHUB_TOKEN, COPILOT_GITHUB_TOKEN, api-key-3) | Active | GitHub Copilot CLI |
| **deepseek** | 1 (DEEPSEEK_API_KEY) | Exhausted (402) | Rate-limited |
| **gemini** | 1 (GOOGLE_API_KEY) | Rate-limited (429) | |
| **huggingface** | 1 (HF_TOKEN) | Active | HF Inference API |
| **nous** | 1 (device_code OAuth) | Active | Nous Research |
| **ollama-cloud** | 1 (OLLAMA_API_KEY) | Active | Ollama Cloud |
| **openai-api** | 2 (api-key-1, OPENAI_API_KEY) | Active | Direct OpenAI API |
| **openai-codex** | 2 (OAuth) | Rate-limited (429) | Codex CLI auth |
| **openrouter** | 1 (OPENROUTER_API_KEY) | Active | Multi-provider gateway |
| **xai-oauth** | 1 (device_code OAuth) | Active | xAI/Grok |

## Model Configuration
- Default profile: deepseek-v4-flash-free (opencode-zen)
- Fallback: nemotron-3-ultra-free (opencode-zen)
- Gateway: opencode-zen (chat_completions API)

## Research Required
For each provider, fetch:
1. Current model catalog
2. Free tier / pricing
4. Rate limits
5. API endpoints
3. Context windows