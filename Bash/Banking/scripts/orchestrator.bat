@echo off
REM orchestrator.bat
REM Thin CMD wrapper that forwards to TypeScript implementation
REM Usage: orchestrator.bat [arguments]

setlocal enabledelayedexpansion
set "SCRIPT_DIR=%~dp0"
set "TS_PATH=%SCRIPT_DIR%orchestrator.ts"

bunx tsx "%TS_PATH%" %*
exit /b %ERRORLEVEL%
