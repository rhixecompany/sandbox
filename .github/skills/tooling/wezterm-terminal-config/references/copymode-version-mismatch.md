# CopyMode Version Mismatch — Debugging Path

## Context
WezTerm `20240203-110809-5046fc22` (stable release, Feb 2024). 
Copy mode key table derived from nightly docs (wezterm.org) but the installed version
supports a different set of CopyModeAssignment variants.

## Error Chain (in order of appearance)

| Error | Root Cause | Fix |
|---|---|---|
| `'Yank' is not a valid CopyModeAssignment variant` | `CopyMode 'Yank'` doesn't exist. `y` is not a single CopyMode action — it's a `Multiple` composition. | → `Multiple { CopyTo = 'ClipboardAndPrimarySelection', CopyMode 'Close' }` |
| `'MoveToTop'`/`'MoveToBottom'` not valid | Wrong enum names. The variants are `MoveToScrollbackTop` and `MoveToScrollbackBottom`. | → `CopyMode 'MoveToScrollbackTop'` / `'MoveToScrollbackBottom'` |
| `'ScrollToBottom'` not valid inside `Multiple` | Online docs include `ScrollToBottom` in the `y` binding, but the installed release version doesn't support it. | → Omitted from `Multiple`; just `CopyTo` + `Close` |
| `/`, `n`, `N` in copy_mode block built-in search | Overriding these in the copy_mode key table prevents the automatic `search_mode` key table activation. | → Removed; falls through to built-in search behavior |

## Key Technique: Validate Against Installed Version

```bash
# Check version
wezterm --version

# Extract the actual valid key table for the installed version
wezterm show-keys --lua --key-table copy_mode
wezterm show-keys --lua --key-table search_mode
```

This gives you the ground truth for ALL valid `CopyModeAssignment` variants.
Compare your custom table against this — not against the online docs.

## search_mode Defaults (v20240203)

```lua
return {
  key_tables = {
    search_mode = {
      { key = 'Enter', mods = 'NONE', action = act.CopyMode 'PriorMatch' },
      { key = 'Escape', mods = 'NONE', action = act.CopyMode 'Close' },
      { key = 'n', mods = 'CTRL', action = act.CopyMode 'NextMatch' },
      { key = 'p', mods = 'CTRL', action = act.CopyMode 'PriorMatch' },
      { key = 'r', mods = 'CTRL', action = act.CopyMode 'CycleMatchType' },
      { key = 'u', mods = 'CTRL', action = act.CopyMode 'ClearPattern' },
      { key = 'PageUp', mods = 'NONE', action = act.CopyMode 'PriorMatchPage' },
      { key = 'PageDown', mods = 'NONE', action = act.CopyMode 'NextMatchPage' },
      { key = 'UpArrow', mods = 'NONE', action = act.CopyMode 'PriorMatch' },
      { key = 'DownArrow', mods = 'NONE', action = act.CopyMode 'NextMatch' },
    },
  }
}
```

Valid search-mode-specific variants: `PriorMatch`, `NextMatch`, `PriorMatchPage`, `NextMatchPage`, `CycleMatchType`, `ClearPattern`.

Note: `PriorMatch` and `NextMatch` are valid in `search_mode` only — they are NOT valid CopyModeAssignment variants in the `copy_mode` key table. If you bind `/`, `n`, or `N` in `copy_mode` to them, they will either error or break the built-in search activation.

## Valid `CopyModeAssignment` String Variants (v20240203)

From `wezterm show-keys --lua --key-table copy_mode`:
```
MoveLeft, MoveRight, MoveUp, MoveDown
MoveForwardWord, MoveBackwardWord, MoveForwardWordEnd
MoveToStartOfLine, MoveToStartOfLineContent, MoveToEndOfLineContent
MoveToStartOfNextLine
MoveToScrollbackTop, MoveToScrollbackBottom
MoveToViewportTop, MoveToViewportMiddle, MoveToViewportBottom
MoveToSelectionOtherEnd, MoveToSelectionOtherEndHoriz
PageUp, PageDown
JumpAgain, JumpReverse, JumpForward{}, JumpBackward{}
Close
```

Table-form variants: `{ SetSelectionMode = 'Cell'|'Line'|'Block' }`, `{ MoveByPage = float }`, `{ JumpForward = { prev_char = bool } }`, `{ JumpBackward = { prev_char = bool } }`

NOT valid in this version: `Yank`, `ScrollToBottom`, `MoveToTop`, `MoveToBottom`, `NextMatch`/`PriorMatch` (these are valid in search_mode only).

## The Default `y` Binding (v20240203)

```lua
{ key = 'y', mods = 'NONE', action = act.Multiple {
    { CopyTo = 'ClipboardAndPrimarySelection' },
    { CopyMode = 'Close' },
} }
```

Note: NO `ScrollToBottom`. The nightly docs include it, but this release doesn't.

## Search Mode Activation

In copy mode, pressing `/` automatically activates the `search_mode` key table.
DO NOT bind `/`, `n`, `N` in the `copy_mode` table — this breaks the automatic search flow.
Instead, customize the `search_mode` key table if needed.
