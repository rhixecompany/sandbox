# Cache Cleaner — thin wrapper (forwards to TypeScript implementation)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir
bunx tsx src/cache-clean.ts @args
