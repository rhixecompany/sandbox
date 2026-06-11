---
name: "Session Auto-Commit"
description: "Automatically commits and pushes changes when a Hermes coding agent session ends"
tags: ["automation", "git", "productivity", "hermes"]
---

# Session Auto-Commit Hook

Automatically commits and pushes changes when a Hermes coding agent session ends, ensuring work is always saved and backed up.

## Overview

This hook runs at the end of each Hermes agent session and:

1. Checks if inside a Git repository
2. Detects uncommitted changes via `git status --porcelain`
3. Stages all changes with `git add -A`
4. Creates a timestamped commit: `hermes-auto-commit: YYYY-MM-DD HH:MM:SS`
5. Attempts to push to remote (non-blocking on failure)

## Hook Events

| Event | Script | Timeout |
|-------|--------|---------|
| `sessionEnd` | `auto-commit.sh` | 30s |

## Installation

1. Ensure the script is executable:

   ```bash
   chmod +x C:/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/auto-commit.sh
   ```

2. Register the hook in `config.yaml` under `hooks:`.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SKIP_AUTO_COMMIT` | unset | Set to `true` to disable auto-commit |

## How It Works

```
Session End → Check git repo? → Check changes? → git add -A → git commit → git push
                  ↓ no             ↓ none           ↓           ↓            ↓ fail
              Skip (exit 0)    Skip (exit 0)    —           —         Log warning
```

- Uses `--no-verify` to skip pre-commit hooks
- Failed pushes don't block session termination
- Requires appropriate git credentials configured

## Safety

- Only commits when there are actual changes
- Never force-pushes
- Never commits in non-git directories
- Push failures are logged but non-fatal

## Source

Built-in Hermes hook.
