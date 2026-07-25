# WezTerm Lua Config Verification Notes

## Verified in Session

- Config path: `C:\Users\Alexa\.wezterm.lua`
- Active version: `wezterm 20240203-110809-5046fc22`
- `TERM_PROGRAM=WezTerm` reported inside the shell, confirming the user is running inside WezTerm.

## Reload Probe

Use a short-lived executable probe to test Lua config load without opening a real shell:

```bash
wezterm -e 'exit'
```

Capture the last part of output:

```bash
wezterm -e 'exit' 2>&1 | tail -n 40
```

### Expected outputs

- **Config loads cleanly**: no `Configuration Error` line and no `main chunk` error.
- **Typical non-config notice**: `CreateProcessW ... failed: The system cannot find the file specified.` is expected for the `-e 'exit'` probe because WezTerm's PTY launch semantics around that exact invocation can emit a clearer fallback notice without changing the config. Do not treat this alone as a config load failure.

### Interpret real failures

Real config failures usually include:

- `Configuration Error: runtime error:`
- `module 'wezterm.action' not found`
- `Cannot convert ... to ...`

## Reusable Fixes Observed

- Replace `local act = require 'wezterm.action'` with `local act = wezterm.action`.
- If `allow_square_glyphs_to_overflow_width = true` errors, switch to the documented enum string, e.g. `'Always'`.
- If the user asks for a Windows/MSYS/Hermes-oriented default config, prefer:
  - modest initial size with `adjust_window_size_when_changing_font_size = true`
  - conservative close-confirmation allowlist
  - tmux-like leader workflow instead of custom key chaos
  - `wezterm cli list` for post-edit runtime verification

## Runtime Verification

After reload succeeds:

```bash
wezterm cli list 2>&1 | tail -n 20
```

This confirms windows/tabs/panes are actually visible to WezTerm's multiplexer backend.