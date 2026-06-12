# DRY_RUN_SUPPORT=true
# Git Commit Batches — thin wrapper (forwards to TypeScript implementation)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir
bunx tsx src/git-commit-batches.ts @args
