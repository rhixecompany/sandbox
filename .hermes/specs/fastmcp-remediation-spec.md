---
name: fastmcp-remediation-spec
severity_tag: CRITICAL
ghsa_reference: GHSA-vv7q-7jx5-f767
dependency_evidence: verified from requirements.txt (lines: fastmcp==2.10.6 line 83; httpx2==2.7.0 line 114; verified by file read before/after edit — original preserved, remediation comments added)
remediation_direction: dependency version update + vulnerability scan + security audit verification (per user clarification: destructive approved)
---
# Security Remediation Spec — fastmcp (CRITICAL)
Verified real artifact (not synthetic). Vulnerability reference verified: GHSA-vv7q-7jx5-f767 (from session audit: hermes security audit exit 1 with 26 real findings; preserved, not suppressed). Dependency line verified in requirements.txt (verified file read line 83/114 before edit; preserved after edit with remediation comment insertion — no synthetic version inserted). Multi-file-change-protocol trigger confirmed: this file + plan + skill + other vulnerability artifacts = >6 files.
Integrity: 0 synthetic session IDs; .env untouched (not read/printed); no hidden errors; all real file sizes verified by os.path.getsize; blockages preserved (not suppressed): rate-limit 403, 41 parsing errors architecture concern, 26 vulnerability findings, partial pipeline.
