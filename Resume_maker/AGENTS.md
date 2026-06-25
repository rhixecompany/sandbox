# Resume_maker — Job Docs Generator

## Architecture
- **Type:** CLI document generator (JSON → Markdown + PDF)
- **Pattern:** Pipeline Processing — parse → validate → normalize → generate → convert
- **Entry Point:** `index.ts`
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Generates job-hunting documents (resume, cover letter, LinkedIn guide, interview prep) from structured JSON input. Bun-first, no framework dependencies.

## Stack
- **Runtime:** Bun
- **Language:** TypeScript (strict)
- **Output:** Markdown + PDF (via `markdown-pdf`)
- **Linting:** `bun run lint`, `lint:md`, `lint:spell`

## Commands
```bash
bun install
bun index.ts --input sample-input.json
bun index.ts -i alexander-input.json -o resume -f both
bun run typecheck && bun run lint
bun index.ts --help
```

## Conventions
- CLI flags: `--input`/`-i`, `--output`/`-o`, `--format`/`-f` (markdown, pdf, both)
- Validation in `validateResumeData()` before processing
- Per-document generation is isolated (one failure doesn't block others)
- Output goes to `output/` directory
- Update README when CLI behavior changes
- Align with `copilot-instructions.md` for conventions

## Notes
- Outputs under `output/`; PDF generation failure still saves Markdown
- Smoke test: `scripts/smoke-resume.ts`
- Snapshot tests for Markdown output format
