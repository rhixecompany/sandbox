# Package Manager Upgrade — thin wrapper (forwards to TypeScript implementation)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir
bunx tsx src/upgrade.ts @args
