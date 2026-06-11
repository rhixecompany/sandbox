# ComicWise Quality Gate Runner (PowerShell)
# Runs lint:strict, triage, type-check, test, build -- each logged to a report file.
# Usage: powershell -ExecutionPolicy Bypass -File quality-gate.ps1 [-SkipTests] [-SkipBuild] [-SkipTypeCheck] [-SkipLint] [-SkipTriage] [-SkipE2E] [-ContinueOnError] [-Json]
# Reports: lint-strict.txt, triage-report.txt, type-check.txt, test-report.txt, build-report.txt
# JSON:    quality-gate.json (with -Json flag)

param(
  [switch]$SkipTests,
  [switch]$SkipBuild,
  [switch]$SkipTypeCheck,
  [switch]$SkipLint,
  [switch]$SkipTriage,
  [switch]$SkipE2E,
  [switch]$ContinueOnError,
  [switch]$Json
)

$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# -- Symbols (plain ASCII for maximum compatibility) -------------------------
$Sym_Check = '+'
$Sym_Cross = 'x'
$Sym_Warn = '!'
$Sym_Arrow = '->'

# -- Simple output helpers (avoid complex ANSI sequences for portability)
function Write-Step([string]$Step, [string]$Label) {
  Write-Host ""
  Write-Host "[$Step] $Label" -ForegroundColor Cyan
  Write-Host ('-' * 60)
}

function Write-Ok([string]$Msg) { Write-Host "  $Sym_Check $Msg" -ForegroundColor Green }
function Write-Fail([string]$Msg) { Write-Host "  $Sym_Cross $Msg" -ForegroundColor Red }
function Write-Warn([string]$Msg) { Write-Host "  $Sym_Warn $Msg" -ForegroundColor Yellow }
function Write-Info([string]$Msg) { Write-Host "  $Msg" -ForegroundColor DarkGray }

function Invoke-Gate {
  param(
    [string]$Step,
    [string]$Label,
    [string]$Command,
    [string]$OutFile
  )
  Write-Step $Step $Label
  Write-Info "$Sym_Arrow $Command"
  Write-Info "$Sym_Arrow logging to $OutFile (streaming with Tee-Object)"

  $sw = [System.Diagnostics.Stopwatch]::StartNew()

  # Create report header
  $header = @(
    "=== ComicWise Quality Gate: $Label ==="
    "Date   : $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    "Command: $Command"
    ('=' * 60)
    ""
  )

  # Write header to file
  $header -join "`n" | Out-File -FilePath $OutFile -Encoding UTF8

  # Run command and pipe through Tee-Object to stream to console and file
  Invoke-Expression "$Command 2>&1" | Tee-Object -FilePath $OutFile -Append | Out-String

  $code = $LASTEXITCODE
  $sw.Stop()
  $time = $sw.Elapsed.ToString("mm\:ss")

  # Append footer with timing info
  $footer = @(
    ""
    ('=' * 60)
    "Exit   : $code"
    "Time   : $time"
  )

  $footer -join "`n" | Out-File -FilePath $OutFile -Append -Encoding UTF8

  # Count errors and warnings in full output (including what was just written)
  $allOutput = Get-Content -Path $OutFile -Raw
  $errCount = ([regex]::Matches($allOutput, '(?i)\berror\b')).Count
  $warnCount = ([regex]::Matches($allOutput, '(?i)\bwarning\b')).Count

  if ($code -eq 0) {
    Write-Ok "$Label passed ($time)"
  }
  else {
    Write-Fail "$Label failed (exit $code) ($time)"
  }

  if ($errCount -gt 0) { Write-Fail "$errCount error(s) detected" }
  if ($warnCount -gt 0) { Write-Warn "$warnCount warning(s) detected" }

  return @{ ExitCode = $code; Errors = $errCount; Warnings = $warnCount; Time = $time; File = $OutFile }
}

