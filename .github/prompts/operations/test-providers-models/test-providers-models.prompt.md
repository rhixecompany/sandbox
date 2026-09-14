---
title: "Test Providers and Models (OpenRouter / OpenCode-Zen)"
description: "Validate configured provider chains and free-model endpoints; run against each free model discovered via openrouter.ai web research; output verified results with real model responses."
version: 1.0.0
id: test-providers-models-v1
profile: default
author: Hermes Agent
skills: [using-superpowers, web-research-pipeline, repo-research-pipeline, user-communication-preferences, multi-file-change-protocol]
tools: [terminal, web_search, web_extract, web_fetch, browser_exec, file_read, file_write]
---

# Test Providers and Models Workflow

## Context
- Providers configured: openrouter (base_url: https://openrouter.ai/api/v1; default: nvidia/nemotron-3-ultra-550b-a55b:free), opencode-zen (default: deepseek-v4-flash-free), nous (fallback), gemini, ollama-cloud, deepseek.
- Free models discovered via web-search (`https://openrouter.ai/models?variant=free`): verified by real page fetch.
- Fallback chain: openrouter → nous → opencode-zen (verified by config.yaml / .env / opencode.json).
- User identity: Alexa (default/adminbot profile); authorization FULL; workspace ~/Desktop/SandBox (branch clean-development).
- Security: no synthetic session IDs / capabilities / quality scores / rankings; .env 3334 B protected; identity/DRY preserved; 26 vulnerability findings + 41 parsing errors preserved honestly.

## Execution Steps
1. Fetch `https://openrouter.ai/models?variant=free` (agent-browser or web-fetch).
2. Convert HTML response to markdown; extract model names/URLs/descriptions.
3. For each free model in report: run provider test via `test-providers-models.prompt.md` execution (call openrouter endpoint with model parameter).
4. Collect real responses (success/failure/status); verify by real file content/checksum.
5. Generate `./plans/` + `./specs/` + `results/` artifacts with verified outputs.
6. Request approvals for crud batches.

## Verification Gates
- Real page fetched (verified by content hash / file size).
- Markdown conversion artifact verified.
- Model list verified by real web content (not synthetic names).
- Response artifacts contain real API outputs (verified by content check — no fabricated results).
- No hidden errors; all blockers reported (503/service errors, missing tokens, connection failures) preserved honestly.

## Non-Functional Constraints
- Communication: concise, table-first, direct, action-first, verification-first, no filler.
- DRY: cross-reference provider/model info from `.hermes.md` / `.env` / `opencode.json` / `.vscode/mcp.json`; don't duplicate identity/routing.
- Multi-file protocol: sequential execution after Subgoal A; approvals requested; subagent delegated.
- Security: preserve vulnerability findings; don't suppress parsing errors; don't expose .env; don't fabricate artifacts.
