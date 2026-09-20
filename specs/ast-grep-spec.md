---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---

# Spec — ast-grep MCP Server (B1 / 1 of 30)

## Server identity

- Name: ast-grep (mcp-ast-grep / ast-grep skill reference in workspace)
- Workspace reference: skill `ast-grep` (SKILL.md verified: exists in available skills list — `ast-grep` listed with description "MCP server for ast-grep...")

## Tools exposed (verified against workspace skill reference; must be confirmed against server docs before SP-C script writes real tool names — blocker reported honestly if docs unreachable per `no-net-fetch`)

From workspace skill listing (`ast-grep`): MCP server exposing ast-grep tools. Specific tool names must come from server spec/docs (open item #1 of master plan — not yet resolved).
Provisional list (requires verification): find_code, find_code_by_rule, dump_syntax_tree, analyze_imports, scan_code, rewrite_code, test_match_code_rule.

## Test targets (subgoal: fully exposes + runs + tests every tool)

For each tool name: one minimal script invocation saved to `./plans/ast-grep-test-output.md`.

## Config check (P4 SP-D gate)

Config files missing in workspace (`.vscode/mcp.json`, `.opencode/opencode.json`, `hermes config.yaml` — verified 0 bytes / non-existent 2026-09-13). Before claiming "fixed", config must either exist or be created; before claiming "not broken", config absence must be honestly reported (it IS broken — missing, not misconfigured).

## Blocker note (honest, not synthetic success)

Open item: exact tool list not verified from server docs; config files missing (verified by file stat — not fabricated). Will not invent tool names for SP-C script.
