# WezTerm Terminal Setup for VSCode

**Context:** Windows 11, WezTerm 20240203, VSCode

## Key Insight

WezTerm is a **terminal emulator** (like Windows Terminal, ConEmu), not a **shell** (like bash, PowerShell). VSCode's integrated terminal pane expects a shell inside it — you __cannot__ set WezTerm as `terminal.integrated.defaultProfile.windows`.

## Correct Configuration

### External Terminal (Ctrl+Shift+C opens WezTerm)

```json
"terminal.external.windowsExec": "C:\\Program Files\\WezTerm\\wezterm.exe start"
```

### Integrated Terminal Profile (manual selection in dropdown)

```json
"terminal.integrated.profiles.windows": {
  "WezTerm": {
    "icon": "terminal",
    "path": "C:\\Program Files\\WezTerm\\wezterm.exe",
    "args": ["start", "--cwd", "${workspaceFolder}"]
  }
}
```

### Integrated Terminal Default (shell INSIDE VSCode pane)

Keep as a shell (bash/powershell/wsl). Windows convention:

```json
"terminal.integrated.defaultProfile.windows": "Git Bash"
```

## Consistency Rule

User settings (`Code\User\settings.json`) and workspace settings (`.vscode\settings.json`) should have the same `defaultProfile.windows` value. If they differ, the workspace value wins when that workspace is open, but the user value takes effect in new windows — causing confusion.

## Path Discovery

```powershell
# WezTerm install path
where wezterm  # → C:\Program Files\WezTerm\wezterm.exe
```
