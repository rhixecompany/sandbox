# DRY_RUN_SUPPORT=true
# quality-gate.ps1 - ComicWise Quality Gate Runner (PowerShell)
# Thin orchestrator wrapper that delegates to pnpm quality:gate:sh
#
# Usage:
#   .\quality-gate.ps1                              # Run all quality gates
#   .\quality-gate.ps1 -SkipLint                    # Skip linting
#   .\quality-gate.ps1 -SkipBuild                   # Skip build
#   .\quality-gate.ps1 -ContinueOnError             # Continue on first failure
#   .\quality-gate.ps1 -Json                        # Output JSON report
#   .\quality-gate.ps1 -Help                        # Show help
#
# For all options, see: pnpm quality:gate:sh --help
#
# Exit codes:
#   0  All gates passed
#   1  One or more gates failed

param(
  [switch]$SkipLint,
  [switch]$SkipBuild,
  [switch]$SkipTypeCheck,
  [switch]$SkipTests,
  [switch]$SkipTriage,
  [switch]$ContinueOnError,
  [switch]$Json,
  [switch]$Help
)

if ($Help) {
  Write-Host "ComicWise Quality Gate Runner"
  Write-Host ""
  Write-Host "Usage:"
  Write-Host "  .\quality-gate.ps1                              # Run all quality gates"
  Write-Host "  .\quality-gate.ps1 -SkipLint                    # Skip linting"
  Write-Host "  .\quality-gate.ps1 -SkipBuild                   # Skip build"
  Write-Host "  .\quality-gate.ps1 -ContinueOnError             # Continue on first failure"
  Write-Host "  .\quality-gate.ps1 -Json                        # Output JSON report"
  Write-Host "  .\quality-gate.ps1 -Help                        # Show this help message"
  Write-Host ""
  Write-Host "Quality gates run in order:"
  Write-Host "  1. lint:strict (ESLint with no warnings allowed)"
  Write-Host "  2. triage (Quality analysis)"
  Write-Host "  3. type-check (TypeScript compilation check)"
  Write-Host "  4. test (Unit tests with Vitest)"
  Write-Host "  5. build (Production build)"
  Write-Host ""
  exit 0
}

# Build args array for delegated script
$args_list = @()
if ($SkipLint) { $args_list += "--skip-lint" }
if ($SkipBuild) { $args_list += "--skip-build" }
if ($SkipTypeCheck) { $args_list += "--skip-type-check" }
if ($SkipTests) { $args_list += "--skip-tests" }
if ($SkipTriage) { $args_list += "--skip-triage" }
if ($ContinueOnError) { $args_list += "--continue-on-error" }
if ($Json) { $args_list += "--json" }

# Delegate to pnpm quality:gate:sh
& pnpm quality:gate:sh @args_list @args
exit $LASTEXITCODE
