# Workspace Tooling & Documentation Verification Pattern

Durable technique distilled from verified session 2026-09-10 (Alexa, profile=default, workspace ~/Desktop/SandBox).

## Pattern: verify → patch → verify-gate → document

Applicability: any multi-file enhancement task across `.hermes.md`, `.cursorrules`, `AGENTS.md`, `CLAUDE.md`, `.vscode/mcp.json`, `.opencode/opencode.json`, `.mcp/registry.json`, `.github/copilot-instructions.md`, `.github/instructions/*.md`, `.github/prompts/*.prompt.md`, workspace/skills/*, scripts/, requirements.txt.

## Verified command sequence (re-runnable)

```bash
# 1. State audit
cat .hermes.md | grep -i mcp
cat requirements.txt | grep '^mcp=='
ls ~/myvenv/pyvenv.cfg
~/myvenv/Scripts/python.exe -c "import importlib.metadata; print('mcp:', importlib.metadata.version('mcp'))"

# 2. Package upgrade (only if needed)
~/myvenv/Scripts/python.exe -m pip install -U "mcp==2.0.0"
# If ImportError `request_ctx` appears with fastmcp 3.4.7:
~/myvenv/Scripts/python.exe -m pip install -U "fastmcp==4.0.3" "fastmcp-slim[server]==4.0.3"

# 3. Config updates (always verify JSON after edit)
python -c "
import json
for f in ['.mcp/registry.json','.vscode/mcp.json','.opencode/opencode.json','.copilot/mcp.json']:
    json.load(open(f, encoding='utf-8'))
    print(f, 'VALID')
"

# 4. Structural debt checks
find .github/instructions/ -name '*.md' | head -10
grep -rni '^name:' .github/instructions/domains/*.instructions.md || echo 'some files missing name field'

# 5. Prompt structure fixes
# Check frontmatter completeness: tags, metadata, dependencies
head -25 .github/prompts/tooling/tooling-implementation/tooling-implementation.prompt.md

# 6. Script syntax repair
# If `def main()` in .ts file: replace with `function main(): void { ... }` + `main();`
# Remove leftover garbage (`def main(); __name__ = True` etc)
```

## Pitfalls (always-on rules)

- **Profile identity confusion**: user's profile is `default` (identity Alexa). `adminbot` is ONLY a routing target for ops/devops tasks — never assign it as the user's profile identity in skills, prompts, or memory notes.
- **Never invent profile `adminbot`**: verify against `.cursorrules`/`AGENTS.md`/`CLAUDE.md` routing tables before using. Routing table: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot, general→default.
- **Dependency conflict resolution**: `mcp==2.0.0` requires `fastmcp>=4.0.3`; `fastmcp==3.4.7` + `mcp==2.0.0` produces `ImportError: cannot import name 'request_ctx'`. The fix is to upgrade both together (verified via actual import test), not downgrade `mcp`.
- **JSON syntax after edit**: `.vscode/mcp.json` had a trailing comma at the last `mcpServers` entry before closing `}` — this breaks parsing silently. Always run `python -c "json.load(open(...))"` after any JSON patch.
- **Instructions file structural debt**: `.github/instructions/*.instructions.md` files often miss `name:` field or contain placeholder descriptions (`PLACEHOLDER: ...`). Fix by adding `name:` and replacing placeholder with a concise description.
- **No simulated results**: all verification must use real tool output (`python -c`, `grep`, `json.load`, `bun run lint`). Never describe a gate as passing without the actual command output.
- **DRY reference**: `.omo/templates/myvenv-reference.md` is the single source of truth for `~/myvenv`. All `.opencode/opencode.json`, `.vscode/mcp.json`, `.mcp/registry.json` tooling server entries must reference `~/myvenv` rather than duplicating `hermes-agent/venv`.
- **Strict sequential execution**: complete Phase N (e.g., package upgrade) and verify with real output before Phase N+1 (e.g., config updates). Never skip a verification gate.
- **Non-destructive by default**: no branch deletes, no commits/pushes, no destructive file removals without explicit authorization; `.env` untouched; secrets never printed.
