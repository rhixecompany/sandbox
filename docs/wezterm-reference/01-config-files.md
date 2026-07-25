# WezTerm Configuration — Files & Structure

Source: <https://wezterm.org/config/files.html>

## Quick Start

Create `.wezterm.lua` in your home directory:

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()
config.initial_cols = 120
config.initial_rows = 28
config.font_size = 10
config.color_scheme = 'AdventureTime'
return config
```

## Config File Discovery Order

1. `--config-file` CLI argument
2. `$WEZTERM_CONFIG_FILE` environment variable
3. Windows thumb-drive mode: same dir as `wezterm.exe`
4. `$XDG_CONFIG_HOME/wezterm/wezterm.lua`
5. `$HOME/.config/wezterm/wezterm.lua`
6. `$HOME/.wezterm.lua` (recommended default)

## Configuration Overrides

```bash
wezterm --config enable_scroll_bar=true
wezterm --config 'exit_behavior="Hold"'
```

Per-window overrides via `window:set_config_overrides()`.

## Making Your Own Lua Modules

`package.path` search order:

1. `wezterm_modules/` (next to `wezterm.exe`)
2. `~/.config/wezterm/`
3. `~/.wezterm/`

### Module pattern:

```lua
-- helpers.lua — place in ~/.config/wezterm/helpers.lua
local wezterm = require 'wezterm'
local module = {}

local function private_helper()
  wezterm.log_error 'hello!'
end

function module.apply_to_config(config)
  private_helper()
  config.color_scheme = 'Batman'
end

return module
```

### Usage in wezterm.lua:

```lua
local helpers = require 'helpers'
local config = {}
helpers.apply_to_config(config)
return config
```

## Auto-reload

- Config file is watched; changes auto-apply
- Manual: `CTRL+SHIFT+R`
- **Avoid side effects** in config (config may be evaluated multiple times)
