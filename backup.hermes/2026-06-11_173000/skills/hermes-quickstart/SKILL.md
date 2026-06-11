---
name: hermes-quickstart
description: Complete Hermes Agent quickstart - install, provider selection, verification
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, getting-started, quickstart]
    category: getting-started
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.quickstart.enabled
        description: "Enable quickstart skill"
        default: "true"
---

# Hermes Quickstart Skill

## When to Use
- Setting up Hermes Agent for the first time
- Switching LLM providers
- Verifying a working chat configuration
- Troubleshooting "it installed but does nothing" scenarios

## Procedure
1. **Install Hermes Agent** (if not already installed):
   ```bash
   # Option A: pip (simplest)
   pip install hermes-agent
   hermes postinstall  # optional: installs Node.js, browser, ripgrep, ffmpeg
   
   # Option B: git installer (tracks main branch)
   curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
   source ~/.bashrc
   ```

2. **Choose a Provider** (most important step):
   ```bash
   hermes model  # Interactive provider selection
   
   # Easiest path: Nous Portal (one subscription = 300+ models + Tool Gateway)
   hermes setup --portal
   ```
   Provider options: OpenRouter, Anthropic, OpenAI Codex, Google Gemini, xAI, AWS Bedrock, Azure, local (Ollama/LM Studio), and 20+ more.

3. **Verify It Works**:
   ```bash
   hermes chat
   # Type a message - if you get a coherent response, you're done!
   ```

4. **If It Fails - Troubleshooting**:
   | Symptom | Likely Cause | Fix |
   |---------|--------------|-----|
   | "No model configured" | `hermes model` not run | Run `hermes model` and pick one |
   | "Authentication failed" | Bad API key / expired OAuth | Re-run `hermes model`; check `~/.hermes/.env` |
   | "Connection refused" | Network / proxy / DNS | Check internet; try different provider |
   | "Model not found" | Wrong model name for provider | Use `hermes model` picker (validates names) |

5. **Next Steps (Optional)**:
   - Connect a messenger: `hermes gateway setup` (Telegram, Discord, Slack, etc.)
   - Add skills: `/skills` → `/skill install`
   - Enable memory: `hermes memory setup`
   - Schedule tasks: `hermes cron create "daily summary" "0 9 * * *" "Summarize yesterday's commits"`

## Pitfalls
- **Don't add features before basic chat works** — Rule: if Hermes cannot complete a normal chat, do not add more features yet
- **PyPI vs main branch** — PyPI tracks tagged versions; for bleeding-edge use git installer
- **Windows requires WSL2** — Install WSL2 first, then run installer inside WSL2
- **Provider-specific limits** — Some providers need OAuth (Anthropic, OpenAI Codex), others need API keys

## Verification
- `hermes chat` responds coherently to a test message
- `hermes config show` displays correct provider and model
- No authentication errors in logs

## References
- `references/commands.md` — CLI commands reference
- `references/providers.md` — Complete provider catalog
- `references/troubleshooting.md` — Common issues and fixes