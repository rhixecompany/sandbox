---
name: acpx-agent-routing
title: ACPX Agent Routing
description: "Route coding tasks to the optimal ACPX agent (Qwen Code, OpenCode, Copilot CLI) based on task type."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ACPX, Agent-Routing, Multi-Agent, Orchestration]
    related_skills: [qwen-code, opencode, copilot-cli, dispatching-parallel-agents]
---

# ACPX Agent Routing

Route coding tasks to the optimal agent based on task type. Uses three ACPX-enabled agents:

| Agent | Version | Install | ACP Mode | Auth | Status |
|-------|---------|---------|----------|------|--------|
| Qwen Code | 0.17.0 | `bun add -g qwen-code` | `qwen --acp` | OpenRouter API key | ✅ Verified |
| OpenCode | 1.15.12 | `npm i -g opencode-ai` | `opencode acp` | Copilot/Google/Zen | ✅ Verified |
| Copilot CLI | 1.0.56 | `npm i -g @github/copilot` | Built-in ACP via config | GH_TOKEN or OAuth | ✅ Verified |


## When to Use

- Use this skill when working with acpx agent routing tasks
- Triggered by: `acpx-agent-routing` related operations

## Agent Routing Table

| Task Type | Primary Agent | Fallback | Why |
|-----------|--------------|----------|-----|
| Quick explain/suggest | Copilot CLI | Qwen Code | Fastest for small queries |
| Code generation | OpenCode | Qwen Code | Best code quality, provider-agnostic |
| Refactoring | OpenCode | Copilot CLI | Full tool access |
| Code review | OpenCode (plan agent) | Copilot CLI | Read-only analysis |
| Large codebase exploration | Qwen Code | OpenCode | Optimized for Qwen models |
| Test generation | OpenCode | Qwen Code | Best test patterns |
| Architecture/design | OpenCode (plan agent) | Qwen Code | Structured thinking |
| Debugging | OpenCode | Qwen Code | Interactive debugging |
| Prompt engineering / text analysis | OpenCode | Copilot CLI | Best structural analysis for prompt quality |
| File analysis / verification | Copilot CLI | Qwen Code | Read-only, fastest, cannot write files |
| Bulk text conversion | ❌ None reliable | ❌ None reliable | ACPX agents degrade file content — use execute_code or direct tools instead |
| PR review | Copilot CLI | OpenCode | GitHub-native context |

> **File I/O warning:** ACPX agents are unreliable for file writes. Qwen Code may overwrite files with degraded content (e.g. wrapping text in code blocks). OpenCode may analyze completely but never write the output. Copilot CLI is safest because it's read-only. For any task that requires creating or modifying files, handle the edits yourself with patch/write_file after getting analysis from an ACPX agent.

## Recommended Models

| Agent | Model | Notes |
|-------|-------|-------|
| Qwen Code | `OpenRouter \| openai/gpt-oss-120b:free` | Free tier, works headless with `--yolo` |
| OpenCode | `opencode/big-pickle` | Default model, same as Hermes agent |
| Copilot CLI | `auto` | Auto-selects best available model. No `--model` flag needed. |

## ACPX Delegation Patterns

### Primary: via acpx exec (ACPX binary, v0.10.0+)

```bash
# Qwen Code via ACPX
acpx --approve-all --timeout 30 qwen exec 'Implement user auth middleware'

# OpenCode via ACPX
acpx --approve-all --timeout 60 opencode exec 'Add rate limiting to API routes'

# Copilot CLI via ACPX (auto model)
acpx --approve-all --timeout 30 copilot exec 'Explain this shell command: find . -name *.py -exec wc -l {} +'

# OpenCode plan agent via ACPX
acpx --approve-all --timeout 60 opencode exec 'Review auth module for security issues'

# OpenCode with specific model via ACPX
acpx --approve-all --timeout 60 opencode exec 'Refactor auth module' --model opencode/claude-sonnet-4-6
```

### Fallback: direct CLI per provider

