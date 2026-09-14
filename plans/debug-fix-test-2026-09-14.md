---
name: debug-fix-test-failed-mcp-servers
version: 1.0
status: running
destructive_approval: FULL (per clarification 2026-09-13)
---
# Plan — Debug, Fix, Test Failed Hermes MCP Servers

> Patient-teacher mode: explain each concept clearly with examples before fixing.
> Protocol: LOAD (skills verified) → PLAN (this file) → VERIFY (evidence review) → EXECUTE (fixes + tests) → GATE (honest results, no hidden errors).

## Evidence (Real — from `./plans/debug-run-logs.md` 53152 B + session audit)

| Server | Config Command | Real Failure (exit stdout) | Category |
|---|---|---|---|
| playwright | `npx -y @playwright/mcp@0.0.78` | `Connection failed (32184ms)` (timeout) | Config/version/handshake |
| doist/todoist-ai | `https://ai.todoist.net/mcp` (HTTP, OAuth) | `Server returned an error response` (13428ms) | External/auth/network |
| io.github.basicmachines-co/basic-memory | `uvx --from basic-memory@0.23.2 basic-memory mcp` | `Connection closed` (21906ms); manual test shows `FastMCP 4.0.0b1` banner; `mcp-stderr.log` shows `unexpected extra argument(s)` error | Handshake/version/command syntax |
| bun run check | — | Exit 1; 41 parsing errors (`No tsconfigRootDir` in `.codex/` + `.copilot/` nested scopes) | Architecture concern (honest preservation) |
| hermes security audit | — | Exit 1; 26 real vulnerabilities (`fastmcp==2.10.6` CRITICAL GHSA-vv7q-7jx5-f767; HIGH `httpx2==2.7.0`) | Security (honest preservation) |

## Fix Strategy (One fix per server; ≤2 attempts; blocker after 2)

### Playwright (SP-A)
- Try: Update to latest compatible version (`@playwright/mcp`) in `.vscode/mcp.json`; verify `npx -y` resolves correctly.
- Gate: `hermes mcp test playwright` returns non-timeout OR honest blocker documented.

### Doist/todoist-ai (SP-B)
- Try: Verify URL and auth config; check if endpoint requires OAuth token from `TAVILY_API_KEY`-style env or different auth.
- Gate: If external server error persists after 2 checks → BLOCKER (honest, not hidden).

### Basic-memory (SP-C)
- Try: Verify `uvx --from` syntax matches FastMCP 4.0.0b1 handshake (`protocolVersion` `2024-11-05` or newer); adjust `.vscode/mcp.json` args if syntax conflict found in `mcp-stderr.log`.
- Gate: Either handshake succeeds OR blocker documented with the exact `unexpected extra argument(s)` error preserved.

### Bun check / parsing errors (SP-D — architecture concern)
- Fix applied already (2026-09-13 `.eslintrc.json` 70 B, `parserOptions.project` = `./tsconfig.json`, `tsconfigRootDir` = `.`). Does NOT suppress remaining 41 errors (nested `.codex`/`.copilot` scope conflict — preserved honestly).
- Gate: Re-run `bun run check`; document exit 1 + 41 errors honestly; no synthetic PASS claimed.

## Verification Gates (Every claim backed by terminal/file evidence)
- [ ] SP-A: `hermes mcp test playwright` executed; result saved to `./plans/playwright-test-result.md`
- [ ] SP-B: `hermes mcp test doist/todoist-ai` executed; result saved; blocker or fix documented
- [ ] SP-C: `hermes mcp test io.github.basicmachines-co/basic-memory` executed; `mcp-stderr.log` inspected; result saved to `./plans/basic-memory-test-result.md`
- [ ] SP-D: `bun run check` re-run; exit code + error count saved honestly
- [ ] Integrity: `.env` 3334 B unchanged (verified); 0 synthetic artifacts; 0 hidden errors; identity/routing preserved
- [ ] Aggregate table entry added to `./plans/30-server-aggregate-verify.md` (or equivalent) for these 3+ servers

## Deliverables (Real files — verified by `ls -la` + `cat` before claiming)
1. `./plans/debug-fix-test-2026-09-14.md` (this plan) — verified
2. `./plans/playwright-test-result.md` — real stdout/exit
3. `./plans/basic-memory-test-result.md` — real stdout + `mcp-stderr.log` reference
4. `./plans/doist-todoist-test-result.md` — real result (success or blocker)
5. Updated `.vscode/mcp.json` (only if syntax/config change needed — verified by diff)
6. `./specs/debug-subgoal-final-verification.md` (gate checklist with real file references)
