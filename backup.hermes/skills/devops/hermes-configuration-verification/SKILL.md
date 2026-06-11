---
name: hermes-configuration-verification
title: "Hermes Configuration Verification & Fast Path Setup"
description: "Verify existing Hermes configurations, validate provider health, and use the fast path for partial/existing setups. When Hermes is already partially configured, skip full 5-phase setup and jump to targeted verification + report generation."
author: Alexa
created: 2026-05-26
version: 1.0
triggers:
  - "verify Hermes configuration"
  - "check Hermes health"
  - "add provider to Hermes"
  - "verify GitHub Copilot fallback"
  - "Hermes configuration verification"
  - "fast path setup"
  - "quick Hermes setup"
---

# Hermes Configuration Verification & Fast Path Setup

## When to Use

- When performing hermes configuration verification operations or tasks
- When managing hermes configuration verification infrastructure or configurations
- When automating or debugging hermes configuration verification workflows
- **Triggers**: "set up devops/hermes-configuration-verification", "configure hermes configuration verification", "debug hermes configuration verification issue"

## Workflow

### Phase 1: Setup

Verify prerequisites and ensure required dependencies are available.

### Phase 2: Execute

Perform the hermes configuration verification operations following the instructions in this skill.

### Phase 3: Verify

Confirm the output meets expectations and address any issues.

### Phase 4: Document

Record any changes, configurations, or decisions made during execution.

## Overview

## User Preferences & Conventions
- User: Alexa — Windows 11. Prefer PowerShell for local commands (do not assume git-bash). Provide PowerShell equivalents for OS-specific steps when the working environment is Windows.
- Response style: concise, action-first. Prefer short numbered steps and checklists; avoid long explanatory prose unless explicitly requested. When corrected on response style or formatting, embed the preference into skill guidance so future runs honour it by default.
- Local moves: prefer PowerShell Move-Item over git clone for local file operations. Require explicit approval before performing git commits or any destructive operation.
- Execution preference: run full end-to-end when all phases/tasks/subtasks are provided. Pause only on blocking errors or when an explicit checkpoint is requested.
- Active model: verify the active model at the start of verification — current known active model: gpt-5-mini (switched from claude-sonnet-4.5). If the model differs, record it in the report and surface it in the header.
- Toolset tip: when subagent or tool counts approach the soft tool-limit, prefer using execute_code scripts instead of delegate_task to avoid loading large toolsets and reduce failure surface. Add an explicit 'how-to' example in references/how-to-use-execute_code.md showing a replaceable script pattern and the hermes_tools helpers to use (web_search, terminal, read_file, write_file).
- Backup policy: do NOT create backup files (.bak) when updating existing configuration or prompt files. Respect the local policy file at C:\\Users\\Alexa\\AppData\\Local\\hermes\\.hermes_policies (key: [backup].enabled = false). Automation scripts should overwrite in-place unless explicitly instructed to keep a backup.
- Validation: when verification runs, include the validate_memories.py check (scripts/validate_memories.py) and report its exit code and output in the verification report.

See references/session-2026-05-26-notes.md for session-specific details (profiles created, tool-count fix, changed files, validation scripts, cron job).

This skill handles **configuration verification** and the **fast path** for Hermes Agent when the system is already partially configured. Use it when you need to:

- Verify an existing Hermes installation is healthy
- Add a new provider (e.g., GitHub Copilot) to an existing setup
- Check MCP server status without full 5-phase setup
- Create verification reports for partially-configured systems

**When to use**: 
- After Hermes updates
- Adding a new provider to existing config
- Post-migration verification
- Confirming system health before work
- Testing fallback chains

**Key outcome**: Comprehensive verification report showing provider health, MCP server status, tool availability, and fallback chain operability — typically in 2-3 minutes.

---

## Prerequisites

- [ ] Hermes v0.14+ already installed
- [ ] `config.yaml` exists and is v22+
- [ ] At least one provider configured (OpenRouter, OpenCode Zen, etc.)
- [ ] hermes doctor available (`hermes --version` succeeds)

---

## Fast Path Workflow (2-3 minutes)

Use this workflow when:
- Config already exists and version is v24+
- Some MCP servers are already enabled
- You're adding a provider or verifying health (not doing fresh setup)

### Step 1: Baseline Health Check

```bash
hermes doctor
```

**What to look for:**
- ✅ Python Environment — should all pass
- ✅ Configuration Files — should show v24+ 
- ✅ API Connectivity — all checks passed
- ✅ Tool Availability — 19+ toolsets enabled
- ⚠️ Known warnings (optional tools, unneeded providers) are OK

**If hermes doctor fails:**
- Note which section failed (e.g., "Auth Providers")
- See **Troubleshooting** section below
- Do NOT proceed until the failure is understood

