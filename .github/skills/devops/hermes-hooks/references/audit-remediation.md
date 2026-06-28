Audit action: add remediation checklist and quarantine template

## References
- `references/audit-remediation.md` — step-by-step immediate remediation checklist for CRITICAL audit findings (created 2026-06-11)

## Quarantine template
- path: backup.hermes/quarantine/YYYY-MM-DD/<skill>/
- copy skill dir to quarantine before making destructive edits

## Quick checklist (for operators)
1. If a script contains hard-coded API keys or `curl -s` piping to shell, move the skill to quarantine:
   mkdir -p backup.hermes/quarantine/$(date +%F)/<skill>
   cp -r ~/.hermes/skills/<skill> backup.hermes/quarantine/$(date +%F)/
2. Redact any docs that contain `curl | sh` with a replacement sentence: "Manual install only; inspect downloaded scripts before running." 3. Open a PR that removes direct secret dumps (e.g., `cat secretfile`) from public docs.

