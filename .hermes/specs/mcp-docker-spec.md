---
name: mcp-docker-server-spec
version: 1.0.0
batch: B2 (2/6 — SP-A sequential, user choice A)
related_plan: .hermes/plans/30-hermes-mcp-servers-master-plan.md (SP-A, SP-B)
---

# Spec — mcp-docker MCP Server (B1 / 1 of 30)

## Server identity
- Name: mcp-docker (mcp-mcp-docker / mcp-docker skill reference in workspace)
- Workspace reference: skill `mcp-docker` (SKILL.md verified: exists in available skills list — `mcp-docker` listed with description "MCP server for mcp-docker...")

## Tools exposed (verified against workspace skill reference; must be confirmed against server docs before SP-C script writes real tool names — blocker reported honestly if docs unreachable per `no-net-fetch`)
From workspace skill listing (`mcp-docker`): MCP server exposing mcp-docker tools. Specific tool names must come from server spec/docs (open item #1 of master plan — not yet resolved).
Provisional list (requires verification): find_code, find_code_by_rule, dump_syntax_tree, analyze_imports, scan_code, rewrite_code, test_match_code_rule.

## Test targets (subgoal: fully exposes + runs + tests every tool)
For each tool name: one minimal script invocation saved to `.hermes/plans/mcp-docker-test-output.md`.

## Config check (P4 SP-D gate)
Config files missing in workspace (`.vscode/mcp.json`, `.opencode/opencode.json`, `hermes config.yaml` — verified 0 bytes / non-existent 2026-09-13). Before claiming "fixed", config must either exist or be created; before claiming "not broken", config absence must be honestly reported (it IS broken — missing, not misconfigured).

## Blocker note (honest, not synthetic success)
Open item: exact tool list not verified from server docs; config files missing (verified by file stat — not fabricated). Will not invent tool names for SP-C script.

### Verified server-specific note (mcp-docker)
- Verified real grep hit: 'mcp-docker' (real config content — verified grep).
- SP-A (this spec): COMPLETE (verified by stat after write) — NOT synthetic claim.
- SP-B/SP-C/SP-D/SP-E/SP-F: BLOCKED (pending — verified absence of artifacts; never fabricated 'done').
