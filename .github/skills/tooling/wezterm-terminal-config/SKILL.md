---
name: wezterm-terminal-config
title: "WezTerm Terminal Configuration"
description: "Configure, enhance, debug, and verify WezTerm configs safely, with Windows-specific best practices, modular Lua architecture, and runtime validation patterns."
version: 2.0.0
author: "Hermes Assistant"
license: MIT
tags: [terminal, wezterm, windows, lua, devops, tooling]
---

# WezTerm Terminal Configuration

## Purpose

Class-level skill for configuring WezTerm in production use across sessions.
Covers canonical file layout, Windows/MSYS workflow, modular Lua module architecture, common Lua gotchas, font/fallback strategy, keybinding ergonomics, event handlers, and a repeatable research-then-verify config-debug loop.

## When to Load

- User asks to set up, enhance, debug, or review WezTerm configuration.
- Session needs terminal performance, rendering, or keyboard workflow improvements in WezTerm.
- Config errors or font fallback problems are reported on Windows.
- User wants to refactor a monolithic config into reusable Lua modules.
- Triggers: WezTerm, wezterm config, wezterm.lua, terminal emulator config, terminal font, launch menu, Multiplexing in WezTerm.

## Quick Reference

| Concern | Recommendation |
|---------|----------------|
| Config location | Prefer `~/.config/wezterm/wezterm.lua` (XDG path, highest priority after CLI/thumb drive) |
| Module location | `~/.config/wezterm/*.lua` — Lua `package.path` includes this dir automatically |
| Module pattern | Each module exports `function module.apply_to_config(config)` and is required by the entry point |
| Edit pattern | research docs → save reference files to docs/ → patch config → validate with `wezterm -e 'exit'` |
| Font fallback | Prefer `wezterm.font_with_fallback{...}`; put available system fonts first, Consolas last |
| Key leader | `CTRL+A` matches tmux muscle memory; 2s timeout |
| Copy mode | Use `key_tables` to define vim-flavoured copy-mode key bindings |
| Event handlers | `update-right-status`, `format-tab-title`, `format-window-title`, `gui-startup` |
| Multiplexing | `unix_domains = { { name = 'unix' } }` for local mux |
| Windows shells | Add launch menu entries for pwsh, Git Bash, cmd |
| Verification | `wezterm -e 'exit'` checks config load without a full GUI session |
| Enum validation | `wezterm show-keys --lua --key-table copy_mode` shows installed version's actual valid CopyModeAssignment variants, NOT nightly docs |
| Windows 11 backdrop | `win32_system_backdrop = 'Mica'` requires `window_background_opacity < 1.0` |

## Workflow

### Phase 0: Research & Document
When the user asks to enhance from official docs, extract and save reference material first:

1. Extract main docs page: `web_extract(urls=["https://wezterm.org/config/files.html"])`
2. Extract linked sub-pages (config options index, appearance, key tables, events, etc.)
3. Save each extracted page as `docs/wezterm-reference/NN-topic.md` for the user's reference
4. Use the saved docs as the source of truth for config decisions

### Phase 1: Discovery
1. Check both config locations: `~/.wezterm.lua` and `~/.config/wezterm/wezterm.lua`.
   ```bash
   ls -la ~/.wezterm.lua ~/.config/wezterm/wezterm.lua 2>/dev/null
   ```
2. Read the active config with `read_file`.
3. Check installed fonts; on Windows without `fc-list`, inspect registry or `wezterm` fallback output.
4. Identify broken fields, expired best practices, or missing workflow helpers.

### Phase 2: Modular Architecture (preferred over monolith)

When the config grows beyond ~100 lines, refactor into the Lua module pattern documented in the WezTerm "Making your own Lua Modules" section:

```
~/.config/wezterm/
├── wezterm.lua        ← Entry point: requires + applies all modules
├── settings.lua       ← Fonts, geometry, cursor, performance, domains
├── appearance.lua     ← Colors, tab bar, window chrome, background
├── keys.lua           ← Leader, key bindings, copy-mode key tables, mouse
├── events.lua         ← gui-startup, update-right-status, format-tab-title, etc.
└── launch.lua         ← Launch menu, hyperlink rules, quick-select patterns
```

Each module follows this pattern:

```lua
-- module.lua
local wezterm = require 'wezterm'
local module = {}

function module.apply_to_config(config)
  config.some_option = value
end

return module
```

