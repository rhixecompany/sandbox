# Hermes Provider Support Matrix

## Chat Providers

| Provider | Auth Type | Env Var | Notes |
|----------|-----------|---------|-------|
| openrouter | api-key | OPENROUTER_API_KEY | General chat |
| anthropic | api-key | ANTHROPIC_API_KEY | General chat |
| openai | api-key | OPENAI_API_KEY | General chat |
| deepseek | api-key | DEEPSEEK_API_KEY | General chat |
| xai / xai-oauth | api-key / oauth | XAI_API_KEY | General chat |
| google / gemini | api-key | GOOGLE_API_KEY or GEMINI_API_KEY | General chat |
| ollama-cloud | api-key | OLLAMA_API_KEY | General chat |
| opencode-zen | api-key | OPENCODE_ZEN_API_KEY | General chat |
| opencode-go | api-key | OPENCODE_GO_API_KEY | General chat |
| nous | oauth | device_code | Nous Portal |
| openai-codex | oauth | device_code | OpenAI Codex |
| qwen-oauth | oauth | device_code | Qwen OAuth |
| github-copilot | token | COPILOT_GITHUB_TOKEN | GitHub Copilot |

## STT/TTS Only

| Provider | Env Var | Supported Modes |
|----------|---------|-----------------|
| groq | GROQ_API_KEY | stt only |
| openai | OPENAI_API_KEY | stt, tts |
| mistral | MISTRAL_API_KEY | stt, tts |
| xai | XAI_API_KEY | tts |
| elevenlabs | ELEVENLABS_API_KEY | tts |
| minimax | MINIMAX_API_KEY | tts |
| gemini | GEMINI_API_KEY | tts |
| neutts | none | tts |
| kittentts | none | tts |
| piper | none | tts |

## Custom Endpoint

Configure via `model.base_url` + `model.api_key` in `config.yaml` for OpenAI-compatible endpoints not in the registry.
