# Provider Catalog

| Provider | Type | Setup Method |
|----------|------|--------------|
| **Nous Portal** | Subscription, zero-config | OAuth via `hermes model` |
| **OpenAI Codex** | ChatGPT OAuth, Codex models | Device code auth via `hermes model` |
| **Anthropic** | Claude models | OAuth (requires Max + extra credits) or API key |
| **OpenRouter** | Multi-provider routing | API key |
| **Z.AI** | GLM/Zhipu models | `GLM_API_KEY` / `ZAI_API_KEY` / `Z_AI_API_KEY` |
| **Kimi / Moonshot** | Coding & chat models | `KIMI_API_KEY` or `KIMI_CODING_API_KEY` |
| **Kimi / Moonshot China** | China-region endpoint | `KIMI_CN_API_KEY` |
| **Arcee AI** | Trinity models | `ARCEEAI_API_KEY` |
| **GMI Cloud** | Multi-model direct API | `GMI_API_KEY` |
| **MiniMax (OAuth)** | Frontier model, no API key | `hermes model` → MiniMax (OAuth) |
| **MiniMax** | International endpoint | `MINIMAX_API_KEY` |
| **MiniMax China** | China-region endpoint | `MINIMAX_CN_API_KEY` |
| **Alibaba Cloud** | Qwen via DashScope | `DASHSCOPE_API_KEY` (Qwen Coding: `ALIBABA_CODING_PLAN_API_KEY`) |
| **Hugging Face** | 20+ open models unified router | `HF_TOKEN` |
| **AWS Bedrock** | Claude, Nova, Llama, DeepSeek | IAM role or `aws configure` |
| **Azure Foundry** | Azure AI Foundry models | `AZURE_FOUNDRY_API_KEY` + `AZURE_FOUNDRY_BASE_URL` |
| **Google AI Studio** | Gemini direct API | `GOOGLE_API_KEY` / `GEMINI_API_KEY` |
| **Google Gemini (OAuth)** | Gemini via OAuth, no key | `hermes model` → Google Gemini (OAuth) |
| **xAI** | Grok models direct API | `XAI_API_KEY` |
| **xAI Grok OAuth** | SuperGrok/Premium+, no key | `hermes model` → xAI Grok OAuth |
| **NovitaAI** | Multi-model API gateway | `NOVITA_API_KEY` |
| **StepFun** | Step Plan models | `STEPFUN_API_KEY` |
| **Xiaomi MiMo** | Xiaomi-hosted models | `XIAOMI_API_KEY` |
| **Tencent TokenHub** | Tencent-hosted models | `TOKENHUB_API_KEY` |
| **Ollama Cloud** | Managed Ollama models | `OLLAMA_API_KEY` |
| **LM Studio** | Local OpenAI-compatible API | `LM_API_KEY` (and `LM_BASE_URL` if non-default) |
| **Qwen OAuth** | Qwen Portal OAuth, no key | `hermes model` → Qwen OAuth |
| **Kilo Code** | KiloCode-hosted models | `KILOCODE_API_KEY` |