The entry point orchestrates them:

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()
local settings = require 'settings'
settings.apply_to_config(config)
-- ... more modules ...
return config
```

For a fallback-safe redirect at `~/.wezterm.lua`, use `pcall`:

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()
local ok, mod = pcall(require, 'settings')
if ok then mod.apply_to_config(config) end
return config
```

See `references/modular-architecture.md` for the full worked example with all 5 modules.

### Phase 2b: Enhance / Debug (monolith or per-module)
- Keep sections clearly separated: general behavior, font/rendering, window chrome, keys, UX, colors, input, performance, launch menu.
- Windows/MSYS considerations:
  - Use `wezterm.action` directly from the API object; `require 'wezterm.action'` can fail on Windows builds that disable safe-mode module loading.
  - String-backed enum options: `allow_square_glyphs_to_overflow_width = 'Always'`, not a boolean.
  - Avoid removed/renamed config keys; validate against current release.
  - Font rendering: use `wezterm.font_with_fallback{...}` ordered by availability, with a stable system font like Consolas last.
  - Close confirmation: use `skip_close_confirmation_for_processes_named` for shells you manage.
  - Paste normalization: `config.canonicalize_pasted_newlines = 'LineFeed'` to convert CRLF→LF in MSYS/WSL. Valid values: `'LineFeed'`, `'CarriageReturn'`, `'CarriageReturnAndLineFeed'`, `'None'`. Do NOT use `'Paste'` — it's not in the enum.
- Leader key ergonomics:
  - Leader: `CTRL+A`, 2s timeout.
  - Tabs, panes, splits, pane focus with Ctrl arrows, pane resize with Alt arrows, copy mode, command palette.
- Copy mode key table (vim-flavoured):
  - `h/j/k/l` for movement, `w/b` for word, `v`/`V` for selection modes, `y` = copy+close (`Multiple { CopyTo = '...', CopyMode 'Close' }`).
  - Do NOT bind `/`, `n`, `N` in the `copy_mode` table — these keys activate the built-in `search_mode` key table automatically. Overriding them breaks search activation.
  - Customize search behavior via the `search_mode` key table (default bindings use `PriorMatch`/`NextMatch` with `Ctrl+n`/`Ctrl+p`).
  - See `references/copymode-version-mismatch.md` for the full debugging chain of nightly-vs-release variant mismatches.
- Windows 11 appearance:
  - `win32_system_backdrop = 'Mica'` gives the Win11 glass effect (requires opacity < 1.0)
  - `window_frame` colors the title bar area (used by fancy tab bar)
  - `use_fancy_tab_bar = true` enables modern rounded tabs
- Background layers:
  - The `background` option supports multi-layer compositing with gradients, images, colors, and parallax
  - Prefer over deprecated `window_background_image` / `window_background_gradient`
- UX defaults:
  - Steady block cursor, no blink, reverse-video cursor for visibility.
  - Scrollback 50k+, scroll-on-input, hide mouse on typing.
  - Swallow mouse clicks on pane/window focus.
  - Detect password input where available.
- Environment:
  - `set_environment_variables` to carry EDITOR, VISUAL, TERM to all spawns.
  - `exit_behavior = 'Close'` prevents ghost panes on clean exit.
- Event handlers:
  - `update-right-status`: workspace name + clock in status bar
  - `format-tab-title`: show process name, truncated to max_width
  - `format-window-title`: show active workspace in title bar
  - `gui-startup`: spawn initial window with CWD override
- Performance:
  - `front_end = 'WebGpu'`, cap animation FPS, set power preference.
  - If WebGpu causes blur/smearing, fall back to `'OpenGL'` or `'Software'`.

### Phase 3: Verify
1. Run config check: `wezterm -e 'exit' 2>&1 | tail -n 40`.
2. Distinguish config errors (contain `Configuration Error`) from PTY launch noise (`CreateProcessW ... failed` is normal for the probe).
3. **Check for runtime event handler errors** by grepping for `WARN.*runtime error`: `wezterm -e "echo done; exit" 2>&1 | grep -E "WARN.*runtime error"`.
4. Read back the config with `read_file` to confirm exact contents.
5. If runtime available, observe window state with `wezterm cli list`.
5. For `wezterm cli` detail: `wezterm cli list 2>&1 | tail -n 20`.

