# VS Code Stable Uninstall + Code-Insiders Full Configuration — Specification

## Goal
Uninstall stable VS Code completely, configure Code-Insiders with every installed extension mapped to its supported file types, and verify all extensions work correctly.

## Requirements

### R1: Complete Uninstall of Stable VS Code
- Standard uninstaller executed if available
- All Program Files remnants deleted
- Registry entries cleaned
- All config/data/storage folders removed
- Stable VS Code must not be runnable after completion

### R2: Extension-to-Filetype Coverage
- Every one of the 70+ installed extensions must have its supported file types documented
- Each language/filetype must have a designated formatter/language server extension
- No file type is left without a configured handler

### R3: SandBox .vscode/ Configuration
- settings.json must contain language-specific formatter mappings for ALL supported file types
- tasks.json must reference valid commands for all task types
- launch.json must have debug configs for all supported runtimes
- extensions.json must list all installed extensions as recommendations
- mcp.json must have all MCP servers correctly configured

### R4: Code-Insiders Roaming User/ Configuration
- settings.json must have language-specific formatter settings
- Must mirror SandBox .vscode/ settings for consistency
- Must not conflict with SandBox workspace settings

### R5: Full Verification
- No extension activation errors
- All known file types (js, ts, py, json, yaml, md, toml, shell, css, go, java, csharp, rust, xml, powershell, sql, dockerfile, cmake, makefile) have configured formatters
- code-insiders --health-check passes
- Debug configurations work

## Acceptance Criteria

### AC1: Stable VS Code Removal
```
NOT EXISTS: C:\Users\Alexa\AppData\Local\Programs\Microsoft VS Code\
NOT EXISTS: Registry key for VS Code stable
NOT EXISTS: C:\Users\Alexa\AppData\Roaming\Code\ (stable roaming, NOT Code-Insiders)
```

### AC2: All JSON configs valid
```bash
for f in settings.json tasks.json launch.json extensions.json mcp.json:
  python -m json.tool $f > /dev/null
```

### AC3: Language-specific formatters configured
Each supported language must have `editor.defaultFormatter` and `editor.tabSize` set in both settings files.

### AC4: Extension activation verified
`code-insiders --list-extensions` returns all 70+ extensions with no errors.

### AC5: Known file types have formatters
For each file type in the supported list, `editor.defaultFormatter` is set in settings.json.

## Constraints
- Do NOT use backup files (.bak, .old, .backup) — use git for rollback
- Write JSON with tab indentation (matching existing format)
- Preserve existing settings that are correct
- Only modify what needs changing
- All destructive operations must be explicitly approved (user confirmed)
- No inline scripts — use scripts/ dir for any helper scripts

## File Paths
- Stable VS Code: `C:\Users\Alexa\AppData\Local\Programs\Microsoft VS Code\`
- Code-Insiders: `C:\Users\Alexa\AppData\Local\Programs\Microsoft VS Code Insiders\`
- SandBox .vscode/: `C:\Users\Alexa\Desktop\SandBox\.vscode\`
- Code-Insiders User: `C:\Users\Alexa\AppData\Roaming\Code - Insiders\User\`
- Extensions: `C:\Users\Alexa\.vscode\extensions\`
- Code-Insiders extensions: Same directory
- Code-Insiders Roaming: `C:\Users\Alexa\AppData\Roaming\Code - Insiders\`
