---
name: parallel-mcp-install
title: Install and Validate Parallel MCP Servers in Hermes
description: Register Parallel Search and Parallel Task Streamable HTTP MCP servers
  in the active Hermes Agent harness, preserve credential boundaries, validate discovered
  tools, and begin implementation only after all gates pass.
version: 1.0.0
license: MIT
author: Alexa
toolsets: null
skills: null
formatter: default
plan: null
dependencies:
- skill:using-superpowers
- skill:user-communication-preferences
- skill:hermes-mcp
- skill:smithery-ai-cli
- skill:verification-before-completion
tags:
- agents
- ai-assistant
- api
- backend
- frontend
- mcp
- ml
- prompts
- workflow
trigger: /parallel-mcp-install
metadata:
  hermes: {}
scripts: []
---

# Parallel MCP Installation and Validation Workflow

## Goal

Install and validate these two remote Streamable HTTP MCP servers in the MCP client harness that is actually running the agent:

| Server | Endpoint | Authentication | Required tools |
| --- | --- | --- | --- |
| Parallel Search | `https://search.parallel.ai/mcp` | No auth by default | `web_search`, `web_fetch` |
| Parallel Task | `https://task-mcp.parallel.ai/mcp` | OAuth preferred; API-key fallback | `createDeepResearch`, `createTaskGroup`, `getStatus`, `getResultMarkdown` |

The active harness in this workspace is Hermes Agent CLI. Do not install these servers into Claude Code, Codex, Cursor, VS Code Copilot, or another client unless the runtime check proves that client is the active host.

## Source References

Use these as authoritative Smithery workflow references:

- <https://smithery.ai/docs>
- <https://smithery.ai/docs/concepts/cli>
- <https://smithery.ai/docs/use/connect>

Smithery concepts used here:

- MCP connections have explicit IDs and connection states: `connected`, `auth_required`, `input_required`, and `error`.
- `auth_required` requires a human browser step using the returned setup URL.
- Connected tools must be listed before calling them.
- API keys belong in headers or environment variables, never in source-controlled prompts or config files.
- Smithery CLI is a separate integration surface; for a permanent Hermes-native server, use Hermes MCP configuration.

## Non-Negotiable Security Rules

1. Never print, repeat, log, commit, or write a literal Parallel API key.
2. Never ask the user to paste an API key into chat.
3. Do not configure auth for Parallel Search unless the server explicitly requires it.
4. Prefer Hermes OAuth for Parallel Task when supported.
5. If OAuth is unavailable, configure the client to read `PARALLEL_API_KEY` from the process environment using a supported interpolation mechanism; otherwise tell the user to export it before launching Hermes. Do not invent interpolation support.
6. Inspect config output only with secrets redacted or filtered.
7. Do not use Smithery as a proxy when direct Hermes HTTP MCP configuration is available unless the user specifically requests Smithery-managed connections.

## Phase 1 — Identify the Active Harness

Run these checks before changing configuration:

```bash
hermes profile list
hermes mcp list
hermes mcp --help
hermes config path
hermes config env-path
```

Record:

- Active client/harness and profile
- MCP registration mechanism
- Config path and environment-file path
- Whether the harness supports HTTP/StreamableHTTP and OAuth

If the active harness is not Hermes Agent, stop and use that client’s native MCP mechanism instead. Never configure a different client by assumption.

## Phase 2 — Register Parallel Search

Use the Hermes CLI, not direct YAML editing:

```bash
hermes mcp add parallel-search \
  --url https://search.parallel.ai/mcp \
  --connect-timeout 45
```

When prompted whether auth is required, select no auth. Enable every discovered Search tool. If the endpoint returns a connection error, capture the status and stop before changing auth settings.

Expected result:

- Server saved as `parallel-search`
- HTTP/StreamableHTTP connection succeeds
- `web_search` and `web_fetch` are discovered and enabled

## Phase 3 — Register Parallel Task

Prefer the Hermes OAuth path:

```bash
hermes mcp add parallel-task \
  --url https://task-mcp.parallel.ai/mcp \
  --auth oauth \
  --connect-timeout 45
```

If Hermes prints an authorization URL:

1. Tell the user to complete the browser authorization.
2. Do not request or handle a raw API key in chat.
3. Resume or retry the Hermes MCP registration after authorization.
4. Enable all four discovered tools.

Expected result:

- Server saved as `parallel-task`
- Auth mode is OAuth 2.1 PKCE, or an explicitly documented environment-backed header fallback
- Four required tools are discovered and enabled

## Phase 4 — Validate Configuration and Connectivity

Run all checks:

