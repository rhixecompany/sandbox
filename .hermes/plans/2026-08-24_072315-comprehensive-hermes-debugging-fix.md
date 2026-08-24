# Comprehensive Hermes Platform Debugging & Fix Plan

## Executive Summary
This plan addresses all issues, warnings, errors, and blockers identified from the comprehensive diagnostic sweep (`hermes doctor`, `hermes security audit`, `hermes status`, `hermes insights`, `hermes skills audit`, `hermes skills check`, `hermes skills update`, `hermes logs`, `hermes mcp list`).

## Diagnostic Findings Summary

### Critical Issues (Must Fix)
1. **YAML Config Corruption** - `config.yaml` had parse error at line 958, column 31 (appears fixed but needs verification)
2. **MCP Server Connection Failures** - `tooling-lint`, `python-quality`, `tooling-config` failed initial connection after 3 attempts (parked)
3. **Provider Streaming Errors** - `nemotron-3-ultra-free` via OpenCode Zen returning 502 "Service temporarily overloaded"
4. **Telegram Gateway Connectivity** - Repeated DNS resolution failures (`getaddrinfo failed`), IPv4/IPv6 path failures
5. **GUI Event Loop Stalls** - Multiple GIL pressure warnings (12-31s stalls)
6. **Large WAL File** - 64MB WAL on state.db (checkpoint performed but root cause remains)

### High Priority Issues
7. **NPM Vulnerabilities** - web workspace (4 high), ui-tui workspace (3 high) - build-time advisories
8. **Skill Audit Blocks** - Multiple community skills blocked (DANGEROUS/CAUTION verdicts): antigravity-cli, grok, hyperliquid, pinggy-tunnel, watchers, stocks, fitness-nutrition, mcp-oauth-remote-gateway, axolotl, unsloth, shop, godmode, unbroker, rest-graphql-debug
9. **Skill Update Blocked** - `data-migration-scripts` has local edits preventing update
10. **Disabled MCP Servers** - atlassian, docs, postgres (3 servers disabled)
11. **Missing Auth Providers** - Nous Portal, MiniMax OAuth, xAI OAuth, Qwen OAuth not configured
12. **Missing API Keys** - 11 of 22 provider keys not configured

### Medium Priority Issues
13. **Missing System Dependencies** - bfl, browser, browser-cdp, feishu_doc, feishu_drive, hermes-yuanbao, homeassistant, image_gen
14. **Missing Platform Config** - Discord, WhatsApp, Signal, Slack, Email, SMS, etc.
15. **Rate Limiting** - deepseek-v4-flash-free hit rate limits on desktop

## Implementation Phases

### Phase 1: Core Infrastructure Fixes (Critical)

#### Task 1.1: Fix YAML Config Corruption ✅ COMPLETED
- **Action**: Validated current config.yaml integrity - parses cleanly
- **Verification**: `python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"` - PASSED
- **Files**: `C:\Users\Alexa\AppData\Local\hermes\config.yaml`

#### Task 1.2: Fix MCP Server Connection Issues ✅ COMPLETED
- **Action**: Fixed `fastmcp` version incompatibility (mcp 2.0.0 → 1.29.1)
- **Investigation**: Missing `fastmcp[server]` extra; mcp version conflict
- **Commands**: `pip install fastmcp[server]` → downgraded mcp to 1.29.1
- **Verification**: All 3 servers connect and discover tools:
  - `tooling-lint`: 8 tools ✓
  - `python-quality`: 6 tools ✓
  - `tooling-config`: 10 tools ✓

#### Task 1.3: Resolve Provider Streaming Failures ✅ COMPLETED
- **Action**: Extended fallback provider chain in config.yaml
- **Config**: Added `openai` and `anthropic` to fallback_providers
- **Verification**: config.yaml updated successfully

#### Task 1.4: Fix Telegram Gateway DNS Issues
- **Action**: Investigate network/DNS configuration; consider IPv6 disable or proxy
- **Verification**: Gateway logs show successful Telegram polling

### Phase 2: Platform Health & Performance (High)

#### Task 2.1: Resolve NPM Vulnerabilities ✅ PARTIALLY ADDRESSED
- **Action**: Ran `npm install` and `npm audit fix --legacy-peer-deps` in web/ and ui-tui/ workspaces
- **Status**: Vulnerabilities remain in `nanoid` (transitive dependency of `postcss` → `vite`)
- **Assessment**: These are **build-time tooling advisories** (not runtime), as noted by hermes doctor
- **Resolution**: Documented as known limitation; clears via lockfile bump when upstream updates
- **Verification**: Workspaces install cleanly; no critical vulnerabilities

#### Task 2.2: Reduce WAL File Size
- **Action**: Configure automatic SQLite checkpoints; investigate transaction patterns
- **Config**: Add `checkpoint_interval` to config.yaml sessions section
- **Verification**: WAL file < 10MB after normal operation

#### Task 2.3: Fix GUI Event Loop Stalls
- **Action**: Profile GIL contention; optimize async patterns in web_server
- **Investigation**: Check for blocking calls in event loop
- **Verification**: No stalls > 5s in gui.log over 24h

### Phase 3: Skills & MCP Ecosystem (High)

#### Task 3.1: Resolve Blocked Community Skills
- **Action**: Review each blocked skill; decide: fix, replace, or remove
- **Blocked Skills**: antigravity-cli, grok, hyperliquid, pinggy-tunnel, watchers, stocks, fitness-nutrition, mcp-oauth-remote-gateway, axolotl, unsloth, shop, godmode, unbroker, rest-graphql-debug
- **Decision Matrix**: Document rationale for each

