# Dependency Folder Cleanup — thin wrapper (forwards to TypeScript implementation)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir
bunx tsx src/clean-dep.ts @args
