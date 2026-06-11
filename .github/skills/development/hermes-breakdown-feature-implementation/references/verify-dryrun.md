verify-dryrun: verification harness

Purpose
- Explain the verify-dryrun harness semantics and how CI enforces failing-first DRY_RUN_SUPPORT adoption.

Synopsis
- verify-dryrun.sh scans Bash/ for scripts that contain side-effect patterns (rm, git push, docker, scp, mv, cp, chmod, chown).
- The harness requires each candidate to contain the marker `DRY_RUN_SUPPORT=true`.
- If marker present, harness attempts a dry-run invocation (bash --dry-run or pwsh --dry-run semantics) when possible.
- Harness exits non-zero if any candidate lacks the marker or if a supported runtime invocation fails.

CI behavior
- The job should run on pull_request targeting Bash/** and must block merges until verify-dryrun exits 0.
- The canonical PR flow is failing-first: first PR adds markers only; follow-ups implement dry-run behavior.

Installing/Updating the harness
- Copy scripts/verify-dryrun.template.sh to Bash/tests/verify-dryrun.sh and adapt path patterns as needed.
- Ensure the script is executable (chmod +x).

Pitfalls & notes
- The harness scans many files; update the grep filter to narrow to known-script directories to avoid false-positives from docs and lockfiles.
- For PowerShell scripts, prefer adding a `[switch]$DryRun` param and checking `$env:DRY_RUN` for CI-driven runs.
- Avoid interactive prompts in scripts (Read-Host) unless gated behind an explicit --interactive flag.

Minimal patch example (bash)

Add near top-of-file:

# DRY_RUN_SUPPORT=true
DRY_RUN=${DRY_RUN:-false}
for arg in "$@"; do
  if [ "$arg" = "--dry-run" ] || [ "$arg" = "-n" ]; then DRY_RUN=true; fi
done
if [ "$DRY_RUN" = "true" ]; then
  echo "DRY-RUN: $(basename "$0") would perform actions (no side effects)."
  exit 0
fi