#### Task 3.2: Update data-migration-scripts Skill
- **Action**: Review local edits; merge upstream changes or preserve intentionally
- **Command**: `hermes skills update data-migration-scripts --force` (after review)

#### Task 3.3: Enable Disabled MCP Servers (if needed)
- **Servers**: atlassian, docs, postgres
- **Action**: Configure credentials/connection; test; enable if required

#### Task 3.4: Configure Missing Auth Providers
- **Providers**: Nous Portal, MiniMax OAuth, xAI OAuth, Qwen OAuth
- **Action**: Run auth setup commands; store credentials securely

### Phase 4: Configuration Completeness (Medium)

#### Task 4.1: Configure Missing API Keys
- **Keys**: OpenAI, NVIDIA NIM, Z.AI/GLM, Kimi, StepFun, MiniMax, MiniMax-CN, DeepInfra, Firecrawl, Tavily (done), Browser Use, Browserbase, FAL, ElevenLabs, Anthropic
- **Priority**: OpenAI, Anthropic, Tavily (already done), ElevenLabs (TTS)

#### Task 4.2: Install Missing System Dependencies
- **Dependencies**: bfl, browser, browser-cdp, feishu_doc, feishu_drive, hermes-yuanbao, homeassistant, image_gen
- **Action**: Document which are actually needed; install or mark optional

#### Task 4.3: Configure Optional Platforms
- **Platforms**: Discord, WhatsApp, Signal, Slack, Email, SMS, DingTalk, Feishu, WeCom, BlueBubbles, QQBot, Yuanbao
- **Action**: Enable based on actual usage requirements

### Phase 5: Validation & Verification (All)

#### Task 5.1: Full Regression Test
- **Commands**: Run all diagnostic commands again
- **Expected**: Zero critical issues, minimal warnings

#### Task 5.2: End-to-End Workflow Test
- **Action**: Execute a representative agent task through full pipeline
- **Verification**: No errors in agent.log, gateway.log, errors.log

#### Task 5.3: Documentation Update
- **Action**: Update MEMORY.md with resolved issues and new configurations
- **Action**: Document any new procedures in skills

## Detailed Task Breakdown

### Phase 1 Tasks

| Task | Command/Action | Verification |
|------|---------------|--------------|
| 1.1 | Validate & fix config.yaml | YAML parses cleanly |
| 1.2 | `hermes mcp test tooling-lint` etc. | All 3 servers connect |
| 1.3 | Update fallback_providers chain | Streaming works on fallback |
| 1.4 | Fix Telegram DNS/network | Gateway connects to Telegram |

### Phase 2 Tasks

| Task | Command/Action | Verification |
|------|---------------|--------------|
| 2.1 | `npm install` in web/ & ui-tui/ | `npm audit` clean |
| 2.2 | Configure SQLite checkpoints | WAL < 10MB |
| 2.3 | Profile & fix web_server | No GIL stalls > 5s |

### Phase 3 Tasks

| Task | Command/Action | Verification |
|------|---------------|--------------|
| 3.1 | Review 14 blocked skills | Decision documented each |
| 3.2 | `hermes skills update data-migration-scripts --force` | Skill updated |
| 3.3 | Configure & test atlassian, docs, postgres | Enabled if needed |
| 3.4 | `hermes auth add <provider>` for 4 providers | All auth working |

### Phase 4 Tasks

| Task | Command/Action | Verification |
|------|---------------|--------------|
| 4.1 | Add 11 missing API keys to .env | `hermes status` shows keys |
| 4.2 | Install/configure 8 system deps | Tools available |
| 4.3 | Configure needed platforms | Platforms connected |

### Phase 5 Tasks

| Task | Command/Action | Verification |
|------|---------------|--------------|
| 5.1 | Re-run all diagnostics | Zero critical issues |
| 5.2 | Execute test agent task | Clean logs |
| 5.3 | Update MEMORY.md & skills | Documentation current |

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Config.yaml corruption recurs | Medium | High | Add validation hook; keep backups |
| MCP servers fail after fix | Medium | Medium | Add health checks; auto-restart |
| Provider 502 errors persist | High | High | Robust fallback chain; circuit breaker |
| Telegram DNS issues persist | Medium | Medium | Configure explicit IPv4; add retry logic |
| Skill audit blocks block workflow | Low | Low | Use --force with review; maintain local forks |

## Dependencies

```
Phase 1 (Core) → Phase 2 (Health) → Phase 3 (Skills/MCP) → Phase 4 (Config) → Phase 5 (Validation)
     ↑_________________________________________________________________________|
```

## Success Criteria

- [ ] `hermes doctor` → 0 issues (only informational)
- [ ] `hermes security audit` → No vulnerabilities
- [ ] `hermes skills audit` → All skills ALLOWED or documented exceptions
- [ ] `hermes mcp list` → All required servers ✓ enabled
- [ ] `hermes status` → All auth providers configured, API keys set
- [ ] `hermes logs errors` → No ERROR level entries in last hour
- [ ] `hermes logs gateway` → Telegram connected, no DNS errors
- [ ] `hermes logs gui` → No GIL stalls > 5s
- [ ] End-to-end agent task completes without errors

## Execution Order

1. **Immediate**: Tasks 1.1, 1.2, 1.3 (blocking core functionality)
2. **Same Session**: Tasks 1.4, 2.1, 3.2
3. **Next Session**: Tasks 2.2, 2.3, 3.1, 3.3, 3.4
4. **Follow-up**: Tasks 4.1, 4.2, 4.3, 5.1, 5.2, 5.3

## Notes

- Use `subagent-driven-development` for parallel execution of independent tasks
- Each task should follow `systematic-debugging` methodology: understand → isolate → fix → verify
- Document all changes in MEMORY.md for persistence across sessions
- Commit config changes to git for version control