# Settings Generation Workflow

## Batch Research Pattern

When generating config for many extensions (40+), use batch research:

1. **Group by category** — Python, JS/TS, Git, Visual, Testing, Data, Shell/Config, Theme, Runtime
2. **Fetch 7 at a time** — `web_extract(marketplace_urls=7)` per call
3. **Fill gaps with domain knowledge** — skip marketplace calls for well-known extensions (Prettier, GitLens, markdownlint, etc.) where settings are standardized

## Coverage Matrix Template

After all configs are written, build a coverage matrix per this pattern:

| # | Extension ID | Config in Default | Notes |
|---|-------------|-------------------|-------|
| 1 | example.extension | ✅/🟡/⬜ | Key settings listed |

- ✅ = explicit settings configured
- 🟡 = extension has no user-configurable settings (commands/menus only)
- ⬜ = gap (extension with settings but none configured)

## Both-Scope Update Pattern

| Scope | File | Purpose |
|-------|------|---------|
| User-default | `~/AppData/Roaming/Code/User/settings.json` | Full config for every extension |
| Workspace | `.vscode/settings.json` | Project-relevant subset; overrides for terminal, Python env, formatters |

## Verification Gates

- `python3 -m json.tool <file>` — validates both .json and JSONC
- `code --list-extensions` — deduped live count vs. plan assumption (detect drift)
- Coverage matrix must show 100% coverage (every installed extension accounted for, even if "no settings")
