# WezTerm Key Tables & Events

## key_tables

Source: <https://wezterm.org/config/lua/config/key_tables.html>

Context-sensitive key mappings. When you activate `copy_mode` or `search_mode`, the active key table changes.

### Copy Mode (vim-style):

```lua
config.key_tables = {
  copy_mode = {
    { key = 'h', action = act.CopyMode 'MoveLeft' },
    { key = 'j', action = act.CopyMode 'MoveDown' },
    { key = 'k', action = act.CopyMode 'MoveUp' },
    { key = 'l', action = act.CopyMode 'MoveRight' },
    { key = 'w', action = act.CopyMode 'MoveForwardWord' },
    { key = 'b', action = act.CopyMode 'MoveBackwardWord' },
    { key = '0', action = act.CopyMode 'MoveToStartOfLine' },
    { key = '$', action = act.CopyMode 'MoveToEndOfLineContent' },
    { key = 'v', action = act.CopyMode { SetSelectionMode = 'Cell' } },
    { key = 'V', action = act.CopyMode { SetSelectionMode = 'Line' } },
    { key = 'y', action = act.CopyMode 'Yank' },
    { key = '/', action = act.CopyMode 'PriorMatch' },
    { key = 'n', action = act.CopyMode 'NextMatch' },
    { key = 'N', action = act.CopyMode 'PriorMatch' },
    { key = 'g', action = act.CopyMode 'MoveToTop' },
    { key = 'G', action = act.CopyMode 'MoveToBottom' },
    { key = 'Escape', action = act.CopyMode 'Close' },
    { key = 'q', action = act.CopyMode 'Close' },
  },
  search_mode = {
    { key = 'Escape', action = act.CopyMode 'Close' },
    { key = 'Enter', action = act.CopyMode 'PriorMatch' },
  },
}
```

## GUI Events

See: <https://wezterm.org/config/lua/gui-events/>

### gui-startup

Called on GUI startup to spawn initial windows.

### format-tab-title

Customize tab title rendering:

```lua
wezterm.on('format-tab-title', function(tab, tabs, panes, config, hover, max_width)
  local pane = tab:active_pane()
  local title = pane:foreground_process_name()
  local process = title:match '[/\\]([^/\\]+)$' or title
  if #process > max_width then
    process = process:sub(1, max_width - 1) .. '…'
  end
  return process
end)
```

### format-window-title

Customize window title bar text.

### update-right-status

Right-aligned status text:

```lua
wezterm.on('update-right-status', function(window, pane)
  local workspace = window:active_workspace()
  local time = wezterm.strftime '%H:%M:%S'
  window:set_right_status(wezterm.format {
    { Text = '  ' .. workspace .. '  ' },
    { Foreground = { Color = '#666699' } },
    { Text = '|' },
    { Foreground = { Color = '#f8f8f2' } },
    { Text = '  ' .. time .. '  ' },
  })
end)
```

### update-status

General status updates. Use for left-side status.

### augement-command-palette

Add custom entries to the command palette.

### window-config-reloaded

Fires when config is reloaded.

### window-focus-changed

Fires when window gains/loses focus.

### user-var-changed

Fires when a user variable changes (shell integration).

### open-uri

Handle URI opening.
