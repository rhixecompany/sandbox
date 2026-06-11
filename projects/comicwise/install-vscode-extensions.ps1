#!/usr/bin/env pwsh
# VSCode Extension Manager
# Installs recommended, removes unwanted, idempotent

param(
    [switch]$Force     # Reinstall even if already correct
)

$ErrorActionPreference = "Stop"
$extensionsFile = ".vscode/extensions.json"

Write-Host "=== VSCode Extension Manager ===" -ForegroundColor Cyan

# Check prerequisites
try {
    $null = Get-Content $extensionsFile -Raw -ErrorAction Stop
} catch {
    Write-Host "ERROR: $extensionsFile not found" -ForegroundColor Red
    exit 1
}

# Read extensions.json
$config = Get-Content $extensionsFile -Raw | ConvertFrom-Json
$recommended = $config.recommendations
$unwanted = $config.unwantedRecommendations

Write-Host "Recommended: $($recommended.Count) | Unwanted: $($unwanted.Count)"

# Get current state
$installed = code --list-extensions

# Idempotent check
$missing = $recommended.Where({ $_ -notin $installed })
$stillUnwanted = $unwanted.Where({ $_ -in $installed })

if ($missing.Count -eq 0 -and $stillUnwanted.Count -eq 0) {
    Write-Host "`nAlready configured correctly!" -ForegroundColor Green
    Write-Host "Recommended: All installed ($($recommended.Count))"
    Write-Host "Unwanted: All removed ($($unwanted.Count))"
    exit 0
}

if (-not $Force) {
    Write-Host "`nDifferences detected. Run with -Force to apply changes." -ForegroundColor Yellow
    Write-Host "Missing: $($missing.Count) | Still unwanted: $($stillUnwanted.Count)"
    Write-Host "`nMissing extensions:"
    $missing | ForEach-Object { Write-Host "  - $_" }
    Write-Host "`nStill unwanted:"
    $stillUnwanted | ForEach-Object { Write-Host "  - $_" }
    exit 1
}

# Step 1: Remove unwanted
if ($stillUnwanted.Count -gt 0) {
    Write-Host "`n[1/4] Removing unwanted extensions ($($stillUnwanted.Count))..." -ForegroundColor Yellow
    foreach ($ext in $stillUnwanted) {
        code --uninstall-extension $ext 2>$null
        Write-Host "  [-] $ext" -ForegroundColor Red
    }
}

# Step 2: Uninstall ALL installed (clean slate)
Write-Host "`n[2/4] Uninstalling all extensions ($($installed.Count))..." -ForegroundColor Yellow
$installed | ForEach-Object -Parallel { code --uninstall-extension $_ 2>$null } -ThrottleLimit 8

# Step 3: Install recommended in parallel
Write-Host "`n[3/4] Installing recommended extensions ($($recommended.Count))..." -ForegroundColor Yellow
$jobs = @()
foreach ($ext in $recommended) {
    $jobs += Start-Job -ScriptBlock {
        param($e)
        try {
            code --install-extension $e --force 2>$null
            return @{ Ext = $e; Success = $true }
        } catch {
            return @{ Ext = $e; Success = $false; Error = $_.Exception.Message }
        }
    } -ArgumentList $ext
}

# Collect results
$results = $jobs | Wait-Job | Receive-Job
$jobs | Remove-Job

$failed = $results.Where({ -not $_.Success })
$installed = $results.Where({ $_.Success })

foreach ($r in $installed) {
    Write-Host "  [+] $($r.Ext)" -ForegroundColor Green
}
foreach ($r in $failed) {
    Write-Host "  [!] $($r.Ext): $($r.Error)" -ForegroundColor Red
}

# Step 4: Verify
Write-Host "`n[4/4] Verifying..." -ForegroundColor Yellow
$finalInstalled = code --list-extensions

$verifyRecommended = $recommended.Where({ $_ -notin $finalInstalled })
$verifyUnwanted = $unwanted.Where({ $_ -in $finalInstalled })

# Report
Write-Host "`n=== Results ===" -ForegroundColor Cyan
Write-Host "Installed: $($recommended.Count - $verifyRecommended.Count)/$($recommended.Count)"
Write-Host "Removed: $($unwanted.Count - $verifyUnwanted.Count)/$($unwanted.Count)"

if ($failed.Count -gt 0) {
    Write-Host "`nFailed ($($failed.Count)):" -ForegroundColor Red
    $failed | ForEach-Object { Write-Host "  - $($_.Ext)" }
}

if ($verifyRecommended.Count -gt 0) {
    Write-Host "`nStill missing ($($verifyRecommended.Count)):" -ForegroundColor Red
    $verifyRecommended | ForEach-Object { Write-Host "  - $_" }
}

if ($verifyUnwanted.Count -gt 0) {
    Write-Host "`nStill installed ($($verifyUnwanted.Count)):" -ForegroundColor Red
    $verifyUnwanted | ForEach-Object { Write-Host "  - $_" }
}

if ($verifyRecommended.Count -eq 0 -and $verifyUnwanted.Count -eq 0 -and $failed.Count -eq 0) {
    Write-Host "`nSUCCESS!" -ForegroundColor Green
    exit 0
} else {
    Write-Host "`nISSUES DETECTED" -ForegroundColor Red
    exit 1
}