### Step 2: Verify MCP Servers

```bash
hermes mcp list
```

**Expected output**:
- 7-8 servers listed
- At least 6-7 showing ✅ enabled
- 200+ total tools across servers
- No connection errors

**Acceptable variations:**
- docker-gateway disabled on Windows (by design — WSL2 limitation)
- Unused servers disabled (video, homeassistant, etc.)

**If server is offline:**
- Run: `hermes mcp test <server-name>`
- Check: `~/.hermes/logs/gateway.log`
- Restart: `hermes mcp restart`

### Step 3: Check All Configured Providers

```bash
hermes auth list
```

**Verify**:
- All listed providers have credentials in the pool
- Primary provider (in config.yaml) shows at least 1 token
- Fallback providers all have credentials
- No provider shows "API unreachable"

**For each provider:**
```bash
hermes config show | grep "provider: <name>"
```

### Step 4: Verify Toolsets

```bash
hermes tools list
```

**Check**:
- ✅ Core toolsets enabled: web, browser, terminal, file, code_execution, vision, image_gen
- ✅ Productivity: skills, todo, memory, session_search, messaging
- ✅ Advanced: delegation, cronjob, clarify, moa
- ⚠️ Optional disabled: video, homeassistant, spotify (acceptable)

**Note**: Tool changes take effect on `/reset` (new session), not mid-conversation.

### Step 5: Create Verification Report

Document the results in a summary (text or markdown). Include:

**Report structure** (see template):

```
HERMES CONFIGURATION VERIFICATION REPORT
Date: [YYYY-MM-DD]
Status: ✅ [PASS/FAIL]

PRIMARY PROVIDER:
  Provider: [name]
  Model: [model-id]
  Status: ✅ [operational/error]

FALLBACK CHAIN:
  #1 [provider] — [model]
  #2 [provider] — [model]
  Status: ✅ [all operational/X failed]

MCP SERVERS:
  [name] — ✅ enabled, [tool-count] tools
  Total: X/8 enabled, [total-tools] tools

TOOLSETS:
  Core: [X/Y] enabled
  Optional: [status]

SYSTEM HEALTH:
  ✅ hermes doctor: ALL PASSING
  ✅ API connectivity: 27/27 checks passed
  ✅ Security: 0 advisories

SIGN-OFF:
  Verified on: [date-time]
  Status: ✅ READY FOR [PRODUCTION/TESTING/DEVELOPMENT]
```

---

## Full Path vs Fast Path

| Scenario | Use |
|----------|-----|
| **Fresh Hermes install on new machine** | Full 5-phase (hermes-complete-setup) |
| **Adding provider to existing setup** | Fast Path (this skill) |
| **Post-update verification** | Fast Path (this skill) |
| **Migrating between major versions** | Full 5-phase (hermes-complete-setup) |
| **Confirming system health before work** | Fast Path (this skill) |
| **Troubleshooting provider failures** | Fast Path + Troubleshooting section |

---

## Common Tasks

### Verify GitHub Copilot Fallback

After configuring GitHub Copilot as a fallback provider:

```bash
# 1. Check credential is present
hermes auth list | grep -i copilot

# 2. Verify it's in fallback chain
hermes config show | grep -A 5 "fallback_providers"

# 3. Test it manually (optional)
hermes chat --provider github-copilot -q "Hello"

# 4. Document in report
```

### Verify OpenCode Zen Primary

```bash
# 1. Check config
hermes config show | grep -A 3 "model:"

# 2. Verify endpoint
hermes config show | grep "base_url"

# 3. Test connectivity
hermes chat -q "What model are you?" -Q

# 4. Confirm in report
```

### Check Fallback Chain Is Working

```bash
# Primary model (first in chain)
hermes chat -q "test" --model <primary-model>

# Secondary model (manual override)
hermes chat -q "test" --provider <secondary-provider>

# Verify config has fallback_providers list
hermes config show | grep -B 2 -A 10 "fallback_providers"
```

### Add a New Provider Quickly

1. **Get credentials** → set env var or use `hermes login`
2. **Verify connection** → `hermes doctor` (includes provider connectivity)
3. **Add to fallback** → Edit config.yaml or use `hermes model`
4. **Verify chain** → Run fast path (steps 1-5 above)
5. **Document** → Create verification report

---

## Pitfalls & Solutions

### Pitfall 1: Assuming "Already Configured" Systems Need No Verification

**Symptom**: "Config is from yesterday, so it must be fine" → silence → mystery errors hours later.

**Reality**: Between sessions:
- API endpoints can change
- Provider auth can expire
- MCP servers restart and may fail to come back online
- Credentials rotate in the pool
- Tool availability updates

**Solution**: Always run `hermes doctor` (takes 15 seconds).