```bash
hermes mcp list
hermes mcp test parallel-search
hermes mcp test parallel-task
hermes config check
```

Verify without displaying credentials:

```bash
grep -n -A 12 -E '^  parallel-(search|task):' "$(hermes config path)"
```

Required assertions:

- `parallel-search` is enabled and reports auth `none`.
- `parallel-task` is enabled and reports OAuth or an environment-backed bearer configuration.
- Search exposes `web_search` and `web_fetch`.
- Task exposes `createDeepResearch`, `createTaskGroup`, `getStatus`, and `getResultMarkdown`.
- No literal key appears in `config.yaml`, `.env`, workspace files, prompts, logs, or generated reports.
- `hermes config check` completes without a new MCP configuration error.

## Phase 5 — Runtime Reload Gate

Hermes discovers MCP tools during startup. Configuration changes are not guaranteed to affect the current conversation.

Tell the user exactly which action is required:

- CLI/TUI: start a fresh Hermes session or use `/reload-mcp` if supported; use `/reset` when toolset changes are also involved.
- Gateway: restart the gateway if the server must be available to gateway sessions.
- Other clients: follow that client’s documented MCP reload/restart behavior.

After reload, verify the tools are present in the live tool registry. Do not claim that the current session can call them until this gate passes.

## Phase 6 — Begin Implementation

Only after Phases 1–5 pass:

1. Use Parallel Search for web discovery and source retrieval.
2. Use Parallel Task for explicit research/task-group operations.
3. For long-running tasks, call `getStatus` while pending and call `getResultMarkdown` only after completion.
4. Record server name, tool name, request purpose, status, and verification evidence.
5. Keep all results and generated artifacts free of credentials.
6. If any tool call fails, preserve the exact non-secret error, diagnose the root cause, and do not silently substitute a different client or server.

## Failure Handling

| Condition | Action |
| --- | --- |
| Active harness cannot be identified | Stop; report the observed runtime and ask for the correct client only if necessary |
| Search returns `auth_required` | Stop and ask the user to complete the provided browser flow; do not add a key |
| Task returns `auth_required` | Complete OAuth in the browser, then retry connection |
| Task returns `input_required` | Inspect the server’s required configuration schema; use OAuth or environment-backed auth only |
| Connection times out | Increase `connect_timeout` once, retry once, then report the blocker |
| Tool discovery is incomplete | Do not begin implementation; inspect server status and enabled-tool selection |
| Literal credential appears in config/logs | Stop, redact/remove it through the approved credential path, and report the exposure without repeating it |
| Config changes do not appear live | Restart/reload the active Hermes harness, then retest |

## Completion Checklist

- [ ] Active harness identified from live runtime state
- [ ] Correct native client configuration used
- [ ] Parallel Search added without auth
- [ ] Parallel Task added with OAuth or environment-backed auth
- [ ] No literal API key written anywhere
- [ ] Both servers pass `hermes mcp test`
- [ ] Required tools discovered and enabled
- [ ] `hermes config check` passes
- [ ] Runtime reload/restart requirement reported
- [ ] Live tool availability verified after reload
- [ ] Implementation begins only after all gates pass

## Completion Report

Return a compact table:

| Field | Result |
| --- | --- |
| Active harness/profile | `<value>` |
| Search server | `<connected/error>` |
| Search tools | `<list>` |
| Task server | `<connected/auth_required/error>` |
| Task tools | `<list>` |
| Credential handling | `OAuth` / `PARALLEL_API_KEY env` / `none` |
| Restart/reload | `<required action>` |
| Implementation status | `<started/blocked>` |
| Blocker | `<none or exact non-secret evidence>` |

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md)
- [`go-mcp-server-generator.prompt.md`](go-mcp-server-generator.prompt.md)
- [`java-mcp-server-generator.prompt.md`](java-mcp-server-generator.prompt.md)
- [`kotlin-mcp-server-generator.prompt.md`](kotlin-mcp-server-generator.prompt.md)
- [`php-mcp-server-generator.prompt.md`](php-mcp-server-generator.prompt.md)
- [`python-mcp-server-generator.prompt.md`](python-mcp-server-generator.prompt.md)
- [`ruby-mcp-server-generator.prompt.md`](ruby-mcp-server-generator.prompt.md)
- [`rust-mcp-server-generator.prompt.md`](rust-mcp-server-generator.prompt.md)
- [`swift-mcp-server-generator.prompt.md`](swift-mcp-server-generator.prompt.md)
- [`typescript-mcp-server-generator.prompt.md`](typescript-mcp-server-generator.prompt.md)
