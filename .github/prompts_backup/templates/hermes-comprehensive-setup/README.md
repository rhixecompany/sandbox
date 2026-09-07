# Comprehensive Hermes and OpenCode Setup

## Goal

Perform full Hermes/OpenCode workspace setup, prompt/template migration, MCP/server/hook/skill alignment, validation, and verification using best practices and all available local tools.

## Inputs

- `.github/prompts/` — canonical prompt library
- `.github/prompts/templates/` — extracted template bodies
- `.github/prompts/.enhance/` — enhancement and validation scripts
- `.hermes.md`, `AGENTS.md`, `CLAUDE.md`, `PROJECT_RULES.md`, `MASTER_RULES.md`
- Hermes config at `~/AppData/Local/hermes/config.yaml`
- OpenCode configs at `C:\Users\Alexa\Desktop\andBox\opencode.json` and `~/.config/opencode/opencode.json`
- Hook directories at `~/AppData/Local/hermes/hooks/*`
- Scripts at `~/AppData/Local/hermes/scripts/`

## Mandatory Workflow

1. **Audit**
   - Read `.github/prompts/.enhance/analyze_prompts.py` and run it
   - Read `.github/prompts/index.md` if present
   - Inspect Hermes config sections: `mcp_servers`, `hooks`, `skills`, `plugins`, `model`, `toolsets`
   - Inspect OpenCode configs for schema validity
   - List active skills, hooks, and MCP servers

2. **Prompt and Template Migration**
   - For every `.github/prompts/*.prompt.md`:
     - Preserve frontmatter exactly
     - Extract body to `templates/{trigger}/README.md`
     - Rewrite prompt as thin shell referencing the template
   - Convert any `.prompt.txt` to canonical `.prompt.md`
   - Update `.github/prompts/index.md` or equivalent index

3. **Hermes Configuration**
   - Validate Hermes config schema and required fields
   - Ensure `mcp_servers`, `hooks`, `skills`, and `plugins` match live environment
   - Update `.hermes.md` to reflect actual prompt/template structure and MCP state
   - Update `AGENTS.md` references if paths/counts change
   - Run hook scripts in dry-run mode where possible

4. **OpenCode Configuration**
   - Validate local and global `opencode.json`
   - Align model selection with Hermes defaults
   - Add supported MCP servers without secrets
   - Test with `opencode.cmd run "echo TEST_OK"`
   - Document unsupported Hermes features explicitly

5. **Enhancement and Validation**
   - Run `/enhance-prompt` and `/enhance-markdown` on newly created files
   - Run `analyze_prompts.py` after changes
   - Fix reported issues before continuing
   - Re-run validation after fixes

6. **Verification**
   - Confirm all expected files exist on disk
   - Confirm no secrets are present in migrated files
   - Confirm git status reflects intended changes only
   - Summarize completed vs blocked items

## Rules

- Do not hardcode secrets, API keys, tokens, or credentials
- Preserve exact frontmatter when rewriting prompts
- Use LF-only Markdown writes
- Report blockers honestly; never fabricate success
- Validate after each batch of changes
- Keep Hermes-specific features in Hermes; do not invent OpenCode equivalents
