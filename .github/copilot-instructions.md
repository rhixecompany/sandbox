# Copilot Instructions — SandBox Monorepo

Canonical reference: `../../AGENTS.md`, `../../.hermes.md`, `../../CLAUDE.md`.

This repo is a polyglot monorepo with several autonomous subprojects. Treat each `projects/*` directory as its own app unless the change is clearly root-level configuration, docs, or shared tooling.

## Repository shape

- Root workspace: shared config, GitHub automation, prompt library, linting, and repo-wide scripts.
- `projects/`: self-contained apps and experiments. They usually have their own `AGENTS.md`, `package.json`, README, and CI workflow.
- High-value directories: `.github/workflows/`, `.github/prompts/`, `projects/Banking/`, `projects/comicwise/`, `projects/Bash/`, `projects/ecom/`, `projects/mcp-servers/`.

Read the relevant subproject’s `AGENTS.md` and `package.json` before editing there; don’t assume the root scripts apply directly.

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
- Line endings: CRLF on this Windows-hosted repo.
- Keep changes project-scoped; avoid unrelated formatting churn or broad repo-wide edits in a feature PR.
- Respect existing root and project DoD: check `AGENTS.md`, `.cursorrules`, and relevant package scripts before adding tooling or changing workflows.
- Treat `.env` and secrets as protected; do not expose values in code, logs, or output.

## CI and validation expectations

- Root CI runs generic checks and repo-level validation.
- Project CI is often more relevant than root CI for app work.
- Before opening a PR, run the smallest checks that cover the modified behavior, then the relevant project-local validation if needed.

## Working rules for Copilot

- Prefer the closest project directory over repo-root edits.
- Use project-local scripts and config first.
- If a task is within a subproject, validate there before broad repo checks.
- Keep prompts and generated code consistent with the repo’s existing conventions and toolchain, especially for Next.js/TypeScript work.

See `../../README.md` and the relevant project README for broader project context when a task crosses multiple code paths.
