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
# Resume_maker — Job Docs Generator

**Naming**: `kebab-case.ts` for files; `camelCase` for variables/functions; `PascalCase` for interfaces/types; `kebab-case.json` for input data; `UPPER_CASE.md` for docs.

**Patterns**: Single-entry architecture (`index.ts`); pipeline processing (JSON input → transform → Markdown render → PDF export); `markdown-pdf` for PDF conversion; CLI flag convention (`--input`, `--output`, `--format`, `--help`); dual output (Markdown + PDF).

**Structure**: `index.ts` (single entry point); `output/` (generated files); `scripts/` (utility scripts); `application_materials/` (input materials); `updated_readmes/` (generated README updates); root-level JSON input files.

**TypeScript**: Strict mode; ES Modules (`"type": "module"`); Bun runtime; explicit interface exports for reuse; async/await for file I/O; `parseArgs` from `util` for CLI.

**Document Formats**: Resume, Cover Letter, LinkedIn Guide, Interview Prep — all generated from single JSON input; Markdown for editing/sharing; PDF for final delivery.

**Env**: No secrets committed; `.env` files excluded from VCS.

**Commands**: `bun index.ts` (default — sample input); `bun index.ts --input <file.json> --output <dir> --format both` (custom); `bun run typecheck && bun run lint` (validation); `bun run lint:md && bun run lint:spell` (markdown/spell check).

**Pre-commit**: `bun run typecheck && bun run lint && bun run lint:md && bun run lint:spell`.
