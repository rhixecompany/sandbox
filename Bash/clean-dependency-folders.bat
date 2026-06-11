@echo off
REM Dependency Folder Cleanup — thin wrapper (forwards to TypeScript implementation)
cd /d "%~dp0"
bunx tsx src/clean-dep.ts %*
exit /b %ERRORLEVEL%
