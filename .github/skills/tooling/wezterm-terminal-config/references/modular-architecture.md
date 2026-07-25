# Modular WezTerm Architecture — Worked Example

## Directory Layout

```
~/.config/wezterm/
├── wezterm.lua        ← Entry point (orchestrator)
├── settings.lua       ← Fonts, geometry, cursor, performance, domains
├── appearance.lua     ← Colors, tab bar, window chrome, background
├── keys.lua           ← Leader, key bindings, copy-mode, mouse
├── events.lua         ← Event handlers (gui-startup, status, tab titles)
└── launch.lua         ← Launch menu, hyperlinks, quick-select patterns
```

## Entry Point (`wezterm.lua`)

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()

local settings    = require 'settings'
local appearance  = require 'appearance'
local keys        = require 'keys'
local events      = require 'events'
local launch      = require 'launch'

settings.apply_to_config(config)
appearance.apply_to_config(config)
keys.apply_to_config(config)
events.apply_to_config(config)
launch.apply_to_config(config)

return config
```

## Module Pattern

Every module exports `apply_to_config(config)`:

```lua
local wezterm = require 'wezterm'
local module = {}

function module.apply_to_config(config)
  config.some_option = value
end

return module
```

## Fallback-Safe Redirect (`~/.wezterm.lua`)

When `~/.config/wezterm/wezterm.lua` takes priority, this file at `~/.wezterm.lua` provides a `--config-file`-compatible entry point using `pcall`:

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()

local ok, mod

ok, mod = pcall(require, 'settings')
if ok then mod.apply_to_config(config) end
-- ... repeat for each module ...

return config
```

## Module Responsibilities

| Module | Key Settings |
|--------|-------------|
| `settings.lua` | `automatically_reload_config`, `exit_behavior`, `initial_cols/rows`, `font` + fallbacks, `font_size`, `line_height`, `freetype_*`, `harfbuzz_features`, `scrollback_lines`, `cursor_*`, `front_end`, `max_fps`, `unix_domains`, `enable_kitty_keyboard` |
| `appearance.lua` | `window_decorations`, `use_fancy_tab_bar`, `win32_system_backdrop`, `window_frame`, `color_scheme`, `colors.tab_bar`, `inactive_pane_hsb`, `window_background_opacity`, `background` |
| `keys.lua` | `leader`, `keys[]`, `key_tables`, `mouse_bindings` |
| `events.lua` | `gui-startup`, `update-right-status`, `format-tab-title`, `format-window-title` |
| `launch.lua` | `launch_menu[]`, `hyperlink_rules[]`, `quick_select_patterns[]` |

## Why Modular

- **Single concern per file** — change keys without touching colors, change fonts without touching events
- **No side effects** — modules only mutate the config object, safe across multiple evaluations
- **Git-friendly** — smaller diffs, meaningful file-level history
- **Extensible** — add `plugins.lua`, `ssh.lua`, `wsl.lua` as separate modules later
- **Graceful failure** — `pcall`-based entry point lets a broken module fail silently
