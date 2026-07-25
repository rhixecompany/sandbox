---
name: hermes-quickstart
title: "Hermes Agent Quickstart Guide"
description: "Use when getting started with Hermes Agent — covers installation (pip/git), provider setup (Nous Portal, Codex, Anthropic, OpenRouter, HF, Bedrock, DeepSeek, Copilot, custom), minimum context (64k), settings storage, first chat, and slash commands."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, quickstart, installation, providers, setup, cli, tui, nous-portal]
---
# Hermes Agent Quickstart Guide

## Purpose

Get Hermes Agent running in minutes — from installation to first chat with provider configured.

## When to Use

- First-time Hermes setup
- Switching providers
- New environment onboarding
- CI/CD agent setup

## When NOT to Use

- Deep architecture understanding (use deep-dive guide)
- Course learning (use NetworkChuck course)
- Memory specifics (use memory guides)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug provider auth, installation issues |
| `executing-plans` | Follow setup steps in order |

## Workflow

### Phase 1: Installation

**Option A: pip (stable)**
```bash
pip install hermes-agent
hermes postinstall
```

**Option B: git (bleeding edge)**
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**Platform Notes:**
- Windows: Install WSL2 first
- Android/Termux: See dedicated guide

### Phase 2: Choose Provider

```bash
hermes model          # interactive setup
hermes setup --portal # recommended: Nous Portal (OAuth, zero-config)
```

**Provider Quick Reference:**

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

### Phase 3: Minimum Context Requirement

**64,000 tokens minimum.** Models with smaller context windows are rejected.

### Phase 4: Settings Storage

| File | Contents |
|------|----------|
| `~/.hermes/.env` | Secrets and tokens |
| `~/.hermes/config.yaml` | Non-secret settings |

### Phase 5: First Chat

```bash
hermes          # classic CLI
hermes --tui    # modern TUI (recommended)
```

**TUI Controls:**
- Multi-line input: Alt+Enter or Ctrl+J
- Interrupt: Enter new message or Ctrl+C
- Session resume: `hermes --continue`

### Phase 6: Slash Commands

| Command | Action |
|---------|--------|
| `/help` | Show all commands |
| `/tools` | List available tools |
| `/model` | Switch models |
| `/personality pirate` | Try a personality |
| `/save` | Save conversation |

## Pitfalls

- **Context window too small** → Model rejected; use 64k+ models only
- **Nous Portal** → Easiest for beginners; handles provider complexity
- **Windows** → WSL2 required for full functionality
- **postinstall** → Required after pip install; sets up skills, hooks, config

### Error Handling

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: Use WSL2 for full Hermes functionality")
    elif system == "linux":
        print("Linux: Native support — run hermes --tui directly")
    elif system == "darwin":
        print("macOS: Native support — install via brew or pip")
    return system

# Common setup errors
SETUP_ERRORS = {
    "command_not_found": "Run: pip install hermes && hermes postinstall",
    "provider_not_responding": "Check API key: hermes config set provider.name.api_key KEY",
    "model_not_found": "List models: hermes auth list --provider name",
    "tui_not_launching": "Check terminal/SSH supports TUI (no embedded terminals)",
    "memory_not_loading": "Check file exists: ls -la ~/.hermes/memories/",
}

def resolve_setup_error(error: str) -> str:
    for key, message in SETUP_ERRORS.items():
        if key in error:
            return message
    return "Unknown — check hermes docs at https://hermes-agent.nousresearch.com/docs"
```

## Verification Checklist

- [ ] `hermes --version` shows version
- [ ] Provider configured and tested
- [ ] `hermes --tui` launches successfully
- [ ] Can send/receive messages
- [ ] Slash commands work
- [ ] Settings persist in ~/.hermes/

## References

- `references/provider-setup.md` — Detailed provider configuration
- `references/hermes-quickstart-patterns.md` — Quickstart code patterns

## Templates

- `templates/hermes-config-template.md` — Config file template

## Scripts

- `scripts/hermes-verify-setup.py` — Setup verification script
- `references/troubleshooting.md` — Common install issues
- `references/context-requirements.md` — Model context window list