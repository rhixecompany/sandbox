@echo off
REM opencode-mcp.bat
REM Thin CMD wrapper that forwards to TypeScript implementation
REM Usage: opencode-mcp.bat [arguments]

setlocal enabledelayedexpansion

if "%*"=="" (
    bunx tsx scripts/ts/entrypoints/opencode-mcp-cli.ts --list --catalog-path .opencode/mcp_servers.json
) else (
    bunx tsx scripts/ts/entrypoints/opencode-mcp-cli.ts %*
)
exit /b %ERRORLEVEL%
