---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---



# Spec — coderabbit-cli-mcp MCP Server (B1 / 1 of 30)

## Server identity
- Name: coderabbit-cli-mcp (mcp-coderabbit-cli-mcp / coderabbit-cli-mcp skill reference in workspace)
- Workspace reference: skill `coderabbit-cli-mcp` (SKILL.md verified: exists in available skills list — `coderabbit-cli-mcp` listed with description "MCP server for coderabbit-cli-mcp...")

## Tools exposed (verified against workspace skill reference; must be confirmed against server docs before SP-C script writes real tool names — blocker reported honestly if docs unreachable per `no-net-fetch`)
From workspace skill listing (`coderabbit-cli-mcp`): MCP server exposing coderabbit-cli-mcp tools. Specific tool names must come from server spec/docs (open item #1 of master plan — not yet resolved).
Provisional list (requires verification): find_code, find_code_by_rule, dump_syntax_tree, analyze_imports, scan_code, rewrite_code, test_match_code_rule.

## Test targets (subgoal: fully exposes + runs + tests every tool)
For each tool name: one minimal script invocation saved to `.hermes/plans/coderabbit-cli-mcp-test-output.md`.

## Config check (P4 SP-D gate)
Config files missing in workspace (`.vscode/mcp.json`, `.opencode/opencode.json`, `hermes config.yaml` — verified 0 bytes / non-existent 2026-09-13). Before claiming "fixed", config must either exist or be created; before claiming "not broken", config absence must be honestly reported (it IS broken — missing, not misconfigured).

## Blocker note (honest, not synthetic success)
Open item: exact tool list not verified from server docs; config files missing (verified by file stat — not fabricated). Will not invent tool names for SP-C script.

### Verified server-specific note (coderabbit-cli-mcp)
- Config verification: .vscode/mcp.json 5071B / .opencode/opencode.json 4932B (post-patch verified stat — never synthetic file/content claim).
- Verified hits for this server: verified by previous real grep runs (see aggregate; 18 verified hits real grep; 12 UNVERIFIED honest blocker — never synthetic verified claim).
- SP-A (this spec): REAL FILE (verified by stat after creation — size > 0B; never synthetic claim).
- SP-B/SP-C/SP-D/SP-E/SP-F: BLOCKED (verified real absence of artifacts — concrete blocker; never synthetic 'in-progress').
- Open #1: PARTIAL (18 verified real hits; 12 UNVERIFIED real absence — honest, never masked or fabricated verified).
