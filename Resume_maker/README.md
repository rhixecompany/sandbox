# Resume Maker

Generate job-hunting documents (resume, cover letter, LinkedIn guide, interview prep) from structured JSON data to Markdown + PDF.

## Quick Start

```bash
bun install
bun index.ts --input sample-input.json
```

## CLI Options

| Option | Description |
| --- | --- |
| `-i, --input <file>` | Input JSON file with resume data |
| `-o, --output <name>` | Output filename base under `output/` |
| `-f, --format <type>` | Output format: `markdown`, `pdf`, or `both` |
| `-p, --projectsDir <dir>` | Projects directory for auto-discovery |
| `--skipProjects` | Skip auto-discovery of project entries |
| `-v, --verbose` | Show verbose runtime output |
| `-h, --help` | Show help |

## JSON Input

Provide `contact`, `summary`, `experience`, `education`, `skills`, and optional `projects`.

```json
{
  "name": "Alexander Iseghohi",
  "title": "Full-Stack Developer",
  "contact": { "email": "alex@example.com", "phone": "+1234567890" },
  "summary": "...",
  "experience": [{ "title": "Developer", "company": "Acme", "startDate": "2024", "highlights": ["..."] }],
  "education": [{ "degree": "BSc", "institution": "University", "graduationYear": "2024" }],
  "skills": ["TypeScript", "React"]
}
```

## Validation

`validateResumeData()` requires:

- `name`, `title`, `summary`
- at least one `experience` and `education` entry
- at least one `skill`
- valid contact email and non-empty phone

## Output Files

- `output/<name>.md`
- optionally `output/<name>.pdf`

## Smoke Run

```bash
bun run scripts/smoke-resume.ts
```

## Repo docs

Use the nearest `AGENTS.md` for commands and conventions in subprojects.
