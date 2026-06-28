---
author: Alexa
description: Operational troubleshooting for Hermes Agent resource exhaustion, checkpoint
  issues, MCP connection failures, and provider failover diagnostics. Guides diagnosis;
  destructive actions require explicit user approval.
license: MIT
name: hermes-system-maintenance
tags: null
title: Hermes System Maintenance
version: 1.0.0

---
# Hermes System Maintenance & Recovery

Use this skill when Hermes Agent is experiencing resource exhaustion, checkpoint/memory issues, MCP connection failures, or provider failover problems. This skill DIAGNOSES and GUIDES RECOVERY but does not execute destructive actions without user approval.

## Triggers

- **Memory exhaustion**: `Memory at 2,200/2,200 chars. Adding... would exceed limit`
- **Disk full**: `Out of diskspace`, `No space left on device`
- **Checkpoint failures**: `git gc` errors, `sha1 file write error`
- **MCP connection drops**: `connection lost (attempt N/5)`, `initial connection failed`
- **Provider auth chain**: All fallback providers returning 429/402/401
- **Log file bloat**: rotated log files (*.log.1, *.log.2) accumulating

## Diagnosis Phase

### 1. Resource Bottleneck Identification

**Disk usage:**
```bash
df -h /c/Users/Alexa | tail -1
du -sh /c/Users/Alexa/AppData/Local/hermes/{logs,sessions,checkpoints,skills} 2>/dev/null
ls -lhS /c/Users/Alexa/AppData/Local/hermes/logs/*.log 2>/dev/null | head -5
```

**Memory state:**
```bash
wc -c /c/Users/Alexa/AppData/Local/hermes/memories/{MEMORY.md,USER.md} 2>/dev/null
# Compare against limits: memory_char_limit=2200, user_char_limit=1375
```

**MCP servers:**
```bash
grep "mcp_servers:" /c/Users/Alexa/AppData/Local/hermes/config.yaml -A 30
```

### 2. Log Analysis

**Check errors.log for patterns:**
- `initial connection failed (attempt N/3)` → MCP server command missing or file not found
- `connection lost (attempt N/5)` → Transient network/async exception (usually recovers)
- `Out of diskspace` → Checkpoint git operations failing
- `Memory at X/2200` → Agent memory store exhausted
- `429` → Rate limit hit (provider unhealthy 600s)
- `402/401` → Auth or billing issue (provider unhealthy 600s)

## Recovery Procedures

### Memory Exhaustion (MEMORY.md or USER.md at limit)

**Diagnosis:**
- Run: `wc -c /c/Users/Alexa/AppData/Local/hermes/memories/{MEMORY.md,USER.md}`
- If at 2200 or 1375 chars respectively, memory store is blocked

**Recovery approach:**
1. Read current entries to identify which are stale or verbose
2. Use `memory action=remove old_text="<entry>" target=memory` to drop oldest/least-relevant
3. Consolidate remaining entries (combine related facts into one)
4. Verify new capacity: `wc -c` should show <80% utilization

**Pitfall:** Memory entries cannot be fully read from logs. Always use `memory_char_limit` comparison to estimate.

### Disk Exhaustion (99%+ full)

**Root cause diagnosis:**
- Check if Hermes-owned folders (logs, checkpoints) are bloated, or system-wide (user data)
- Hermes folders typically: logs ~5MB, sessions ~8KB, checkpoints ~30MB, skills ~20MB
- Total Hermes: ~60MB max (excluding user profiles/sessions)

**Safe cleanup (Hermes-owned only):**
- Clear rotated logs: `rm -f /c/Users/Alexa/AppData/Local/hermes/logs/*.log.*`
- Truncate current logs: `cat /dev/null > /c/Users/Alexa/AppData/Local/hermes/logs/{errors,agent,mcp-stderr}.log`
- **Checkpoints reset requires user approval** (destructive, clears session history)

**If still critical after Hermes cleanup:**
- Disk issue is system-wide (user data, browser cache, Downloads, Recycle Bin)
- User must clean their own files or extend partition
- Hermes cannot safely clean user-owned data

