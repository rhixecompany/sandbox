# Hermes Ecosystem Audit Report — 2026-06-11

Summary
-------
This report summarizes the hermes skills audit performed on 2026-06-11. It catalogs critical findings, top offenders, quarantine recommendations, and a prioritized remediation plan.

Key numbers
-----------
- Skills scanned: 99
- Critical findings: 106 (filtered into .hermes/results/skills_critical_actionable.json)
- Top offenders: unsloth (27), lambda-labs (12), web-pentest (9), here-now (6), openclaw-migration (6)

Top offenders & recommended actions
-----------------------------------
- unsloth (27 critical findings) — Quarantine immediately; create PRs to remove hard-coded credentials, remove curl | sh installers, and convert persistent setup into manual steps.
- lambda-labs (12) — Quarantine; sanitize references/troubleshooting docs containing curl -u and ssh examples.
- web-pentest (9) — Quarantine; remove or gate destructive scripts and add explicit warnings.

Action Plan
-----------
1) Quarantine top-10 offenders (preview in .hermes/results/quarantine_plan.md and .hermes/scripts/quarantine_skills.sh). Do not execute the script without reviewing the destination directories.
2) Create PRs for each quarantined skill with targeted patches (remove curl|sh, mask secrets, convert persistent writes to manual steps).
3) Run hermes skills audit --deep on remaining skills flagged as CAUTION to ensure no missed criticals.
4) Add a pre-commit hook or CI step to reject secrets or curl|sh installers in skill repos.

Files produced
--------------
- .hermes/results/skills_critical_actionable.md
- .hermes/results/skills_critical_actionable.json
- .hermes/results/skills_critical_findings.md
- .hermes/results/quarantine_plan.md
- .hermes/scripts/quarantine_skills.sh

Next steps
----------
- Confirm you want me to: (1) run the quarantine script (moves skill dirs), (2) open PR patches automatically for the top offenders, (3) run deep audits, and (4) commit the report files to git.