```bash
# Qwen Code (direct)
QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo 'Implement user auth middleware'

# OpenCode (direct — requires --model)
opencode run 'Add rate limiting to API routes' --model opencode/big-pickle

# Copilot CLI (direct)
copilot -p 'Explain this shell command: find . -name *.py -exec wc -l {} +'
```

### From Hermes via ACP providers

```yaml
# In hermes config, use provider directly:
# model.provider: copilot-acp    # For Copilot CLI (default)
# model.provider: qwen-code      # For Qwen Code
```

> **Note:** `opencode-acp` is not supported as a Hermes ACP provider — no ACP client handler exists for `acp://opencode` in the Hermes agent runtime. Use OpenCode via `acpx opencode exec` or direct CLI instead.

### Parallel Agent Execution

```bash
# Run two agents in parallel via ACPX
acpx --approve-all --timeout 120 opencode exec 'Fix issue #101' &
acpx --approve-all --timeout 120 qwen exec 'Add tests for module-b' &
wait
```

## Procedure

1. **Identify task type** using the routing table above
2. **Select primary agent** — start with the recommended agent
3. **Use ACPX exec** — `acpx --approve-all --timeout <N> <agent> exec '<prompt>'`
4. **Monitor progress** — use `process(action="poll")` for background tasks via `&` / `wait`
5. **Verify output** — test generated code, review changes
6. **Fallback** — if primary agent fails, switch to fallback

## Pitfalls

- Copilot CLI has weekly rate limits (~50 premium requests/week). When exhausted, fall back to OpenCode or Qwen Code.
- **Copilot always uses `auto` model** — no `--model` flag. ACPX handles model selection automatically.
- OpenCode ACPX exec uses default model; for specific models use `acpx --model opencode/<name>`.
- Qwen Code direct CLI requires `--yolo` for non-interactive headless mode. Suppress warning with `QWEN_CODE_SUPPRESS_YOLO_WARNING=1`. ACPX exec handles this automatically.
- Model names for OpenCode require `opencode/` prefix (e.g., `opencode/big-pickle`).
- OpenCode and Qwen Code both use bun-pty on Windows — may be unavailable, but CLI still works.
- Qwen Code does NOT use DashScope OAuth — configured via OpenRouter API key. `qwen auth qwen-oauth` was removed in v0.17.0.
- Copilot CLI 1.0.56+ — use `copilot -p "prompt"` for one-shot, not `gh copilot` (deprecated Oct 2025).
- `opencode-acp` is NOT a valid Hermes ACP provider — no client handler exists. Use `acpx opencode exec` or direct terminal instead.
- **ACPX agents cannot reliably write files.** Qwen Code degrades content (wraps in code blocks), OpenCode analyzes but often doesn't write, Copilot is read-only. For any task that produces output files: use the ACPX agent for analysis/recommendations, then write/update files yourself with patch or write_file.
- **OpenCode cost-guard banner pollutes NDJSON output.** When running `opencode run "prompt"` via ACPX, OpenCode prints a preamble like `[cost-guard] Active — limit: $20.0000 | warn at: 80% | mode: warn` before the actual NDJSON response. This causes parse warnings but doesn't break the response. Workaround: pipe through `tail -n +2` or accept the warnings as cosmetic.

## Read-Only vs Read-Write Task Split Pattern

When a task needs both analysis AND file creation/updating:

```
1. ACPX agent (analysis phase) → review, analyze, recommend
2. YOU (implementation phase) → write_file, patch to apply recommendations
3. ACPX agent (verification phase) → Copilot CLI to verify result is well-formed
```

This split prevents data loss from agent file-I/O failures while still leveraging agent intelligence.

## Verification Checklist

- [ ] All three agents installed and responsive
- [ ] ACPX binary available (`acpx --version` should show 0.10.0+)
- [ ] All three agents smoke tested via `acpx <agent> exec '...'`
- [ ] Agent routing table complete for common task types
- [ ] Fallback chain defined for each task type
- [ ] Model recommendations documented per agent
- [ ] Parallel execution tested without conflicts
