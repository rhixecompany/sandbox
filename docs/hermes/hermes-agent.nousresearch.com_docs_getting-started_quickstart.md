# Source: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart

# Hermes Agent Quickstart - Comprehensive Summary

## Overview

Hermes Agent is a terminal-based AI agent from Nous Research that supports 30+ LLM providers, tool calling, messaging platform integrations, skills, and voice mode. This guide gets you from zero to a working setup that survives real use.

**Key Principle:** Get one clean conversation working first, then layer on gateway, cron, skills, voice, or routing.

---

## 1. Installation

### Recommended: Hermes Desktop Installer (macOS/Windows)
Download from [hermes-agent.nousresearch.com/desktop](https://hermes-agent.nousresearch.com/desktop)

### CLI-Only Install

| Platform | Command |
|----------|---------|
| **Linux/macOS/WSL2/Android (Termux)** | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| **Windows (PowerShell)** | `iex (irm https://hermes-agent.nousresearch.com/install.ps1)` |

**After install:** Reload shell with `source ~/.bashrc` or `source ~/.zshrc`

> **Android/Termux users:** See dedicated [Termux guide](https://hermes-agent.nousresearch.com/docs/getting-started/termux) for tested manual path and Android-specific limitations.

---

## 2. Choose a Provider (Most Critical Step)

Run interactive setup:
```bash
hermes model
```

### Easiest Path: Nous Portal
```bash
hermes setup --portal
```
One subscription covers 300+ models + Tool Gateway (web search, image generation, TTS, cloud browser).

### Provider Catalog

| Provider | Auth Method | Key Notes |
|----------|-------------|-----------|
| **Nous Portal** | OAuth via `hermes model` | Subscription, zero-config |
| **OpenAI Codex** | Device code OAuth | Uses Codex models |
| **Anthropic** | OAuth (Max plan + credits) or API key | Claude models directly |
| **OpenRouter** | API key | Multi-provider routing |
| **Z.AI** | `GLM_API_KEY` / `ZAI_API_KEY` | GLM/Zhipu models |
| **Kimi / Moonshot** | `KIMI_API_KEY` / `KIMI_CODING_API_KEY` | Coding & chat models |
| **Kimi China** | `KIMI_CN_API_KEY` | China-region endpoint |
| **Arcee AI** | `ARCEEAI_API_KEY` | Trinity models |
| **GMI Cloud** | `GMI_API_KEY` | Multi-model direct API |
| **MiniMax (OAuth)** | Browser OAuth via `hermes model` | No API key needed |
| **MiniMax** | `MINIMAX_API_KEY` | International endpoint |
| **MiniMax China** | `MINIMAX_CN_API_KEY` | China-region endpoint |
| **Alibaba Cloud** | `DASHSCOPE_API_KEY` | Qwen via DashScope |
| **Hugging Face** | `HF_TOKEN` | 20+ open models unified router |
| **AWS Bedrock** | IAM role / `aws configure` | Native Converse API |
| **Azure Foundry** | `AZURE_FOUNDRY_API_KEY` + `AZURE_FOUNDRY_BASE_URL` | Azure AI Foundry |
| **Google AI Studio** | `GOOGLE_API_KEY` / `GEMINI_API_KEY` | Gemini direct API |
| **Google Gemini (OAuth)** | OAuth via `hermes model` | No key needed |
| **xAI** | `XAI_API_KEY` | Grok models |
| **xAI Grok OAuth** | OAuth via `hermes model` | SuperGrok/Premium+ |
| **NovitaAI** | `NOVITA_API_KEY` | Multi-model gateway |
| **StepFun** | `STEPFUN_API_KEY` | Step Plan models |
| **Xiaomi MiMo** | `XIAOMI_API_KEY` | Xiaomi-hosted models |
| **Tencent TokenHub** | `TOKENHUB_API_KEY` | Tencent-hosted models |
| **Ollama Cloud** | `OLLAMA_API_KEY` | Managed Ollama |
| **LM Studio** | `LM_API_KEY` (+ `LM_BASE_URL`) | Local OpenAI-compatible API |
| **Qwen OAuth** | OAuth via `hermes model` | Qwen Portal |
| **Kilo Code** | `KILOCODE_API_KEY` | KiloCode-hosted |
| **OpenCode Zen** | `OPENCODE_ZEN_API_KEY` | Pay-as-you-go curated models |
| **OpenCode Go** | `OPENCODE_GO_API_KEY` | $10/mo subscription |
| **DeepSeek** | `DEEPSEEK_API_KEY` | Direct API |
| **NVIDIA NIM** | `NVIDIA_API_KEY` (+ optional `NVIDIA_BASE_URL`) | Nemotron models |
| **GitHub Copilot** | OAuth or `COPILOT_GITHUB_TOKEN`/`GH_TOKEN` | GPT-5.x, Claude, Gemini |
| **GitHub Copilot ACP** | Requires `copilot` CLI + `copilot login` | ACP agent backend |
| **Custom Endpoint** | Base URL + API key | VLLM, SGLang, Ollama, any OpenAI-compatible |

### Critical Requirement
> **Minimum context: 64K tokens** — Models with smaller windows are rejected at startup. For local models: `--ctx-size 65536` (llama.cpp) or `-c 65536` (Ollama).

### Settings Storage
- **Secrets/tokens** → `~/AppData/Local/hermes/.env`
- **Non-secret config** → `~/AppData/Local/hermes/config.yaml`

Set values via CLI (auto-routes to correct file):
```bash
hermes config set model anthropic/claude-opus-4.6
hermes config set terminal.backend docker
hermes config set OPENROUTER_API_KEY sk-or-...
```

---

## 3. Run Your First Chat

```bash
hermes          # Classic CLI
hermes --tui    # Modern TUI (recommended)
```

**Test prompts:**
```
Summarize this repo in 5 bullets and tell me what the main entrypoint is.
Check my current directory and tell me what looks like the main project file.
Help me set up a clean GitHub PR workflow for this codebase.
```

**Success indicators:**
- Banner shows chosen model/provider
- Hermes replies without error
- Can use tools if needed (terminal, file read, web search)
- Conversation continues normally for multiple turns

---

## 4. Next Steps After First Chat

| Goal | Command / Action |
|------|-----------------|
| **Install skills** | `hermes skills browse` → `hermes skills install <name>` |
| **Add MCP** | `hermes mcp` (interactive picker) |
| **Enable messaging** | `hermes gateway` → pick platform → follow OAuth |
| **Schedule cron** | `hermes cron create "daily summary" "0 9 * * *"` |
| **Customize personality** | Edit `~/AppData/Local/hermes/SOUL.md` |
| **Add project context** | Create `AGENTS.md` in project root |

---

## 5. Common Troubleshooting

| Symptom | Fix |
|---------|-----|
| `hermes` not found | Reload shell: `source ~/.bashrc` or `source ~/.zshrc` |
| "Model requires 64K context" | Use a model with ≥64K context or increase local model ctx (`--ctx-size 65536`) |
| Gateway not connecting | Check `hermes gateway logs` and platform OAuth |
| Skills not loading | Run `hermes skills check` |
| Config not taking effect | Run `hermes config reload` or restart Hermes |

---

## 6. Uninstall / Reset

```bash
# Reset config only
hermes config reset

# Full uninstall (removes ~/AppData/Local/hermes/)
# Linux/macOS:
rm -rf ~/AppData/Local/hermes && sed -i '/hermes/d' ~/.bashrc ~/.zshrc 2>/dev/null; source ~/.bashrc
# Windows:
Remove-Item -Recurse -Force ~/AppData/Local/hermes; $env:Path = $env:Path.Replace("$HOME\.hermes\bin;", "")
```