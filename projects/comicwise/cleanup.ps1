# cleanup.ps1 - ComicWise Project Cleanup Wrapper (PowerShell)
# Safely removes project artifacts, cache, and build directories
#
# Usage:
#   .\cleanup.ps1                     # Prompt for confirmation before cleanup
#   .\cleanup.ps1 -Force              # Skip confirmation
#   .\cleanup.ps1 -DryRun             # Show what would be cleaned without executing
#   .\cleanup.ps1 -DryRun -Force      # Show what would be cleaned (no confirm)
#   .\cleanup.ps1 -Verbose            # Show detailed cleanup information
#
# Exit codes:
#   0  Success
#   1  User cancelled cleanup
#   2  Cleanup failed

param(
  [switch]$Force,
  [switch]$DryRun,
  [switch]$Verbose
)

$ErrorActionPreference = "Stop"

# Colors helper
function Write-Info {
  param([string]$Message)
  Write-Host "ℹ️  $Message" -ForegroundColor Cyan
}

function Write-Success {
  param([string]$Message)
  Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-Error_ {
  param([string]$Message)
  Write-Host "✗ $Message" -ForegroundColor Red
}

function Write-Warning_ {
  param([string]$Message)
  Write-Host "⚠️  $Message" -ForegroundColor Yellow
}

Write-Host "ComicWise Project Cleanup Tool"
Write-Host ""

# Show what will be cleaned
Write-Info "Cleanup targets:"
Write-Host "  • .next/       (Next.js build cache)"
Write-Host "  • .turbo/      (Turbo cache)"
Write-Host "  • coverage/    (Test coverage)"
Write-Host "  • dist/        (Build output)"
Write-Host "  • build/       (Build artifacts)"
Write-Host "  • .cache/      (General cache)"
Write-Host "  • *.log        (Log files)"
Write-Host "  • *.tmp        (Temporary files)"
Write-Host "  • .DS_Store    (macOS metadata)"
Write-Host ""

# Prompt for confirmation (unless -Force)
if (-not $Force) {
  Write-Warning_ "This will remove the above directories and files."
  $response = Read-Host "Continue? (y/N)"
  if ($response -notmatch "^[Yy]$") {
    Write-Info "Cleanup cancelled"
    exit 1
  }
}

# Build cleanup command arguments
$cleanupArgs = @("cleanup:project")

if ($DryRun) {
  $cleanupArgs += "--dry-run"
}

if ($Verbose) {
  $cleanupArgs += "--verbose"
}

$cleanupArgs += "--yes"

# Run cleanup
Write-Info "Running: pnpm $($cleanupArgs -join ' ')"
Write-Host ""

try {
  & pnpm @cleanupArgs
  Write-Success "Project cleanup complete!"
  Write-Info "Total disk space freed: [reported by cleanup script]"
  Write-Info "Tip: Run 'pnpm install' to reinstall dependencies if needed"
  exit 0
}
catch {
  Write-Error_ "Project cleanup failed!"
  Write-Host "$_"
  exit 2
}
