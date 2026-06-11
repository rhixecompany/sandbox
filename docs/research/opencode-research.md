# OpenCode AI — Research Documentation

> **Source:** Web research compiled 2026-06-01
> **Version:** v1.15.12 (npm-installed)

---

## 1. Overview

OpenCode is a provider-agnostic, open-source AI coding agent that runs in the terminal. It supports 75+ LLM providers via the AI SDK and Models.dev, making it the most flexible ACPX agent for coding tasks.

**Official Docs:** https://opencode.ai/docs  
**GitHub:** https://github.com/anthropics/opencode  
**NPM:** `opencode-ai`

### Key Features
- Provider-agnostic (75+ LLM providers)
- ACP server mode (`opencode acp`)
- Two built-in agents: `build` (full access) and `plan` (read-only)
- One-shot CLI with `opencode run`
- Interactive TUI with session management
- MCP server integration
- GitHub PR review workflow

---

## 2. Installation

### Via npm (official)
```bash
npm install -g opencode-ai@latest
```

### Via Homebrew (macOS/Linux)
```bash
brew install anomalyco/tap/opencode
```

### Verify
```bash
opencode --version
# 1.15.12
```

---

## 3. Authentication & Provider Setup

OpenCode stores provider credentials in `~/.local/share/opencode/auth.json`. You can authenticate multiple providers.

### Interactive Auth (TUI)
```bash
opencode
# Type /connect and select provider
# Paste API key when prompted
```

### Auth Commands (CLI)
```bash
# List authenticated providers
opencode auth list

# Login to specific provider
opencode auth login --provider anthropic

# Logout from provider
opencode auth logout
```

### Provider Configuration (opencode.json)
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "options": {
        "timeout": 600000,
        "chunkTimeout": 30000,
        "setCacheKey": true
      }
    },
    "openai": {
      "options": {
        "apiKey": "sk-..."
      }
    }
  }
}
```

### Available Providers (Notable)
| Provider | Setup | Notes |
|----------|-------|-------|
| **OpenCode Zen** | `/connect` → OpenCode Zen → opencode.ai/auth | Curated tested models, recommended |
| **OpenCode Go** | `/connect` → OpenCode Go → opencode.ai/auth | Low-cost subscription |
| **GitHub Copilot** | `/connect` → GitHub Copilot | Use Copilot subscription |
| **Anthropic** | API key or OAuth | Claude models |
| **OpenAI** | API key | GPT models |
| **Google Gemini** | API key | Gemini models |
| **OpenRouter** | API key | Many models via one key |
| **Local models** | OpenAI-compatible endpoint | Atomic Chat, Ollama, etc. |

---

## 4. CLI Usage Reference

### Main Commands
```bash
opencode                    # Start TUI
opencode [project]          # Start TUI in project
opencode run "prompt"       # One-shot execution
opencode run -f file.txt    # With file context
opencode acp                # Start ACP server
opencode serve              # Headless HTTP server
opencode web                # Web UI server
opencode attach <url>       # Attach TUI to server
opencode pr <number>        # Review PR
opencode models             # List available models
opencode session list       # List sessions
opencode stats              # Token/cost stats
```

### `opencode run` Flags
| Flag | Short | Description |
|------|-------|-------------|
| `--model` | `-m` | Model in `provider/model` format |
| `--agent` | | Agent to use (`build` or `plan`) |
| `--file` | `-f` | Attach file(s) to message |
| `--format` | | Output format (`default` or `json`) |
| `--thinking` | | Show model thinking blocks |
| `--variant` | | Reasoning effort (high, max, minimal) |
| `--continue` | `-c` | Continue last session |
| `--session` | `-s` | Session ID to continue |
| `--title` | | Session title |
| `--attach` | | Attach to running server |
| `--dir` | | Working directory |
| `--dangerously-skip-permissions` | | Auto-approve all actions |

### Agent Selection
```bash
opencode run "Review auth module" --agent plan     # Read-only review
opencode run "Implement feature" --agent build      # Full access (default)
```

---

## 5. ACPX Integration

### ACP Server Mode
```bash
# Start ACP server (default: stdin/stdout)
opencode acp

