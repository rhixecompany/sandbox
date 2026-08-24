# Next Steps Implementation Specs

Created: 2026-08-25T00:02:23.443575

## Goal
Execute remaining Next Steps: GitHub auth setup, multi-agent-sync verification, test-providers-models live probe

## SPEC-001: GitHub Authentication Setup

**Priority:** P0

**Description:** Configure SSH key or PAT for GitHub to enable push to origin

### Requirements
- Generate or configure SSH key for GitHub
- Add SSH key to GitHub account
- Verify SSH connection works
- Push local commits and tags to origin

### Acceptance Criteria
- git push origin clean-development succeeds
- git push origin --tags succeeds
- No 403 authentication errors

---

## SPEC-002: Multi-Agent Sync Parity Verification

**Priority:** P1

**Description:** Run multi-agent-sync verify_sync.py for 65-check parity verification across root ↔ Codex ↔ OpenCode ↔ mirror ↔ 6 profiles

### Requirements
- Execute verify_sync.py from hermes-profiles directory
- Verify all 65 checks pass
- Report any parity failures

### Acceptance Criteria
- 65 checks pass
- No parity failures between Hermes, Codex, OpenCode configurations

---

## SPEC-003: Test Providers Models Live Probe

**Priority:** P0

**Description:** Execute test-providers-models prompt for live model probe verification

### Requirements
- Run test-providers-models prompt via Hermes
- Dispatch parallel capability probes for 3 provider clusters
- Rank models by working status → vision → reasoning → context
- Update Hermes config with verified fallback chain
- Propagate to installed agents

### Acceptance Criteria
- All authorized providers probed
- Only verified working models in fallback chain
- Hermes config updated with verified models
- Agent configs propagated

---

