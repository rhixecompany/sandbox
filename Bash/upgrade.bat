# DRY_RUN_SUPPORT=true
@echo off
REM Package Manager Upgrade — thin wrapper (forwards to TypeScript implementation)
cd /d "%~dp0"
bunx tsx src/upgrade.ts %*
exit /b %ERRORLEVEL%
