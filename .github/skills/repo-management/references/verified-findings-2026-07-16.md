# Verified Findings — 2026-07-16

## Branch/CI Findings This Repo

- `development` is already protected and requires `lint-and-test`; no create step needed there.
- `master`/`production` are unprotected on this repo; do not conflate research actions with branch mutations.
- GitHub auth is present under multiple accounts; prefer the workspace repo owner when querying branch state in this environment.

## CI Preflight Findings

- Root workflows present: `.github/workflows/ci.yml` and `pr-ci.yml`.
- Bash project CI scripts verified against live workspace state: `typecheck`, `lint:strict`, `test`, `format:check` exist in `projects/Bash/package.json`.
- Do not commit CI changes without confirming every `bun run <script>` used in workflow YAML resolves to a real `scripts` key in the target `package.json`.

## Bun Migration Findings

- npm lockfile scan found these candidates: `projects/ecom/docs/package-lock.json`, `projects/ecom/frontend/package-lock.json`, `projects/mcp-servers/copilot-studio/package-lock.json`, `projects/mcp-servers/typescript/package-lock.json`, `projects/rhixecompany-comics/frontend/package-lock.json`, `projects/xamehi.tv/frontend/package-lock.json`.
- Migration should be project-scoped, with verified install before lockfile removal.