# -- Main ---------------------------------------------------------------------
$startTime = Get-Date
Write-Host ""
Write-Host "$Bold${Blue}+==============================================+$Reset"
Write-Host "$Bold${Blue}|       ComicWise Quality Gate Runner         |$Reset"
Write-Host "$Bold${Blue}+==============================================+$Reset"
Write-Host "${Gray}Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')$Reset"

$results = @{}

# Step 1: Lint Strict
if ($SkipLint) {
  Write-Step "1/5" "ESLint Strict (no auto-fix)"
  Write-Warn "Skipped (-SkipLint)"
  $results["lint"] = @{ ExitCode = 0; Errors = 0; Warnings = 0; Time = "00:00"; File = "lint-strict.txt" }
}
else {
  $results["lint"] = Invoke-Gate -Step "1/5" -Label "ESLint Strict (no auto-fix)" -Command "pnpm lint:strict" -OutFile "lint-strict.txt"
  if ($results["lint"].ExitCode -ne 0 -and -not $ContinueOnError) {
    Write-Host ""
    Write-Host "$Bold$Red$Sym_Cross ESLint Strict failed — stopping here.$Reset"
    Write-Host "$Yellow  Review lint-strict.txt for details.$Reset"
    Write-Host ""
    exit 1
  }
}

# Step 2: Triage
if ($SkipTriage) {
  Write-Step "2/5" "Quality Gate Triage"
  Write-Warn "Skipped (-SkipTriage)"
  $results["triage"] = @{ ExitCode = 0; Errors = 0; Warnings = 0; Time = "00:00"; File = "triage-report.txt" }
}
else {
  $results["triage"] = Invoke-Gate -Step "2/5" -Label "Quality Gate Triage" -Command "pnpm triage" -OutFile "triage-report.txt"
  if ($results["triage"].ExitCode -ne 0 -and -not $ContinueOnError) {
    Write-Host ""
    Write-Host "$Bold$Red$Sym_Cross Triage failed — stopping here.$Reset"
    Write-Host "$Yellow  Review triage-report.txt for details.$Reset"
    Write-Host ""
    exit 1
  }
}

# Step 3: Type Check
if ($SkipTypeCheck) {
  Write-Step "3/5" "TypeScript Type Check"
  Write-Warn "Skipped (-SkipTypeCheck)"
  $results["type-check"] = @{ ExitCode = 0; Errors = 0; Warnings = 0; Time = "00:00"; File = "type-check.txt" }
}
else {
  $results["type-check"] = Invoke-Gate -Step "3/5" -Label "TypeScript Type Check" -Command "pnpm type-check" -OutFile "type-check.txt"
  if ($results["type-check"].ExitCode -ne 0 -and -not $ContinueOnError) {
    Write-Host ""
    Write-Host "$Bold$Red$Sym_Cross Type Check failed — stopping here.$Reset"
    Write-Host "$Yellow  Review type-check.txt for details.$Reset"
    Write-Host ""
    exit 1
  }
}

# Step 4: Tests
if ($SkipTests) {
  Write-Step "4/5" "Unit Tests"
  Write-Warn "Skipped (-SkipTests)"
  $results["test"] = @{ ExitCode = 0; Errors = 0; Warnings = 0; Time = "00:00"; File = "test-report.txt" }
}
else {
  if ($SkipE2E) {
    $testCmd = "pnpm test"
  }
  else {
    $testCmd = "pnpm test; pnpm test:ui"
  }
  $results["test"] = Invoke-Gate -Step "4/5" -Label "Vitest Unit Tests" -Command $testCmd -OutFile "test-report.txt"
  if ($results["test"].ExitCode -ne 0 -and -not $ContinueOnError) {
    Write-Host ""
    Write-Host "$Bold$Red$Sym_Cross Tests failed — stopping here.$Reset"
    Write-Host "$Yellow  Review test-report.txt for details.$Reset"
    Write-Host ""
    exit 1
  }
}

