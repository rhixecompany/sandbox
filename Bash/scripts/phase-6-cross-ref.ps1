#!/usr/bin/env pwsh
# scripts/phase-6-cross-ref.ps1
# Cross-Reference Check â€” Parallel Script Drift Detection (PowerShell)
# Compares parallel script implementations (sh/ps1/bat) for drift.
<#
.SYNOPSIS
    Detects drift between parallel script implementations (sh/ps1/bat pairs).

.DESCRIPTION
    Scans known parallel script pairs across Bash/, Rhixe-company/comicwise/,
    and rhixecompany/Banking/scripts/. Checks shebangs, error handling flags,
    version alignment, shellcheck directives, and file size ratios.

.PARAMETER Fix
    Auto-align version strings to the maximum version found.

.PARAMETER Json
    Output results as JSON for CI platform consumption.

.EXAMPLE
    .\phase-6-cross-ref.ps1
    .\phase-6-cross-ref.ps1 -Fix
    .\phase-6-cross-ref.ps1 -Json
#>
param([switch]$Fix, [switch]$Json)


Set-StrictMode -Version Latest
$exitCode = 0

# â”€â”€ Script Pairs â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
$pairs = @(
    ,@("Bash/clean_dependency_folders.sh", "Bash/clean-dependency-folders.ps1", "Bash/clean-dependency-folders.bat")
    ,@("Bash/cache-clean.sh", "Bash/cache-clean.ps1", "Bash/cache-clean.bat")
    ,@("Bash/git-commit-batches.sh", "Bash/git-commit-batches.ps1")
    ,@("Bash/upgrade.sh", "Bash/upgrade.ps1", "Bash/upgrade.bat")
    ,@("Bash/scripts/phase-2-light-inventory.sh", "Bash/scripts/phase-2-light-inventory.ps1")
    ,@("Rhixe-company/comicwise/quality-gate.sh", "Rhixe-company/comicwise/quality-gate.ps1")
)

# Add skills-commit-batch pairs
1..26 | ForEach-Object {
    $sh = "Bash/scripts/skills-commit-batch-$_.sh"
    $ps = "Bash/scripts/skills-commit-batch-$_.ps1"
    if ((Test-Path $sh) -and (Test-Path $ps)) {
        $pairs += ,@($sh, $ps)
    }
}

# â”€â”€ Helpers â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
$scriptDir = Split-Path -Parent $PSCommandPath

function Get-VersionString {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return $null }
    $content = Get-Content -Path $Path -Raw
    if ($content -match 'Version:\s*(\d+\.\d+\.\d+)') {
        return $Matches[1]
    }
    return $null
}

function Get-Shebang {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return $null }
    return (Get-Content -Path $Path -TotalCount 1)
}

function Has-SetFlags {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return $false }
    $ext = [System.IO.Path]::GetExtension($Path)
    switch ($ext) {
        '.sh' { return (Select-String -Path $Path -Pattern 'set -euo pipefail' -Quiet) }
        '.ps1' { return (Select-String -Path $Path -Pattern 'ErrorActionPreference.*Stop' -Quiet) }
        default { return $true }
    }
}

function Has-Shellcheck {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return $false }
    if ([System.IO.Path]::GetExtension($Path) -ne '.sh') { return $true }
    return (Select-String -Path $Path -Pattern 'shellcheck shell=bash' -Quiet)
}

function Get-FileLines {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return 0 }
    return (Get-Content -Path $Path | Measure-Object -Line).Lines
}

function Write-Ok { if (-not $Json) { Write-Host "  âœ“ $args" -ForegroundColor Green } }
function Write-Warn { if (-not $Json) { Write-Host "  âš  $args" -ForegroundColor Yellow } }

# â”€â”€ Analyze â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
$results = @()

foreach ($pair in $pairs) {
    $issues = @()
    $names = @()
    $versions = @()
    $sizes = @()

    foreach ($file in $pair) {
        if (-not (Test-Path $file)) {
            $issues += "missing:$file"
            continue
        }
        $names += (Split-Path $file -Leaf)

        # Shebang
        if ($file -like '*.sh') {
            $sh = Get-Shebang $file
            if ($sh -ne '#!/usr/bin/env bash') { $issues += "wrong_shebang:$(Split-Path $file -Leaf)" }
        }
        if ($file -like '*.ps1') {
            $sh = Get-Shebang $file
            if ($sh -ne '#!/usr/bin/env pwsh') { $issues += "wrong_shebang:$(Split-Path $file -Leaf)" }
        }

        # Set flags
        if (-not (Has-SetFlags $file)) {
            $issues += "missing_set_flags:$(Split-Path $file -Leaf)"
        }

        # Shellcheck
        if (-not (Has-Shellcheck $file)) {
            $issues += "missing_shellcheck:$(Split-Path $file -Leaf)"
        }

        $versions += Get-VersionString $file
        $sizes += Get-FileLines $file
    }

    # Version drift
    $uniqueV = ($versions | Where-Object {$_ -ne $null} | Sort-Object -Unique)
    if ($uniqueV.Count -gt 1) {
        $issues += "version_drift:$($uniqueV -join '|')"
        if ($Fix) {
            $maxVer = ($uniqueV | Sort-Object -Descending)[0]
            foreach ($file in $pair) {
                if (Test-Path $file) {
                    (Get-Content $file -Raw) -replace 'Version:\s*\d+\.\d+\.\d+', "Version: $maxVer" | Set-Content $file -NoNewline
                    Write-Ok "Aligned $(Split-Path $file -Leaf) â†’ $maxVer"
                }
            }
        }
    }

    # Size drift
    if ($sizes.Count -ge 2) {
        $maxS = ($sizes | Measure-Object -Maximum).Maximum
        $minS = ($sizes | Measure-Object -Minimum).Minimum
        if ($minS -gt 0) {
            $ratio = [math]::Round(($maxS - $minS) / $minS * 100)
            if ($ratio -gt 30) {
                $issues += "size_drift_${ratio}pct:$($sizes -join ',')"
            }
        }
    }

    $pairName = $names -join ' â†” '
    if ($issues.Count -eq 0) {
        Write-Ok $pairName
    } else {
        $exitCode = 1
        Write-Warn $pairName
        foreach ($issue in $issues) { Write-Warn "  â””â”€ $issue" }
        $results += @{pair = $pairName; issues = $issues}
    }
}

# â”€â”€ Output â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
if ($Json) {
    $output = @{
        timestamp = (Get-Date -Format 'o')
        exit_code = $exitCode
        drifted_pairs = $results
    }
    Write-Output ($output | ConvertTo-Json -Depth 3)
}

if ($exitCode -eq 0) {
    if (-not $Json) { Write-Host "`nAll parallel scripts are in sync." -ForegroundColor Green }
} else {
    if (-not $Json) { Write-Host "`nDrift detected. Run with -Fix to auto-align versions." -ForegroundColor Yellow }
}

exit $exitCode
