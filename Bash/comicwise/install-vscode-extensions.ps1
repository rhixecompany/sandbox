# install-vscode-extensions.ps1 - ComicWise VSCode Extensions Manager (PowerShell)
# Installs recommended, removes unwanted, idempotent
#
# Usage:
#   .\install-vscode-extensions.ps1              # Check and report differences
#   .\install-vscode-extensions.ps1 -Force       # Apply changes (install/remove)
#   .\install-vscode-extensions.ps1 -Help        # Show help
#
# Exit codes:
#   0  Success (all configured correctly)
#   1  Differences detected or operation failed

param(
  [switch]$Force,
  [switch]$Help
)

if ($Help) {
  Write-Host "ComicWise VSCode Extensions Manager"
  Write-Host ""
  Write-Host "Usage:"
  Write-Host "  .\install-vscode-extensions.ps1              # Check and report differences"
  Write-Host "  .\install-vscode-extensions.ps1 -Force       # Apply changes (install/remove)"
  Write-Host "  .\install-vscode-extensions.ps1 -Help        # Show this help message"
  Write-Host ""
  Write-Host "Configuration: .vscode/extensions.json"
  Write-Host "  • recommendations: Extensions to install"
  Write-Host "  • unwantedRecommendations: Extensions to remove"
  Write-Host ""
  exit 0
}

$EXT_FILE = ".vscode/extensions.json"

Write-Host "=== VSCode Extension Manager ===" -ForegroundColor Cyan
Write-Host ""

# Check prerequisites
if (-not (Get-Command code -ErrorAction SilentlyContinue)) {
  Write-Host "ERROR: 'code' command not found. Install VSCode CLI." -ForegroundColor Red
  exit 1
}

if (-not (Get-Command jq -ErrorAction SilentlyContinue)) {
  Write-Host "ERROR: 'jq' not found. Install jq." -ForegroundColor Red
  exit 1
}

if (-not (Test-Path $EXT_FILE)) {
  Write-Host "ERROR: $EXT_FILE not found" -ForegroundColor Red
  exit 1
}

# Read extensions
$jsonContent = Get-Content $EXT_FILE | ConvertFrom-Json
$RECOMMENDED = $jsonContent.recommendations
$UNWANTED = $jsonContent.unwantedRecommendations
$REC_COUNT = ($RECOMMENDED | Measure-Object).Count
$UNWANT_COUNT = ($UNWANTED | Measure-Object).Count

Write-Host "Recommended: $REC_COUNT | Unwanted: $UNWANT_COUNT"
Write-Host ""

# Get current state
$INSTALLED = & code --list-extensions

# Idempotent check
$MISSING = 0
foreach ($ext in $RECOMMENDED) {
  if ($INSTALLED -notcontains $ext) {
    $MISSING++
  }
}

$STILL_UNWANTED = 0
foreach ($ext in $UNWANTED) {
  if ($INSTALLED -contains $ext) {
    $STILL_UNWANTED++
  }
}

if ($MISSING -eq 0 -and $STILL_UNWANTED -eq 0) {
  Write-Host "✓ Already configured correctly!" -ForegroundColor Green
  Write-Host "  Recommended: All installed ($REC_COUNT)"
  Write-Host "  Unwanted: All removed ($UNWANT_COUNT)"
  exit 0
}

if (-not $Force) {
  Write-Host "⚠ Differences detected. Run with -Force to apply changes." -ForegroundColor Yellow
  Write-Host "  Missing: $MISSING | Still unwanted: $STILL_UNWANTED"
  Write-Host ""
  if ($MISSING -gt 0) {
    Write-Host "Missing extensions:"
    foreach ($ext in $RECOMMENDED) {
      if ($INSTALLED -notcontains $ext) {
        Write-Host "  - $ext"
      }
    }
  }
  if ($STILL_UNWANTED -gt 0) {
    Write-Host "Still unwanted:"
    foreach ($ext in $UNWANTED) {
      if ($INSTALLED -contains $ext) {
        Write-Host "  - $ext"
      }
    }
  }
  exit 1
}

# Apply changes
Write-Host "Configuring extensions..." -ForegroundColor Cyan
Write-Host ""

# Step 1: Remove unwanted
if ($STILL_UNWANTED -gt 0) {
  Write-Host "[1/3] Removing unwanted extensions ($STILL_UNWANTED)..." -ForegroundColor Cyan
  foreach ($ext in $UNWANTED) {
    & code --uninstall-extension $ext 2>$null | Out-Null
    Write-Host "  [-] $ext"
  }
  Write-Host ""
}

# Step 2: Install recommended
Write-Host "[2/3] Installing recommended extensions ($REC_COUNT)..." -ForegroundColor Cyan
foreach ($ext in $RECOMMENDED) {
  & code --install-extension $ext --force 2>$null | Out-Null
  Write-Host "  [+] $ext"
}
Write-Host ""

# Step 3: Verify
Write-Host "[3/3] Verifying..." -ForegroundColor Cyan
$FINAL = & code --list-extensions

$VERIFY_MISSING = 0
foreach ($ext in $RECOMMENDED) {
  if ($FINAL -notcontains $ext) {
    $VERIFY_MISSING++
  }
}

$VERIFY_STILL_UNWANTED = 0
foreach ($ext in $UNWANTED) {
  if ($FINAL -contains $ext) {
    $VERIFY_STILL_UNWANTED++
  }
}

Write-Host ""
Write-Host "=== Results ===" -ForegroundColor Cyan
Write-Host "Installed: $(($REC_COUNT - $VERIFY_MISSING))/$REC_COUNT"
Write-Host "Removed: $(($UNWANT_COUNT - $VERIFY_STILL_UNWANTED))/$UNWANT_COUNT"
Write-Host ""

if ($VERIFY_MISSING -eq 0 -and $VERIFY_STILL_UNWANTED -eq 0) {
  Write-Host "✓ SUCCESS!" -ForegroundColor Green
  exit 0
} else {
  Write-Host "✗ Issues detected:" -ForegroundColor Red
  if ($VERIFY_MISSING -gt 0) {
    Write-Host "  Still missing ($VERIFY_MISSING):"
    foreach ($ext in $RECOMMENDED) {
      if ($FINAL -notcontains $ext) {
        Write-Host "    - $ext"
      }
    }
  }
  if ($VERIFY_STILL_UNWANTED -gt 0) {
    Write-Host "  Still installed ($VERIFY_STILL_UNWANTED):"
    foreach ($ext in $UNWANTED) {
      if ($FINAL -contains $ext) {
        Write-Host "    - $ext"
      }
    }
  }
  exit 1
}
