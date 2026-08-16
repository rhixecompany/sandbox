# Quick Commands Reference

Cross-platform reference for Hermes quick commands. These are Hermes CLI-native
and are available to any agent that runs through the Hermes backend.

**As of**: 2026-08-16

## Available Commands

| Command | Type | What it does | Platform availability |
|---|---|---|---|
| `diff` | exec | `git diff --stat origin/development...HEAD` | Hermes only |
| `gc` | alias | Routes to `/commit` | Hermes only |
| `log` | exec | `git log --oneline -10` | Hermes only |
| `pr` | exec | Branch + unpushed log summary | Hermes only |
| `st` | exec | `git status --short \| head -30` | Hermes only |
| `tree` | exec | Project directory tree (`ls -d projects/*/`) | Hermes only |
| `ws` | exec | `pwd` — print working directory | Hermes only |

## Platform Coverage

- **Hermes**: All 7 commands available natively via `quick_commands:` in config.yaml
- **OpenCode**: Inherits via Hermes backend (opencode-zen provider)
- **Codex**: No direct equivalent; use shell commands directly
- **GitHub Copilot**: No direct equivalent; use VS Code keybindings or terminal
- **VS Code**: No direct equivalent; use `tasks.json` or terminal

## Source

Defined in `~/AppData/Local/hermes/config.yaml` under `quick_commands:`.

```yaml
quick_commands:
  diff:
    command: cd ~/Desktop/SandBox && git diff --stat origin/development...HEAD
    type: exec
  gc:
    target: /commit
    type: alias
  log:
    command: cd ~/Desktop/SandBox && git log --oneline -10
    type: exec
  pr:
    command: 'cd ~/Desktop/SandBox && echo Branch: && git branch --show-current && echo === Unpushed === && git log origin/development..HEAD --oneline'
    type: exec
  st:
    command: cd ~/Desktop/SandBox && git status --short | head -30
    type: exec
  tree:
    command: ls -d ~/Desktop/SandBox/projects/*/ | sed 's|.*/projects/||;s|/||'
    type: exec
  ws:
    command: pwd
    type: exec
```
