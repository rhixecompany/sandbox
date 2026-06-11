# Safe, repeatable workflow for refactoring repository prompt files

1. Discovery
   - search_files('Prompts/*.md') and search_files('.github/prompts/*.md') with pagination (use offset) to avoid truncated results.
   - If search_files returns a JSON parse error, retry with a narrower file_glob or read files one-by-one using read_file.

2. Preview
   - Pick the first matching file and produce a DRY frontmatter + normalized body sample.
   - Present sample to the user and request one of: Approve, Iterate, Cancel.

3. Backup
   - Create docs/prompt-backups/{YYYYMMDD-HHMMSS}/ and copy matched files there verbatim.
   - Record a single backup manifest file listing source -> backup path.

4. Apply
   - Patch each target file: replace old content with the new frontmatter + body while preserving a machine-readable copy of the original in references/originals/{filename}.md in the backup folder.
   - For prompts that indicate required skills or subagents, create SKILL.md stubs under skills/<skill-name>/ if the skill is missing (include frontmatter and minimal workflow placeholders).
   - For prompts that request MCP generators or indicate an MCP server, scaffold a metadata file under mcp_stubs/<prompt-name>.json but do NOT start servers automatically.

5. Post-checks
   - Run search_files to ensure no prompt files were missed.
   - Produce a summary diff and a changelog file docs/prompt-backups/{ts}/changes.md listing edited files and their backup paths.

Pitfalls
- DO NOT run git commits, pushes, or destructive mv/rm commands without explicit user permission.
- If a prompt file contains credentials, replace with [REDACTED] in the edited copy and include a note in the backup manifest.
- When search_files truncates, don't repeat the wide query verbatim; use pagination or targeted globs.

Verification
- Each modified prompt should have a backup path and a manifest entry.
- Each new SKILL.md stub must include 'author: Alexa' in frontmatter by default unless overridden.
- The workflow should be reversible using the backup manifest.