# Step 5: Build
if ($SkipBuild) {
  Write-Step "5/5" "Production Build"
  Write-Warn "Skipped (-SkipBuild)"
  $results["build"] = @{ ExitCode = 0; Errors = 0; Warnings = 0; Time = "00:00"; File = "build-report.txt" }
}
else {
  $results["build"] = Invoke-Gate -Step "5/5" -Label "Production Build (debug)" -Command "pnpm build:debug" -OutFile "build-report.txt"
  if ($results["build"].ExitCode -ne 0 -and -not $ContinueOnError) {
    Write-Host ""
    Write-Host "$Bold$Red$Sym_Cross Build failed — stopping here.$Reset"
    Write-Host "$Yellow  Review build-report.txt for details.$Reset"
    Write-Host ""
    exit 1
  }
}

# -- Summary ------------------------------------------------------------------
$elapsed = (Get-Date) - $startTime
$totalTime = $elapsed.ToString("mm\:ss")
$totalSecs = [int]$elapsed.TotalSeconds
$allPassed = ($results.Values | Where-Object { $_.ExitCode -ne 0 }).Count -eq 0
$totalErrors = ($results.Values | ForEach-Object { $_.Errors } | Measure-Object -Sum).Sum
$totalWarnings = ($results.Values | ForEach-Object { $_.Warnings } | Measure-Object -Sum).Sum
$failedGateNames = @($results.GetEnumerator() | Where-Object { $_.Value.ExitCode -ne 0 } | ForEach-Object { $_.Key })

Write-Host ""
Write-Host "$Bold${Blue}=== Summary ============================================$Reset"
foreach ($key in @("lint", "triage", "type-check", "test", "build")) {
  $r = $results[$key]
  if ($r.ExitCode -eq 0) { $icon = "$Green$Sym_Check" } else { $icon = "$Red$Sym_Cross" }
  $name = switch ($key) {
    "type-check" { "Type Check    " }
    "lint" { "Lint Strict   " }
    "triage" { "Triage        " }
    "test" { "Unit Tests    " }
    "build" { "Build (debug) " }
  }
  # Compute timing percentage
  $parts = $r.Time -split ':'
  $gateSecs = [int]$parts[0] * 60 + [int]$parts[1]
  if ($totalSecs -gt 0) { $pct = [math]::Round($gateSecs * 100 / $totalSecs) } else { $pct = 0 }
  Write-Host "  $icon $Reset$name $Gray$($r.Time) ($pct)%  $Sym_Arrow $($r.File)$Reset"
}
Write-Host ""
Write-Host "  ${Gray}Total: $totalTime | Errors: $totalErrors | Warnings: $totalWarnings$Reset"
Write-Host ""

# -- JSON Output --------------------------------------------------------------
if ($Json) {
  $jsonData = [ordered]@{
    timestamp     = (Get-Date -Format "yyyy-MM-ddTHH:mm:ss")
    duration      = $totalTime
    passed        = $allPassed
    totalErrors   = $totalErrors
    totalWarnings = $totalWarnings
    failedGates   = $failedGateNames
    gates         = [ordered]@{}
  }
  foreach ($key in @("lint", "triage", "type-check", "test", "build")) {
    $r = $results[$key]
    $jsonData.gates[$key] = [ordered]@{
      exitCode = $r.ExitCode
      errors   = $r.Errors
      warnings = $r.Warnings
      time     = $r.Time
      file     = $r.File
    }
  }
  $jsonData | ConvertTo-Json -Depth 4 | Set-Content -Path "quality-gate.json" -Encoding UTF8
  Write-Info "$Sym_Arrow JSON written to quality-gate.json"
}

if ($allPassed) {
  Write-Host "$Bold$Green$Sym_Check All quality gates passed$Reset (total: $totalTime)"
  Write-Host ""
  exit 0
}
else {
  $failCount = ($results.Values | Where-Object { $_.ExitCode -ne 0 }).Count
  Write-Host "$Bold$Red$Sym_Cross $failCount gate(s) failed$Reset (total: $totalTime)"
  Write-Host "Review the .txt report files for details."
  Write-Host ""
  exit 1
}
