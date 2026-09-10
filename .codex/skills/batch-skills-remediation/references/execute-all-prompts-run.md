# Execute-All-Prompts Orchestrator Run (2026-07-16)

Run the 5-phase orchestrator by executing `%LOCALAPPDATA%/hermes/prompts/execute-all-prompts.prompt.md`.

## Phase Order

1. **Audit Skills Judge Fix** — `audit-skills-judge-fix.prompt.md`
2. **Agents System Prompt Context Fix** — `agents-system-prompt-context-fix.prompt.md`
3. **Audit Plans** — `audit-plans` skill
4. **Prompts Repair** — `fix_prompts.py` (211 prompts in `%LOCALAPPDATA%/hermes/prompts/`)
5. **Test Providers & Models** — `test-providers-models.prompt.md`

## Key Outcomes

| Phase | Counts |
|-------|--------|
| Skills | 574 skills, 0 fail (after removing `.restore-backups.DISABLED` + `.archive` duplicates) |
| Agents | 174 Copilot agents, 186 instructions, 1 Codex twin pair |
| Plans | 1 plan in `.hermes/plans/`, `SESSION_REPORT.md` regenerated |
| Prompts | 211 scanned, 2 fixed (tags format), 209 clean |
| Providers | 9 providers, 342 OpenRouter models (23 free) |

## Known Pitfalls

- **`hermes skills repair-official` fails on corrupt cache**: Delete `%LOCALAPPDATA%/hermes/skills/.hub/lock.json` and `index-cache/*.json` files that have non-UTF8 encoding, then re-run.
- **Duplicate skill dirs inflate judge failures**: Remove `.archive`, `.restore-backups.DISABLED` from skills root before judging.
- **`fix_prompts.py` targets `~/Desktop/SandBox/prompts` by default**: Override via `PROMPTS_DIR` env var to point at `%LOCALAPPDATA%/hermes/prompts`.
