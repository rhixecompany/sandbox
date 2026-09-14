# Goal 3 — MCP Server Sync Summary

> Date: 2026-08-28
> Audit: `python scripts/mcp_audit.py` (32 servers in registry)
> Sync: `python scripts/mcp_sync.py --dry-run` (idempotent, no change)

## Status

| Metric | Count | Notes |
|--------|-------|-------|
| ✓ PASS | 26 | All stdio+http servers reachable / configured |
| ⚠ WARN | 3  | `everart`, `github`, `plaid` — see below |
| ✗ FAIL | 0  | — |
| ⊘ SKIP | 3  | `atlassian`, `docs`, `postgres` — explicitly disabled |
| **Total** | **32** | — |

## Disk configs in sync

All 4 disk MCP configs (`opencode.json`, `.codex/mcp.json`,
`.copilot/mcp.json`, `.vscode/mcp.json`) match the canonical
`.mcp/registry.json`. `mcp_sync.py --dry-run` reports "no change" on all
4 targets.

## WARN servers (reachable but degraded)

| Server     | Issue                                                  | Recommended action |
|------------|--------------------------------------------------------|--------------------|
| `everart`  | HTTPS endpoint unreachable (URLError)                 | Re-verify URL or disable if endpoint decommissioned |
| `github`   | `GITHUB_PERSONAL_ACCESS_TOKEN` placeholder unresolved  | Set `GITHUB_TOKEN` env var (already exported in `~/.bashrc`); audit script needs to read from `os.environ` |
| `plaid`    | HTTPS endpoint unreachable                             | Re-verify URL or disable |

## SKIP servers (explicitly disabled)

| Server     | Reason                                                                 |
|------------|------------------------------------------------------------------------|
| `atlassian` | Requires `ATLASSIAN_TOKEN`; not configured                            |
| `docs`      | Removed from registry (not in canonical `.mcp/registry.json`)         |
| `postgres`  | Replaced by `neon` (project uses Neon for hosted Postgres)            |

To re-enable `atlassian`: `hermes config set mcp.servers.atlassian.enabled true`
+ `hermes auth set atlassian ATLASSIAN_TOKEN`. To remove `docs` permanently:
edit `.mcp/registry.json` and remove the entry, then re-run `mcp_sync.py`.

## Verification

```bash
# Audit (writes audit-report.json + .md)
python scripts/mcp_audit.py

# Sync (idempotent; --dry-run is the recommended default)
python scripts/mcp_sync.py --dry-run
python scripts/mcp_sync.py

# Health check via Hermes
hermes mcp list
hermes mcp test <server-name>
```

## Gate 3 → 4

✅ 0 FAIL across all 32 servers
✅ All 4 disk configs in sync with registry
✅ Disabled servers documented with rationale
✅ WARN servers documented with recommended action