### Checkpoint Corruption (git gc failures)

**Diagnosis:**
- Error: `fatal: sha1 file 'X' write error. Out of diskspace` or `gc is already running`
- Usually tied to disk full or locked process

**Recovery:**
1. Verify disk has free space (see Disk Exhaustion above)
2. If disk ok but git still fails: `gc is already running` → wait for other git process to finish, or ask user to kill pid
3. **Checkpoint reset (destructive):** Requires user approval to delete `/c/Users/Alexa/AppData/Local/hermes/checkpoints` and reinit

**Pitfall:** Checkpoint data is persistent. Deleting it loses session recovery history. Only reset if corruption is confirmed and unrecoverable.

### MCP Connection Failures

**docker-gateway** (most common):
- Verify not in config: `grep "docker-gateway" /c/Users/Alexa/AppData/Local/hermes/config.yaml`
- If present, user must remove (protected file, agent cannot edit)
- Status: Already removed in current config ✓

**context7** (occasional reconnects):
- Pattern: `connection lost (attempt 1-5)` then `giving up`
- Transient; retries with exponential backoff work
- Check network connectivity; verify `CONTEXT7_API_KEY` set in config
- Normal to see occasional reconnects in logs

**filesystem/playwright MCP** (WinError 2, WinError 193):
- WinError 2 = file not found (binary missing or PATH issue)
- WinError 193 = not a valid Win32 app (architecture mismatch or shell incompatibility)
- Verify binary exists: `which mcp-server-filesystem` or `which playwright-mcp`
- If missing: User reinstalls via package manager

### Provider Failover Chain Issues

**Diagnosis:**
```bash
# Check primary and fallback config
grep -E "^model:|^  provider:" /c/Users/Alexa/AppData/Local/hermes/config.yaml | head -5
grep -A 10 "^fallback_providers:" /c/Users/Alexa/AppData/Local/hermes/config.yaml
```

**Interpret error codes from errors.log:**
- `429` = Rate limit (quota exceeded). Provider marked unhealthy 600s. Requires upgrade or wait.
- `402` = Insufficient credits (billing issue). Requires account action.
- `401` = Auth failure (wrong key, expired token, model deprecated).

**Recovery prioritization:**
1. Primary: Use GitHub Copilot (copilot provider) — most reliably funded
2. Fallback: gpt-5-mini on same provider if available
3. Disable problematic providers in config to avoid retry overhead (avoid OpenCode/OpenRouter/Gemini if out of credits)
4. Update API keys if known stale: ask user via `hermes auth`

**Pitfall:** Provider keys are redacted in logs for security. Cannot verify key correctness from logs alone.

### Credential Pool Seed Failures

**Symptom:** Repeated DEBUG logs on every Hermes startup:
```
Qwen OAuth token seed failed: Qwen CLI credentials not found. Run 'qwen auth qwen-oauth' first.
```
(or similar for `nous`, `copilot`, `minimax-oauth`, `xai-oauth`)

**Root cause:** The credential pool's `_seed_from_singletons()` has hardcoded branches for specific providers. When Hermes config.yaml includes a provider block that maps to one of these (e.g. `qwen-acp: base_url: acp://qwen`), the pool tries to seed credentials by reading a file or env that doesn't exist.

**Fix:**
1. Identify the triggering provider: `grep -B2 -A2 "qwen\|acp://" ~/AppData/Local/hermes/config.yaml`
2. Verify it's unused (not in active model, fallback chain, or routing)
3. Remove the provider block via sed: `sed -i '13,15d' ~/AppData/Local/hermes/config.yaml` (adjust line numbers)
4. Verify removal: `grep "qwen" ~/AppData/Local/hermes/config.yaml` → empty

**Note:** `qwen auth` was REMOVED in Qwen v0.17.0. The command no longer exists. If Qwen is configured for OpenRouter (API key-based), it works headless without OAuth credentials. See `references/acp-provider-credential-pool.md` for full technical trace and provider-specific details.

### Browser Tool Vulnerabilities

**Diagnosis:**
- `hermes doctor` reports "Browser tools (agent-browser) has N npm vulnerabilities"
- These are in the hermes-agent Node.js dependencies

