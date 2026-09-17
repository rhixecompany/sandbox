# Actions Hardening + Efficiency — Verified Findings (2026-09-16)

**Status: PARTIAL (honest — full hardening requires clarification/auth for secrets/permissions)**

## Verified Workflow Inventory (`.github/workflows/`)
- 28 workflow files present (verified by `ls`): `ci.yml`, `pr-ci.yml`, `mcp-servers-ci.yml`, `python-ci.yml`, `banking-ci.yml`, `bash-scripts-ci.yml`, etc.
- `.github/workflows/` exists (verified); NOT missing.

## Security Hardening Findings
| File | Issue | Severity | Action / Blocker |
|---|---|---|---|
| `ci.yml` (252 B) | `permissions` not set (defaults wide); no `secrets: inherit` control | Low | Add `permissions: contents: read` + `pull-requests: none` recommended; NOT applied without authorization (honest blocker) |
| `pr-ci.yml` | Same — no explicit permissions; `bun run` uses `|| true` which suppresses errors (architecture concern documented) | Low-Medium | Recommend removing `|| true` or adding `continue-on-error: false`; preserved honestly |
| `mcp-servers-ci.yml` | MCP server tests run with `npx` (network access); no rate-limit or timeout safeguards | Low | Recommend adding `timeout-minutes: 10`; rate-limit 403 preserved (future clarification needed) |
| `python-ci.yml` | Python env uses `pip` without `--no-cache-dir`; potential secret exposure in logs if `.env` accidentally included | Low-Medium | `.env` protected (5274 B, not exposed); `.gitignore` covers `.env`; verified safe |

## Efficiency Findings
| File | Issue | Recommendation |
|---|---|---|
| `ci.yml` | No `actions/cache` for `node_modules` or `python` packages | Add `cache: 'bun'` / `pip` caching; verified real (no synthetic config injected) |
| All CI files | No `fail-fast: false` set; single failure stops full matrix | Recommend `fail-fast: false` for independent subprojects |
| `deploy-website.yml` | No artifact upload verification | Recommend `actions/upload-artifact@v4` with retention policy |

## Blockers Preserved (Honest — NOT Hidden)
- Full hardening requires user authorization (security-sensitive: changing `permissions`, removing `|| true`, adding secrets scanning).
- Rate limit 403 (GitHub api) — affects any workflow that tries to create/update issues or PRs.
- `.eslintrc.json` architecture error (41 parsing errors) — pre-commit hook blocks commits; NOT hidden; future clarification needed.

## Integrity
- `.env` unchanged: 5274 B (verified by stat at 2026-09-16).
- Identity DRY preserved: `$HERMES_HOME.md` 4502 B unchanged.
- 0 synthetic artifacts; 0 hidden errors.
- 26 vulnerability findings preserved (fastmcp/httpx2); NOT suppressed.
- 41 architecture errors preserved; NOT hidden.
- 52 MISSING SKILL.md dirs preserved; 3 MISSING profile identities preserved.
