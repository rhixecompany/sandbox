# GitHub Copilot CLI — Research Documentation

> **Source:** Web research compiled 2026-06-01
> **Version:** v1.0.33 (npm-installed)
> **Auth Method:** GH_TOKEN (fine-grained PAT with Copilot Requests permission)

---

## 1. Overview

GitHub Copilot CLI brings AI-powered coding assistance directly to the terminal. It's the successor to the deprecated `gh-copilot` extension (deprecated October 2025). It uses the same agentic harness as GitHub's Copilot coding agent with deep GitHub integration.

**Official Docs:** https://docs.github.com/en/copilot  
**GitHub:** https://github.com/github/copilot-cli  
**NPM:** `@github/copilot`

### Key Features
- Natural language coding assistance
- Deep GitHub integration (PRs, issues, repos)
- `/plan` and `/fleet` commands for parallel execution
- `/delegate` to Copilot in the cloud
- LSP server integration
- BYOK (Bring Your Own Key) support

---

## 2. Installation

### Via npm (cross-platform)
```bash
npm install -g @github/copilot
```

### Via WinGet (Windows)
```bash
winget install --id GitHub.CopilotCLI
```

### Via Homebrew (macOS/Linux)
```bash
brew install --cask copilot-cli
```

### Via install script (macOS/Linux)
```bash
curl -fsSL https://raw.githubusercontent.com/github-copilot-cli/main/install.sh | bash
```

### Verify
```bash
copilot --version
# 1.0.33
```

---

## 3. Authentication

### Authentication Priority
1. **Environment Variable** (highest): `COPILOT_GITHUB_TOKEN` > `GH_TOKEN` > `GITHUB_TOKEN`
2. **OAuth stored token**: From `copilot login` / `/login` device flow
3. **GitHub CLI fallback**: Uses `gh auth token`

### Via OAuth Device Flow (Interactive)
```bash
# Terminal login
copilot login

# In-session login
# Type: /login

# Enter the one-time code at https://github.com/login/device
```

### Via Fine-grained PAT (Non-interactive)
1. GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Resource owner: **Must be personal account** (not org)
3. Permissions → Account → **Copilot Requests** (Read)
4. Set env var:
```bash
export GH_TOKEN="github_pat_...your_token..."
```

### Critical Authentication Notes
| Token Type | Prefix | Supported | Notes |
|-----------|--------|-----------|-------|
| OAuth token (device flow) | `gho_` | Yes | Default method |
| Fine-grained PAT | `github_pat_` | Yes | Must be user-owned with Copilot Requests permission |
| GitHub App token | `ghu_` | Yes | Via env variable |
| Classic PAT | `ghp_` | **No** | Not supported |

> **Warning:** `GH_TOKEN` env var silently overrides stored OAuth tokens. Unset it if you prefer OAuth login.

### BYOK (Bring Your Own Key)
If you configure your own LLM provider API keys:
- GitHub authentication is NOT required
- `/delegate`, GitHub MCP, and GitHub Code Search are disabled
- Set `COPILOT_OFFLINE=true` for fully offline mode

---

## 4. CLI Usage

### Interactive TUI
```bash
copilot
# Default model: Claude Sonnet 4.5
# Commands: /help, /login, /model, /plan, /fleet, /delegate
```

### One-Shot (Non-interactive)
```bash
copilot -p "Explain what 'git rebase -i HEAD~3' does"
copilot -p "Write a Python function to merge two sorted lists"
```

### Slash Commands (In-session)
| Command | Description |
|---------|-------------|
| `/login` | Authenticate with GitHub |
| `/logout` | Sign out |
| `/model` | Switch model (Claude Sonnet 4, GPT-5, etc.) |
| `/plan` | Create a multi-step implementation plan |
| `/fleet` | Distribute tasks to parallel agents |
| `/delegate` | Delegate to Copilot in the cloud |
| `/user list` | List available accounts |
| `/user switch` | Switch accounts |
| `/feedback` | Send feedback |
| `/experimental` | Enable experimental features |

### Experimental Mode
```bash
copilot --experimental
# Or in-session: /experimental
# Features: Shift+Tab autocomplete, etc.
# Setting persists after first activation
```

---

## 5. ACPX Integration

### ACP Provider in Hermes
```yaml
providers:
  copilot-acp:
    base_url: acp://copilot
    api_mode: chat_completions
```

### Delegation Patterns
```python
# Quick explanation
terminal(command="copilot -p 'Explain what this bash command does'", timeout=30)

# Code generation
terminal(command="copilot -p 'Write a JavaScript debounce function'", timeout=60)

# Interactive session
terminal(command="copilot", background=true, pty=true)
process(action="submit", session_id="<id>", data="Review main.py for bugs")
process(action="log", session_id="<id>")
process(action="write", session_id="<id>", data="\x03")
```

---

## 6. Rate Limits

| Tier | Request Type | Limit | Reset |
|------|-------------|-------|-------|
| Free | Premium requests | ~50/week | Sunday/Monday UTC |
| Pro/Pro+ | Premium requests | Higher quota | Weekly |
| Business/Enterprise | Premium requests | Higher quota | Weekly |

### When Rate Limited
- CLI returns rate limit errors
- Basic queries may still work at reduced priority
- **Fallback to OpenCode or Qwen Code**

### Check Status
```bash
copilot -p "check my quota"
```

---

## 7. LSP Server Integration

Copilot CLI supports Language Server Protocol for enhanced code intelligence.

### Configuration Files
- User-level: `~/.copilot/lsp-config.json`
- Repo-level: `.github/lsp.json`

### Example Configuration
```json
{
  "servers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "fileTypes": ["typescript", "typescriptreact"],
      "rootPatterns": ["tsconfig.json"]
    }
  }
}
```

> LSP servers are NOT bundled — install separately.

---

## 8. Usage Examples

### Quick Explain
```bash
copilot -p "Explain what 'docker compose up -d --scale web=3' does"
```

### Code Generation
```bash
copilot -p "Write a Python decorator that measures execution time"
```

### Debugging
```bash
copilot -p "Help me debug this error: TypeError: Cannot read property 'map' of undefined"
```

### PR Review
```bash
# In interactive session, navigate to PR context
# Or use /delegate for cloud-assisted review
```

---

## 9. Pitfalls & Troubleshooting

- **Rate limited (~50/week)** — biggest constraint. Use OpenCode or Qwen Code as fallback.
- **GH_TOKEN must be fine-grained PAT** — classic PATs (`ghp_`) won't work.
- **Env var overrides OAuth** — if `GH_TOKEN` is set, it's used regardless of saved OAuth tokens.
- **Org policy** — org admin must enable Copilot CLI in org settings.
- **`copilot` command, not `gh copilot`** — old `gh-copilot` extension deprecated Oct 2025.
- **LSP servers not bundled** — install `typescript-language-server` etc. separately.
- **BYOK disables some features** — `/delegate`, GitHub MCP, Code Search require GitHub auth.
- **First launch banner** — animated; use `copilot --banner` to see again.
- **Premium requests** — each prompt costs one premium request from monthly quota.

---

## 10. Sources

1. Auth Docs: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli  
2. GitHub Repo: https://github.com/github/copilot-cli  
3. Community Discussion (GH_TOKEN): https://github.com/orgs/community/discussions/167158  
4. NPM: https://www.npmjs.com/package/@github/copilot  
5. Premium Requests: https://docs.github.com/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premise-requests  
6. WinGet: https://github.com/microsoft/winget-pkgs/tree/master/manifests/g/GitHub/CopilotCLI  
