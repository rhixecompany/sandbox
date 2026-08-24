# Comprehensive Platform Remediation Plan

**Plan ID:** 2026-08-24_comprehensive-platform-remediation
**Created:** 2026-08-24
**Status:** Not Started
**Priority:** Critical
**Author:** Hermes Agent (via systematic debugging workflow)
**Profile:** exec-assistant

---

## Executive Summary

This plan addresses all issues discovered during the comprehensive platform diagnostic run:
`hermes doctor && hermes doctor --fix && hermes security audit && hermes status && hermes insights && hermes skills audit && hermes skills check && hermes skills update && hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway && hermes logs gui && hermes logs agent`

---

## Phase 1: Database & Storage Remediation

### 1.1 WAL Checkpoint & Vacuum
- **Issue**: Large WAL file (64 MB) — may indicate missed checkpoints
- **Action**: Run `hermes doctor --fix` to perform WAL checkpoint
- **Verification**: WAL size < 10 MB after checkpoint
- **Risk**: Low (auto-fixable)

### 1.2 State Database Optimization
- **Issue**: state.db at 409.8 MB logical size, 104,909 pages
- **Action**: 
  - Run VACUUM on state.db
  - Consider pruning old sessions (`hermes sessions prune --older-than 30d`)
  - Enable automatic WAL checkpointing via config
- **Verification**: Database size reduced by >20%, query performance improved
- **Risk**: Medium (requires backup before VACUUM)

---

## Phase 2: npm Vulnerability Remediation

### 2.1 Web Workspace (4 High Vulnerabilities)
- **Issue**: Build-time tooling advisories in `web` workspace
- **Action**: 
  - Navigate to web workspace
  - Run `npm audit fix --force` or bump lockfile
  - If arborist crash occurs (known npm bug): delete package-lock.json, run `npm install`
- **Verification**: `npm audit` shows 0 high/critical vulnerabilities
- **Risk**: Low (build-time only, not runtime)

### 2.2 UI-TUI Workspace (3 High Vulnerabilities)
- **Issue**: Build-time tooling advisories in `ui-tui` workspace
- **Action**: Same as web workspace
- **Verification**: `npm audit` shows 0 high/critical vulnerabilities
- **Risk**: Low

### 2.3 Lockfile Strategy
- **Action**: Implement `npm audit` in CI pipeline to catch regressions
- **Risk**: Low

---

## Phase 3: Authentication & Provider Configuration

### 3.1 Nous Portal Auth
- **Issue**: Invalid refresh token
- **Action**: Run `hermes portal` to re-authenticate
- **Verification**: Auth shows ✓ logged in
- **Risk**: Low

### 3.2 MiniMax OAuth
- **Issue**: Not logged in
- **Action**: Run `hermes auth add minimax-oauth`
- **Verification**: Auth shows ✓ logged in
- **Risk**: Low

### 3.3 xAI OAuth (Grok)
- **Issue**: Not logged in, no credentials stored
- **Action**: 
  - Run `hermes model` → select xAI Grok OAuth (SuperGrok / Premium+)
  - Run `hermes auth add xai-oauth`
- **Verification**: Auth shows ✓ logged in
- **Risk**: Low

### 3.4 Qwen OAuth
- **Issue**: Credentials not found
- **Action**: Run `qwen auth qwen-oauth` 
- **Verification**: Auth shows ✓ logged in
- **Risk**: Low

### 3.5 API Key Providers (Unconfigured)
- **Providers missing**: Z.AI/GLM, Kimi/Moonshot, StepFun, MiniMax, MiniMax-CN, DeepInfra, Firecrawl, Browser Use, Browserbase, FAL, ElevenLabs, Anthropic
- **Action**: For each needed provider:
  - Run `hermes model` to configure
  - Or add keys to `.env` file
- **Verification**: `hermes status` shows ✓ for configured providers
- **Risk**: Low

---

## Phase 4: System Dependencies & Tool Availability

### 4.1 Missing System Dependencies (⚠ warnings)
| Tool | Missing Dependency | Action |
|------|-------------------|--------|
| bfl | System dependency | Install bfl CLI or disable if unused |
| browser | System dependency | Install browser automation deps |
| browser-cdp | System dependency | Install CDP dependencies |
| discord | DISCORD_BOT_TOKEN | Add token to .env or disable |
| feishu_doc | System dependency | Install feishu SDK |
| feishu_drive | System dependency | Install feishu SDK |
| hermes-yuanbao | System dependency | Install yuanbao CLI |
| homeassistant | System dependency | Install HA integration |
| image_gen | System dependency | Install image generation deps |

- **Action**: For each needed tool, install dependencies; for unused tools, disable in config
- **Verification**: `hermes doctor` shows no ⚠ for enabled tools
- **Risk**: Low

---

## Phase 5: Skills Audit Remediation

### 5.1 Dangerous/Blocked Community Skills
The skills audit found **multiple dangerous skills** from community source that are BLOCKED:

