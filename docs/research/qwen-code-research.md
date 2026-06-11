# Qwen Code CLI — Research Documentation

> **Source:** Web research compiled 2026-06-01
> **Version:** v0.17.0 (Bun-installed)
> **Auth Method:** OpenRouter API key (not DashScope OAuth)

---

## 1. Overview

Qwen Code CLI is an open-source, agentic coding tool forked from Gemini CLI, adapted for the Qwen3-Coder model. It lives in the terminal and helps turn ideas into code through autonomous agentic workflows.

**Official Docs:** https://qwenlm.github.io/qwen-code-docs/en  
**GitHub:** https://github.com/QwenLM/qwen-code  
**NPM:** `@qwen-code/qwen-code`

### Capabilities
- Navigate and understand codebases
- Detect and fix coding issues
- Generate code and unit tests
- Create documentation and flowcharts
- Automate GitHub workflows
- Multi-agent roles (code, debug, architect)

---

## 2. Installation

### Via npm (official)
```bash
npm install -g @qwen-code/qwen-code
```

### Via Bun (Alexa's setup)
```bash
bun add -g qwen-code
```

### Verify
```bash
qwen --version
# 0.17.0
```

---

## 3. Authentication & Configuration

Qwen Code stores its config in `~/.qwen/settings.json`. The CLI uses OpenAI-compatible env vars for provider configuration:

### OpenRouter Configuration (Alexa's Setup)
```json
{
  "openai": {
    "baseUrl": "https://openrouter.ai/api/v1",
    "apiKey": "sk-or-...",
    "env": {
      "OPENROUTER_API_KEY": "sk-or-..."
    },
    "model": "openai/gpt-oss-120b:free"
  }
}
```

### Alternative Providers
| Provider | Base URL | Model |
|----------|----------|-------|
| OpenRouter | `https://openrouter.ai/api/v1` | `qwen/qwen3-coder` or any |
| Alibaba DashScope | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | `qwen3-coder-plus` |
| SambaNova | `https://api.sambanova.ai/v1` | `DeepSeek-V3.1` |

### Auth via Environment Variables
```bash
export OPENAI_API_KEY="your_key"
export OPENAI_BASE_URL="https://openrouter.ai/api/v1"
export OPENAI_MODEL="qwen/qwen3-coder"
```

> **Note:** `qwen auth qwen-oauth` was **removed** in v0.17.0. Auth is done interactively via `/auth` in the TUI or via env vars for headless/CI use.

---

## 4. CLI Usage

### Interactive TUI
```bash
qwen
# Press Enter to start
```

### One-Shot (Headless)
```bash
qwen "Your prompt here"
```

### YOLO Mode (Auto-approve)
```bash
qwen --yolo "Your prompt here"
# Suppress warning with: QWEN_CODE_SUPPRESS_YOLO_WARNING=1
```

### With File Context
```bash
qwen "Explain the architecture of this codebase"
# Qwen automatically scans files in the current directory
```

### Common Flags
| Flag | Description |
|------|-------------|
| `--yolo` | Auto-approve changes |
| `--model` | Specify model |
| `--debug` | Debug output |
| `--verbose` | Verbose logging |

---

## 5. ACPX Integration

Qwen Code can act as an ACPX agent via the `--acp` flag:

```bash
qwen --acp
# Starts ACP server mode on stdin/stdout
```

### Hermes ACP Provider Configuration
```yaml
providers:
  qwen-code:
    base_url: acp://qwen
    api_mode: chat_completions
```

### Delegation Patterns
```python
# Direct via terminal
terminal(command="qwen 'Implement Fibonacci generator' --yolo", timeout=60)

# With env var
terminal(command="QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo 'Write tests'", timeout=120)

# ACP server mode (background)
terminal(command="qwen --acp", background=true, pty=true)
```

---

## 6. Usage Examples

### Codebase Exploration
```bash
qwen "Explain the architecture of this codebase"
```
Qwen scans all files and returns architectural breakdown.

### Code Refactoring
```bash
qwen "Optimize the transcribe_audio function in @app.py"
```
Uses `@filename` syntax for scoped edits.

### Test Generation
```bash
qwen "Write pytest unit tests for the recent changes"
```
Creates test files, updates requirements.txt, runs tests.

### GitHub Automation
```bash
qwen "Create a new branch and commit changes with message 'v2: optimization'"
```
Uses WebFlow tool for git operations.

### Flowchart Generation
```bash
qwen "Create a Mermaid.js flowchart illustrating module interactions"
```

---

## 7. Key Differences from Other Agents

| Aspect | Qwen Code | OpenCode | Copilot CLI |
|--------|-----------|----------|-------------|
| Model | Qwen3-Coder (default) | Provider-agnostic | Claude Sonnet 4.5 |
| Installation | npm or Bun | npm | npm, brew, winget |
| Auth | OpenRouter / DashScope | Provider API keys | GH_TOKEN or OAuth |
| Headless | `qwen "prompt" --yolo` | `opencode run "prompt"` | `copilot -p "prompt"` |
| ACP mode | `qwen --acp` | `opencode acp` | Built-in ACP |
| Cost | Free tier via OpenRouter | Varies by provider | Copilot subscription |
| Rate limits | OpenRouter rate limits | None | ~50/week premium |

---

## 8. Pitfalls & Troubleshooting

- **`qwen auth qwen-oauth` removed** — command no longer exists in v0.17.0. Use OpenRouter or env vars for headless auth.
- **`--yolo` warning** — first use shows a safety warning. Set `QWEN_CODE_SUPPRESS_YOLO_WARNING=1` to suppress.
- **OAuth credential file (`oauth_creds.json`)** — not created with OpenRouter auth; only needed for DashScope OAuth.
- **OpenRouter model names** — use OpenAI-compatible format (`openai/gpt-oss-120b:free` or `qwen/qwen3-coder`).
- **No MCP server** — `qwen mcp` was removed in v0.17.0; MCP config files don't exist.
- **Node.js 20+ required** — verify with `node -v`.

---

## 9. Sources

1. Official Docs: https://qwenlm.github.io/qwen-code-docs/en  
2. DataCamp Tutorial: https://www.datacamp.com/tutorial/qwen-code  
3. SambaNova Integration: https://docs.sambanova.ai/docs/en/integrations/qwen-code-cli  
4. GitHub Repo: https://github.com/QwenLM/qwen-code  
5. NPM: https://www.npmjs.com/package/@qwen-code/qwen-code  
