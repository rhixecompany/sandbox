# Hermes Log Triage Techniques

Techniques verified during a full log triage on Windows 11 (Hermes desktop app, ~15 MB logs).

---

## 1. Pattern-Frequency Analysis

The fastest path from raw logs to triaged issues is **frequency-sorted grep** on `errors.log`:

```bash
# Count and sort error signatures by frequency
grep -iE "WARN|ERROR|FAIL" "$LOCALAPPDATA/hermes/logs/errors.log" \
  | sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}[T ].*?(WARN|ERROR|FAIL)[^:]*: //' \
  | cut -c1-80 \
  | sort | uniq -c | sort -rn | head -30
```

**Why this works:** `errors.log` is the compressed signal across all sessions. Frequency immediately separates:
- **High-count** (30-150×) → usually noise (check_fn, Telegram, reconnection loops)
- **Medium-count** (5-30×) → investigate (lock issues, transient failures)
- **Low-count** (1-5×) → real failures or one-off events

**Cross-reference with current state:** A high-count error doesn't mean it's still broken. Always validate current state:
```bash
# Is the service actually down NOW?
grep "mcp-docker" "$LOCALAPPDATA/hermes/logs/mcp-stderr.log" | tail -3
# Or was it fixed yesterday?
tail -3 "$LOCALAPPDATA/hermes/logs/errors.log" | grep -c "mcp-docker"
```

---

## 2. Parallel Log Reading Strategy

Read all 4 Hermes log layers in parallel and cross-reference timestamps:

```bash
echo "=== errors.log (aggregated warnings) ==="
tail -20 "$LOCALAPPDATA/hermes/logs/errors.log"
echo "=== mcp-stderr.log (MCP server state) ==="
tail -20 "$LOCALAPPDATA/hermes/logs/mcp-stderr.log"
echo "=== gui.log (UI/WebSocket/GIL) ==="
tail -10 "$LOCALAPPDATA/hermes/logs/gui.log"
echo "=== agent.log (runtime activity) ==="
tail -10 "$LOCALAPPDATA/hermes/logs/agent.log"
```

---

## 3. Additional Verified Patterns

Patterns confirmed during a July 2026 triage session, not yet in the SKILL.md classification table:

| Log Pattern | Count | Classification | Action |
|-------------|-------|---------------|--------|
| `GITHUB_TOKEN is not supported: Classic Personal Access Tokens (ghp_*)` | 67× | **Fixed** — `.env` already has `#GITHUB_TOKEN` commented out | Verify `.env` fix holds; no action |
| `check_fn check_read_terminal_requirements returned False` | 18× | **Noise** — TUI session mode, terminal tools available via other paths | None |
| `check_fn check_close_terminal_requirements returned False` | 18× | **Noise** — same as above | None |
| `RuntimeError: The current task is not holding this lock` | 6-18× | **Upstream bug** — `mcp/client/auth/oauth2.py` + `anyio._core._synchronization.py` lock release during async generator cancellation | Not config-fixable; upstream Hermes/anyio |
| `ws write slow (loop stalled >10.0s) peer=127.0.0.1:56576` | 8× | **Noise** — GIL pressure on Windows Python 3.11; transient | Monitor; if persistent, reduce concurrent tool calls |
| `MCP server 'smithery' failed after 5 reconnection attempts, parking; will self-probe every 300s` | 13× | **Noise/self-healing** — Smithery OAuth registry unreachable; parks and retries | None; or disable if not used |
| `action-skills-update.log` (51 bytes) | 1 | **Expected** — action stub, no content | None |
| `action-tools-post-setup.log` (204 bytes) | 1 | **Expected** — action stub, tools working | None |

---

## 4. Fix Categories from This Session

### Fix: mcp-docker Disabled
**Symptom:** `MCP server 'mcp-docker' connection lost: CancelledError` on every session.
**Root cause:** Docker Desktop installed but daemon not running. MCP Docker server can't connect to the Docker named pipe.
**Fix:** `hermes config set mcp.servers.mcp-docker.enabled false`
**Verify:** `python3 -c "import yaml; cfg=yaml.safe_load(open(r'...config.yaml')); print(cfg['mcp']['servers']['mcp-docker']['enabled'])"` → `False`

### Fix: Skill Name Collisions from .restore-backups
**Symptom:** `Ambiguous skill name 'subagent-driven-development': 4 skills match` on `skill_view`/`skill_manage`.
**Root cause:** `.restore-backups/official-optional-*/` contains duplicate SKILL.md files that Hermes index picks up.
**Fix:** Move backup dir out of the skills tree:
```bash
mv "$LOCALAPPDATA/hermes/skills/.restore-backups" "$LOCALAPPDATA/hermes/skills/.restore-backups.DISABLED"
```
**Verify:** Zero 4-way collisions — `hermes profile list` and `skill_view` no longer get ambiguous matches.

---

## 5. Pending Queue Cleanup

When `memory.write_approval` is enabled, stale entries accumulate in `~/AppData/Local/hermes/pending/memory/`. Check and purge:

```bash
ls "$LOCALAPPDATA/hermes/pending/memory/" 2>/dev/null | wc -l
# If 10+ entries, most are stale — purge entries older than 24h
# Keep recent ones from current session
```

If the `apply_pending_skills.py` script already processed the skills pending queue, clean up the temp dir:
```bash
rm -rf "$LOCALAPPDATA/hermes/pending/skills/" 2>/dev/null
rm -rf "C:/path/to/_pending_skills_inbox/" 2>/dev/null
```
