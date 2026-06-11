---
name: copilot-cli
title: GitHub Copilot CLI
description: "Use GitHub Copilot CLI as an ACPX coding agent for all coding tasks."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Copilot, GitHub, ACP, Autonomous]
    related_skills: [opencode, qwen-code, hermes-agent]
---
## Goal
Use GitHub Copilot CLI as an ACPX coding agent for all coding tasks.


# GitHub Copilot CLI ACPX Integration

Use [GitHub Copilot CLI](https://github.com/github/copilot-cli) as an ACPX coding agent orchestrated by Hermes. Brings AI-powered coding assistance directly to your terminal, enabling you to build, debug, and understand code through natural language conversations.

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

- User explicitly asks to use Copilot CLI
- Quick command explanations (`copilot explain`)
- Code generation with GitHub context awareness
- PR review and GitHub-native workflows (`review PR #N`)
- GitHub issue investigation
- CI/CD workflow debugging
- Repository structure overview
- `/plan` and `/fleet` parallel agent execution

## Prerequisites

- Copilot CLI installed:
  - npm: `npm install -g @github/copilot`
  - WinGet: `winget install --id GitHub.CopilotCLI`
  - macOS: `brew install --cask copilot-cli`
- Active GitHub Copilot subscription (Free, Pro, Pro+, Business, or Enterprise)
- Auth: `GH_TOKEN` or `GITHUB_TOKEN` environment variable with "Copilot Requests" permission, or interactive `/login`
- Verify: `copilot --version`

## ACPX Configuration

### Hermes Config.yaml (Already Configured)

```yaml
providers:
  copilot-acp:
    base_url: acp://copilot
    api_mode: chat_completions
```

### Recommended Model
Set to `auto` — Copilot CLI auto-selects the best available model (currently Claude Sonnet 4.5 default).

### Auth Setup

```bash
# Option 1: Interactive login (recommended)
copilot login
# Or type /login inside interactive session

# Option 2: Personal Access Token (fine-grained PAT only)
export GH_TOKEN="github_pat_..."
# Note: GH_TOKEN env var overwrites OAuth login. Unset it to use OAuth.

# Option 3: GitHub CLI fallback
gh auth login
copilot  # auto-uses gh token
```

> **Critical:** Only fine-grained PATs (`github_pat_`) with "Copilot Requests" permission work. Classic PATs (`ghp_`) are NOT supported. The env var `GH_TOKEN` silently overrides stored OAuth tokens.

## Usage Modes

### Non-Interactive (One-Shot)

```bash
copilot -p "explain what 'git rebase -i HEAD~3' does"
```

### Interactive TUI

```bash
copilot
# Works best with pty=true for background sessions
```

### Experimental Mode (New Features)

```bash
copilot --experimental
# Enables Shift+Tab autocomplete and other in-development features
# Setting persists after initial activation
```

### Model Switching

```bash
# In interactive session:
/model claude-sonnet-4-5

# Default model: Claude Sonnet 4.5
# Available: Claude Sonnet 4, GPT-5, and more
```

### LSP Integration

```json
// ~/.copilot/lsp-config.json
{
  "servers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "fileTypes": ["typescript", "typescriptreact"]
    }
  }
}
```

## Model Configuration

**Default model:** `auto` — Copilot CLI auto-selects the best available model. **No `--model` flag is needed or supported.** The `auto` model uses Claude Sonnet 4.5 by default.

To switch models in interactive session:
```
/model claude-sonnet-4.5     # Switch to Claude Sonnet
/model gpt-5                 # Switch to GPT-5
/model auto                  # Back to auto-select
```

## ACPX Delegation from Hermes

**Copilot always uses `auto` model** — no `--model` flag needed. ACPX and direct CLI both handle model selection automatically.

### Primary: via acpx exec (ACPX binary v0.10.0+)

```bash
# PR review via ACPX
acpx --approve-all --timeout 30 copilot exec "review the changes in the current branch"

# Issue analysis
acpx --approve-all --timeout 30 copilot exec "analyze issue #42 and suggest a fix"

# Code explanation
acpx --approve-all --timeout 30 copilot exec "explain the auth flow in src/auth/"

# Chained: {prompt} then {then}
acpx --approve-all --timeout 30 copilot exec '{prompt}' && acpx --approve-all --timeout 30 copilot exec '{then}'
```

### Fallback: direct CLI

```bash
# Non-interactive one-shot
copilot -p 'Write a Python function to merge two sorted lists'

# Chained via &&
copilot -p '{prompt}' && copilot -p '{then}'

# Interactive session
copilot
```

### Via ACP provider (Hermes config)

The `copilot-acp` provider connects to Copilot CLI via ACP protocol. Already configured in Hermes config:

```yaml
providers:
  copilot-acp:
    base_url: acp://copilot
    api_mode: chat_completions
```

## Common Flags

| Flag | Use |
|------|-----|
| `-p "prompt"` | Non-interactive prompt |
| `--experimental` | Enable experimental features |
| `--model` | Switch model (in-session) |
| `--banner` | Show animated banner |
| `--version` | Show version |

## Procedure

1. Verify installation: `copilot --version`
2. Check auth: `copilot` (interactive login if needed)
3. For quick questions, use `copilot -p "..."`
4. For coding tasks, use interactive TUI mode
5. Rate limited: 1 premium request per prompt (monitor quota)

## Pitfalls

- **Weekly rate limit** of ~50 premium requests applies. Once exhausted, CLI returns rate limit errors until reset.
- **Copilot always uses `auto` model** — no `--model` flag. Model switching only works inside interactive session with `/model` command.
- `GH_TOKEN` must include "Copilot Requests" permission — a classic PAT without this scope won't work.
- Organization/Enterprise users: admin must enable Copilot CLI in org settings.
- LSP servers are NOT bundled — install separately (e.g., `npm install -g typescript-language-server`).
- Copilot CLI uses `copilot` command (not `gh copilot`) — the old `gh-copilot` extension was deprecated Oct 2025.

## Rate Limit Management

Copilot CLI has a weekly premium request quota (~50/week). When exhausted:
1. Fall back to OpenCode or Qwen Code for coding tasks
2. Rate limits reset weekly (Sunday night/Monday morning UTC)
3. ACPX exec also respects the same rate limits — use fallback agents if `acpx copilot exec` fails

## Verification

Smoke test:

```bash
# Via ACPX exec (primary)
acpx --approve-all --timeout 30 copilot exec "Explain what 'ls -la' does"

# Direct CLI (fallback)
copilot -p "Explain what 'ls -la' does"
```

Success criteria:
- `acpx copilot exec` returns result without errors
- Direct CLI responds without connection errors
- ACP provider connects properly
- Can explain commands or generate code
- Expect rate limit messages if quota exhausted — still counts as "working, quota exhausted"

## Verification Checklist

- [ ] Copilot CLI installed and version confirmed
- [ ] Auth configured (PAT or interactive login)
- [ ] ACP provider integrated with Hermes
- [ ] Rate limit status documented
- [ ] Fallback agent strategy defined
