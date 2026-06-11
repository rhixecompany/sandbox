# Development Environment Setup Script (Windows PowerShell)
# Enhanced with: colored output, progress tracking, error handling
# Usage: powershell -ExecutionPolicy Bypass -File setup-dev.ps1

# Helper functions (use PowerShell -ForegroundColor for Windows compatibility)
function Write-Info([string]$Message) { Write-Host "ℹ $Message" -ForegroundColor Cyan }
function Write-Success([string]$Message) { Write-Host "✓ $Message" -ForegroundColor Green }
function Write-Warn([string]$Message) { Write-Host "⚠ $Message" -ForegroundColor Yellow }
function Write-Error-Custom([string]$Message) { Write-Host "✗ $Message" -ForegroundColor Red }
function Write-Header([string]$Title) { Write-Host ""; Write-Host "*** $Title ***" -ForegroundColor Cyan; Write-Host "" }

# Parse arguments
$SkipDb = $false
$SkipSeed = $false
$SkipInstall = $false

foreach ($arg in $args) {
  if ($arg -eq '--skip-db') { $SkipDb = $true }
  if ($arg -eq '--skip-seed') { $SkipSeed = $true }
  if ($arg -eq '--skip-install') { $SkipInstall = $true }
}

# Main setup
Write-Header "ComicWise Development Environment Setup"

# Check Node.js
Write-Info "Checking prerequisites..."
try {
  $nodeVersion = (& node --version) 2>$null
  if (-not $nodeVersion) { throw "node not found" }
  Write-Success "Node.js $nodeVersion"
}
catch {
  Write-Error-Custom "Node.js not found. Please install Node.js 18+"
  exit 1
}

# Check pnpm
try {
  $pnpmVersion = (& pnpm --version) 2>$null
  if (-not $pnpmVersion) { throw "pnpm not found" }
  Write-Success "pnpm $pnpmVersion"
}
catch {
  Write-Warn "pnpm not found. Installing globally..."
  & npm install -g pnpm
  $pnpmVersion = (& pnpm --version) 2>$null
  Write-Success "pnpm $pnpmVersion installed"
}

# Install dependencies (optional)
if (-not $SkipInstall) {
  Write-Header "Installing Dependencies"
  # Run pnpm install and check exit code
  Write-Info "Running: pnpm install --frozen-lockfile"
  $proc = Start-Process -FilePath "pnpm" -ArgumentList @("install", "--frozen-lockfile") -NoNewWindow -Wait -PassThru
  if ($proc.ExitCode -ne 0) {
    Write-Error-Custom "Failed to install dependencies (exit $($proc.ExitCode))"
    exit 1
  }
  Write-Success "Dependencies installed successfully"
}
else {
  Write-Info "Skipping dependency installation (--skip-install)"
}

# Copy .env files
Write-Header "Environment Configuration"
if (-not (Test-Path ".env.local")) {
  Write-Info "Creating .env.local from template..."
  if (Test-Path ".env.local.example") {
    Copy-Item ".env.local.example" ".env.local"
    Write-Warn "Please edit .env.local with your database credentials:"
    Write-Warn "  DATABASE_URL: PostgreSQL 14+ connection string"
    Write-Warn "  AUTH_SECRET: Run 'openssl rand -hex 32' to generate"
    Write-Warn "  AUTH_URL: http://localhost:3000 (local dev)"
  }
  else {
    Write-Error-Custom ".env.local.example not found"
    exit 1
  }
}
else {
  Write-Success ".env.local already configured"
}

# Type checking
Write-Header "Type Safety Check"
$proc = Start-Process -FilePath "pnpm" -ArgumentList @("type-check") -NoNewWindow -Wait -PassThru
if ($proc.ExitCode -ne 0) {
  Write-Error-Custom "TypeScript errors detected (exit $($proc.ExitCode)). Please fix above."
  exit 1
}
Write-Success "TypeScript validation passed"

# Database setup (optional)
if (-not $SkipDb) {
  Write-Header "Database Setup"
  $proc = Start-Process -FilePath "pnpm" -ArgumentList @("db:push") -NoNewWindow -Wait -PassThru
  if ($proc.ExitCode -ne 0) {
    Write-Error-Custom "Database setup failed (exit $($proc.ExitCode))"
    exit 1
  }
  Write-Success "Database schema applied"
}

# Seeding (optional)
if (-not $SkipSeed -and -not $SkipDb) {
  Write-Header "Database Seeding (Validation)"
  $proc = Start-Process -FilePath "pnpm" -ArgumentList @("seed:validate") -NoNewWindow -Wait -PassThru
  if ($proc.ExitCode -eq 0) {
    Write-Success "Seed validation passed. Proceeding with data insertion..."
    $proc2 = Start-Process -FilePath "pnpm" -ArgumentList @("seed:all") -NoNewWindow -Wait -PassThru
    if ($proc2.ExitCode -ne 0) {
      Write-Error-Custom "Seeding failed (exit $($proc2.ExitCode))"
      exit 1
    }
    Write-Success "Database seeded successfully"
  }
}

# Summary
Write-Header "Setup Complete ✅"
Write-Info "Development environment ready!"
Write-Host ""
Write-Host "${Bold}Next steps:${Reset}"
Write-Host "  1. Start the dev server: ${Bold}pnpm dev${Reset}"
Write-Host "  2. Open in browser: ${Bold}http://localhost:3000${Reset}"
Write-Host ""
Write-Host "${Gray}Useful commands:${Reset}"
Write-Host "  ${Gray}pnpm type-check${Reset}    - Validate TypeScript"
Write-Host "  ${Gray}pnpm lint:fix${Reset}       - Format and lint code"
Write-Host "  ${Gray}pnpm test${Reset}           - Run unit tests"
Write-Host "  ${Gray}pnpm test:ui${Reset}        - Run E2E tests"
Write-Host "  ${Gray}pnpm db:studio${Reset}      - Open database viewer"
Write-Host ""
Write-Host ""
Write-Host "Next steps:"
Write-Host "1. Edit .env.local with database credentials"
Write-Host "2. Run: pnpm db:push (to apply migrations)"
Write-Host "3. Run: pnpm dev (to start development server)"
Write-Host ""
