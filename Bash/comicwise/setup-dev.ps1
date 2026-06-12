# DRY_RUN_SUPPORT=true
# setup-dev.ps1 - ComicWise Development Setup Launcher (PowerShell)
# Thin orchestrator wrapper that delegates to pnpm setup
#
# Usage:
#   .\setup-dev.ps1                    # Interactive setup wizard
#   .\setup-dev.ps1 -Help              # Show help
#   .\setup-dev.ps1 -All               # Full setup (all tasks)
#   .\setup-dev.ps1 -Deps              # Install/verify dependencies
#
# Exit codes:
#   0  Success
#   1  Command failed
#
# See unified-dev-setup.ts for all available options.

param([switch]$Help, [switch]$All, [switch]$Deps, [switch]$Env)

if ($Help) {
  Write-Host "ComicWise Development Setup Launcher"
  Write-Host ""
  Write-Host "Usage:"
  Write-Host "  .\setup-dev.ps1                    # Interactive setup wizard"
  Write-Host "  .\setup-dev.ps1 -All               # Full setup (all tasks)"
  Write-Host "  .\setup-dev.ps1 -Deps              # Install/verify dependencies"
  Write-Host "  .\setup-dev.ps1 -Env               # Initialize .env.local"
  Write-Host "  .\setup-dev.ps1 -Help              # Show this help message"
  Write-Host ""
  Write-Host "For complete options, run:"
  Write-Host "  pnpm setup --help"
  Write-Host ""
  exit 0
}

# Build args array
$args_list = @()
if ($All) { $args_list += "--all" }
if ($Deps) { $args_list += "--deps" }
if ($Env) { $args_list += "--env" }

# Delegate to pnpm setup
& pnpm setup @args_list @args
exit $LASTEXITCODE
