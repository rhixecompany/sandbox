# VS Code Tool Name → Hermes Toolset Mapping

When normalizing Copilot-imported prompts for Hermes, the `tools:` field must be renamed to `toolsets:` AND each tool name mapped from VS Code's vocabulary to Hermes equivalents.

## Mapping Table

| VS Code / Copilot Tool Name | Hermes Toolset | Notes |
|---|---|---|
| `edit/editFiles` | `file` | |
| `edit` | `file` | |
| `createFile` | `file` | |
| `search/codebase` | `file` | |
| `codebase` | `file` | |
| `runCommands` | `terminal` | |
| `runInTerminal` | `terminal` | |
| `execute/runInTerminal` | `terminal` | |
| `execute/getTerminalOutput` | `terminal` | |
| `runCommands/getTerminalOutput` | `terminal` | |
| `runCommands/terminalLastCommand` | `terminal` | |
| `runCommands/terminalSelection` | `terminal` | |
| `terminalCommand` | `terminal` | |
| `terminalLastCommand` | `terminal` | |
| `terminalSelection` | `terminal` | |
| `web/fetch` | `web` | |
| `fetch` | `web` | |
| `openSimpleBrowser` | `web` | |
| `githubRepo` | — | Remove — no Hermes toolset equivalent |
| `github` | — | Remove |
| `problems` | — | Remove |
| `todos` | — | Remove |
| `testFailure` | — | Remove |
| `usages` | — | Remove |
| `vscodeAPI` | — | Remove |
| `extensions` | — | Remove |
| `runTasks` | — | Remove |
| `searchResults` | — | Remove |
| `new` | — | Remove |
| `changes` | — | Remove |
| `think` | — | Remove |
| `findTestFiles` | — | Remove |
| `runTests` | — | Remove |
| `pylanceRunCodeSnippet` | `code_execution` | |
| `playwright/*` | `browser` | |
| `io.github.chromedevtools/*` | `browser` | |

## Batch Cleanup Steps

1. **Rename** `tools:` to `toolsets:` (handled by prompt migration scripts).
2. **Map** each entry — translate every string via the table above.
3. **Drop** unmapped entries — VS Code-only tools have no Hermes equivalent.
4. **Deduplicate** — check for duplicate entries after mapping.
5. **Default fallback** — if the list is empty after cleanup, assign `[terminal, file]`.

## Detection Commands

### Find unknown/VS-Code toolset names
```bash
python3 -c "
import pathlib, yaml, re
known = {'web','browser','terminal','file','code_execution','vision','image_gen',
         'moa','tts','skills','todo','memory','context_engine','session_search',
         'clarify','delegation','cronjob','search'}
all_vals = set()
for f in pathlib.Path('prompts').glob('*.prompt.md'):
    m = re.match(r'^---\n(.*?)\n---', f.read_text('utf-8'), re.DOTALL)
    if m:
        fm = yaml.safe_load(m.group(1)) or {}
        for t in (fm.get('toolsets') or []):
            all_vals.add(t)
unknown = sorted(all_vals - known)
if unknown:
    print(f'{len(unknown)} unknown toolsets: {unknown}')
else:
    print('All toolsets are valid Hermes names')
"
```

### Find duplicate entries in a single prompt's toolsets
```bash
python3 -c "
import pathlib, yaml, re
for f in sorted(pathlib.Path('prompts').glob('*.prompt.md')):
    m = re.match(r'^---\n(.*?)\n---', f.read_text('utf-8'), re.DOTALL)
    if m:
        fm = yaml.safe_load(m.group(1)) or {}
        t = fm.get('toolsets') or []
        if len(t) != len(set(t)):
            print(f'{f.name}: {t}')
"
```

## Real Session Reference

Session 2026-07-16 applied this mapping to all 215 prompts in the workspace. After the pass:
- 82 prompts had tool names replaced
- 1 prompt had duplicate entries deduplicated
- Zero unknown tool names remain

## See Also

- `references/copilot-hermes-migration.md` (under prompt-management) — the `tools:` → `toolsets:` rename and bracket-fix workflow; this reference is the second half (name mapping).
