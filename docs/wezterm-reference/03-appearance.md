# WezTerm Appearance Settings

## window_decorations

Source: <https://wezterm.org/config/lua/config/window_decorations.html>

Flags:

- `"NONE"` — borderless (problems with resize/minimize)
- `"TITLE"` — title bar only
- `"RESIZE"` — resizable border only (recommended for borderless)
- `"TITLE | RESIZE"` — default
- `"INTEGRATED_BUTTONS|RESIZE"` — buttons in tab bar, no title bar

Window dragging: CTRL+SHIFT + drag (Windows)

## background

Source: <https://wezterm.org/config/lua/config/background.html>

Multi-layer background compositing. Layers can be images, gradients, or colors.

### Layer properties:

- `source` — `{File="path"}`, `{Gradient={...}}`, or `{Color="name"}`
- `attachment` — `"Fixed"`, `"Scroll"`, or `{Parallax=0.1}`
- `opacity` — 0.0 to 1.0
- `hsb` — hue/saturation/brightness transform
- `width`/`height` — `"Cover"`, `"Contain"`, pixels, `"N%"`, `"Ncell"`
- `repeat_x`/`repeat_y` — `"Repeat"`, `"Mirror"`, `"NoRepeat"`
- `vertical_align`/`horizontal_align` — positioning
- `vertical_offset`/`horizontal_offset` — offset values

### Gradient example:

```lua
config.background = {
  {
    source = { Gradient = {
      colors = { '#1a1a2e', '#16213e', '#0f3460' },
      orientation = 'Vertical',
    }},
    width = '100%',
    height = '100%',
    opacity = 0.85,
  },
}
```

### Parallax example (multi-layer with dimming):

```lua
local dimmer = { brightness = 0.1 }
config.background = {
  {
    source = { File = '/path/to/background.png' },
    repeat_x = 'Mirror',
    hsb = dimmer,
    attachment = { Parallax = 0.1 },
  },
  -- overlay layers with increasing parallax factors...
}
```

## win32_system_backdrop (Windows 11)

Source: <https://wezterm.org/config/lua/config/win32_system_backdrop.html>

- `"Auto"` — system chooses (default)
- `"Disable"` — disable
- `"Acrylic"` — blur-behind effect (Win10+, higher GPU cost)
- `"Mica"` — Mica effect (Win11 22621+)
- `"Tabbed"` — Tabbed effect (Win11 22621+)

Requires `window_background_opacity < 1.0`. For Mica/Tabbed, `opacity = 0` works best.

## window_frame

Source: <https://wezterm.org/config/lua/config/window_frame.html>

Customize titlebar colors and add window border:

```lua
config.window_frame = {
  inactive_titlebar_bg = '#353535',
  active_titlebar_bg = '#2b2042',
  inactive_titlebar_fg = '#cccccc',
  active_titlebar_fg = '#ffffff',
  inactive_titlebar_border_bottom = '#2b2042',
  active_titlebar_border_bottom = '#2b2042',
  button_fg = '#cccccc',
  button_bg = '#2b2042',
  button_hover_fg = '#ffffff',
  button_hover_bg = '#3b3052',
  -- Optional border:
  border_left_width = '0.5cell',
  border_right_width = '0.5cell',
  border_bottom_height = '0.25cell',
  border_top_height = '0.25cell',
  border_left_color = 'purple',
  border_right_color = 'purple',
  border_bottom_color = 'purple',
  border_top_color = 'purple',
  -- Tab bar font:
  font = wezterm.font 'Roboto',
  font_size = 12,
}
```

## exit_behavior

Source: <https://wezterm.org/config/lua/config/exit_behavior.html>

- `"Close"` — close pane immediately (new default since 20220624)
- `"Hold"` — keep pane open
- `"CloseOnCleanExit"` — close only on clean exit
