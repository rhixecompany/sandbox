# Resume_maker — Job Docs Generator

CLI: JSON → Markdown + PDF for resume, cover letter, LinkedIn, interview prep.

Entry: `index.ts`. Bun-first.

## Commands
```bash
cd Resume_maker
bun install
bun index.ts --input sample-input.json
bun index.ts -i alexander-input.json -o resume -f both
bun run typecheck && bun run lint
bun index.ts --help
```

## Notes
- Outputs under `output/`
- Use `bun run lint`, `lint:md`, `lint:spell`
- Update README when CLI behavior changes
- Align with `.github/copilot-instructions.md` for this project