**DANGEROUS (Blocked - cannot override with --force):**
- antigravity-cli (supply_chain CRITICAL)
- grok (supply_chain CRITICAL, persistence CRITICAL ×3)
- pinggy-tunnel (exfiltration CRITICAL, network HIGH ×3)
- watchers (exfiltration CRITICAL ×2)
- stocks (exfiltration CRITICAL ×4)
- fitness-nutrition (exfiltration CRITICAL ×4, obfuscation HIGH)
- mcp-oauth-remote-gateway (exfiltration HIGH ×2, network MEDIUM ×4)
- axolotl (supply_chain CRITICAL)
- unsloth (supply_chain CRITICAL ×12, exfiltration HIGH ×30+, privilege_escalation HIGH ×8, injection HIGH ×2)

**CAUTION (Blocked - can override with --force):**
- hyperliquid (exfiltration HIGH)

- **Action**: 
  1. Review each blocked skill - determine if needed
  2. If needed: fork to local, remediate security findings, re-audit
  3. If not needed: uninstall/remove from hub
  4. For CAUTION skills: evaluate risk vs utility, use --force only with documentation
- **Verification**: `hermes skills audit` shows 0 dangerous/blocked skills
- **Risk**: High (security implications)

### 5.2 Missing Skill Paths
- code-wiki — path missing
- subagent-driven-development — path missing  
- cloudflare-temporary-deploy — path missing

- **Action**: Reinstall or relocate missing skills
- **Verification**: Skills load without path warnings
- **Risk**: Low

---

## Phase 6: Runtime & Performance Issues

### 6.1 Event Loop Stalls (GIL Pressure)
- **Issue**: Multiple "event loop stalled" warnings (5s - 31s) in web server logs
- **Pattern**: Occurs during high-load periods (Aug 11, 16, 19)
- **Root Cause**: CPU-bound work blocking async event loop
- **Action**:
  - Profile web server to identify blocking operations
  - Move CPU-intensive work to thread pool (`run_in_executor`)
  - Consider worker processes for heavy endpoints
  - Add monitoring/alerting for stall duration > 5s
- **Verification**: No stalls > 1s in 7-day period
- **Risk**: High (impacts responsiveness)

### 6.2 Streaming Failures (502 Upstream Errors)
- **Issue**: "Streaming response failed: [502] Upstream error from Nvidia: Service temporarily overloaded"
- **Pattern**: Multiple occurrences in agent.log (latest: 2026-08-24 19:48:07)
- **Root Cause**: Provider (Nvidia/Nemotron) returning 502
- **Action**:
  - Implement retry with exponential backoff for 502/503/504
  - Add circuit breaker for repeated failures
  - Configure fallback model chain: nemotron → deepseek → gemini → ollama-cloud
  - Add health check for provider before routing
- **Verification**: Zero unhandled 502 errors in 7-day period
- **Risk**: High (user-facing failures)

### 6.3 Connection Reset Errors
- **Issue**: `httpx.ReadError: [WinError 10054] An existing connection was forcibly closed by the remote host`
- **Action**:
  - Increase HTTP timeout settings
  - Add connection pooling configuration
  - Implement automatic reconnection logic
- **Verification**: Zero connection reset errors in 7-day period
- **Risk**: Medium

---

## Phase 7: Configuration File Consolidation

### 7.1 Duplicate MCP Configurations
**Files found:**
- `~/Desktop/SandBox/opencode.json` (OpenCode config with MCP servers)
- `~/Desktop/SandBox/.mcp.json` (Standard MCP config)

**Analysis:**
| Aspect | opencode.json | .mcp.json |
|--------|---------------|-----------|
| Format | OpenCode-specific | Standard MCP (VS Code compatible) |
| Servers | 26 configured | 30 configured |
| Unique to opencode | DJANGO, DOCS, PYTEST, POSTGRES, MCP-DOCKER, HONCHO (remote) | — |
| Unique to .mcp.json | — | honcho (remote), python-quality, tooling-lint, tooling-config, parallel-search, parallel-task |

- **Action**: 
  1. Consolidate into single source of truth (recommend `.mcp.json` as canonical)
  2. Generate `opencode.json` from `.mcp.json` via script
  3. Add both to version control with clear ownership
  4. Document sync process in README
- **Verification**: Single source, auto-generated derivative, no drift
- **Risk**: Medium (configuration drift)

### 7.2 Missing Configuration Files
- `omo.json` — not found (only `.omo/run-continuation/` dir exists)
- `.instructions.md` files — none found in `.github/`

- **Action**: 
  - Create `omo.json` if using Oh My OpenCode
  - Audit `.github/prompts/` for `.instructions.md` pattern compliance
- **Risk**: Low

---

## Phase 8: Logging & Observability

### 8.1 Log Rotation & Retention
- **Issue**: Logs growing without rotation (agent.log, web_server.log)
- **Action**:
  - Configure log rotation (daily, max 7 days, compress)
  - Set max file size (100 MB)
  - Add structured logging (JSON) for parsing
- **Verification**: Logs rotate, disk usage stable
- **Risk**: Low

### 8.2 Error Alerting
- **Action**: 
  - Set up alerts for: 502 errors, connection resets, event loop stalls > 5s
  - Integrate with Telegram (already configured)
