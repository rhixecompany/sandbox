# cleanup.ps1 - ComicWise Project Cleanup Wrapper (PowerShell)
# Thin orchestrator wrapper that delegates to pnpm cleanup:project
#
# Usage:
#   .\cleanup.ps1                     # Prompt for confirmation before cleanup
#   .\cleanup.ps1 -Force              # Skip confirmation
#   .\cleanup.ps1 -DryRun             # Show what would be cleaned without executing
#   .\cleanup.ps1 -Help               # Show help
#
# Exit codes:
#   0  Success
#   1  User cancelled or cleanup failed

param(
  [switch]$Force,
  [switch]$DryRun,
  [switch]$Help
)

if ($Help) {
  Write-Host "ComicWise Project Cleanup Tool"
  Write-Host ""
  Write-Host "Usage:"
  Write-Host "  .\cleanup.ps1                     # Prompt for confirmation before cleanup"
  Write-Host "  .\cleanup.ps1 -Force              # Skip confirmation"
  Write-Host "  .\cleanup.ps1 -DryRun             # Show what would be cleaned without executing"
  Write-Host "  .\cleanup.ps1 -Help               # Show this help message"
  Write-Host ""
  Write-Host "Removes:"
  Write-Host "  • .next/ (Next.js build cache)"
  Write-Host "  • .turbo/ (Turbo cache)"
  Write-Host "  • coverage/ (Test coverage)"
  Write-Host "  • dist/, build/ (Build artifacts)"
  Write-Host "  • .cache/ (General cache)"
  Write-Host "  • *.log, *.tmp, .DS_Store"
  Write-Host ""
  exit 0
}

# Build args array
$args_list = @()
if ($Force) { $args_list += "--force" }
if ($DryRun) { $args_list += "--dry-run" }

# Delegate to pnpm cleanup:project
& pnpm cleanup:project @args_list @args
exit $LASTEXITCODE
