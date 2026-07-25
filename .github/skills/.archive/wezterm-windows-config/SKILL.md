---
name: wezterm-windows-config
title: "WezTerm Windows Configuration"
description: "Research, edit, debug, and verify WezTerm config on Windows. Covers config file location, safe defaults, Lua config issues, keybinding behavior, font rendering, and runtime load errors."
version: 1.1.0
author: "Hermes Assistant"
license: MIT
tags: [wezterm, terminal, windows, lua, config]
related_skills: []
---

# WezTerm Windows Configuration

Use this skill when the user wants to review, benchmark, debug, or improve a WezTerm config on Windows.

## When to Use

- User mentions WezTerm config improvement, best-practice review, or debugging.
- User wants a safer or more ergonomic terminal setup on Windows.
- Config review should become a with-research => edit => reload-verify loop.

## Trigger Phrases

- "wezterm config"
- "wezterm best practices"
- "enhance wezterm config"
- "debug wezterm configuration"
- "wezterm lua error"

## Goal

Deliver a working config change backed by actual verification, not a description of one.

## Workflow

### Phase 1: Inspect the existing config

Do not install or rewrite blindly. First read the current config.

```bash
read_file(path="C:\\Users\\<user>\\.wezterm.lua", limit=500, offset=1)
```

If the config may be elsewhere on this machine, check home-directory candidates first:

```bash
terminal(command="ls -la ~/.wezterm.lua ~/.config/wezterm/wezterm.lua 2>/dev/null || echo no-wezterm-config")
```

If the user is inside WezTerm, note that `TERM_PROGRAM=WezTerm` is a strong signal that reload/verify commands can be run immediately.

### Phase 2: Research current best practices

Prefer authoritative sources first: official docs, then high-signal community guides.

Use `web_search` and `web_extract` to gather current guidance on:

- config location and reload behavior
- font, line height, tab bar, leader keys, pane workflow
- Windows-specific settings
- known breaking changes in current WezTerm releases

Key topics to research:

- `inactive_pane_hsb` -- dim inactive panes for focus (default: { saturation = 0.9, brightness = 0.8 })
- `window_padding` -- default is 1cell left/right, 0.5cell top/bottom; tighter px values reclaim space
- `freetype_load_target` / `freetype_render_target` -- major Windows font rendering quality: 'Light' + 'HorizontalLcd' approximates Windows Terminal rendering
- `underline_thickness` / `underline_position` -- use '2px' and -2 for better underline visibility
- `front_end` version history: default was 'WebGpu' briefly around 20240128, reverted to 'OpenGL' after; verify version before commenting
- `bypass_mouse_reporting_modifiers` -- defaults to 'SHIFT', sufficient for most setups
- `unix_domains` on Windows is dead config without WSL multiplexer use

Capture only the pieces that affect this config. Do not mirror upstream docs.

## Pitfalls

- Do not copy macOS- or Linux-specific settings blindly.
- `web_search` results may describe features from newer WezTerm releases than the installed binary. Cross-check with `terminal(command="wezterm --version")` before assuming an option exists.
- **front_end default history**: Before 20240128-x default was OpenGL. Around 20240128(wezterm 20240203-x) default briefly became WebGpu. After 20240128-y default reverted back to OpenGL. Check version before commenting.
- **read_file backslash display**: read_file double-escapes backslashes in display (shown as \\\\ but actual file has \\). Verify Lua escaping with cat -A or hexdump if unsure.
- **Lua unknown escapes**: \G, \P, \F etc are not standard Lua escapes. Behavior differs by Lua version. Use \\ pairs for guaranteed single backslash.
- Do not inline scripts or install packages unless the user asked; keep this skill scoped to WezTerm config editing and verification.

### Phase 3: Plan minimal, safe changes

Prefer small, reversible edits over rewrites.

Safe defaults for a Windows/MSYS/Hermes workflow often include:

- a configurable initial size with `adjust_window_size_when_changing_font_size = true`
- tighter `window_padding` (e.g. { left = '6px', right = '6px', top = '2px', bottom = '2px' })
- `inactive_pane_hsb` with saturation=0.9 brightness=0.75 to dim inactive panes
- sensible close-confirmation behavior (`skip_close_confirmation_for_processes_named`)
- tmux-like leader key workflow for split/tab/pane commands
- freetype_load_target='Light' + freetype_render_target='HorizontalLcd' for Windows font rendering
- conservative performance defaults: capped animation FPS, high-performance GPU preference
- persistent local-session support via `unix_domains` if the user wants multiplexing later

Keep unchanged what you did not evaluate.

### Phase 4: Apply changes with verification

Edit with `write_file` for whole-file rewrites or `patch` for targeted fixes.

After every edit, verify load behavior:

```bash
terminal(command="wezterm -e 'exit' 2>&1 | tail -n 40", timeout=60)
```

Interpret output carefully:

- If config loads cleanly, WezTerm may still report a PTY fallback message like `CreateProcessW ... failed`; that is typical for the `-e 'exit'` probe and is not necessarily a config failure.
- If config load fails, the error usually names the exact option and expected type.

### Phase 5: Debug config load failures

Common failure classes:

1. **Wrong module require**
   - Error shape: `module 'wezterm.action' not found`
   - Cause: older/newer config style expecting a non-existent module path
   - Fix: use `local act = wezterm.action` from `local wezterm = require 'wezterm'`

2. **Enum/bool mismatch**
   - Error shape: `Cannot convert 'Bool' to 'AllowSquareGlyphOverflow'`
   - Cause: option changed from boolean to enum scheme
   - Fix: use the documented string value, often `'Always'`

3. **Window/chrome options**
   - Prefer `window_decorations = 'RESIZE'` unless the user explicitly wants frameless.

4. **Leader-keybind conflicts**
   - If leader key collides with shell shortcuts, change the binding instead of silently overriding input behavior.

### Phase 6: Runtime sanity checks

If the user is actually using WezTerm, confirm behavior with one of these rather than assuming success:

```bash
terminal(command="wezterm cli list 2>&1 | tail -n 20")
```

Use `wezterm cli list` to verify whether the active window reflects the new config.

### Phase 7: Summarize changes in proof, not prose

Report:

- changed settings
- exact load-verify result
- runtime check result, if available
- next manual reload shortcut, if applicable

## General Principles

- User prefers concise, action-first output.
- Do not narrate research; show the finding and the change.
- Do not create backup files; use git for rollback.
- Prefer MCP-first tool precedence when equivalent MCP filesystem actions apply.

## References

- `references/verify-lua-config-probes.md` -- lightweight reload probes and how to interpret WezTerm config-load output on Windows

## Verification Checklist

- [ ] Existing config inspected before changes
- [ ] Research completed with source-of-truth preference
- [ ] Changes are minimal and reversible
- [ ] Config reload probe executed after edits
- [ ] Known config errors debugged or reported honestly
- [ ] User got changed settings + verification evidence in one summary