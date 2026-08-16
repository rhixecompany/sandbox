# npm → bun migration — worked transcript (2026-08-08)

Workspace: `~/Desktop/SandBox` (branch `development`), 20 `package.json` manifests across root + 19 sub-repos. Target: make `bun`/`bunx` the only package-manager commands. Proven with `bun 1.3.14`.

## Inventory that drove the plan

| Repo dir | Before | Notes |
|---|---|---|
| `.` (SandBox root) | bun.lock + package-lock.json | root `check` script used `npm run` |
| projects/Banking, Bash | bun.lock + bunfig.toml | already bun; Banking had `npm-check-updates` CLI still |
| projects/comicw-se | bun.lock + package-lock.json | packageManager was `pnpm@9.12.3`; had recursive `node_modules` nest |
| projects/Resume_maker, rhixe_scans, selenium_webdriver, mcp-servers/typescript, copilot-driver | bun.lock only | clean |
| projects/rhixecompany-comics/frontend | bun.lock + package-lock.json | stale npm lock |
| projects/{Django-Scrapy-Selenium, ecom/docs, ecom/frontend, mcp-server-typescript, university-libary-jsm, xamehi, xamehi.tv/frontend} | package-lock.json only | needed `bun install` to migrate lockfile |
| cookiecutter template | package-lock.json | deleted lock, no install (Jinja) |
| ~/AppData/Local/hermes | NO package.json | npm/npx hits = VS Code template strings in Python + MCP npx.cmd wrappers → documented exceptions |

## Regex recipes (ran against `"scripts"` block only)

```python
re.sub(r'\bnpm run\b',  'bun run', body)
re.sub(r'\bnpx\b',      'bunx',    body)
body = body.replace('npm ci', 'bun install --frozen-lockfile')
body = body.replace('npm install', 'bun install')
```

Direct CLI naming: `npm check-updates → bunx npm-check-updates` (package name unchanged). pnpm schema tool calls `pnpm foo → bunx foo`, then collapse `bunx bunx foo`.

`packageManager: "bun@1.3.14"` added to all 20; only change needed beyond script swaps in manifests.

## CI before/after (the gotcha)

Before:
```yaml
- uses: actions/setup-node@v4
  with:
    node-version: "22"
    cache: "npm"
- run: npm ci 2>/dev/null || npm install
- run: npm run build || echo "Build skipped"
```

After:
```yaml
- uses: oven-sh/setup-bun@v2
  with:          # empty with! must be deleted
    cache: "bun"
- run: bun install --frozen-lockfile
- run: bun run build || echo "Build skipped"
```

Gotcha fixed mid-session: first pass only rewrote `uses: setup-node@v4` → `oven-sh/setup-bun@v2`, leaving `node-version:` and `cache: "npm"` — setup-bun rejects unknown input `node-version` and the old npm cache keys were stale. Second-pass cleanup:
1. remove leftover `node-version:` lines directly under a `setup-bun` `with:`
2. delete now-empty `with:` blocks
3. `cache: "npm"` → `cache: "bun"`
4. manual cache actions: `~/.npm` → `~/.bun/install/cache`, key `npm-ci-…hashFiles('package-lock.json')` → `bun-ci-…hashFiles('bun.lock')`, restore-keys `npm-ci-` → `bun-ci-`
5. `yaml.safe_load` every edited workflow (found 0 invalid after cleanup)

Also convert `npm run contributors:check` etc. — same table as manifests.

## Verification (per repo)

```bash
bun install          # first — also creates bun.lock for package-lock-only repos
bun run lint bun run typecheck bun run check
grep -rInE '\b(npm|npx)\b' --include='*.json' --include='*.md' --include='*.yml' . | grep -v node_modules
```

Watch: npm from CRA ≥ big trees can exceed a 300s foreground cap — kick off `bun install` in background with notify.

## Pitfalls observed

- `pathlib.Path.glob("**/package.json")` threw `WinError 1921` on `projects/comicwise/node_modules/comicbook/node_modules/…` recursion (~127-deep). Switched to pruned `os.walk` — never recursive glob across `node_modules` on Windows.
- `.disabled` workflows and `*.lock.yml` contain `package-lock.json` in bot-config `protected_files` lists → false grep hits; don't touch them.
- Hermes root has no manifest to migrate; its npm strings are template content (VS Code launch/task JSON, `npx.cmd` for MCP server wrappers) → leave, document.