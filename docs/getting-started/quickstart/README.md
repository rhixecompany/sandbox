# Hermes Agent Quickstart — Comprehensive Summary

> **Goal:** Get from zero to a working Hermes setup that survives real use. Install, choose a provider, verify a working chat, and know exactly what to do when something breaks.

---

## 🎯 Who This Is For

- Brand new users wanting the shortest path to a working setup
- Users switching providers who don't want config mistakes
- Teams setting up bots or always-on workflows
- Anyone tired of "it installed, but it still does nothing"

---

## ⚡ The Fastest Path

| Goal | First Step | Then |
|------|------------|------|
| Just want Hermes working | `hermes setup` | Run a real chat and verify it responds |
| Already know provider | `hermes model` | Save config, then start chatting |
| Bot/always-on setup | `hermes gateway setup` (after CLI works) | Connect Telegram, Discord, Slack, etc. |
| Local/self-hosted model | `hermes model` → custom endpoint | Verify endpoint, model name, context length |
| Multi-provider fallback | `hermes model` first | Add routing/fallback only after base chat works |

> **Rule of thumb:** If Hermes cannot complete a normal chat, **do not add more features yet**. Get one clean conversation working first.

---

## 1️⃣ Install Hermes Agent

### Option A — pip (simplest)
```bash
pip install hermes-agent
hermes postinstall     # optional: installs Node.js, browser, ripgrep, ffmpeg + runs setup
```
> PyPI releases track tagged versions (major/minor), not every commit on `main`. For bleeding-edge, use Option B.

### Option B — git installer (tracks main branch)
```bash
# Linux / macOS / WSL2 / Android (Termux)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### Platform Notes
- **Desktop downloads:** [GitHub Releases](https://github.com/NousResearch/hermes-agent/releases/latest)
- **Android/Termux:** See dedicated [Termux guide](https://hermes-agent.nousresearch.com/docs/getting-started/termux)
- **Windows:** Install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) first, then run the command above inside WSL2

### Post-Install
```bash
source ~/.bashrc   # or source ~/.zshrc
```
For detailed options, prerequisites, and troubleshooting → [Installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation)

---

## 2️⃣ Choose a Provider (Most Important Step)

```bash
hermes model    # Interactive provider selection
```

### Easiest Path: Nous Portal
```bash
hermes setup --portal
```
> One subscription covers 300+ models plus the [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway) (web search, image generation, TTS, cloud browser). Logs you in, sets Nous as provider, and turns on Tool Gateway in one command.

### Provider Catalog

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
| **AWS Bedrock** | Claude, Nova, Llama, DeepSeek | IAM role or `aws configure` ([guide](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)) |
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

---

## 3️⃣ Verify It Works

```bash
hermes chat
```
Type a message. If you get a coherent response → **done**.

### If It Fails

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| "No model configured" | `hermes model` not run | Run `hermes model` and pick one |
| "Authentication failed" | Bad API key / expired OAuth | Re-run `hermes model`; check `~/.hermes/.env` |
| "Connection refused" | Network / proxy / DNS | Check internet; try different provider |
| "Model not found" | Wrong model name for provider | Use `hermes model` picker (validates names) |

---

## 4️⃣ Next Steps (Optional)

### Connect a Messenger (Bot/Always-On)
```bash
hermes gateway setup
```
Interactive wizard for Telegram, Discord, Slack, WhatsApp, Signal, Feishu, WeCom, QQBot, Yuanbao, Teams.

### Add Skills
```bash
/skills              # Browse installed
/skill install       # Install from hub
```

### Enable Memory
```bash
hermes memory setup
```

### Schedule Tasks (Cron)
```bash
hermes cron create "daily summary" "0 9 * * *" "Summarize yesterday's commits"
```

---

## 🆘 Troubleshooting Cheatsheet

| Task | Command |
|------|---------|
| Re-run setup | `hermes setup` |
| Change provider | `hermes model` |
| View config | `hermes config show` |
| Check logs | `tail -f ~/.hermes/logs/hermes/*.log` |
| Reset everything | `rm -rf ~/.hermes && hermes setup` |

---

## 📚 Full Documentation

- [Installation Guide](/docs/getting-started/installation)
- [Configuration](/docs/user-guide/configuration)
- [CLI Usage](/docs/user-guide/cli)
- [Messaging Platforms](/docs/user-guide/messaging)
- [Provider Routing](/docs/user-guide/features/provider-routing)

---

**Source:** [Hermes Agent Docs - Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)  
**Extracted:** 2026-06-08