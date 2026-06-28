Audit Findings — 2026-06-11

Summary
- Performed `hermes skills audit` across the profile and workspace.
- Generated artifacts: .hermes/results/skills_audit.log and .hermes/results/skills_audit_summary.txt
- High-severity findings: multiple instances of exfiltration patterns (hard-coded API keys, curl -u usage), supply-chain risks (curl-based installers in docs), persistence/privilege hints (SSH key writes, container init scripts), and references to secret-bearing environment variables in scripts.

Immediate remediation recommendations
1. Quarantine or remove skill dirs that contain clear secret-exfiltration code. Files to inspect first (examples from summary):
   - scripts/canvas_api.py (CANVAS_API_TOKEN), scripts/parrot_openrouter.py, templates/api_wrapper.py
   - scripts/publish.sh (reads API_KEY via cat)
   - references/troubleshooting.md lines referencing `curl -u`
2. Replace or redact any documentation that demonstrates curl -fsSL piping directly to shell. Replace with a note:
   "Do not pipe remote scripts into sh. Download to inspect the script first, verify provenance, then run locally."
3. For any skill that performs privileged writes, schedule a human review. If a skill claims to add SSH keys or run as root, either sandbox it or remove it until reviewed.
4. Use `hermes skills inspect <identifier>` to pick the exact official identifier when multiple matches exist. Do NOT rely on short names for deterministic installs in automation.
5. The CLI does not accept `--security-scan` on install; the correct flow is to run `hermes skills install <identifier>` then `hermes skills check <identifier>` and `hermes skills inspect <identifier>`.

Operational notes for future runs
- Always capture audit output to .hermes/results/ and create a short summary file that filters CRITICAL findings (already implemented here: .hermes/results/skills_audit_summary.txt).
- When automating installs, prefer full identifiers (e.g. `official/security/web-pentest`) and `--yes` for batch installs to skip interactive prompts.
- If a skill directory exists on disk before install, treat it as "already present" and still run `hermes skills inspect` and `hermes skills check` to verify state and updates.

References
- .hermes/results/skills_audit_summary.txt
- .hermes/results/skills_audit.log
- .hermes/results/skills_install_batch1.log
- .hermes/results/skills_install_batch1_verification.log

Next steps template
- Create a quarantined copy of questionable skill dirs under `backup.hermes/quarantine/YYYY-MM-DD/skill-name/`.
- Run `hermes skills inspect <full-identifier>` for each candidate and decide: update in place / remove / sandbox.
- Draft PRs that redact dangerous docs and replace them with safe-install guidance.
