# Provider-by-Provider Free Tier Analysis (Web Research — 2026-07-27)

## OpenRouter

- **Auth**: OPENROUTER_API_KEY (configured, active)
- **Free models**: 18 models (see openrouter-free-models.md)
- **Context**: Up to 1M tokens (Nemotron Ultra, Qwen3-Coder)
- **Rate limits**: ~20 RPM typical free tier
- **Strengths**: Multi-provider gateway, auto-fallback, huge model catalog
- **Weaknesses**: Free models rotate, router not reproducible

## Google Gemini

- **Auth**: GOOGLE_API_KEY (configured, rate-limited 429)
- **Free tier**: AI Studio (Google AI Studio) - generous limits
- **Models**: Gemini 2.5 Flash, Gemma 4 (31B, 26B MoE)
- **Context**: 1M+ tokens on Flash
- **Rate limits**: High on AI Studio, tighter on API key
- **Note**: Can use Google AI Studio web UI for free access

## Hugging Face

- **Auth**: HF_TOKEN (configured, active)
- **Free tier**: Inference API - rate-limited free calls
- **Models**: 1000+ via inference providers (Together, Fireworks, Novita, Scaleway, DeepInfra)
- **Free models**: Many community models via Inference Providers
- **Context**: Up to 1M+ on some providers
- **Rate limits**: Varies by provider; free tier ~30 RPM
- **Strengths**: Largest open model catalog, multiple inference backends

## Nous Research

- **Auth**: device_code OAuth (configured, active)
- **Free tier**: Unknown - check nousresearch.com
- **Models**: Hermes 3, Nemotron 3 Ultra, custom fine-tunes
- **Focus**: Open-weight, agentic models

## Ollama Cloud

- **Auth**: OLLAMA_API_KEY (configured, active)
- **Free tier**: Unknown - check ollama.com/cloud
- **Models**: All Ollama-compatible models

## OpenAI API

- **Auth**: 2 keys (configured, active)
- **Free tier**: $5 credit for new accounts (expired for most)
- **Models**: GPT-4o, GPT-4o mini, o1, o3-mini
- **Rate limits**: Tier-based

## OpenAI Codex

- **Auth**: 2 OAuth device codes (rate-limited 429)
- **Free tier**: Limited Codex CLI usage
- **Models**: Codex variants

## XAI (xAI)

- **Auth**: device_code OAuth (configured)
- **Free tier**: Unknown - check x.ai/api
- **Models**: Grok series

## DeepSeek

- **Auth**: DEEPSEEK_API_KEY (exhausted 402)
- **Free tier**: Was generous, now exhausted
- **Models**: DeepSeek V4, Coder, R1

## Copilot (GitHub)

- **Auth**: 3 credentials (GITHUB_TOKEN, COPILOT_GITHUB_TOKEN, api-key-3)
- **Free tier**: GitHub Copilot Free (50 req/mo chat, 2000 code completions/mo)
- **Models**: GPT-4o, o1-preview via GitHub
- **CLI**: `copilot` command available

## Summary Table

| Provider           | Auth Status | Free Models | Free Context | Est. Free RPM | Best For                     |
| ------------------ | ----------- | ----------- | ------------ | ------------- | ---------------------------- |
| OpenRouter         | ✅ Active   | 18          | 1M           | ~20           | Multi-model gateway, variety |
| Google (AI Studio) | ⚠️ 429      | 3+          | 1M+          | High          | Long context, multimodal     |
| Hugging Face       | ✅ Active   | 100s        | 1M+          | ~30           | Open models, provider choice |
| Nous               | ✅ Active   | ?           | ?            | ?             | Agentic/orchestration        |
| Ollama Cloud       | ✅ Active   | ?           | ?            | ?             | Local-like cloud             |
| OpenAI API         | ✅ Active   | 0 (credits) | 128K-1M      | Tier          | Quality, tools               |
| XAI                | ✅ Active   | ?           | ?            | ?             | Grok access                  |
| Copilot            | ✅ Active   | 1-2         | 128K         | 50/mo         | GitHub-integrated            |

## Next Steps

1. Benchmark OpenRouter free models (primary gateway)
2. Test Hugging Face Inference Providers for specific models
3. Verify Google AI Studio access via browser
4. Check Nous/Ollama/XAI free tiers via web
5. Document fallback chain

EOF
cat docs/research/provider-free-tier-analysis.md
