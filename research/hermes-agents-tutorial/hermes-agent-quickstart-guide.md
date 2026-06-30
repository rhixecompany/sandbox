# Hermes Agent Quickstart Guide

> **Source:** https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
> **Retrieved:** 2026-06-01T00:00:00

---

## Installation

### Option A: pip (stable)
```bash
pip install hermes-agent
hermes postinstall
```

### Option B: git (bleeding edge)
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Platform notes:
- Windows: Install WSL2 first
- Android/Termux: See dedicated guide

## Choosing a Provider

```bash
hermes model  # interactive setup
hermes setup --portal  # recommended: Nous Portal (OAuth)
```

### Provider Quick Reference

| Provider | Type | Setup |
|----------|------|-------|
| Nous Portal | Subscription, zero-config | `hermes setup --portal` |
| OpenAI Codex | ChatGPT OAuth | `hermes model` |
| Anthropic | Claude (Max OAuth or API key) | `hermes model` |
| OpenRouter | Multi-provider routing | API key |
| Hugging Face | 20+ open models | HF_TOKEN |
| AWS Bedrock | Claude, Nova, Llama | IAM role |
| DeepSeek | Direct API | DEEPSEEK_API_KEY |
| GitHub Copilot | Copilot subscription | OAuth |
| Custom Endpoint | vLLM, Ollama, etc. | Base URL + API key |

## Minimum Context Requirement

**64,000 tokens minimum.** Models with smaller context windows are rejected.

## Settings Storage

| File | Contents |
|------|----------|
| ~/AppData/Local/hermes/.env | Secrets and tokens |
| ~/AppData/Local/hermes/config.yaml | Non-secret settings |

## First Chat

```bash
hermes          # classic CLI
hermes --tui    # modern TUI (recommended)
```

## Slash Commands

| Command | Action |
|---------|--------|
| /help | Show all commands |
| /tools | List available tools |
| /model | Switch models |
| /personality pirate | Try a personality |
| /save | Save conversation |

## Key Features

- Multi-line input: Alt+Enter or Ctrl+J
- Interrupt: Enter new message or Ctrl+C
- Session resume: `hermes --continue`
- Sandboxed terminal
- Skills system
- MCP support
- Cron jobs

---

*Extracted by web-research-pipeline v1.0.0*