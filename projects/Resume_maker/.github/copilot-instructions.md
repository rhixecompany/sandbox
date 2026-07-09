# Copilot Instructions

Project-wide guidance for the Resume Maker CLI.

## Source of truth

- `Resume_maker/AGENTS.md`
- `README.md`
- `package.json`
- `index.ts`

## Commands

Run from `Resume_maker/`:

```bash
bun install
bun index.ts --help
bun index.ts --input sample-input.json
bun run start
bun run build
bun run help
bun run typecheck
bun run lint
bun run lint:fix
bun run lint:md
bun run lint:spell
```

## Architecture

- Bun-first TypeScript CLI centered on `index.ts`.
- Input JSON is transformed into Markdown and PDF resume artifacts.
- Generated output is written under `output/`.

## Conventions

- Keep CLI flags, defaults, and README examples synchronized.
- Prefer Bun commands over npm/pnpm/yarn.
- Treat generated output and source JSON as sensitive personal data.
- Keep changes scoped to the CLI behavior being updated.

