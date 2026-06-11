@echo off
REM Cache Cleaner — thin wrapper (forwards to TypeScript implementation)
cd /d "%~dp0"
bunx tsx src/cache-clean.ts %*
exit /b %ERRORLEVEL%
