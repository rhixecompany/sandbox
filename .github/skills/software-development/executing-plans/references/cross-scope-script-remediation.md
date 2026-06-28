# Cross-Scope Script Remediation Notes

This reference captures reusable lessons from a multi-repo Bash/PowerShell/BAT/TypeScript remediation session.

## Durable execution pattern

- Create the plan artifact first, then create the issue/progress/verification artifacts before changing code.
- Treat the inventory/context file as a prerequisite, not a nicety.
- Keep implementation batches small: 7 files max per batch unless the batch is verification-only.
- Prefer wrapper normalization before core runner rewrites so behavior stays observable.
- Keep progress logs append-only and use explicit completion markers so interrupted sessions can resume safely.

## Cross-scope rollout order

1. Bash first when wrapper density is highest.
2. Banking second when it already models the target wrapper-to-TS delegation style.
3. Comicwise last when root-level launchers need to converge only after the canonical pattern is stable.

## Verification contract

- Verify syntax by script type rather than with one generic command.
- Verify dry-run separately from mutation paths.
- Verify wrapper-to-runner parity for exit codes, argument forwarding, and output shape.
- Keep command aliases only while they still serve a real compatibility need.
- Do not delete a wrapper until the replacement runner is live and verified.

## Artifact checklist

- `docs/{task}-list-context.md`
- `docs/{task}-issues-context.md`
- `docs/{task}-fix-issues-context.md`
- `docs/{task}-verification-report.md`

## Pitfalls observed

- Updating the plan alone is not enough; execution-ready artifacts must also exist.
- If a file is read with pagination and then overwritten, re-read the full file first to avoid clobbering unseen content.
- When a phase claims completion, confirm the corresponding artifact or completion marker exists on disk before skipping work.
- If a validation report is generated early, keep it as a scaffold until the batch work is done.
