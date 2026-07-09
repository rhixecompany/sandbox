# Resume_maker — Job Documents Generator

> **Stack:** Bun / TypeScript | **Type:** CLI Document Generator | **Status:** Active

A CLI tool that generates job-hunting documents (resume, cover letter, LinkedIn guide, interview prep) from structured JSON input to Markdown and PDF formats.

---

## Technology Stack

| Category | Technology |
|---|---|
| **Runtime** | Bun (latest), Node.js (fallback) |
| **Language** | TypeScript ^5 (strict) |
| **PDF Generation** | markdown-pdf ^11.0.0 |
| **Linting** | ESLint 10.x, Prettier 3.x, Markdownlint, CSpell |

## Architecture

The generator follows a **Pipeline Processing Pattern**:

```
JSON Input File → index.ts (Entry Point)
                      ↓
            ┌─────────┼─────────┐
            ↓         ↓         ↓
      Resume    Cover Letter  LinkedIn     Interview Prep
       Gen        Gen          Gen            Gen
            ↓         ↓         ↓
            └─────────┼─────────┘
                      ↓
               Markdown Output
                      ↓
              markdown-pdf (PDF)
                      ↓
              output/ directory
```

## Project Structure

```
Resume_maker/
├── index.ts                 # Main entry point
├── sample-input.json        # Sample input data
├── alexander-input.json     # Author's resume data
├── output/                  # Generated documents
│   ├── resume.md / .pdf
│   ├── alexander-resume.md / .pdf
│   ├── project-walkthrough.md
│   └── interview-qa.md
├── scripts/
│   └── smoke-resume.ts      # Smoke test script
├── updated_readmes/         # Generated README updates
├── application_materials/
└── docs/Project_Architecture/
```

## Getting Started

```bash
# Install dependencies
cd Resume_maker
bun install

# Generate documents from sample input
bun index.ts --input sample-input.json

# Generate with specific options
bun index.ts -i alexander-input.json -o resume -f both

# Run quality checks
bun run typecheck && bun run lint
bun run lint:md       # Markdown linting
bun run lint:spell    # Spell checking

# Get help
bun index.ts --help
```

## Key Features

- **Multi-Document Generation** — Resume, cover letter, LinkedIn guide, interview prep
- **Dual Output** — Markdown for editing/sharing, PDF for final delivery
- **Structured JSON Input** — Reproducible data-driven document generation
- **CLI Options** — `--input`, `--output`, `--format` flags for customization
- **Quality Checks** — Linting, formatting, and spell-checking built in

## CLI Commands

| Command | Description |
|---|---|
| `bun index.ts --input <file.json>` | Generate from JSON input |
| `bun index.ts -i <file> -o <dir> -f <both\|md\|pdf>` | Specific output configuration |
| `bun index.ts --help` | Display CLI help |
| `bun run typecheck` | TypeScript type checking |
| `bun run lint` | ESLint + Prettier check |

## Coding Standards

- **ES Modules**: `"type": "module"`
- **TypeScript strict**: Full type safety
- **Entry point**: `index.ts` (main module)
- **Markdown linting**: Strict MD formatting rules
- **Output structure**: Generated files under `output/`
- **CLI conventions**: `--help`, `--input`, `--output`, `--format` flags

## Extensibility

- Add new document types (e.g., portfolio, bio)
- Add new output formats (e.g., DOCX, HTML)
- Support additional input formats (YAML, TOML)
- Add template customization via command-line options

## License

MIT — © Alexander Iseghohi
