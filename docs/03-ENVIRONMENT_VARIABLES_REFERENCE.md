# Hermes Agent Environment Variables Complete Reference

**Document Type:** Environment Configuration Reference  
**Version:** 1.0  
**Hermes Version:** v0.14.0+  
**Updated:** May 25, 2026

---

## Overview

All environment variables are stored in:

```
~/.hermes/.env
```

Or set via CLI:

```bash
hermes config set VARIABLE_NAME value
```

---

## Table of Contents

1. [LLM Providers](#llm-providers)
2. [Tool API Keys](#tool-api-keys)
3. [Terminal Backend Configuration](#terminal-backend-configuration)
4. [MCP Server Configuration](#mcp-server-configuration)
5. [Agent Behavior](#agent-behavior)
6. [Logging & Diagnostics](#logging--diagnostics)
7. [Platform-Specific](#platform-specific)

---

## LLM Providers

### Primary Providers (Choose One or More)

#### OpenRouter (Recommended)

```bash
OPENROUTER_API_KEY=sk-or-...
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
HERMES_OPENROUTER_CACHE=true
HERMES_OPENROUTER_CACHE_TTL=3600
```

**Sign Up:** https://openrouter.ai/  
**Use Case:** 200+ models, flexible pricing, recommended for beginners

#### OpenAI (GPT-4, GPT-4o)

```bash
OPENAI_API_KEY=sk-proj-...
OPENAI_BASE_URL=https://api.openai.com/v1
```

**Sign Up:** https://platform.openai.com/  
**Use Case:** Latest GPT models, production-grade

#### Anthropic (Claude)

```bash
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_BASE_URL=https://api.anthropic.com
```

**Sign Up:** https://console.anthropic.com/  
**Use Case:** Claude 3.5 Sonnet, best for reasoning

#### Google Gemini

```bash
GOOGLE_API_KEY=AIzaSy...
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai
HERMES_GEMINI_CLIENT_ID=...        # Optional OAuth
HERMES_GEMINI_CLIENT_SECRET=...    # Optional OAuth
HERMES_GEMINI_PROJECT_ID=...       # For paid tiers
```

**Sign Up:** https://aistudio.google.com/app/apikey  
**Use Case:** Free tier, Gemini models

#### GitHub Copilot (ACP)

```bash
COPILOT_GITHUB_TOKEN=ghp_... or gho_... or github_pat_...
GH_TOKEN=...                      # Fallback
GITHUB_TOKEN=...                  # Third priority
HERMES_COPILOT_ACP_COMMAND=copilot
HERMES_COPILOT_ACP_ARGS=--acp --stdio
```

**Note:** Only `gho_*` and `github_pat_*` tokens supported; not classic `ghp_*`  
**Sign Up:** GitHub Copilot subscription  
**Use Case:** Enterprise, GitHub-native

#### MiniMax (Global & China)

```bash
MINIMAX_API_KEY=...
MINIMAX_BASE_URL=https://api.minimax.io/v1
MINIMAX_CN_API_KEY=...            # China region
MINIMAX_CN_BASE_URL=https://api.minimaxi.com/v1
```

**Sign Up:** https://www.minimax.io/  
**Use Case:** Fast, affordable global models

#### Kimi / Moonshot AI

```bash
KIMI_API_KEY=...
KIMI_BASE_URL=https://api.moonshot.ai/v1
KIMI_CN_API_KEY=...               # China endpoint
KIMI_CN_BASE_URL=https://api.moonshot.cn/v1
```

**Sign Up:** https://platform.kimi.ai/  
**Use Case:** Kimi K2.5, strong coding

#### GLM / ZhipuAI (China)

```bash
GLM_API_KEY=...
GLM_BASE_URL=https://api.z.ai/api/paas/v4
ZAI_API_KEY=...                   # Alias
Z_AI_API_KEY=...                  # Alias
```

**Sign Up:** https://z.ai/ or https://open.bigmodel.cn/  
**Use Case:** GLM-4-Plus, China market

#### Nous Portal

```bash
NOUS_API_KEY=...
NOUS_BASE_URL=https://portal.nousresearch.com/api/v1
NOUS_INFERENCE_BASE_URL=...
```

**Sign Up:** https://portal.nousresearch.com/  
**Use Case:** Nous Research models

#### OpenCode Zen (Pay-as-you-go)

```bash
OPENCODE_ZEN_API_KEY=...
OPENCODE_ZEN_BASE_URL=https://opencode.ai/zen/v1
```

**Sign Up:** https://opencode.ai/auth  
**Use Case:** Curated, tested models

#### OpenCode Go ($10/month)

```bash
OPENCODE_GO_API_KEY=...
OPENCODE_GO_BASE_URL=https://opencode.ai/zen/go/v1
```

**Sign Up:** https://opencode.ai/auth  
**Use Case:** Open models (GLM-5, Kimi K2.5, MiniMax M2.5)

#### Qwen OAuth (Alibaba)

```bash
DASHSCOPE_API_KEY=...
DASHSCOPE_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1
HERMES_QWEN_BASE_URL=https://portal.qwen.ai/v1
```

**Sign Up:** https://dashscope.aliyun.com/  
**Use Case:** Qwen Cloud models

#### Other Providers

```bash
# Arcee Trinity
ARCEEAI_API_KEY=...
ARCEE_BASE_URL=...

# Xiaomi MiMo
XIAOMI_API_KEY=...
XIAOMI_BASE_URL=https://api.xiaomimimo.com/v1

# Tencent TokenHub
TOKENHUB_API_KEY=...
TOKENHUB_BASE_URL=https://tokenhub.tencentmaas.com/v1

# DeepSeek
DEEPSEEK_API_KEY=...
DEEPSEEK_BASE_URL=...

# NVIDIA
NVIDIA_API_KEY=...
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1

# Ollama
OLLAMA_API_KEY=...
OLLAMA_BASE_URL=https://ollama.com/v1

# xAI Grok
XAI_API_KEY=...
XAI_BASE_URL=https://api.x.ai/v1

# GMI Cloud
GMI_API_KEY=...
GMI_BASE_URL=https://api.gmi-serving.com/v1

# Kilo Code
KILOCODE_API_KEY=...
KILOCODE_BASE_URL=https://api.kilo.ai/api/gateway

# Novita
NOVITA_API_KEY=...
NOVITA_BASE_URL=https://api.novita.ai/openai/v1

# StepFun
STEPFUN_API_KEY=...
STEPFUN_BASE_URL=https://api.stepfun.com/v1
```

### Cloud & Enterprise Providers

#### Azure OpenAI

```bash
AZURE_FOUNDRY_API_KEY=...
AZURE_FOUNDRY_BASE_URL=https://<resource>.openai.azure.com/openai/v1
AZURE_ANTHROPIC_KEY=...           # For Claude on Azure

# Entra ID Authentication
AZURE_TENANT_ID=...
AZURE_CLIENT_ID=...
AZURE_CLIENT_SECRET=...
AZURE_FEDERATED_TOKEN_FILE=...    # AKS Workload Identity
AZURE_AUTHORITY_HOST=https://login.microsoftonline.com
IDENTITY_ENDPOINT=...             # Managed Identity
MSI_ENDPOINT=...
```

#### AWS Bedrock

```bash
AWS_REGION=us-east-1
AWS_PROFILE=default               # From ~/.aws/credentials
BEDROCK_BASE_URL=https://bedrock-runtime.us-east-1.amazonaws.com
```

#### Vercel AI Gateway

```bash
AI_GATEWAY_API_KEY=...
AI_GATEWAY_BASE_URL=https://ai-gateway.vercel.sh/v1
```

---

## Tool API Keys

### Web Search & Content

```bash
# Exa AI (AI-native search)
EXA_API_KEY=...

# Parallel.ai (Search/extract)
PARALLEL_API_KEY=...

# Firecrawl (Web search, extract, crawl)
FIRECRAWL_API_KEY=...

# Tavily (Research API)
TAVILY_API_KEY=...
```

### Image Generation

```bash
# FAL.ai (Image generation)
FAL_KEY=...
FAL_API_KEY=...

# OpenAI DALL-E (with OPENAI_API_KEY)
# Automatic if OPENAI_API_KEY set
```

### Audio & Music

```bash
# Suno AI (Music generation)
SUNO_AUTH_TOKEN=...
SUNO_SESSION_ID=...

# Mistral (Voxtral TTS/STT)
MISTRAL_API_KEY=...
```

### User Modeling

```bash
# Honcho (Cross-session AI understanding)
HONCHO_API_KEY=...
# Also requires ~/.honcho/config.json with enabled=true
```

---

## Terminal Backend Configuration

### Backend Selection

```bash
# Local (default)
TERMINAL_ENV=local

# Docker containers
TERMINAL_ENV=docker

# Remote SSH
TERMINAL_ENV=ssh

# Modal (serverless)
TERMINAL_ENV=modal

# Singularity
TERMINAL_ENV=singularity
```

### Container Configuration

```bash
# Docker/Podman binary
HERMES_DOCKER_BINARY=/usr/local/bin/docker
# Or: /usr/local/bin/podman

# Container images
TERMINAL_DOCKER_IMAGE=nikolaik/python-nodejs:python3.11-nodejs20
TERMINAL_SINGULARITY_IMAGE=docker://nikolaik/python-nodejs:python3.11-nodejs20
TERMINAL_MODAL_IMAGE=nikolaik/python-nodejs:python3.11-nodejs20
```

### Working Directory

```bash
# Local backend
TERMINAL_CWD=.

# Remote backends (use absolute path inside target)
TERMINAL_CWD=/home/agent/work
```

### Timeout & Cleanup

```bash
TERMINAL_TIMEOUT=60                # Command timeout (seconds)
TERMINAL_LIFETIME_SECONDS=300      # Auto-cleanup inactive environments
```

### SSH Remote Execution

```bash
TERMINAL_SSH_HOST=192.168.1.100
TERMINAL_SSH_USER=agent
TERMINAL_SSH_PORT=22
TERMINAL_SSH_KEY=~/.ssh/id_rsa
TERMINAL_SSH_TIMEOUT=10            # Connection timeout
```

### Sudo Support

```bash
# Enable passwordless sudo on remote (if configured)
TERMINAL_SUDO=true
```

**Note:** Can safely configure passwordless sudo on remote server since API keys are protected (agent cannot read `.env`)

---

## MCP Server Configuration

### Filesystem Server

```bash
HERMES_MCP_FILESYSTEM_ENABLED=true
HERMES_MCP_FILESYSTEM_COMMAND=fs
```

### Docker MCP Server

```bash
HERMES_MCP_DOCKER_ENABLED=true
HERMES_MCP_DOCKER_BINARY=/usr/bin/docker
# Or: /usr/local/bin/podman
```

### Next.js DevTools

```bash
HERMES_MCP_NEXTJS_ENABLED=true
```

### Playwright

```bash
HERMES_MCP_PLAYWRIGHT_ENABLED=true
```

### Custom MCP Servers

```bash
# Generic
HERMES_MCP_CUSTOM_ENABLED=true
HERMES_MCP_CUSTOM_COMMAND=npx custom-server
HERMES_MCP_CUSTOM_ENV_VAR=value
```

---

## Agent Behavior

```bash
# Maximum conversation turns
HERMES_MAX_TURNS=90

# Maximum retry attempts
HERMES_MAX_RETRIES=3

# API timeout (milliseconds)
HERMES_GATEWAY_TIMEOUT=3000

# Tool output max bytes
HERMES_TOOL_OUTPUT_MAX_BYTES=50000

# Max lines returned
HERMES_MAX_LINES=2000

# Enable verbose logging
HERMES_DEBUG=true
```

---

## Logging & Diagnostics

```bash
# Log level: DEBUG, INFO, WARNING, ERROR
HERMES_LOG_LEVEL=INFO

# Log format: json, text
HERMES_LOG_FORMAT=json

# Log file path
HERMES_LOG_FILE=~/.hermes/hermes.log

# Enable request/response logging
HERMES_DEBUG_HTTP=false
HERMES_DEBUG_TOOLS=false
```

---

## Platform-Specific

### Windows (WSL2)

```bash
# Git Bash path
TERMINAL_SHELL=/bin/bash

# Make sure WSL2 is installed
# Check: wsl --version
```

### macOS

```bash
# Homebrew prefix for tools
HOMEBREW_PREFIX=/usr/local
```

### Linux

```bash
# Standard paths work
# Check: which docker, which ssh
```

---

## Configuration Examples

### Minimal Setup (OpenRouter)

```bash
OPENROUTER_API_KEY=sk-or-...
```

### Full Development Setup

```bash
# LLM
OPENROUTER_API_KEY=sk-or-...

# Tools
EXA_API_KEY=...
FAL_KEY=...

# Terminal
TERMINAL_ENV=docker
TERMINAL_DOCKER_IMAGE=nikolaik/python-nodejs:python3.11-nodejs20

# MCP
HERMES_MCP_DOCKER_ENABLED=true

# Logging
HERMES_LOG_LEVEL=INFO
HERMES_DEBUG=false
```

### Remote Production Setup

```bash
# LLM
OPENAI_API_KEY=sk-proj-...

# Terminal (SSH remote)
TERMINAL_ENV=ssh
TERMINAL_SSH_HOST=prod.example.com
TERMINAL_SSH_USER=agent
TERMINAL_SSH_KEY=/home/hermes/.ssh/id_rsa

# Timeouts
TERMINAL_TIMEOUT=120
HERMES_GATEWAY_TIMEOUT=5000

# Logging
HERMES_LOG_LEVEL=INFO
HERMES_LOG_FILE=/var/log/hermes/hermes.log
```

### Enterprise Azure Setup

```bash
# Azure OpenAI
AZURE_FOUNDRY_API_KEY=...
AZURE_FOUNDRY_BASE_URL=https://resource.openai.azure.com/openai/v1
AZURE_TENANT_ID=...
AZURE_CLIENT_ID=...

# Terminal
TERMINAL_ENV=docker

# Logging
HERMES_DEBUG=true
```

---

## Setting Variables

### Via CLI

```bash
hermes config set OPENROUTER_API_KEY sk-or-...
```

### Via .env File

```bash
# Edit file
nano ~/.hermes/.env

# Add variables
OPENROUTER_API_KEY=sk-or-...
TERMINAL_ENV=docker
```

### Via export (Session Only)

```bash
export OPENROUTER_API_KEY=sk-or-...
hermes chat "Hello"
```

---

## Verification

### Check Configuration

```bash
hermes config show
```

### Test API Key

```bash
hermes chat "What is 2 + 2?"
```

### List Active Tools

```bash
hermes tools list
```

### Check MCP Servers

```bash
hermes mcp list
```

---

## Security Best Practices

✅ **DO:**
- Store API keys in `~/.hermes/.env`
- Use SSH backend for remote execution (protects API keys)
- Rotate API keys regularly
- Use strong, unique keys per provider
- Enable logging for auditing

❌ **DON'T:**
- Commit `.env` to git
- Share API keys via email/chat
- Use API keys in `.hermes.md` (project config)
- Store passwords in plain text
- Log API keys to console

---

**Document Version:** 1.0  
**Hermes Version:** v0.14.0+  
**Last Updated:** May 25, 2026  
**Author:** Alexa
