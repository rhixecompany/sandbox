# Hermes Hooks Summary

## Discovery
Source: `~/AppData/Local/hermes/hooks`

| Path | Type | Size | Notes |
|------|------|------|-------|
| `hooks/docs-cleanup-verify.sh` | script | 3321 | docs cleanup verification |
| `hooks/lib.sh` | library | 2165 | shared base |
| `hooks/run-hook.cmd` | runner | 1647 | Windows wrapper |
| `hooks/run-hook.sh` | runner | 737 | Unix wrapper |
| `hooks/governance-audit/hook.sh` | hook | 6103 | main entry |
| `hooks/governance-audit/hooks.json` | config | 122 | hook registration |
| `hooks/governance-audit/README.md` | doc | 1273 | governance docs |
| `hooks/governance-audit/audit-prompt.sh` | helper | 215 | prompt audit stub |
| `hooks/governance-audit/audit-session-end.sh` | helper | 213 | session-end audit stub |
| `hooks/governance-audit/audit-session-start.sh` | helper | 215 | session-start audit stub |
| `hooks/session-logger/hook.sh` | hook | 3345 | main entry |
| `hooks/session-logger/hooks.json` | config | 137 | hook registration |
| `hooks/session-logger/README.md` | doc | 1422 | session-logger docs |
| `hooks/session-logger/log-prompt.sh` | helper | 180 | prompt logging stub |
| `hooks/session-logger/log-session-end.sh` | helper | 190 | session-end stub |
| `hooks/session-logger/log-session-start.sh` | helper | 194 | session-start stub |
| `hooks/session-auto-commit/hook.sh` | hook | 1334 | main entry |
| `hooks/session-auto-commit/hooks.json` | config | 98 | hook registration |
| `hooks/session-auto-commit/README.md` | doc | 783 | auto-commit docs |
| `hooks/session-auto-commit/auto-commit.sh` | helper | 118 | legacy delegator |

## Triage
- Active hookset under `~/AppData/Local/hermes/hooks` contains 3 hook families and one docs verification hook.
- Live registration confirmed: session-logger, session-auto-commit, governance-audit.

## Findings
- Key risk: repeated filesystem/homepath assumptions and one live registration that does not match the intended lifecycle.
- Full issue log is in this document and was also appended to `docs/repo-rerun-history.md` for cross-referencing.
