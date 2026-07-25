-- WezTerm template
-- Windows/MSYS/Hermes-oriented best-practice starting config

local wezterm = require 'wezterm'
local config = wezterm.config_builder()
local act = wezterm.action

local is_windows = wezterm.target_triple:find 'windows' ~= nil

-- General behavior
config.automatically_reload_config = true
config.check_for_updates = false
config.quit_when_all_windows_are_closed = true
config.initial_cols = 140
config.initial_rows = 36
config.adjust_window_size_when_changing_font_size = true
config.skip_close_confirmation_for_processes_named = {
  'DefaultShell', 'login', 'bash', 'zsh', 'pwsh', 'powershell.exe',
  'cmd.exe', 'wsl.exe', 'wezterm', 'tmux', 'nu',
}

-- Font / rendering
config.font = wezterm.font_with_fallback {
  'Consolas',
  'Fira Code',
  'Cascadia Code',
  'JetBrainsMono Nerd Font Mono',
}
config.font_size = 12
config.line_height = 1.2
config.allow_square_glyphs_to_overflow_width = 'Always'
config.warn_about_missing_glyphs = false
config.anti_alias_custom_block_glyphs = true

-- Appearance / window chrome
config.window_decorations = 'RESIZE'
config.enable_tab_bar = true
config.hide_tab_bar_if_only_one_tab = true
config.show_tab_index_in_tab_bar = true
config.show_new_tab_button_in_tab_bar = true

-- Keyboard / leader workflow
config.leader = { key = 'a', mods = 'CTRL', timeout_milliseconds = 2000 }

config.keys = {
  { key = 'c', mods = 'LEADER', action = act.SpawnTab 'CurrentPaneDomain' },
  { key = 'n', mods = 'LEADER', action = act.ActivateTabRelative(1) },
  { key = 'p', mods = 'LEADER', action = act.ActivateTabRelative(-1) },
  { key = '&', mods = 'LEADER', action = act.CloseCurrentTab { confirm = true } },
  { key = '|', mods = 'LEADER', action = act.SplitHorizontal { domain = 'CurrentPaneDomain' } },
  { key = '-', mods = 'LEADER', action = act.SplitVertical { domain = 'CurrentPaneDomain' } },
  { key = 'x', mods = 'LEADER', action = act.CloseCurrentPane { confirm = true } },
  { key = 'z', mods = 'LEADER', action = act.TogglePaneZoomState },
  { key = 'h', mods = 'CTRL', action = act.ActivatePaneDirection 'Left' },
  { key = 'j', mods = 'CTRL', action = act.ActivatePaneDirection 'Down' },
  { key = 'k', mods = 'CTRL', action = act.ActivatePaneDirection 'Up' },
  { key = 'l', mods = 'CTRL', action = act.ActivatePaneDirection 'Right' },
  { key = 'h', mods = 'ALT', action = act.AdjustPaneSize { 'Left', 5 } },
  { key = 'j', mods = 'ALT', action = act.AdjustPaneSize { 'Down', 5 } },
  { key = 'k', mods = 'ALT', action = act.AdjustPaneSize { 'Up', 5 } },
  { key = 'l', mods = 'ALT', action = act.AdjustPaneSize { 'Right', 5 } },
  { key = '[', mods = 'LEADER', action = act.ActivateCopyMode },
  { key = ']', mods = 'LEADER', action = act.ActivateCommandPalette },
  { key = 'a', mods = 'LEADER|CTRL', action = act.SendKey { key = 'a', mods = 'CTRL' } },
}

-- UX / ergonomics
config.scrollback_lines = 5000
config.scroll_to_bottom_on_input = true
config.hide_mouse_cursor_when_typing = false
config.pane_focus_follows_mouse = false
config.swallow_mouse_click_on_pane_focus = true
config.default_cursor_style = 'SteadyBlock'
config.cursor_blink_rate = 0
config.force_reverse_video_cursor = true

-- Colors / window chrome
config.color_scheme = 'AdventureTime'
config.window_background_opacity = 1.0

-- Mouse / input
config.enable_csi_u_key_encoding = true
config.enable_kitty_keyboard = true
config.treat_left_ctrlalt_as_altgr = true

-- Performance
config.max_fps = 120
config.animation_fps = 60
config.front_end = 'WebGpu'
config.webgpu_power_preference = 'HighPerformance'

-- Local multiplexing
config.unix_domains = { { name = 'unix' } }

-- Launch menu
config.launch_menu = {
  { label = 'PowerShell', args = { 'pwsh.exe' } },
  { label = 'Git Bash', args = { 'C:\\Program Files\\Git\\bin\\bash.exe', '-l' } },
  { label = 'Windows Command Prompt', args = { 'cmd.exe' } },
  { label = 'Command Palette', args = {} },
}

return config