- **Risk**: Low

---

## Implementation Timeline

| Phase | Duration | Start Date | End Date | Dependencies |
|-------|----------|------------|----------|--------------|
| 1: Database & Storage | 1 day | Day 1 | Day 1 | None |
| 2: npm Vulnerabilities | 1 day | Day 1 | Day 2 | None |
| 3: Auth & Providers | 2 days | Day 1 | Day 3 | None |
| 4: System Dependencies | 2 days | Day 2 | Day 4 | Phase 3 |
| 5: Skills Audit | 3 days | Day 2 | Day 5 | None |
| 6: Runtime Performance | 5 days | Day 3 | Day 8 | Phase 1 |
| 7: Config Consolidation | 1 day | Day 4 | Day 5 | None |
| 8: Logging & Observability | 1 day | Day 5 | Day 6 | Phase 6 |

**Total Estimated Duration:** 8 days
**Critical Path:** Phase 6 (Runtime) depends on Phase 1 completion

---

## Resource Allocation

| Resource | Allocation | Notes |
|----------|------------|-------|
| Primary Engineer | 100% | All phases |
| Subagent (parallel) | 2x | Phases 2, 3, 5 (independent tasks) |
| Compute | Medium | Phase 6 profiling |
| External APIs | As needed | Provider auth, npm registry |

---

## Milestones

| Milestone | Target Date | Criteria |
|-----------|-------------|----------|
| M1: Storage & Vulns Fixed | Day 2 | WAL < 10MB, npm audit clean |
| M2: Auth Complete | Day 3 | All needed providers ✓ |
| M3: Skills Clean | Day 5 | 0 dangerous, 0 missing paths |
| M4: Runtime Stable | Day 8 | 0 stalls > 1s, 0 unhandled 502 |
| M5: Config Unified | Day 5 | Single MCP source, auto-sync |
| M6: Observability Live | Day 6 | Alerts firing, logs rotating |

---

## Verification Gates

### Gate 1 (End of Day 2)
- [ ] `hermes doctor` shows 0 issues (or only manual-intervention items)
- [ ] `npm audit` in web/ and ui-tui/ shows 0 high/critical
- [ ] WAL file < 10 MB

### Gate 2 (End of Day 3)
- [ ] All required auth providers show ✓
- [ ] All needed API keys configured
- [ ] System dependencies resolved for enabled tools

### Gate 3 (End of Day 5)
- [ ] `hermes skills audit` shows 0 dangerous/blocked
- [ ] All skill paths resolve
- [ ] Config consolidation complete

### Gate 4 (End of Day 8)
- [ ] Zero event loop stalls > 1s in 48h
- [ ] Zero unhandled 502/connection errors in 48h
- [ ] Log rotation & alerting operational
- [ ] All phases verified, docs updated

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Provider 502 persists | High | High | Multi-provider fallback chain |
| npm arborist crash | Medium | Low | Lockfile bump strategy documented |
| Skill remediation breaks functionality | Medium | Medium | Test in isolation, maintain backups |
| Event loop stall root cause elusive | Medium | High | Profiling tools, consider architecture change |
| Config drift recurs | Medium | Low | Automated sync script + CI check |

---

## Success Criteria

1. **Health**: `hermes doctor` returns ✓ on all checks (except optional/unconfigured)
2. **Security**: `hermes security audit` returns clean
3. **Skills**: `hermes skills audit` returns 0 dangerous, 0 missing paths
4. **Runtime**: No event loop stalls > 1s, no unhandled streaming errors in 7 days
5. **Config**: Single MCP config source, auto-generated derivatives
6. **Observability**: Structured logs, rotation, alerting operational

---

## File Inventory & Summary

### Configuration Files Analyzed

| File | Purpose | Status | Action Needed |
|------|---------|--------|---------------|
| `opencode.json` | OpenCode CLI config with 26 MCP servers | Active | Consolidate into .mcp.json |
| `.mcp.json` | Standard MCP config (VS Code compatible) with 30 servers | Active | Make canonical source |
| `omo.json` | Oh My OpenCode config | **Missing** | Create if needed |
| `.github/prompts/*.instructions.md` | Instruction files for prompts | **None found** | Audit prompt library |

### File Purposes

- **opencode.json**: Configures OpenCode agent with MCP servers, model settings, plugins
- **.mcp.json**: Standard Model Context Protocol server configuration for cross-editor compatibility
- **omo.json**: Oh My OpenCode configuration for agent marketplace/plugins
- **.instructions.md**: Reusable instruction snippets for prompt composition (DRY pattern)

---

## Next Steps

1. **Immediate**: Run Phase 1 & 2 fixes (auto-fixable)
2. **Today**: Begin Phase 3 auth configuration
3. **This Week**: Execute Phases 4-8 per timeline
4. **Ongoing**: Monitor verification gates, adjust timeline as needed

---

## Approval

This plan requires validation before execution. Review the phases, timeline, and success criteria. Once approved, implementation will begin with Phase 1.

**Approval Status:** ⬜ Pending
**Approved By:** ________________
**Date:** ________________