**Prevention**: Make verification a habit before starting work. One quick check prevents hours of troubleshooting.

### Pitfall 2: Not Checking Fallback Chain

**Symptom**: Primary provider fails, but fallback doesn't trigger → work stops.

**Cause**: Fallback not configured or credentials missing for secondary provider.

**Solution**:
```bash
# Verify fallback_providers list exists
hermes config show | grep "fallback_providers" -A 10

# Check credentials for each fallback
hermes auth list | grep <fallback-provider-name>

# Test manually if unsure
hermes chat --provider <fallback-provider> -q "test"
```

### Pitfall 3: MCP Server Offline After Update

**Symptom**: `hermes mcp list` shows server as ✗ disabled or error.

**Cause**: MCP server process crashed or endpoint changed.

**Solution**:
```bash
# Test specific server
hermes mcp test <server-name>

# Check logs
tail -20 ~/.hermes/logs/gateway.log | grep <server-name>

# Restart all MCP servers
hermes mcp restart

# Verify
hermes mcp list
```

### Pitfall 4: Provider Endpoint Misconfiguration

**Symptom**: `hermes doctor` shows "API unreachable" for a provider.

**Cause**: 
- Typo in base_url (most common: missing `/chat/completions` segment)
- API key expired or invalid
- Provider changed endpoint

**Solution**:
```bash
# View current config for provider
hermes config show | grep -A 5 "<provider-name>"

# Verify base_url is correct (check docs)
# Common pitfall: https://opencode.ai/zen/v1 (WRONG — missing path)
# Correct: https://opencode.ai/zen/v1/chat/completions (RIGHT)

# Test with curl (if endpoint is HTTP/HTTPS)
curl -X POST "https://api.example.com/v1/chat/completions" \
  -H "Authorization: Bearer *** \
  -d '{"messages": [{"role": "user", "content": "test"}]}'
```

### Pitfall 5: Tool Availability Changes After Config Update

**Symptom**: Tool you used yesterday is gone today.

**Cause**: Toolset disabled in config or MCP server offline.

**Solution**:
```bash
# Check toolset status
hermes tools list | grep <tool-name>

# If disabled, enable it
hermes tools enable <toolset>

# Changes take effect on /reset (new session)
```

---

## Verification Checklist

Use this before marking "verification complete":

```
✅ Health
  [ ] hermes doctor runs and shows no critical errors
  [ ] Python 3.11+ detected
  [ ] Config version v22+
  [ ] Security: 0 advisories

✅ Providers
  [ ] Primary provider API key present
  [ ] All fallback providers have credentials
  [ ] hermes doctor shows all configured providers responding
  [ ] At least 2-3 providers in fallback chain

✅ MCP Servers
  [ ] 6+ servers enabled (7/8 with docker-gateway)
  [ ] At least 200+ tools available
  [ ] No "connection error" messages
  [ ] hermes mcp list succeeds in <5 sec

✅ Toolsets
  [ ] Core toolsets enabled: web, browser, terminal, file, code_execution
  [ ] 19+ toolsets enabled total
  [ ] Optional tools (video, spotify, etc.) status documented

✅ Credentials & Auth
  [ ] hermes auth list shows all providers in pool
  [ ] No provider showing "not logged in" (if required)
  [ ] Credential rotation configured (if using pools)

✅ System Health
  [ ] API connectivity: 27/27 checks passed
  [ ] No timeout warnings
  [ ] Tool discovery: <1 second
  [ ] Session store operational (115+ sessions indexed)

✅ Report
  [ ] Verification report created with timestamp
  [ ] Provider chain documented
  [ ] MCP server status recorded
  [ ] System health summary included
  [ ] Sign-off with "READY FOR [PRODUCTION/TESTING]"
```

---

## Quick Commands

```bash
# Verify everything (single command)
hermes doctor

# List MCP servers
hermes mcp list

# Check provider credentials
hermes auth list

# View toolset status
hermes tools list

# View current config
hermes config show

# Test specific provider
hermes chat --provider <name> -q "test"

# View session history
hermes sessions list

# Check memory
/memory  (in interactive chat)
```

---

## Related Skills

- **[hermes-complete-setup](./hermes-complete-setup)** — Full 5-phase setup (use for fresh installs)
- **[hermes-agent](./hermes-agent)** — CLI reference, provider setup, troubleshooting

---

## Support

- `hermes doctor` — Comprehensive health check
- `hermes config show` — View current configuration
- `~/.hermes/logs/` — Gateway and error logs
- https://hermes-agent.nousresearch.com/docs/user-guide/configuration

---

**Skill Version**: 1.0  
**Last Updated**: May 26, 2026  
**Status**: Production Ready  
**Author**: Alexa

