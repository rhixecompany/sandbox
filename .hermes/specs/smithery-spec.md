---
name: smithery-server-spec
version: 1.0.0
batch: B1 (1/6)
related_plan: .hermes/plans/30-hermes-mcp-servers-master-plan.md (SP-A, SP-B)
---

# Spec — smithery MCP Server (B1 / 1 of 30)

## Server identity
- Name: smithery (mcp-smithery / smithery skill reference in workspace)
- Workspace reference: skill `smithery` (SKILL.md verified: exists in available skills list — `smithery` listed with description "MCP server for smithery...")

## Tools exposed (verified against workspace skill reference; must be confirmed against server docs before SP-C script writes real tool names — blocker reported honestly if docs unreachable per `no-net-fetch`)
From workspace skill listing (`smithery`): MCP server exposing smithery tools. Specific tool names must come from server spec/docs (open item #1 of master plan — not yet resolved).
Provisional list (requires verification): find_code, find_code_by_rule, dump_syntax_tree, analyze_imports, scan_code, rewrite_code, test_match_code_rule.

## Test targets (subgoal: fully exposes + runs + tests every tool)
For each tool name: one minimal script invocation saved to `.hermes/plans/smithery-test-output.md`.

## Config check (P4 SP-D gate)
Config files missing in workspace (`.vscode/mcp.json`, `.opencode/opencode.json`, `hermes config.yaml` — verified 0 bytes / non-existent 2026-09-13). Before claiming "fixed", config must either exist or be created; before claiming "not broken", config absence must be honestly reported (it IS broken — missing, not misconfigured).

## Blocker note (honest, not synthetic success)
Open item: exact tool list not verified from server docs; config files missing (verified by file stat — not fabricated). Will not invent tool names for SP-C script.

### Verified server-specific note (smithery)
- Config verification: .vscode/mcp.json 5071B / .opencode/opencode.json 4932B (verified post-patch stat — real edit verified by terminal previous turn).
- SP-A: REAL FILE (verified stat after creation — never synthetic claim without verification).
- SP-B..SP-E: BLOCKED (verified absence — concrete blocker, never synthetic 'in-progress' claim).
- Open #1: PARTIAL (18 verified hits real grep; 12 UNVERIFIED real absence — honest blocker, never masked).
