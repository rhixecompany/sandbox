# WezTerm Config Options Index

Source: <https://wezterm.org/config/lua/config/index.html>

Full config struct fields:

| Setting                                       | Description                                          |
| --------------------------------------------- | ---------------------------------------------------- |
| `adjust_window_size_when_changing_font_size`  | Resize window when font changes                      |
| `allow_square_glyphs_to_overflow_width`       | Allow square glyphs to overflow cell width           |
| `allow_win32_input_mode`                      | Enable Win32 input mode                              |
| `alternate_buffer_wheel_scroll_speed`         | Scroll speed in alt screen                           |
| `animation_fps`                               | Animation framerate                                  |
| `anti_alias_custom_block_glyphs`              | Anti-alias block glyphs                              |
| `audible_bell`                                | Bell sound                                           |
| `automatically_reload_config`                 | Auto-reload on file change                           |
| `background`                                  | Multi-layer background (gradients, images, parallax) |
| `bold_brightens_ansi_colors`                  | Bold → brighter ANSI colors                          |
| `bypass_mouse_reporting_modifiers`            | Modifiers to bypass mouse reporting                  |
| `canonicalize_pasted_newlines`                | Normalize CRLF/LF on paste                           |
| `cell_width`                                  | Override cell width                                  |
| `cell_widths`                                 | Per-character cell widths                            |
| `char_select_bg_color`                        | Character selector bg                                |
| `char_select_fg_color`                        | Character selector fg                                |
| `char_select_font`                            | Character selector font                              |
| `char_select_font_size`                       | Character selector font size                         |
| `check_for_updates`                           | Check for updates                                    |
| `clean_exit_codes`                            | Exit codes considered clean                          |
| `color_schemes`                               | Define custom color schemes                          |
| `colors`                                      | Full color customization                             |
| `command_palette_bg_color`                    | Command palette bg                                   |
| `command_palette_fg_color`                    | Command palette fg                                   |
| `command_palette_font`                        | Command palette font                                 |
| `command_palette_font_size`                   | Command palette font size                            |
| `command_palette_rows`                        | Command palette rows                                 |
| `cursor_blink_ease_in`                        | Cursor blink ease-in                                 |
| `cursor_blink_ease_out`                       | Cursor blink ease-out                                |
| `cursor_blink_rate`                           | Cursor blink rate                                    |
| `cursor_thickness`                            | Cursor thickness                                     |
| `custom_block_glyphs`                         | Use custom block glyphs                              |
| `daemon_options`                              | Multiplexer daemon options                           |
| `debug_key_events`                            | Log key events                                       |
| `default_cursor_style`                        | Default cursor style                                 |
| `default_cwd`                                 | Default working directory                            |
| `default_domain`                              | Default multiplexer domain                           |
| `default_gui_startup_args`                    | Args for GUI startup                                 |
| `default_mux_server_domain`                   | Default mux server domain                            |
| `default_prog`                                | Default program                                      |
| `default_ssh_auth_sock`                       | Default SSH auth sock                                |
| `default_workspace`                           | Default workspace name                               |
| `detect_password_input`                       | Detect password input                                |
| `disable_default_mouse_bindings`              | Disable default mouse bindings                       |
| `disable_default_quick_select_patterns`       | Disable default quick select patterns                |
| `display_pixel_geometry`                      | Pixel geometry                                       |
| `dpi`                                         | DPI override                                         |
| `enable_csi_u_key_encoding`                   | Enable CSI u key encoding                            |
| `enable_kitty_keyboard`                       | Enable Kitty keyboard protocol                       |
| `enable_scroll_bar`                           | Show scrollbar                                       |
| `enable_tab_bar`                              | Show tab bar                                         |
| `enable_wayland`                              | Enable Wayland                                       |
| `exit_behavior`                               | Close/Hold on exit                                   |
| `exit_behavior_messaging`                     | Show message on exit                                 |
| `font`                                        | Font configuration                                   |
| `font_antialias`                              | Font antialiasing                                    |
| `font_dirs`                                   | Font directories                                     |
| `font_hinting`                                | Font hinting                                         |
| `font_locator`                                | Font locator backend                                 |
| `font_rules`                                  | Per-settings font rules                              |
| `font_shaper`                                 | Font shaping engine                                  |
| `font_size`                                   | Font size                                            |
| `force_reverse_video_cursor`                  | Force reverse video cursor                           |
| `foreground_text_hsb`                         | HSB transform on text                                |
| `freetype_*`                                  | FreeType rendering options                           |
| `front_end`                                   | Rendering frontend (OpenGL/WebGpu/Software)          |
| `harfbuzz_features`                           | OpenType features (liga, calt, etc.)                 |
| `hide_mouse_cursor_when_typing`               | Auto-hide mouse                                      |
| `hide_tab_bar_if_only_one_tab`                | Hide tab bar with single tab                         |
| `hyperlink_rules`                             | URL detection rules                                  |
| `ime_preedit_rendering`                       | IME preedit rendering                                |
| `initial_cols`                                | Initial window width (cols)                          |
| `initial_rows`                                | Initial window height (rows)                         |
| `integrated_title_*`                          | Integrated title buttons                             |
| `kde_window_background_blur`                  | KDE blur                                             |
| `key_map_preference`                          | Key map preference                                   |
| `key_tables`                                  | Custom key tables                                    |
| `launch_menu`                                 | Launch menu entries                                  |
| `launcher_alphabet`                           | Launcher alphabet                                    |
| `line_height`                                 | Line height                                          |
| `log_unknown_escape_sequences`                | Log unknown escape sequences                         |
| `macos_*`                                     | macOS-specific settings                              |
| `max_fps`                                     | Max FPS                                              |
| `min_scroll_bar_height`                       | Min scrollbar height                                 |
| `mouse_wheel_scrolls_tabs`                    | Scroll wheel switches tabs                           |
| `mux_*`                                       | Multiplexer settings                                 |
| `notification_handling`                       | Notification behavior                                |
| `pane_focus_follows_mouse`                    | Focus follows mouse                                  |
| `pane_select_font`                            | Pane selector font                                   |
| `prefer_egl`                                  | Prefer EGL over GLX                                  |
| `prefer_to_spawn_tabs`                        | Prefer tabs over windows                             |
| `quick_select_*`                              | Quick select mode settings                           |
| `quit_when_all_windows_are_closed`            | Quit when no windows                                 |
| `quote_dropped_files`                         | Quote dropped file paths                             |
| `reverse_video_cursor_min_contrast`           | Min contrast for reverse cursor                      |
| `scroll_to_bottom_on_input`                   | Scroll to bottom on input                            |
| `scrollback_lines`                            | Scrollback buffer lines                              |
| `selection_word_boundary`                     | Word selection boundaries                            |
| `serial_ports`                                | Serial port connections                              |
| `set_environment_variables`                   | Environment variables                                |
| `show_*`                                      | Various visibility toggles                           |
| `skip_close_confirmation_for_processes_named` | Skip close confirmation                              |
| `ssh_*`                                       | SSH settings                                         |
| `status_update_interval`                      | Status update poll interval                          |
| `strikethrough_position`                      | Strikethrough position                               |
| `swallow_mouse_click_*`                       | Swallow clicks on focus                              |
| `swap_backspace_and_delete`                   | Swap BS and Del                                      |
| `switch_to_last_active_tab_when_closing_tab`  | Last active tab on close                             |
| `tab_*`                                       | Tab bar settings                                     |
| `term`                                        | TERM environment variable value                      |
| `text_*`                                      | Text blink settings                                  |
| `tiling_desktop_environments`                 | Tiling DE detection                                  |
| `tls_*`                                       | TLS domain settings                                  |
| `treat_east_asian_ambiguous_width_as_wide`    | East Asian width                                     |
| `treat_left_ctrlalt_as_altgr`                 | Handle Ctrl+Alt as AltGr                             |
| `ui_key_cap_rendering`                        | Key cap rendering                                    |
| `ulimit_*`                                    | ulimit settings                                      |
| `underline_*`                                 | Underline position/thickness                         |
| `unicode_version`                             | Unicode version                                      |
| `unix_domains`                                | Unix domain sockets                                  |
| `unzoom_on_switch_pane`                       | Unzoom on pane switch                                |
| `use_cap_height_to_scale_fallback_fonts`      | Scale fallback fonts                                 |
| `use_fancy_tab_bar`                           | Modern tab bar style                                 |
| `use_ime`                                     | Use IME                                              |
| `use_resize_increments`                       | Resize in cell increments                            |
| `visual_bell`                                 | Visual bell                                          |
| `warn_about_missing_glyphs`                   | Warn about missing glyphs                            |
| `wayland_window_background_blur`              | Wayland blur                                         |
| `webgpu_*`                                    | WebGPU adapter/power settings                        |
| `win32_*`                                     | Windows-specific settings                            |
| `window_*`                                    | Window settings                                      |
| `wsl_domains`                                 | WSL domain config                                    |
| `xim_im_name`                                 | XIM input method name                                |
