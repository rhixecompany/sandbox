---
name: tmux-terminal-multiplexer
title: "tmux — Terminal Multiplexer"
description: "Guide for tmux (Windows port) — session management, window/panel operations, and persistent terminal workflows."
version: 1.0.0
author: "Hermes Assistant"
tags: [tmux, terminal, multiplexer, windows]
---

# tmux — Terminal Multiplexer

## When to Use
- Running long-lived processes in the background
- Managing multiple terminal sessions in one window
- Persisting sessions across disconnects (SSH/remote work)

## Key Commands

### Session Management
| Command | Purpose |
|---------|---------|
| `tmux` | Start new session |
| `tmux new -s <name>` | Start named session |
| `tmux ls` | List sessions |
| `tmux a` | Attach to last session |
| `tmux a -t <name>` | Attach to named session |
| `tmux kill-ses -t <name>` | Kill session |
| `tmux has -t <name>` | Check if session exists |

### Within tmux (Prefix: Ctrl+b)
| Binding | Action |
|---------|--------|
| `Ctrl+b c` | New window |
| `Ctrl+b n/p` | Next/previous window |
| `Ctrl+b w` | List windows |
| `Ctrl+b %` | Vertical split |
| `Ctrl+b "` | Horizontal split |
| `Ctrl+b arrow` | Navigate panes |
| `Ctrl+b d` | Detach session |
| `Ctrl+b ,` | Rename window |
| `Ctrl+b x` | Kill pane |

## Pitfalls
- Windows tmux port has slightly different key bindings than Linux tmux
- Use `tmux kill-ses` to clean up stale sessions
- Prefix key remapping can be configured in `~/.tmux.conf`
- `tmux has -t <name>` returns exit code 0 if session exists (useful for scripting)
