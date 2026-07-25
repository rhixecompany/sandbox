# Codebase-grounded AGENTS.md — method & worked example

## Enumeration recipe (run from the repo root)
```bash
# Reliable on Windows/MSYS shares where search_files times out:
find . -maxdepth 3 -not -path '*/node_modules/*' -not -path '*/.git/*' | head -200
# Count asset types
echo "agents: $(find .github/agents -name '*.agent.md' 2>/dev/null | wc -l)"
echo "instructions: $(find .github/instructions -name '*.instructions.md' 2>/dev/null | wc -l)"
# Verify package manager reality
grep -m1 '"packageManager"' projects/Bash/package.json   # -> bun@1.3.14
# Detect stale path citations (example: root Bash/ that moved to projects/Bash/)
grep -rn "Bash/" .github/copilot-instructions.md
```

## Grounding files to always open
- `package.json` (root + each subproject): `packageManager`, `scripts`, `engines`.
- `tsconfig.json`: strictness flags.
- `.editorconfig`: indent/line-ending (crlf on Windows CI).
- Lockfile: `bun.lock` ⇒ bun; `pnpm-lock.yaml` ⇒ pnpm; `package-lock.json` ⇒ npm.
- `.github/instructions/*.instructions.md` that define agent/instruction frontmatter.
- `.github/workflows/*.yml`: path triggers + CI gates.

## Worked example — SandBox (2026-07-09)
Repo: Hermes agent-dev workspace + Copilot asset library (174 `.agent.md`, 186
`.instructions.md`) + `projects/Bash` Bun/TS toolkit + ~17 subprojects.

Real drift found (all verified, not assumed):
1. `copilot-instructions.md` said "`Bash/` is the main automation toolkit" with 13
   `Bash/` references — but the toolkit is at **`projects/Bash/`** (root `Bash/` doesn't
   exist). Existing root `AGENTS.md` already had it right.
2. `.github/workflows/bash-scripts-ci.yml` path trigger is `Bash/**` (wrong path) — CI
   may miss toolkit changes.
3. Root `AGENTS.md` linked to `SOUL.md` for "core operating principles" — **no SOUL.md
   exists** anywhere. Rules were consolidated inline.
4. `README.md` referenced `PROJECT_RULES.md` — **that file does not exist**.
5. Prompt boilerplate said "always use pnpm" — repo toolchain is **bun** (`packageManager:
   bun@1.3.14`, `bun.lock`, all scripts via `bun`/`bunx`). Artifact used bun.
6. Inventory counts in `copilot-instructions.md` (Agents 159, Instructions 34) were stale
   vs actual (Agents 174, Instructions 186). Treated `reports/inventory/` refresh summary
   as live source.

## Deliverable convention
- Write standalone copy to `results/<prompt-name>.output.md` with a provenance HTML
  comment block at top (author, date, prompt fidelity note) and `<!-- END ARTIFACT -->`
  at bottom.
- Apply cleaned text (strip the wrapper) to root `AGENTS.md`.
- Verify applied file: `head -3 AGENTS.md | grep AGENTS.md` and `grep -c ARTIFACT AGENTS.md`
  should be 0.
