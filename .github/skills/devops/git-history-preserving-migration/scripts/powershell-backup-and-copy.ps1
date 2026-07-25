<# PowerShell backup and copy script

Usage: Run from PowerShell with admin privileges if needed.
#>
param(
    [string]$SourcePath,
    [string]$TargetPath,
    [switch]$Move
)

$timestamp = Get-Date -Format yyyyMMddHHmmss
$basename = Split-Path $TargetPath -Leaf
$backupZip = Join-Path -Path (Join-Path -Path $PSScriptRoot -ChildPath '..\docs\migration-logs\backups') -ChildPath ($basename + "-pre-replace-" + $timestamp + ".zip")

# Ensure backup directory exists
$backupDir = Split-Path $backupZip -Parent
if (-not (Test-Path $backupDir)) { New-Item -ItemType Directory -Path $backupDir -Force | Out-Null }

if (Test-Path $TargetPath) {
    Write-Host "Creating backup $backupZip ..."
    Compress-Archive -Path (Join-Path $TargetPath '*') -DestinationPath $backupZip -Force
} else {
    Write-Host "Target not present; skipping backup."
}

if ($Move) {
    Write-Host "Moving from $SourcePath to $TargetPath"
    Move-Item -Path $SourcePath -Destination $TargetPath -Force -Recurse
} else {
    Write-Host "Copying from $SourcePath to $TargetPath"
    Copy-Item -Path $SourcePath -Destination $TargetPath -Recurse -Force
}

Write-Host "Done. Backup: $backupZip"
