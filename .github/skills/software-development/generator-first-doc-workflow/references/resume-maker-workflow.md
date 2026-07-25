# Resume_maker Workflow Notes

## Discovery

From `C:\Users\Alexa\Desktop\SandBox\projects\Resume_maker`:

- Entrypoint: `index.ts`
- Runtime: Bun with TypeScript
- Input: structured JSON such as `basil-input.json` or `alexander-input.json`
- Output directory: `output/`
- Default smoke script: `scripts/smoke-resume.ts`
- Reported capabilities in `package.json`: resume, cover letter, LinkedIn guide, interview prep
- Actual implementation in `index.ts`: resume only

## Input Schema Minimum

Use at least these fields in project-local JSON:

- `name`
- `title`
- `contact.email`
- `contact.phone`
- `summary`
- `experience[]` with `title`, `company`, `startDate`, `highlights[]`
- `education[]` with one object; when unknown use placeholders such as `To be updated`
- `skills[]`

## Validation Behavior

The generator requires non-empty `name`, `title`, `summary`, `experience`, `education`, `skills`, `contact.email`, and `contact.phone`. Experience entries require `title`, `company`, and `startDate`. Education entries with a non-empty `degree` also require `institution` and `graduationYear`. A single placeholder education object satisfies the required education entry rule.

## Generation Commands

Generate Markdown and PDF:

- `cd C:\Users\Alexa\Desktop\SandBox\projects\Resume_maker`
- `bun index.ts --input basil-input.json --output basil-resume --format both --verbose`

Use `--skipProjects` when the document should not include repo-discovered portfolio projects.

Use `--skipProjects --format both` for Basil's focused resume artifact.

## Output Artifacts

From a successful run with `--output basil-resume`:

- `output/basil-resume.md`
- `output/basil-resume.pdf`

Use the output filename as the base name and do not add extensions manually.

## Known Limitation

Cover letter, LinkedIn guide, and interview prep are listed in `package.json` but not implemented in `index.ts`. The existing `application_materials/COVER_LETTER.md` is a hand-written template, not generated output. Tell the user when an advertised artifact type is missing rather than silently creating a manual substitute.
