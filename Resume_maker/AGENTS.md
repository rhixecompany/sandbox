# Resume_maker — Job Docs Generator
## Architecture

- **Blueprint**: [Resume_maker Architecture](../docs/Project_Architecture/Resume_maker_architecture.md)
- **Folders**: [Resume_maker Folder Structure](../docs/Project_Architecture/Resume_maker_folders.md)
- **Tech Stack**: [Resume_maker Technology Stack](../docs/Project_Architecture/Resume_maker_techstack.md)
- **Stack Type**: Bun/TypeScript


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
