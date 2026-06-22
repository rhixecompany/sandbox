# 3. Detailed Instructions & Standards

> Extracted from `refactor-mardown-files.prompt.md`.

## 3. Detailed Instructions & Standards

1. **Analyze the Target Documentation:**
   - Read the full content of `AGENTS.md`,`.cursorrules` and `.github/copilot-instructions.md`.
   - Identify outdated, redundant, or unclear sections.
   - Cross-reference with authoritative project sources (e.g., `README.md`, blueprints, instruction files).

2. **Refactor for Clarity and Actionability:**
   - Rewrite sections to be concise, actionable, and easy for both humans and AI agents to follow.
   - Use clear headings, bullet points, and code blocks for patterns, commands, and examples.
   - Remove or update any obsolete instructions, references, or links.

3. **Enforce Banking Project Conventions:**
   - Ensure all instructions align with current project architecture, naming conventions, and workflow patterns.
   - Reference file paths and section headings explicitly (e.g., “See `dal/` for DAL patterns”).
   - Use Diátaxis documentation principles: separate how-to guides, reference, explanation, and tutorials.

4. **Optimize for AI Agent Productivity:**
   - Structure content so that AI agents can quickly extract actionable rules and patterns.
   - Highlight critical rules (e.g., “No `any` types”, “No N+1 queries”, “No raw `process.env`”).
   - Use callout blocks for warnings, tips, and critical requirements.

5. **Maintain Consistency and Quality:**
   - Use consistent markdown formatting, heading levels, and code block styles.
   - Ensure all code samples are up-to-date and match the current codebase.
   - Validate that all referenced files, commands, and patterns exist and are correct.

6. **Document Update Process:**
   - At the end of each file, add a “Last Updated” section with the date and a summary of major changes.
   - If major conventions change, update all related documentation and reference sections accordingly.

- **Standards:**
  - Follow the Banking documentation standards in `.github/instructions/documentation.instructions.md`.
  - Adhere to Diátaxis and markdown best practices.
  - Reference authoritative sources by path and section.
  - Prioritize actionable, concise, and context-rich instructions.
