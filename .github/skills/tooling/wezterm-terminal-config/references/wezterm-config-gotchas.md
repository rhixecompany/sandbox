# WezTerm Config Gotchas — Windows/MSYS Session Notes

## Error: module 'wezterm.action' not found
- Cause: Windows safe-mode module loading does not expose `wezterm.action` as a Lua module.
- Fix: use `local act = wezterm.action` after `local wezterm = require 'wezterm'`.

## Error: Bool-to-enum conversion failure
- Example: `allow_square_glyphs_to_overflow_width = true`
- Cause: field expects a specific enum, not a boolean.
- Fix: use `'Always'` or the documented enum value.

## Error: invalid Config field
- Example: `show_close_tab_button_in_tabs = true`
- Cause: current version does not define this field name.
- Fix: remove the field or use a supported sibling from the error suggestion.

## Font fallback logs
- Cause: preferred font family is not installed.
- Fix: list available font families in order with `wezterm.font_with_fallback{...}`; put commonly available Windows fonts first for fast visual change.

## Runtime PTY error after config loads cleanly
- Example: `CreateProcessW 'exit' ... failed: The system cannot find the file specified.`
- Cause: CLI invocation pattern `wezterm -e 'exit'` can emit PTY launch noise in MSYS even if config is valid.
- Fix: separate config-load errors from runtime PTY errors; use `wezterm cli list` to observe live state.

## Runtime event handler errors (no config error shown)
- **format-tab-title**: In WezTerm 20240203, the first arg `tab` is a `PaneInformation` (not `TabInformation`). Calling `tab:active_pane()` throws `attempt to call a PaneInformation value (method 'active_pane')`.
- **format-window-title**: `tab:window()` method does not exist in this version. Attempting it throws `attempt to get an unknown field 'window'`.
- **PaneInformation field access**: Direct reads like `pane.tab_id` throw `attempt to get an unknown field 'tab_id'` even when pane is non-nil — WezTerm's strict Lua binding blocks unknown field reads.
- **`foreground_process_name` type varies**: On `Pane` (from `tab:active_pane()`) it's a method `pane:foreground_process_name()`. On `PaneInformation` (raw tab in `format-tab-title`) it's a field `tab.foreground_process_name`.
- **Detection**: Run `wezterm -e "echo done; exit"` and grep for `WARN`. Event handler errors appear as `WARN   wezterm_gui::tabbar > format-tab-title: runtime error: ...`.
- **Fix**: Wrap all event handler API accesses in `pcall` so a version mismatch degrades gracefully instead of spewing warnings.

## Path detection gotcha
- `wezterm.target_triple` contains OS info string; safely detect Windows before OS-specific settings even though this config assumes Windows.

## Error: CopyModeAssignment variant mismatch (nightly docs ≠ release)
- Example: `'Yank'`, `'MoveToTop'`, `'MoveToBottom'`, `'ScrollToBottom'` not valid.
- Cause: online docs from wezterm.org may document features that only exist in nightlies.
- Fix: run `wezterm show-keys --lua --key-table copy_mode` and `wezterm show-keys --lua --key-table search_mode` to get the installed version's actual valid enum values. Compare against THOSE, not against online docs. See `references/copymode-version-mismatch.md` for full chain.

## `canonicalize_pasted_newlines` enum values
- Valid: `'LineFeed'`, `'CarriageReturn'`, `'CarriageReturnAndLineFeed'`, `'None'`
- Invalid: `'Paste'` (will crash config load)
- Use `'LineFeed'` for Git Bash/MSYS clean paste behavior.
