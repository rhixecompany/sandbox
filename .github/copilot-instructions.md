# Copilot Instructions — SandBox Monorepo

**Canonical guidance:** [`../AGENTS.md`](../AGENTS.md). **Hermes overrides:** [`../.hermes.md`](../.hermes.md).

This file is a Copilot adapter, not a second rulebook. Read the canonical context first, then apply the nearest subproject instructions.

## Root-level commands

Run from the repo root (`C:/Users/Alexa/Desktop/SandBox`):

```bash
bun install
bun run lint
bun run lint:fix
bun run format
bun run format:check
bun run typecheck
bun run markdownlint
bun run spellcheck
bun run check
```

The root `check` script is the broad validation pass for workspace-level code:

```bash
bun run check
```

## Subproject commands

Use project-local commands, not root assumptions, for app work.

### Banking

```bash
cd projects/Banking
bun run dev
bun run build
bun run lint
bun run type-check
bun run test:browser -- src/path/to/test.ts
bunx playwright test tests/path/to/spec.ts --project=chromium
```

### comicwise

```bash
cd projects/comicwise
bun run dev
bun run build
bun run lint
bun run type-check
bun run test -- src/path/to/test.ts
bunx playwright test tests/path/to/spec.ts
```

### Bash

```bash
cd projects/Bash
bun run lint
bun run typecheck
bun run test -- src/path/to/test.ts
```

### For a single file or test

Prefer targeted validation instead of full-suite runs:

```bash
# ESLint a specific file
bunx eslint projects/Banking/app/some-file.ts

# Vitest one test file
cd projects/Bash && bun run test -- src/cache-clean.test.ts

# Playwright one spec
cd projects/Banking && bunx playwright test tests/auth/login.spec.ts --project=chromium
```

## High-value project commands

Use the local project manifest as the source of truth. These are the confirmed entry points for the main stacks:

| Project | Build / run | Lint or type-check | Single-test pattern |
| --- | --- | --- | --- |
| `projects/Banking` | `bun run dev`, `bun run build` | `bun run lint`, `bun run type-check` | `bunx playwright test tests/path/to/spec.ts --project=chromium` or `bun run test:browser -- src/path/to/test.ts` |
| `projects/comicwise` | `bun run dev`, `bun run build` | `bun run lint`, `bun run type-check` | `bun run test -- src/path/to/test.ts` or `bunx playwright test tests/path/to/spec.ts` |
| `projects/Bash` | project-local `bun run dev`/scripts as documented | `bun run lint:strict`, `bun run typecheck` | `bun run test -- src/path/to/test.ts` |
| `projects/ecom` | Django backend plus `cd frontend && bun run dev` | `cd frontend && bun run lint`; backend `ruff check .` and `pyright .` | Run the relevant frontend test from `frontend/package.json` or the targeted backend pytest path |
| `projects/mcp-servers` | use the language-specific package or README command | use the language-local lint/type-check command | run the language-local test selector |
| `projects/Python-projects` | run the documented Python entry point | `ruff check .`, `pyright` | `pytest path/to/test_file.py -k test_name` |

For any other project, read its nearest `AGENTS.md`, `README.md`, and manifest before choosing commands.

## MCP server mapping

The canonical workspace mapping is [`.github/mcp.json`](mcp.json), mirrored for editor use by [`.vscode/mcp.json`](../.vscode/mcp.json) and referenced by Hermes/OpenCode configuration. Relevant enabled servers include:

- `playwright` for browser and UI validation across Next.js/React projects.
- `tooling-lint` for ESLint, Prettier, and Markdown linting.
- `python-quality` for Ruff and Pyright checks.
- `github` for repository, issue, and pull-request operations.

Use the existing mappings and credentials flow. Do not add duplicate servers, hardcode credentials, or read protected `.env` files. If the two mappings diverge, treat `.github/mcp.json` as the repository source and record the discrepancy before changing it.

## High-level architecture

The repo follows a monorepo-with-autonomy model:

- root handles repo-level config, shared workflows, and generic tooling
- subprojects are independently runnable and usually own their own schema, UI, and CI pipeline
- there is no single app entrypoint for the whole workspace; most changes belong to one project under `projects/`

The most important app families currently in this repo are:

