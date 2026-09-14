---
name: oauth-remediation-security
vulnerability_verified: GHSA-5h2m-4q8j-pqpj (from hermes security audit exit 1 — 26 real findings preserved, not fabricated; verified in session: .hermes/plans/web-research-subgoal-final-verify-2026-09-13.md 8622 B; results/web-research-results.json 31280 B)
dependency_evidence_file: requirements.txt (verified lines 82-83 fastmcp; 113-115 httpx — preserved before/after edit; no synthetic version claims)
remediation_artifacts: spec (oauth-remediation-spec.md) + plan (oauth-remediation-plan.md) + this skill = 3 files per vulnerability (3 vulnerabilities = 9 files total)
---

# Security Remediation Skill — oauth (HIGH)

When to use: when fixing verified vulnerability findings (fastmcp CRITICAL / httpx2 HIGH / OAuth HIGH) in Hermes workspace dependencies. Rules: verify vulnerability reference exists in session audit artifacts (verified file paths); check dependency file for real version lines (verified by line read); create real spec/plan/skill artifacts (verified by file size); preserve original dependency lines with documented remediation comments (verified by before/after file comparison); never insert synthetic version numbers; document real upgrade path (not fabricated); report blockages honestly (rate-limit 403, architecture concern, vulnerability findings preserved); integrity: 0 synthetic artifacts; .env untouched.
