# OOB Debug Session — MCP Servers + opencode agents (2026-09-11)

Instruction: `hermes mcp test tooling-lint/tooling-config/python-quality`, `opencode agent list`, systematic-debugging fix all findings.

## Before → After

| Check | Before | After |
|---|---|---|
| `hermes mcp test tooling-lint` | ✗ Connection closed (~22s) | ✓ Connected (4.5s), 8 tools |
| `hermes mcp test tooling-config` | ✗ Connection closed (~17s) | ✓ Connected (4.7s), 10 tools |
| `hermes mcp test python-quality` | ✗ Connection closed (~17s) | ✓ Connected (8.8s), 6 tools |
| `opencode agent list` | ✗ "Expected object, got [...] tools" (tdd-refactor) | ✓ exit 0, full agent list |
| `pip check` (myvenv) | 8 conflicts | ✓ "No broken requirements found." |

## Root Causes (investigate → fix → verify)

### 1. MCP servers: fastmcp↔mcp version break
- **Evidence**: `from fastmcp import FastMCP` → `ImportError: cannot import name 'request_ctx' from 'mcp.server.lowlevel.server'`. fastmcp 2.10.6 (requires `mcp>=1.10.0`, no upper cap) uses API removed in mcp 2.0.0.
- **Fix (class)**: `pip install --force-reinstall "fastmcp-slim[server]"` → fastmcp 4.0.3 + mcp 2.2.0. `FastMCP` construction verified; all 3 server scripts import OK; `hermes mcp test` all pass.
- fastmcp 4.x `[server]` extra is the documented server-support path (fastmcp's own install hint).

### 2. myvenv hermes-agent pin violations (surfaced by the reinstall)
- pydantic 2.13.5→2.13.4, python-dotenv 1.2.3→1.2.2, pywin32 312→`>=306,<312`, rich 15.0.0→14.3.3, websockets 17.1→15.0.1, cryptography 50.0.1→50.0.0, packaging 26.3→26.0. `pip check` clean after.

### 3. opencode agents: deprecated `tools` array form
- **Evidence**: schema error on .agent.md frontmatter. Official docs (opencode.ai/docs/agents): "`tools` is **deprecated**... setting tools to true/false; schema now expects object".
- **Fix (class)**: `scripts/fix_opencode_agent_tools.py` converted array → object map (`tool: true`) in all 17 affected `.opencode/agents/*.agent.md` files. `opencode agent list` exit 0.

### 4. Stray python `cspell 0.0.1a1` package
- tooling-lint shells out to npm cspell (repo-scoped node_modules/.bin); python pkg unused → uninstalled (cleared `pip check`).

## Files
- `scripts/fix_opencode_agent_tools.py` — reusable agent-frontmatter fixer
- `scripts/model_benchmark_2026.py` — G3 runner (this session)
- `.opencode/agents/*.agent.md` — 17 files updated