**Recovery:**
```bash
cd /c/Users/Alexa/AppData/Local/hermes/hermes-agent && npm audit fix
```
- This auto-fixes vulnerabilities in agent-browser, electron, and related packages
- After fix, `hermes doctor` should show "no known vulnerabilities"
- If `npm audit fix` doesn't resolve all, run `npm audit` to see remaining issues

### Memory Tool Drift (Issue #26045)

**Diagnosis:**
- `memory()` calls fail with "file on disk has content that wouldn't round-trip"
- `.bak.*` files appear in `~/AppData/Local/hermes/memories/`
- Happens after `patch` tool modifies MEMORY.md or USER.md

**Recovery:**
1. Delete `.bak.*` files: `rm -f ~/AppData/Local/hermes/memories/*.bak.*`
2. Skip memory updates this session — the file content is already correct
3. Memory tool resyncs automatically on next session start
4. Do NOT retry `memory()` — all attempts will fail until resync

## Preventive Maintenance

- **Weekly:** Check disk free space (`df -h`). Target >10% free.
- **Monthly:** Review memory usage (`wc -c MEMORY.md`). Keep <50% of limit.
- **After major tasks:** Verify logs aren't bloated (`ls -lh logs/*.log`). Archive if >100MB.
- **Quarterly:** Check MCP connection stability in errors.log. Note any patterns.
- **After hermes update:** Run `hermes doctor --fix` and `npm audit fix` in hermes-agent.

## Workflow

### Phase 1: Setup

Verify prerequisites and ensure required dependencies are available.

### Phase 2: Execute

Perform the hermes system maintenance operations following the instructions in this skill.

### Phase 3: Verify

Confirm the output meets expectations and address any issues.

### Phase 4: Document

Record any changes, configurations, or decisions made during execution.

## Overview

Hermes System Maintenance is a skill for handling hermes system maintenance tasks and automation workflows. Use this skill when you need to perform hermes system maintenance operations efficiently.


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

After recovery:

```bash
# 1. Memory below limit
wc -c /c/Users/Alexa/AppData/Local/hermes/memories/MEMORY.md
# Should be <1760 chars (80% of 2200)

# 2. Disk with breathing room
df -h /c/Users/Alexa | tail -1
# Should show >=5% free (ideally >20%)

# 3. MCP servers active
grep "enabled: true" /c/Users/Alexa/AppData/Local/hermes/config.yaml | grep -c "true"
# Should be 4+ (filesystem, sequential-thinking, playwright, context7)

# 4. Logs fresh, not bloated
ls -lh /c/Users/Alexa/AppData/Local/hermes/logs/*.log | grep -v ".log\.[0-9]"
# Should show recent modtimes, sizes <100MB

# 5. Provider config valid
grep "^model:" /c/Users/Alexa/AppData/Local/hermes/config.yaml
# Should show primary provider (copilot) with model (claude-haiku-4.5)
```

## Related Hermes Commands

- `hermes gateway status` — Check gateway health and uptime
- `hermes auth` — Re-authenticate provider credentials
- `hermes config show` — Display full config (values redacted)
- `hermes logs tail errors` — Stream errors.log in real-time

## Key Paths

- Config: `/c/Users/Alexa/AppData/Local/hermes/config.yaml`
- Memory: `/c/Users/Alexa/AppData/Local/hermes/memories/MEMORY.md` (2200 char limit)
- Logs: `/c/Users/Alexa/AppData/Local/hermes/logs/` (errors.log, agent.log, mcp-stderr.log, gateway.log)
- Checkpoints: `/c/Users/Alexa/AppData/Local/hermes/checkpoints/` (git-backed session snapshots)
- Scripts home: `/c/Users/Alexa/AppData/Local/hermes/scripts/` (relative path for cron jobs)

## When to Use


- When you need to perform Hermes System Maintenance operations or tasks
- When managing Hermes System Maintenance infrastructure or configurations
- When automating or debugging Hermes System Maintenance workflows
- **Triggers**: "hermes system maintenance" required for a project

