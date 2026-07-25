-- Full vim-flavoured copy-mode key table for WezTerm
-- Paste into keys.lua inside the config.key_tables = { ... } block

copy_mode = {
  -- Movement: vim arrows
  { key = 'h',       mods = 'NONE', action = act.CopyMode 'MoveLeft' },
  { key = 'j',       mods = 'NONE', action = act.CopyMode 'MoveDown' },
  { key = 'k',       mods = 'NONE', action = act.CopyMode 'MoveUp' },
  { key = 'l',       mods = 'NONE', action = act.CopyMode 'MoveRight' },

  -- Word movement
  { key = 'w',       mods = 'NONE', action = act.CopyMode 'MoveForwardWord' },
  { key = 'b',       mods = 'NONE', action = act.CopyMode 'MoveBackwardWord' },
  { key = 'e',       mods = 'NONE', action = act.CopyMode 'MoveForwardEndOfWord' },
  { key = 'W',       mods = 'NONE', action = act.CopyMode 'MoveForwardWord' },     -- same as w (alt: MoveForwardWordEnd)
  { key = 'B',       mods = 'NONE', action = act.CopyMode 'MoveBackwardWord' },

  -- Line navigation
  { key = '0',       mods = 'NONE', action = act.CopyMode 'MoveToStartOfLine' },
  { key = '$',       mods = 'NONE', action = act.CopyMode 'MoveToEndOfLineContent' },
  { key = '^',       mods = 'NONE', action = act.CopyMode 'MoveToStartOfLineContent' },
  { key = 'Enter',   mods = 'NONE', action = act.CopyMode 'MoveToStartOfNextLine' },

  -- Selection modes
  { key = 'v',       mods = 'NONE', action = act.CopyMode { SetSelectionMode = 'Cell' } },
  { key = 'V',       mods = 'NONE', action = act.CopyMode { SetSelectionMode = 'Line' } },

  -- Yank / copy
  { key = 'y',       mods = 'NONE', action = act.CopyMode 'Yank' },
  { key = 'Y',       mods = 'NONE', action = act.CopyMode 'Yank' },

  -- Search
  { key = '/',       mods = 'NONE', action = act.CopyMode 'PriorMatch' },
  { key = 'n',       mods = 'NONE', action = act.CopyMode 'NextMatch' },
  { key = 'N',       mods = 'NONE', action = act.CopyMode 'PriorMatch' },

  -- Top / bottom of scrollback
  { key = 'g',       mods = 'NONE', action = act.CopyMode 'MoveToTop' },
  { key = 'G',       mods = 'NONE', action = act.CopyMode 'MoveToBottom' },
  { key = 'gg',      mods = 'NONE', action = act.CopyMode 'MoveToTop' },
  { key = 'GH',      mods = 'NONE', action = act.CopyMode 'MoveToTop' },
  { key = 'GL',      mods = 'NONE', action = act.CopyMode 'MoveToBottom' },

  -- Page up/down
  { key = 'PageUp',  mods = 'NONE', action = act.CopyMode 'PageUp' },
  { key = 'PageDown',mods = 'NONE', action = act.CopyMode 'PageDown' },
  { key = 'b',       mods = 'CTRL', action = act.CopyMode 'PageUp' },
  { key = 'f',       mods = 'CTRL', action = act.CopyMode 'PageDown' },
  { key = 'u',       mods = 'CTRL', action = act.CopyMode 'PageUp' },
  { key = 'd',       mods = 'CTRL', action = act.CopyMode 'PageDown' },

  -- Exit copy mode
  { key = 'Escape',  mods = 'NONE', action = act.CopyMode 'Close' },
  { key = 'q',       mods = 'NONE', action = act.CopyMode 'Close' },
  { key = 'c',       mods = 'CTRL', action = act.CopyMode 'Close' },
}

search_mode = {
  { key = 'Escape',  mods = 'NONE', action = act.CopyMode 'Close' },
  { key = 'Enter',   mods = 'NONE', action = act.CopyMode 'PriorMatch' },
}
