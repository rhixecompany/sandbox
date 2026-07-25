---
author: Hermes Agent
description: Use this skill when someone wants to learn GitHub Copilot CLI from scratch. Covers installation, authentication, basic commands, chat workflows, and common troubleshooting.
license: MIT
metadata:
  hermes:
    tags: [imported, github, copilot, cli, onboarding, tutorial]
name: copilot-cli-quickstart
tags:
- imported
- github
- copilot
- cli
- onboarding
- tutorial
- scripts
title: GitHub Copilot CLI Quickstart
version: 1.0.0
---

# GitHub Copilot CLI Quickstart

## Overview

Learn GitHub Copilot CLI from scratch. This skill covers installation, authentication, basic commands, chat workflows, and common troubleshooting.

## When to Use

- First-time Copilot CLI users
- Teams onboarding to Copilot CLI
- Setting up Copilot in CI/CD pipelines
- Switching from other AI coding tools

## When NOT to Use

- Advanced Copilot features (use `copilot-sdk`)
- Extension development (use `vscode-extension-playbook`)
- Copilot agent customization (use `vscode-ext-commands`)

## Workflow

### Phase 1: Install & Authenticate

```bash
# Install Copilot CLI (via npm)
npm install -g @github/copilot

# Or via GitHub CLI extension
gh extension install github/gh-copilot

# Authenticate
gh auth login
# or
copilot auth
```

### Phase 2: Basic Commands

```bash
# Start a chat session
copilot chat "How do I read a file in Python?"

# Explain code
copilot explain path/to/file.ts

# Generate tests
copilot test path/to/function.py

# Fix issues
copilot fix "Handle null pointer in user service"
```

### Phase 3: Chat Workflows

```bash
# Interactive chat
copilot chat

# With context files
copilot chat --context src/main.py "Add error handling"

# Save session
copilot chat --save session.json

# Load session
copilot chat --load session.json
```

### Phase 4: Configuration

```bash
# Set default model
copilot config set model gpt-4

# Configure preferences
copilot config set editor vscode

# View config
copilot config list
```

## Verification Checklist

- [ ] Copilot CLI installed successfully
- [ ] Authentication completed (gh auth status shows logged in)
- [ ] Basic chat command works
- [ ] Code explanation works
- [ ] Test generation works
- [ ] Configuration persists

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `gh-cli` | GitHub CLI operations |
| `github` | GitHub API access |

## Related Skills

- `copilot-sdk` — Advanced Copilot integration
- `vscode-ext-commands` — VS Code extension commands
- `github` — GitHub API operations

## Usage Examples

```bash
# Quick question
copilot chat "What's the difference between map and flatMap?"

# Code review
copilot chat --context src/ "Review this for security issues"

# Generate documentation
copilot chat --context src/api.ts "Generate JSDoc comments"

# Debug help
copilot chat "Why is my async function not awaiting properly?"
```

## Error Handling

- **Auth failed:** Run `gh auth login` or `copilot auth` again
- **Model not available:** Check `copilot config list` and GitHub Copilot subscription
- **Network timeout:** Use `--timeout` flag, default 30s
- **Command not found:** Ensure `copilot` is on PATH or use `gh copilot`

## Pitfalls

- **Subscription required:** GitHub Copilot subscription needed for full features
- **Model limits:** Free tier has different model access than Pro/Business
- **Context window:** Large files may exceed context — use `--context` selectively
- **Rate limits:** API calls are rate-limited — batch requests when possible

## References

- Copilot CLI docs: <https://docs.github.com/en/copilot/github-copilot-in-the-cli>
- `references/copilot-commands.md` — Complete command reference
- `references/copilot-models.md` — Model comparison and selection