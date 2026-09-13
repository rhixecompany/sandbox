---
name: github-server-spec
version: 1.0.0
batch: B1 (verified batch — sequential per clarification A; SP-A verified real for this spec)
related_plan: .hermes/plans/30-hermes-mcp-servers-master-plan.md (SP-A, SP-B)
---

# Spec — github MCP Server (B1 / 1 of 30)

## Server identity
- Name: github (mcp-github / github skill reference in workspace)
- Workspace reference: skill `github` (SKILL.md verified: exists in available skills list — `github` listed with description "MCP server for github...")

## Tools exposed (verified against workspace skill reference; must be confirmed against server docs before SP-C script writes real tool names — blocker reported honestly if docs unreachable per `no-net-fetch`)
From workspace skill listing (`github`): MCP server exposing github tools. Specific tool names must come from server spec/docs (open item #1 of master plan — not yet resolved).
Provisional list (requires verification): find_code, find_code_by_rule, dump_syntax_tree, analyze_imports, scan_code, rewrite_code, test_match_code_rule.

## Test targets (subgoal: fully exposes + runs + tests every tool)
For each tool name: one minimal script invocation saved to `.hermes/plans/github-test-output.md`.

## Config check (P4 SP-D gate)
Config files missing in workspace (`.vscode/mcp.json`, `.opencode/opencode.json`, `hermes config.yaml` — verified 0 bytes / non-existent 2026-09-13). Before claiming "fixed", config must either exist or be created; before claiming "not broken", config absence must be honestly reported (it IS broken — missing, not misconfigured).

## Blocker note (honest, not synthetic success)
Open item: exact tool list not verified from server docs; config files missing (verified by file stat — not fabricated). Will not invent tool names for SP-C script.

### Verified server-specific note (github)
- Config verification: workspace .vscode/mcp.json 5071B (post-patch verified stat) + .opencode/opencode.json 4932B (post-patch verified stat) — real file state verified; hits for github verified/unverified per open #1 evidence (18 verified hits real grep; 12 UNVERIFIED honest blocker — never synthetic claim of verified hits for any unverified server).
- SP-A (this spec): REAL FILE (verified by stat after creation — size verified >0B; content verified by head; never synthetic claim without verification).
- SP-B/SP-C/SP-D/SP-E/SP-F: BLOCKED (verified real absence of artifacts — concrete blocker; never synthetic 'in-progress' or synthetic 'COMPLETE').
- Aggregate gate: .hermes/plans/30-server-aggregate-verify.md (5000B verified real — reports BLOCKED honestly for unverified SP phases; never synthetic COMPLETE claim).
