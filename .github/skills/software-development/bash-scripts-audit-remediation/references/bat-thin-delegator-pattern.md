# BAT → PowerShell Thin Delegator Pattern

**Problem**: `.bat` files with inline PowerShell one-liners are hard to maintain (escaping hell), duplicate logic from `.ps1` counterparts, and are typically 500+ lines of fragile code.

**Solution**: Replace the monolithic `.bat` with a thin delegator that passes all arguments to the existing `.ps1` script.

```batch
@echo off
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "PS_SCRIPT=%SCRIPT_DIR%cache-clean.ps1"

REM Fallback if .ps1 is missing
if not exist "%PS_SCRIPT%" (
    echo ERROR: .ps1 not found
    REM Minimal fallback for basic operations
    exit /b 1
)

REM Forward all arguments
powershell -NoProfile -ExecutionPolicy Bypass -File "%PS_SCRIPT%" %*
exit /b %ERRORLEVEL%
```

**Trade-offs**:
+ Single source of truth (logic lives in .ps1)
+ No escaping/multiline PS-in-BAT issues
+ Can still run without PS via the fallback path
- Requires PowerShell on PATH (standard on Windows 10+)
- Slightly slower startup (PS overhead vs cmd.exe)
