# dev.ps1 - ComicWise Development Server Launcher (PowerShell)
# Thin orchestrator wrapper that delegates to pnpm dev
#
# Usage:
#   .\dev.ps1                    # Start dev server
#   .\dev.ps1 -Help              # Show help
#
# Exit codes:
#   0  Success
#   1  Command failed

param([switch]$Help)

if ($Help) {
  Write-Host "ComicWise Development Server Launcher"
  Write-Host ""
  Write-Host "Usage:"
  Write-Host "  .\dev.ps1                    # Start dev server"
  Write-Host "  .\dev.ps1 -Help              # Show this help message"
  Write-Host ""
  Write-Host "For more setup options, use:"
  Write-Host "  .\setup-dev.ps1              # Initialize dev environment"
  Write-Host ""
  exit 0
}

# Delegate to pnpm dev
& pnpm dev @args
exit $LASTEXITCODE
