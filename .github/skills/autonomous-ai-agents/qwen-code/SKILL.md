---
name: qwen-code
title: Qwen Code CLI
description: "Use Qwen Code v0.17.0 (Bun-installed) as an ACPX coding agent via OpenRouter API key for headless coding tasks."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Qwen, OpenRouter, Autonomous, ACPX]
    related_skills: [acpx-agent-routing, opencode, copilot-cli]
---
## Goal
Use Qwen Code v0.17.0 (Bun-installed) as an ACPX coding agent via OpenRouter API key for headless coding tasks.


# Qwen Code CLI

Use Qwen Code v0.17.0 as an autonomous coding worker orchestrated via Hermes terminal tools. Qwen Code is a CLI tool forked from Gemini CLI, adapted for agentic coding with Qwen3-Coder and other models.

## Workflow
### Phase 1: Preparation

- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution

- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification

- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.


## When to Use

- User explicitly asks to use Qwen Code
- Large codebase exploration and understanding
- Code refactoring and optimization
- Automatic test generation
- GitHub workflow automation
- Long-running autonomous tasks

## Prerequisites

- Qwen Code installed: `bun add -g qwen-code` or `npm install -g @qwen-code/qwen-code`
- OpenRouter API key configured in `~/.qwen/settings.json`
- Verify: `qwen --version` (should be 0.17.0+)
- Settings file at `~/.qwen/settings.json` with `openai` provider config

## Auth & Configuration

Qwen Code uses OpenAI-compatible provider configuration. Auth is done via API key in settings, NOT via DashScope OAuth.

### Settings Structure (`~/.qwen/settings.json`)
```json
{
  "modelProviders": {
    "openai": [{
      "id": "openai/gpt-oss-120b:free",
      "name": "[OpenRouter] openai/gpt-oss-120b:free",
      "baseUrl": "https://openrouter.ai/api/v1",
      "envKey": "OPENROUTER_API_KEY"
    }]
  },
  "model": {
    "name": "openai/gpt-oss-120b:free"
  },
  "env": {
    "OPENROUTER_API_KEY": "sk-or-..."
  }
}
```

### Key Facts
- **Auth method:** OpenRouter API key (NOT DashScope OAuth)
- **`qwen auth qwen-oauth` was removed** in v0.17.0 — this command no longer exists
- **No `oauth_creds.json` needed** — that file is only for DashScope OAuth
- **Headless flag:** `--yolo` required (suppress warning with `QWEN_CODE_SUPPRESS_YOLO_WARNING=1`)

## One-Shot Tasks

### Primary: via acpx exec

```bash
acpx --approve-all --timeout 30 qwen exec "Implement a Fibonacci generator in Python with memoization"
acpx --approve-all --timeout 30 qwen exec "Write pytest unit tests for the recent changes"
```

### Fallback: direct CLI

```bash
QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo "Implement a Fibonacci generator in Python with memoization"
QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo "Write pytest unit tests for the recent changes"
```

With scoped file context (direct only):
```bash
qwen "Optimize the transcribe_audio function in @app.py" --yolo
```

## ACPX Integration

Qwen Code supports ACP server mode via the `--acp` flag:

```bash
# Start ACP server
qwen --acp
```

### Hermes ACP Provider
```yaml
providers:
  qwen-code:
    base_url: acp://qwen
    api_mode: chat_completions
```
### Delegation from Hermes

**Primary: via acpx exec**

```bash
# Quick one-shot (recommended)
acpx --approve-all --timeout 30 qwen exec 'Write tests for auth module'

# Chained: {prompt} then {then}
acpx --approve-all --timeout 30 qwen exec '{prompt}' && acpx --approve-all --timeout 30 qwen exec '{then}'

# Codebase exploration
acpx --approve-all --timeout 60 qwen exec 'Explain the architecture of this codebase'

# Refactoring
acpx --approve-all --timeout 60 qwen exec 'Refactor the API routes to use async/await'
```

**Fallback: direct CLI**

```bash
# Quick one-shot
terminal(command="QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo 'Write tests for auth module'", timeout=120)

# Chained
terminal(command="QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo '{prompt}' && QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo '{then}'", timeout=600)
```

## Model Configuration

**Default model:** `OpenRouter | openai/gpt-oss-120b:free`

This is the primary model for all Qwen Code tasks via OpenRouter. It provides free tier access.

### Alternative OpenRouter Models
| Model | Cost | Notes |
|-------|------|-------|
| `openai/gpt-oss-120b:free` | Free | **Default** — 120B parameter model, free tier |
| `qwen/qwen3-coder` | $0.302/M tokens | Native Qwen model, best for code tasks |
| Any OpenAI-compatible model | Varies | Change `baseUrl` and model name |

### Config in `~/.qwen/settings.json`
```json
{
  "modelProviders": {
    "openai": [{
      "id": "openai/gpt-oss-120b:free",
      "name": "[OpenRouter] openai/gpt-oss-120b:free",
      "baseUrl": "https://openrouter.ai/api/v1",
      "envKey": "OPENROUTER_API_KEY"
    }]
  }
}
```

## Model Configuration (deprecated section)

Use the section above instead. This section kept for reference:

- **Default model:** `openai/gpt-oss-120b:free` via OpenRouter

## OpenRouter Rate Limits

- Free tier: Limited tokens/day
- Paid: $0.30-0.50/M tokens depending on model
- Rate limit resets based on subscription

## Pitfalls

- `--yolo` flag required for non-interactive (headless) mode — otherwise Qwen asks for confirmation
- Set `QWEN_CODE_SUPPRESS_YOLO_WARNING=1` to avoid the yolo warning every time
- `qwen auth qwen-oauth` command was REMOVED in v0.17.0 — do not attempt to use it
- No `oauth_creds.json` will ever exist with OpenRouter auth — ignore related Hermes log warnings (DEBUG level)
- MCP server feature (`qwen mcp`) was removed in v0.17.0
- Node.js 20+ required (Bun handles this automatically)
- OpenRouter model names use `openai/` prefix format (OpenAI-compatible)

## Verification

Smoke test (ACPX exec — primary):

```bash
acpx --approve-all --timeout 30 qwen exec "Reply with exactly: QWEN_ALIVE"
```

Direct CLI (fallback):

```bash
QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo "Reply with exactly: QWEN_ALIVE"
```

Success criteria:
- ACPX exec: output contains `QWEN_ALIVE`, exit code 0
- Direct CLI: output contains `QWEN_ALIVE`, exit code 0
- No auth errors

## Verification Checklist

- [ ] Qwen Code installed and version confirmed (0.17.0+)
- [ ] ACPX binary available (`acpx --version` should show 0.10.0+)
- [ ] Qwen responds via `acpx qwen exec`
- [ ] Direct CLI smoke test passes (`--yolo` works with env var)
- [ ] OpenRouter API key configured in settings.json
- [ ] Fallback strategy defined for rate limits
