# DRY_RUN_SUPPORT=true
@echo off
REM Unified Script Orchestrator - Batch Wrapper
REM Automatically runs the PowerShell orchestrator with arguments

setlocal enabledelayedexpansion

echo.
echo ╔══════════════════════════════════════════════════════════════════════════════╗
echo ║ 🎼 UNIFIED SCRIPT ORCHESTRATOR - Batch Wrapper (PowerShell Backend)          ║
echo ╚══════════════════════════════════════════════════════════════════════════════╝
echo.

REM Default values
set MODE=auto
set DRY_RUN=
set CATEGORY=
set LOG_PATH=./logs

REM Parse arguments
:parse_args
if "%1"=="" goto run_orchestrator
if "%1"=="-m" set MODE=%2& shift& shift& goto parse_args
if "%1"=="--mode" set MODE=%2& shift& shift& goto parse_args
if "%1"=="-c" set CATEGORY=%2& shift& shift& goto parse_args
if "%1"=="--category" set CATEGORY=%2& shift& shift& goto parse_args
if "%1"=="-d" set DRY_RUN=-DryRun& shift& goto parse_args
if "%1"=="--dry-run" set DRY_RUN=-DryRun& shift& goto parse_args
if "%1"=="-l" set LOG_PATH=%2& shift& shift& goto parse_args
if "%1"=="--log-path" set LOG_PATH=%2& shift& shift& goto parse_args
if "%1"=="--help" goto show_help
shift
goto parse_args

:show_help
echo Usage: %0 [OPTIONS]
echo.
echo OPTIONS:
echo   -m, --mode MODE             auto^|interactive^|discover^|validate (default: auto)
echo   -c, --category CATEGORY     Filter to category (Banking, Comicwise, etc.)
echo   -d, --dry-run              Preview operations without execution
echo   -l, --log-path PATH         Custom log directory
echo   --help                     Show this help
echo.
exit /b 0

:run_orchestrator
REM Build PowerShell command
set PS_CMD=^& .\orchestrator-unified.ps1 -Mode %MODE%
if not "!CATEGORY!"=="" set PS_CMD=!PS_CMD! -Category '!CATEGORY!'
if not "!DRY_RUN!"=="" set PS_CMD=!PS_CMD! !DRY_RUN!
if not "!LOG_PATH!"=="" set PS_CMD=!PS_CMD! -LogPath '!LOG_PATH!'

REM Execute PowerShell orchestrator
pwsh -NoProfile -ExecutionPolicy Bypass -Command "!PS_CMD!"
set EXIT_CODE=%ERRORLEVEL%

echo.
if %EXIT_CODE% equ 0 (
    echo ✓ Orchestrator completed successfully
) else (
    echo ✗ Orchestrator failed with exit code %EXIT_CODE%
)

exit /b %EXIT_CODE%
