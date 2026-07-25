# WezTerm Font Probe — Windows Notes

Use this session reference when choosing or verifying terminal fonts for WezTerm on Windows.

## Goal
Pick a font that exists on the system, minimize fallback noise, and preserve usability for proportional fallback characters.

## Fast Checks
- `fc-list : family` on Linux/macOS.
- On Windows without `fc-list`, inspect `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts` registry via `powershell.exe`.
- Let WezTerm report the active fallback path from `wezterm.font('...')` errors when config is invalid.

## Recommended Probe Order
1. `wezterm.font_with_fallback{ 'Consolas', 'Fira Code', 'Cascadia Code', 'JetBrainsMono Nerd Font Mono' }`
2. If JetBrains/Cascadia/Fira and Nerd Font variants are missing, webfont/install fallback.

## Gotchas
- Nerd-font variants must be installed as exact family names used in config.
- Some Windows builds do not expose fontconfig; use registry recognition or manual install checks.
- If Hermes-style glyph rendering is important, ensure patched/Nerd Font is installed; otherwise accept standard code fonts.
