# dev.ps1 - ComicWise Development Environment Launcher (PowerShell)
# Checks prerequisites, verifies database connectivity, launches dev server + browser
#
# Usage:
#   .\dev.ps1                    # Start dev server and open browser
#   .\dev.ps1 -NoBrowser         # Start dev server only
#   .\dev.ps1 -SkipDbCheck       # Skip database connectivity check
#
# Exit codes:
#   0  Success
#   1  Prerequisite check failed
#   2  Database connectivity check failed
#   3  .env.local missing

param(
  [switch]$NoBrowser,
  [switch]$SkipDbCheck
)


$ErrorActionPreference = "Stop"

# Simple colored helpers
function Write-Info([string]$Message) { Write-Host "ℹ $Message" -ForegroundColor Cyan }
function Write-Success([string]$Message) { Write-Host "✓ $Message" -ForegroundColor Green }
function Write-Error_([string]$Message) { Write-Host "✗ $Message" -ForegroundColor Red }
function Write-Warning_([string]$Message) { Write-Host "⚠ $Message" -ForegroundColor Yellow }

# Check Node.js version (18+)
Write-Info "Checking Node.js version..."
try {
  $nv = (& node --version) 2>$null
  if (-not $nv) { throw "node missing" }
  $nodeMajor = [int](($nv -replace 'v', '').Split('.')[0])
  if ($nodeMajor -lt 18) { Write-Error_ "Node.js 18 or higher is required. Current: $nv"; exit 1 }
  Write-Success "Node.js $nv"
}
catch {
  Write-Error_ "Node.js is not installed or not in PATH"
  exit 1
}

# Check pnpm version (8+)
Write-Info "Checking pnpm version..."
try {
  $pv = (& pnpm --version) 2>$null
  if (-not $pv) { throw "pnpm missing" }
  $pnpmMajor = [int]($pv.Split('.')[0])
  if ($pnpmMajor -lt 8) { Write-Error_ "pnpm 8 or higher is required. Current: $pv"; exit 1 }
  Write-Success "pnpm $pv"
}
catch {
  Write-Error_ "pnpm is not installed or not in PATH. Install with: npm install -g pnpm"
  exit 1
}

# Check .env.local exists
Write-Info "Checking .env.local..."
if (-not (Test-Path ".env.local")) {
  Write-Warning_ ".env.local not found"
  if (Test-Path ".env.local.example") {
    Write-Info "Creating .env.local from .env.local.example..."
    Copy-Item .env.local.example .env.local
    Write-Success "Created .env.local"
    Write-Warning_ "Please update .env.local with your actual environment values"
  }
  else {
    Write-Error_ ".env.local.example not found either. Cannot proceed."
    exit 3
  }
}
Write-Success ".env.local exists"

# Check database connectivity (unless skipped)
if (-not $SkipDbCheck) {
  Write-Info "Checking database connectivity..."
  try {
    $p = Start-Process -FilePath "pnpm" -ArgumentList @("health:db", "--turbo") -NoNewWindow -Wait -PassThru -ErrorAction Stop
    if ($p.ExitCode -eq 0) { Write-Success "Database connected" }
    else { Write-Warning_ "Database health command exited $($p.ExitCode)" }
  }
  catch {
    Write-Warning_ "Database connectivity check failed"
    Write-Warning_ "You may need to: pnpm db:push"
    Write-Info "Continuing with dev server startup..."
  }
}

# Clear build artifacts
Write-Info "Clearing build artifacts..."
try {
  $p = Start-Process -FilePath "pnpm" -ArgumentList @("clean") -NoNewWindow -Wait -PassThru
  Write-Success "Artifacts cleared"
}
catch {
  Write-Warning_ "pnpm clean failed or not available"
}

# Start dev server
Write-Info "Starting development server..."
Write-Host "Dev server will be available at: http://localhost:3000" -ForegroundColor Cyan
Write-Host ""

# Start pnpm dev in the background
$devProcess = Start-Process -FilePath "pnpm" -ArgumentList @("dev") -NoNewWindow -PassThru

# Wait for dev server to be ready
Write-Info "Waiting for development server to start..."
$retryCount = 0
$maxRetries = 30

while ($retryCount -lt $maxRetries) {
  try {
    $null = Invoke-WebRequest -Uri "http://localhost:3000" -UseBasicParsing -TimeoutSec 1
    Write-Success "Development server is ready!"
    break
  }
  catch {
    $retryCount++
    Start-Sleep -Seconds 1
  }
}

if ($retryCount -eq $maxRetries) {
  Write-Warning_ "Development server took longer than expected to start"
}

Write-Host ""

# Open browser (unless -NoBrowser)
if (-not $NoBrowser) {
  Write-Info "Opening browser..."
  try {
    Start-Process "http://localhost:3000"
    Write-Success "Browser should open shortly"
  }
  catch {
    Write-Warning_ "Could not open browser automatically"
  }
}

Write-Host ""
Write-Success "Development environment ready!"
Write-Info "Stop the server with: Ctrl+C"
Write-Info "View logs: pnpm health:all"
Write-Host ""

# Wait for process
$devProcess.WaitForExit()