- `projects/Banking`: Next.js 16 + Drizzle + fintech integrations (Plaid/Dwolla)
- `projects/comicwise`: Next.js 15 + Prisma + Stripe
- `projects/Bash`: Bun/TypeScript automation toolkit
- `projects/ecom`: Django + React stack
- `projects/mcp-servers`: multi-language MCP server implementations

## Conventions specific to this repo

- Branch naming: `<type>/<project>/<kebab-case>` (for example `feat/banking/add-plaid-webhook`).
- PR target: `development`.
- TypeScript naming: `kebab-case.ts` for scripts; `PascalCase.tsx` for components.
- Python naming: `snake_case.py`.
- Style: TS uses 2-space indent, single quotes, `strict` mode; Python uses 4-space indent and PEP 8.
- Line endings: follow `.editorconfig` (`lf`); do not normalize unrelated files.
- Keep changes project-scoped; avoid unrelated formatting churn or broad repo-wide edits in a feature PR.
- Respect existing root and project DoD: check `AGENTS.md`, `.cursorrules`, and relevant package scripts before adding tooling or changing workflows.
- Treat `.env` and secrets as protected; do not expose values in code, logs, or output.

## CI and validation expectations

- Root CI runs generic checks and repo-level validation.
- Project CI is often more relevant than root CI for app work.
- Before opening a PR, run the smallest checks that cover the modified behavior, then the relevant project-local validation if needed.

## Copilot execution rules

- Prefer the closest project directory over repo-root edits.
- Use project-local scripts, tests, and configuration first.
- For multi-file changes, state the affected files and validation command before editing.
- Preserve unrelated worktree changes and avoid broad formatting churn.
- Verify the exact requested behavior; do not treat a green proxy check as proof.
- Keep prompts and generated code consistent with the existing toolchain, especially for Next.js/TypeScript work.
- For new or changed requests, clarify first when possible: ask up to three focused questions per turn and cover scope, remaining tasks, blockers, and approval gates.
- Before implementation, maintain the current objective's spec, plan, and prompt under `ai-agent-home/{specs,plans,prompts}/<unique-timestamped-run>/`.
- Update those artifacts as status changes and mark them complete only after the relevant validation passes.
- Use the workflow examples below for new objectives; do not skip clarification, artifact initialization, or final evidence updates.

See [`../README.md`](../README.md) and the relevant project README for broader context.


## Agentic Engineering Workflow Reference

Use the repository's agentic workflow when the task warrants it: `scope` (plan), `architect` (design/spec), `develop` (implementation), `audit` (context), `check` (real behavior and review), `test` (regression coverage), `document` (human record), `debug` (root cause), and `sync` (state reconciliation).
Rules: No synthetic IDs/capabilities. Verify real behavior, not just green tests. Design decisions written down, never buried in code. Build only from approved specs (`/develop` routes back to `/architect` if a load-bearing decision is missing). Fix root cause (`/debug`), not symptoms. Document actual changes (`/document`), not AI memory. Keep durable state in files (AGENTS.md, docs/); never rely on chat context. Marketing/course reference from source file excluded per clarification.
Blockers preserved honestly: adminbot/default profile MISSING; MSYS2 FAIL; rate-limit 403; `.env` protected.

### Required objective workflow

1. **Clarify:** ask up to three focused questions per turn until required, optional, recommended, blocker, and approval decisions are covered.
2. **Record:** create `ai-agent-home/specs/<run>/`, `ai-agent-home/plans/<run>/`, and `ai-agent-home/prompts/<run>/` with `IN_PROGRESS` status.
3. **Audit:** inspect the nearest instructions, manifests, tests, existing patterns, and relevant MCP mappings.
4. **Implement:** make the smallest complete change and update the three artifacts after each material checkpoint.
5. **Verify:** run the exact relevant project-local checks plus structure, reference, Markdown, and diff validation.
6. **Close:** mark all three artifacts `COMPLETE` only after evidence is recorded; otherwise mark `BLOCKED` with the exact unresolved issue.


## MCP Server Sync Note (2026-09-20)
- Same MCP server list applied globally across opencode/copilot/cursor-agent/hermes/agent configs (per clarification turns 1-3).
- Heavy servers replaced with lightweight native equivalents: playwright→browser_exec; code-sandbox→execute_code; smithery→tool_search; mcp-docker→terminal; mindstudio→subagent/delegate.
- Canonical mapping: .github/mcp.json preserved; no duplicate .env exposure.
