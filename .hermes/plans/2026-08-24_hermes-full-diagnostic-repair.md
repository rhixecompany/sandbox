# Hermes Full Diagnostic Repair Plan
**Date:** 2026-08-24
**Profile:** default
**Model:** nemotron-3-ultra-free (opencode-zen)
**Status:** approved

## Goal
Run the full Hermes diagnostic battery, capture all findings, then systematically debug and fix every real bug, issue, warning, and error until clean.

## Scope
- Diagnostic chain: `hermes doctor && hermes doctor --fix && hermes security audit && hermes status && hermes insights && hermes skills audit && hermes skills check && hermes skills update && hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway && hermes logs gui && hermes logs agent`
- Log triage across desktop/gateway/gui/agent/errors
- Systematic root-cause debugging for all actionable findings
- Verification gate: no unresolved real bugs; intentional guards and transient noise documented

## Phases

### Phase 1 — Diagnostic Battery
Run the full 14-command chain in the background with unbounded timeout, tee output to `.hermes/diagnostics-2026-08-24.log`, and capture `CHAIN_EXIT`.
- Entry: background terminal session
- Success: `CHAIN_EXIT=0`
- Failure: rerun skipped commands individually; do not proceed to Phase 2 with truncated evidence

### Phase 2 — Classification
Read the captured log and classify every finding:
1. **Real code bug** → Phase 3
2. **Intentional guard** → report only
3. **Transient external** → document, verify self-heal
4. **Config advisory** → report only

Output: `.hermes/plans/diagnostics-findings-2026-08-24.md`

### Phase 3 — Root-Cause Debugging
For each real bug:
- Follow `systematic-debugging` 4-phase method
- Form single hypothesis, test minimally, verify before continuing
- If 3+ fixes fail on one bug → stop and re-evaluate architecture
- Fix at source, not symptom

### Phase 4 — Verification
Re-run the diagnostic battery; confirm:
- `hermes doctor` / `--fix` all pass
- `hermes security audit` 0 findings
- `hermes skills check` returns `0 update(s) available`
- No new ERROR patterns in logs
- All patched tests pass

### Phase 5 — Report
Deliver a scannable summary:
- Fixed bugs with evidence
- Intentional guards left untouched
- Transient issues observed
- Advisory items noted
- Final verification evidence (exit codes, counts)

## Files Likely to Change
- `C:\Users\Alexa\AppData\Local\hermes\skills\devops\hermes-diagnostic-repair\references\*` (if new patterns emerge)
- `C:\Users\Alexa\AppData\Local\hermes\config.yaml` (only via `hermes config set` per user prefs)
- Potential source patches under `$LOCALAPPDATA\hermes\hermes-agent\tools\` if a real code bug is confirmed

## Risks
- Chain short-circuits on first failure → mitigated by `{ ...; }` grouping + `CHAIN_EXIT` capture
- Skills update loop re-flags after fix → acceptance gate is `hermes skills check` post-update
- Windows CRLF/path issues in hooks/logs → classified per `log-analysis-and-triage` heuristics

## Approval
Plan approved for execution. Proceed to Phase 1 immediately.
