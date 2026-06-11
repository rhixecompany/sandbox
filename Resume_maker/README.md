# Resume Maker

Generate job-hunting documents (resume, cover letter, LinkedIn guide, interview prep) from structured data to Markdown + PDF formats.

## Quick Start

```bash
# Install dependencies
bun install

# Generate resume with sample data
bun index.ts

# Show help
bun index.ts --help
```

## CLI Options

| Option                    | Description                                                                    |
| ------------------------- | ------------------------------------------------------------------------------ |
| `-i, --input <file>`      | Input JSON file with resume data                                               |
| `-o, --output <name>`     | Output filename (saved to `output/` dir, default: output_resume)                      |
| `-f, --format <type>`     | Output format: markdown, pdf, both (default: markdown)                         |
| `-p, --projectsDir <dir>` | Projects directory to auto-discover portfolio entries (default: `../projects`) |
| `--skipProjects`          | Disable project auto-discovery                                                 |
| `-v, --verbose`           | Show verbose output                                                            |
| `-h, --help`              | Show help message                                                              |

## Examples

```bash
# Generate with sample data
bun index.ts

# Load from JSON file
bun index.ts --input my-data.json

# Generate PDF
bun index.ts -o my-resume -f pdf

# Generate both Markdown and PDF
bun index.ts -i data.json -o resume -f both

# Auto-include projects from ../projects
bun index.ts -p ../projects

# Skip auto-discovered projects
bun index.ts --skipProjects
```

## Project Auto-Discovery

By default, Resume Maker scans the top-level folders under `../projects` and adds a `Projects` section to generated resumes.

For each discovered project, Resume Maker includes:

- Project folder name
- A short summary extracted from `README.md` (when available)
- Inferred stack (for example, JavaScript/TypeScript, Python, React, Django)
- First detected GitHub repository URL in the project README (if present)

If your JSON input includes a `projects` array, it is merged with auto-discovered projects and de-duplicated by project name.

## JSON Input Format

Create a JSON file with this structure:

```json
{
  "contact": {
    "email": "john@example.com",
    "phone": "+1234567890",
    "linkedin": "linkedin.com/in/johndoe",
    "github": "github.com/johndoe"
  },
  "education": [
    {
      "degree": "Bachelor of Science",
      "institution": "University Name",
      "graduationYear": "2020"
    }
  ],
  "experience": [
    {
      "title": "Developer",
      "company": "Company Name",
      "location": "City, Country",
      "startDate": "2023",
      "endDate": "Present",
      "highlights": ["Achievement 1", "Achievement 2"]
    }
  ],
  "name": "John Doe",
  "projects": [
    {
      "name": "Banking",
      "summary": "A Next.js fintech banking application with PostgreSQL and Drizzle ORM",
      "stack": ["Next.js", "TypeScript", "PostgreSQL"],
      "repository": "https://github.com/rhixecompany/banking"
    }
  ],
  "skills": ["JavaScript", "TypeScript", "React"],
  "summary": "Your professional summary...",
  "title": "Senior Developer"
}
```

## Output Files

All generated files are written to `output/`:

- `output/resume.md`, `output/cover-letter.md` — Markdown documents
- `output/resume.pdf` — PDF version (when using `--format pdf` or `both`)

For the full list of available templates and guides, see `application_materials/`.

## TypeScript

All types are exported and can be imported:

```typescript
import { ResumeData, ContactInfo, validateResumeData } from './index';
```

## License

MIT