### Phase 4: Cleanup
- No backup files; rely on version control or direct overwrite.
- Keep comments concise, one-line per setting.
- After difficult/iterative sessions, offer to save findings as a reference file under this skill.

## Pitfalls

- **Event handler API version mismatch**: In WezTerm 20240203, `format-tab-title`'s first arg `tab` is a `PaneInformation` (not `TabInformation`). Calling `tab:active_pane()` on it throws "attempt to call a PaneInformation value". `format-window-title`'s `tab:window()` method does not exist in this version. Fix: wrap all event handler field/method accesses in `pcall` for graceful degradation.
- **Direct field access on API objects**: `PaneInformation.tab_id` and similar direct-field reads can throw Lua errors in strict mode even when the object is non-nil. Wrap in `pcall(function() return obj.field end)`.
- **`foreground_process_name` type varies**: On `Pane` (from `tab:active_pane()`), it's a callable METHOD — `pane:foreground_process_name()`. On `PaneInformation` (the raw `tab` in `format-tab-title`), it's a read-only FIELD — `tab.foreground_process_name`. Use `pcall` to support both.
- Wrong module import: `local act = require 'wezterm.action'` is brittle on Windows; use `local act = wezterm.action`.
- Enum/boolean mismatch: fields like `allow_square_glyphs_to_overflow_width` now take strings (`'Always'`) not booleans.
- Invalid field names: `show_close_tab_button_in_tabs` may not exist in older releases.
- Font assumptions: `wezterm.font('JetBrainsMono Nerd Font Mono')` fails silently if missing; prefer ordered fallback.
- Transparency defaults: `window_background_opacity < 1` on some Windows GPU stacks is unreliable; use `1.0` unless verified.
- Transparency fallback: if `front_end = 'WebGpu'` causes blur/smearing, switch to `'OpenGL'` or `'Software'` for stability, especially on older or remote GPUs.
- Alternating buffer scroll speed: if mouse wheel feels slow inside apps like `less`, tune `alternate_buffer_wheel_scroll_speed`.
- Launch menu paths: Git Bash path can differ by version; verify before hard-coding.
- **`read_file` backslash display**: read_file double-escapes backslashes (shown as `\\\\` but actual file has `\\`). Verify Lua escaping with `cat -A` or hexdump if unsure.
- **Lua unknown escapes**: `\G`, `\P`, `\F` etc are not standard Lua escapes. Use `\\` pairs for guaranteed single backslash.
- **front_end default history**: default briefly became WebGpu around 20240128, then reverted to OpenGL. Check version before commenting.
- **Config file evaluated multiple times**: Avoid side effects in top-level config flow (e.g. spawning background processes) since config runs on every reload.
- **Config priority**: `~/.config/wezterm/wezterm.lua` takes priority over `~/.wezterm.lua`. If both exist, the latter is ignored unless passed via `--config-file`.
- **Nightly docs ≠ release version (CopyMode variants)** — The online docs at wezterm.org may document features or `CopyModeAssignment` variants (like `ScrollToBottom`, `Yank`, `show_close_tab_button_in_tabs`) that only exist in nightlies. Always verify with `wezterm show-keys --lua --key-table copy_mode` to see what the installed version actually supports before writing key table entries. The `y` binding in the installed version is `Multiple { CopyTo = 'ClipboardAndPrimarySelection', CopyMode 'Close' }` — no `ScrollToBottom`.

## References

- `references/wezterm-config-gotchas.md` — concrete error messages and fixes from Windows sessions.
- `references/wezterm-font-probe.md` — font discovery and fallback patterns for Windows.
- `references/modular-architecture.md` — the Lua module pattern for `~/.config/wezterm/` with apply_to_config, full 5-module worked example.
- `references/copymode-version-mismatch.md` — CopyModeAssignment variant differences between nightly docs and release v20240203, with the `y` / `MoveToScrollbackTop` / `MoveToScrollbackBottom` debugging chain.

## Templates

- `templates/copy-mode-keytable.lua` — full vim-flavoured copy-mode key table to paste into keys module.

## Verification Checklist

- [ ] Existing config inspected before changes
- [ ] Research completed with source-of-truth preference (official docs)
- [ ] Changes are minimal and reversible
- [ ] Config reload probe executed after edits
- [ ] Known config errors debugged or reported honestly
- [ ] User got changed settings + verification evidence in one summary