# With network port
opencode acp --port 8080 --hostname 0.0.0.0

# With CORS for browser clients
opencode acp --cors http://localhost:5173
```

### Hermes ACP Provider Configuration
```yaml
providers:
  opencode-acp:
    base_url: acp://opencode
    api_mode: chat_completions
```

### Delegation Patterns
```python
# One-shot coding task (no pty needed)
terminal(command="opencode run 'Add retry logic to API calls'", timeout=300)

# With specific model (must include opencode/ prefix)
terminal(command="opencode run 'Write tests' --model opencode/claude-haiku-4-5", timeout=300)

# With file context
terminal(command="opencode run 'Review this' -f config.yaml -f .env.example", timeout=300)

# Code review (plan agent)
terminal(command="opencode run 'Review auth for security' --agent plan", timeout=300)

# Interactive session
terminal(command="opencode", background=true, pty=true)
process(action="submit", session_id="<id>", data="Implement OAuth flow")
process(action="log", session_id="<id>")
process(action="write", session_id="<id>", data="\x03")  # Exit
```

### Model Prefix Requirement
**Important:** Model names require `opencode/` prefix:
- ✅ `opencode run --model "opencode/claude-haiku-4-5"`
- ❌ `opencode run --model "claude-haiku-4-5"` (will fail)

---

## 6. Configuration (opencode.json)

Locations (merged, highest priority wins):
1. Remote: `/.well-known/opencode` (org defaults)
2. Global: `~/.config/opencode/opencode.json`
3. `OPENCODE_CONFIG` env variable
4. Per-project: `opencode.json` in project root
5. `.opencode/` subdirectories (agents, commands, plugins, etc.)
6. `OPENCODE_CONFIG_CONTENT` env variable
7. Managed files (OS-specific)

### Key Config Options
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5",
  "default_agent": "build",
  "autoupdate": true,
  "server": { "port": 4096 },
  "shell": "pwsh",
  "tools": { "write": true, "bash": true },
  "disabled_providers": [],
  "enabled_providers": ["anthropic", "openai"]
}
```

---

## 7. MCP Server Integration

```bash
# Add MCP server
opencode mcp add

# List configured MCP servers
opencode mcp list

# OAuth for MCP servers
opencode mcp auth <name>

# Debug MCP issues
opencode mcp debug <name>
```

---

## 8. Usage Examples

### Code Generation
```bash
opencode run "Create a Python FastAPI CRUD for users with SQLite"
```

### Code Review
```bash
opencode run "Review the authentication module for security issues" --agent plan
```

### Refactoring
```bash
opencode run "Refactor main.py to use async/await patterns"
```

### PR Review
```bash
opencode pr 42
```

### Bug Fixing
```bash
opencode run "Fix the type error in src/parser.ts"
```

---

## 9. Pitfalls & Troubleshooting

- **Model prefix required** — always use `opencode/` prefix for model names.
- **Timeout on slow providers** — use long timeouts (300s+) for first-run cold starts.
- **`/exit` is NOT a valid command** — use Ctrl+C to exit TUI.
- **bun-pty unavailable on Windows** — TUI features limited but `run` works fine.
- **PATH mismatch** — multiple OpenCode binaries may exist; use `which -a opencode` to check.
- **Parallel sessions** — use separate workdirs to avoid git conflicts.
- **Credentials stored at** `~/.local/share/opencode/auth.json` — protect this file.
- **`opencode run` needs `--model` for non-default models** — if no default set, specify explicitly.

---

## 10. Sources

1. Official Docs: https://opencode.ai/docs  
2. Providers: https://opencode.ai/docs/providers  
3. CLI Reference: https://opencode.ai/docs/cli  
4. Config: https://opencode.ai/docs/config  
5. Dev.to Quickstart: https://dev.to/rosgluk/opencode-quickstart-install-configure-and-use-the-terminal-ai-coding-agent-4kcb  
6. GitHub: https://github.com/anthropics/opencode  
