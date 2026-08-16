---
name: tmux-terminal-multiplexer
title: "tmux — Terminal Multiplexer"
description: "Guide for tmux (Windows port) — session management, window/panel operations, and persistent terminal workflows."
version: 1.0.0
author: "Hermes Assistant"
tags: [tmux, terminal, multiplexer, windows]
license: MIT
---
# tmux — Terminal Multiplexer

## Overview

Automated reasoning and workflow tool for `tmux-terminal-multiplexer`. Execute multi-step tasks with deterministic quality controls and structured outputs.

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

## Verification Checklist

- [ ] All tasks completed
- [ ] Output verified
- [ ] Edge cases handled

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "tmux — Terminal Multiplexer".

### Phase 2: Execution

Run the primary "tmux — Terminal Multiplexer" operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
