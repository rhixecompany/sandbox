Phase 1 Reconstruction — reference

When Phase 1 artifacts (docs/{purpose}-context.md or docs/{purpose}-issues-context.md) are missing but Phase 2 or Phase 4 artifacts exist, follow this deterministic reconstruction path.

Steps:
1. Parse docs/{purpose}-verify-context.md for a verification table. Extract Issue IDs, File names, short description, status, and notes. Use regex: `\|\s*([A-Z]{3}-\d{3})\s*\|` to locate Issue IDs.
2. Parse docs/{purpose}-fix-issues-context.md for batch progress and logged issue IDs. Extract listed IDs (regex: `\b([A-Z]{3}-\d{3})\b`) and any "Progress > Batch N" notes.
3. Read target files (Prompts/, docs/, .opencode/) to re-derive forward references: markdown links `[text](file.md)`, agent mentions `@agent-name`, and `/command` triggers. Record forward references per file.
4. For reverse references: search docs/ and .opencode/ artifacts for the filenames discovered in step 3 and list the files that mention them.
5. Produce docs/{purpose}-context.md containing:
   - Generated header with provenance: list source artifacts used for reconstruction and timestamps
   - Forward References table
   - Reverse References table
   - File Inventory enumerating the target files with assigned priority (source files: Critical; forward refs: Major; reverse refs: Minor)
6. Produce docs/{purpose}-issues-context.md with placeholder entries for each Issue ID discovered in steps 1–2. If a description is available from verify-context, include it; otherwise use `See verify-context for details.`
7. Write both files to docs/ and record the reconstruction action in an audit note appended to docs/{purpose}-fix-issues-context.md under "## Progress > Administrative Actions" with a timestamp and list of source artifacts.

Pitfalls & notes:
- If verify-context.md parsing fails due to table formatting differences, fall back to extracting capitalized ID-like tokens (pattern `[A-Z]{3}-\d{3}`) from both verify and fix logs and then map them to files by heuristic (look for filename mentions nearby).
- Include a clear provenance header: "Reconstructed from: <list of artifact paths> — run at <UTC timestamp>".
- Avoid overwriting existing Phase 1 artifacts unless the user explicitly asks for a fresh re-run. When overwriting, move the existing docs/{purpose}-context.md to docs/prompt-backups/{timestamp}/ first and record the action.
