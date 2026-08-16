# Batch Dependency Restore After Workspace Cleanup

Proven 2026-08-01 on the SandBox monorepo: after a cleanup phase deletes every
`node_modules` / `.venv` / `venv`, the TOOLING phase must restore deps across
all repos. Naive per-repo installs are slow and fail on lifecycle scripts.
Use these two background bash loops.

## Node modules (bun or npm, auto-detected)

```bash
cd ~/Desktop/SandBox
for d in . projects/* projects/*/*; do
  [ -f "$d/package.json" ] || continue
  case "$d" in *hermes-profiles*) continue;; esac        # gitignored mirror — skip
  [ -d "$d/node_modules" ] && continue                    # skip already-installed
  echo "NODE $d"
  if [ -f "$d/bun.lock" ] || [ -f "$d/bun.lockb" ]; then
    (cd "$d" && bun install --ignore-scripts)
  else
    (cd "$d" && (npm ci --ignore-scripts --no-audit --no-fund \
      || npm install --ignore-scripts --no-audit --no-fund))
  fi
done
```

Run as `terminal({"background": true, "notify_on_complete": true})`, then
`process(action="wait")` in 180s steps (process wait clamps at 180s).

Key points:
- `--ignore-scripts` is non-negotiable in headless restore: phantomjs
  postinstall and `db:migrate` hooks fail without a display/db. Dev tooling
  (eslint, prettier, typescript) installs fine without postinstall side effects.
- `npm ci` fails loudly on lockfile drift; fall back to `npm install` only when
  ci fails.
- Depth `projects/*/*` covers nested app dirs (ecom/frontend, mcp-servers/…).
- The `{{cookiecutter.*}}` template dirs may match and get junk node_modules —
  harmless (ignored), or exclude `*cookiecutter*`.

## Python venvs (uv)

```bash
cd ~/Desktop/SandBox
for d in . projects/* projects/*/*; do
  [ -d "$d" ] || continue
  case "$d" in *hermes-profiles*) continue;; esac
  [ -d "$d/.venv" ] && continue
  if [ -f "$d/requirements.txt" ] || [ -f "$d/.ruff.toml" ]; then
    echo "VENV $d"
    (cd "$d" && uv venv .venv \
      && { [ -f requirements.txt ] \
           && uv pip install --python .venv/Scripts/python.exe -r requirements.txt; } \
      && echo "  done")
  fi
done
```

Key points:
- **uv is a native Windows exe — it cannot see MSYS `/tmp/`.** Never hand uv a
  `/tmp/...` path; use cwd-relative temp files (`.req_sandbox.tmp.txt`).
- The `{ ...; }` group returns 1 when requirements.txt is absent, so "done"
  only prints for repos that actually installed — missing "done" does NOT mean
  the venv failed; verify with `find . -maxdepth 3 -name .venv -type d | wc -l`.
- Windows venv python lives at `.venv/Scripts/python.exe` (not `bin/python`).

## Post-restore integrity sweep

```bash
echo "venvs: $(find . -maxdepth 3 -name .venv -type d 2>/dev/null | grep -v hermes-profiles | wc -l)"
echo "node_modules: $(find . -maxdepth 3 -name node_modules -type d 2>/dev/null | grep -v hermes-profiles | wc -l)"
# git status per repo — expect ONLY lowercase 'm' (untracked/ignored content inside submodules), never uppercase 'M'
```

The lowercase-`m` submodule state is EXPECTED noise after restore (new ignored
deps inside subrepos). Uppercase `M` = submodule HEAD differs → needs a root
pointer sync commit (`git add projects/ && git commit`).
