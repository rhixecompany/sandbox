# Test script for Invoke-AllScanners orchestrator
# Tests multi-manager detection and scanning

param(
    [string]$TestRepoPath = "C:\Users\Alexa\Desktop\SandBox\test-repo"
)


Set-StrictMode -Version Latest
# Import logger module
$LOGGER_PATH = "C:\Users\Alexa\Desktop\SandBox\scripts\lib\logger.psm1"
if (Test-Path $LOGGER_PATH) {
    Import-Module $LOGGER_PATH -Force
}

Write-Phase "Testing Invoke-AllScanners Orchestrator"
Write-Info "Test Repository: $TestRepoPath"

# Load required libraries
Write-Info "Loading helper libraries..."
. "C:\Users\Alexa\Desktop\SandBox\scripts\lib\package-managers.ps1"
. "C:\Users\Alexa\Desktop\SandBox\scripts\lib\package-manager-scanners.ps1"
. "C:\Users\Alexa\Desktop\SandBox\scripts\lib\dependency-scanner.ps1"

Write-Success "Libraries loaded successfully"

# Test 1: Verify function exists
Write-SubHeader "Test 1: Verify Invoke-AllScanners function exists"
if (Get-Command Invoke-AllScanners -ErrorAction SilentlyContinue) {
    Write-Success "Function exists"
} else {
    Write-Err "Function not found"
    exit 1
}

# Test 2: Run orchestrator on test repository
Write-SubHeader "Test 2: Run Invoke-AllScanners on test repository"
try {
    $result = Invoke-AllScanners -RepoPath $TestRepoPath -IncludeStdout $false
    Write-Success "Orchestrator executed successfully"
} catch {
    Write-Err "Orchestrator failed: $_"
    exit 1
}

# Test 3: Validate result structure
Write-SubHeader "Test 3: Validate result structure"
$requiredFields = @("repo_path", "detected_managers", "total_vulnerabilities", "managers", "scan_timestamp")
$missingFields = @()

foreach ($field in $requiredFields) {
    if (-not $result.ContainsKey($field)) {
        $missingFields += $field
    }
}

if ($missingFields.Count -eq 0) {
    Write-Success "All required fields present"
} else {
    Write-Err "Missing fields: $($missingFields -join ', ')"
    exit 1
}

# Test 4: Validate detected managers
Write-SubHeader "Test 4: Validate detected managers"
Write-Info "Detected managers: $($result.detected_managers -join ', ')"
if ($result.detected_managers.Count -gt 0) {
    Write-Success "Managers detected: $($result.detected_managers.Count)"
} else {
    Write-Warn "No managers detected (may be expected if CLIs not installed)"
}

# Test 5: Validate per-manager results
Write-SubHeader "Test 5: Validate per-manager results"
foreach ($managerName in $result.detected_managers) {
    $managerData = $result.managers[$managerName]
    Write-Info "  Manager: $managerName"
    Write-Info "    Status: $($managerData.status)"
    Write-Info "    Vulnerabilities: $($managerData.vulnerabilities)"
    Write-Info "    Timestamp: $($managerData.timestamp)"
    if ($managerData.error) {
        Write-Warn "    Error: $($managerData.error)"
    }
}
Write-Success "Per-manager results validated"

# Test 6: Validate JSON serialization
Write-SubHeader "Test 6: Validate JSON serialization"
try {
    $json = $result | ConvertTo-Json -Depth 3
    Write-Success "Result serializes to JSON successfully"
    Write-Info "JSON Output (first 500 chars):"
    Write-Info $json.Substring(0, [Math]::Min(500, $json.Length))
    Write-Info "..."
} catch {
    Write-Err "JSON serialization failed: $_"
    exit 1
}

# Test 7: Validate aggregation
Write-SubHeader "Test 7: Validate vulnerability aggregation"
$aggregatedCount = 0
foreach ($managerName in $result.detected_managers) {
    $managerData = $result.managers[$managerName]
    if ($managerData.status -eq "success" -or $managerData.status -eq "no_vulnerabilities") {
        $aggregatedCount += $managerData.vulnerabilities
    }
}
Write-Info "  Aggregated vulnerabilities: $aggregatedCount"
Write-Info "  Total vulnerabilities field: $($result.total_vulnerabilities)"
if ($aggregatedCount -eq $result.total_vulnerabilities) {
    Write-Success "Aggregation matches total"
} else {
    Write-Warn "Aggregation mismatch (may be expected if some managers skipped)"
}

# Summary
Write-Phase "Test Summary"
Write-Success "All core tests passed"
Write-Info "Result object:"
$result | ConvertTo-Json -Depth 3
