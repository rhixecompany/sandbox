# Fast Path Workflow: Step-by-Step Reference

## Session 1: Hermes Configuration Verification (May 26, 2026)

**Context**: Alexa configured Hermes with GitHub Copilot + OpenCode Zen fallback chain.

**Commands executed** (in order):
```bash
hermes doctor                          # Health baseline
hermes config show                     # Review config
hermes auth list                       # Check credentials
hermes mcp list                        # Verify MCP servers
hermes tools list                      # Confirm toolset status
```

**Outcomes**:
- ✅ hermes doctor: ALL PASSING
- ✅ 7/8 MCP servers enabled (260+ tools)
- ✅ 2 providers configured + fallback chain
- ✅ 19+ toolsets active
- ✅ 0 security advisories
- ✅ 27/27 API connectivity checks passed

**Time taken**: ~3 minutes for complete verification

**Key insight**: When config is already v24+ and some providers are configured, skip full 5-phase setup and jump straight to verification + report generation.

---

## When Fast Path Is Right

✅ **Use Fast Path When:**
- Config already exists (version v22+)
- At least one provider is configured
- hermes doctor shows >50% systems passing
- You're adding a provider or verifying post-update
- Target: 2-3 minute verification cycle

❌ **Don't Use Fast Path When:**
- Fresh Hermes install from scratch
- Config is v20 or older (needs migration)
- Multiple critical hermes doctor failures
- Setting up for a team (need comprehensive docs)
- Use hermes-complete-setup (full 5 phases) instead

---

## Command Reference

| Goal | Command | Time |
|------|---------|------|
| Full health check | `hermes doctor` | 15-20s |
| Review config | `hermes config show` | 1-2s |
| List MCP servers | `hermes mcp list` | 2-5s |
| Check provider credentials | `hermes auth list` | 1-2s |
| View toolsets | `hermes tools list` | 1-2s |
| Verify fallback chain | `hermes config show \| grep -A 10 fallback_providers` | 2-3s |
| Test secondary provider | `hermes chat --provider <name> -q "test"` | 5-10s |

**Total for complete verification**: 2-3 minutes

---

## Common Verification Scenarios

### Scenario 1: Adding GitHub Copilot to OpenCode Zen

**Before**:
- Primary: OpenCode Zen
- No fallback configured

**Steps**:
1. Set GitHub Copilot auth: `hermes login github-copilot`
2. Verify credentials: `hermes auth list | grep copilot`
3. Check fallback config: `hermes config show | grep fallback_providers`
4. Test: `hermes chat --provider github-copilot -q "Hello"`
5. Document in report

**Time**: 2-3 minutes

---

### Scenario 2: Post-Update Verification

**After Hermes update:**
1. Run `hermes doctor` (catches API changes, endpoint updates)
2. Run `hermes mcp list` (confirms servers still responding)
3. If any ❌ errors → run troubleshooting from skill
4. Document in report with update version
5. Mark as "Verified after v0.14.0 → v0.15.0 upgrade"

**Time**: 1-2 minutes

---

### Scenario 3: Confirming Fallback Chain Before Workflow

**Before starting critical work:**
1. `hermes doctor` → verify baseline
2. `hermes config show | grep -A 5 "fallback_providers"` → confirm chain exists
3. `hermes chat --provider <primary> -q "test"` → test primary
4. `hermes chat --provider <secondary> -q "test"` → test secondary
5. Mark as "Fallback chain verified operational" in notes

**Time**: 3-5 minutes

**Why**: Prevents 2-hour debugging session if primary provider goes down mid-work.

---

## Key Metrics from May 26 Session

| Metric | Value | Acceptable |
|--------|-------|-----------|
| MCP servers enabled | 7/8 | ✅ (8th is optional) |
| Total tools available | 260+ | ✅ |
| Toolsets active | 19+ | ✅ |
| Providers configured | 2 (OpenCode + Copilot) | ✅ |
| hermes doctor exit | 0 | ✅ |
| API connectivity | 27/27 passed | ✅ |
| Security advisories | 0 | ✅ |
| Session store | 115 indexed | ✅ |
| Python version | 3.11.14 | ✅ |

---

## Red Flags That Require Full Troubleshooting

- ❌ hermes doctor exit code > 0
- ❌ MCP server shows "connection error"
- ❌ Provider shows "API unreachable"
- ❌ Tool count < 150 (suggests server offline)
- ❌ Security advisories present

**If you see any red flag**: Don't proceed. See **Troubleshooting** section in main skill.

---

## Pitfall Prevention Checklist

Before considering verification "complete":

- [ ] Ran `hermes doctor` and saw all green
- [ ] Ran `hermes mcp list` and saw 6+ servers ✅ enabled
- [ ] Ran `hermes auth list` and confirmed all providers have credentials
- [ ] Checked fallback chain: `hermes config show | grep fallback_providers`
- [ ] Tested at least primary + secondary providers manually (optional but recommended)
- [ ] Created verification report with timestamp
- [ ] No unexplained warnings or errors in output

---

**Fast Path Workflow**: Ready to use in future Hermes sessions.  
**Reference Date**: May 26, 2026  
**Last Updated**: May 26, 2026
