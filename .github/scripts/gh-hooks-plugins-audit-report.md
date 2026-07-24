# Repo-Side Hermes Hook/Plugin Audit

**Workdir:** `C:\Users\Alexa\Desktop\SandBox`  
**Scope:** `.github/` repo-side assets only  
**Date:** 2026-07-24

---

## 1) Inventory: hook-/plugin-related files under `.github/`

### `.github/scripts/`
- `add_hooks_to_config.py` — inserts Hermes `hooks:` block into `config.yaml`
- `fix_duplicate_hooks.py` — dedupes `hooks_auto_accept: true` in local Hermes `config.yaml`
- `hook-health-check.sh` — validates hook.json-style behavior from repo-side `.github/hooks/`
- `session-logger` — wrapper delegating to `~/AppData/Local/hermes/hooks/session-logger/hook.sh`
- `session-auto-commit` — wrapper delegating to `~/AppData/Local/hermes/hooks/session-auto-commit/hook.sh`
- `governance-audit` — wrapper delegating to `~/AppData/Local/hermes/hooks/governance-audit/hook.sh`

### `.github/workflows/`
- `check-plugin-structure.yml` — PR gate for `plugins/**` paths; asserts plugin dirs contain only `.github/plugin/plugin.json` + `README.md`
- `webhook-caller.yml` — invokes HTTPS webhooks on `main` push; unrelated to Hermes plugin system, but repo-side webhook artifact
- `publish.yml` — contains plugin materialization step (`node eng/materialize-plugins.mjs`)
- `copilot-setup-steps.yml` — referenced in `copilot-instructions.md` as CI expectation for Bash toolkit
- `validate-agentic-workflows-pr.yml` — forbids `.github/**` modifications in workflow contributions

### `.github/copilot-instructions.md`
- Declares canonical hook inventory: `session-logger`, `session-auto-commit`, `governance-audit`
- Declares canonical plugin inventory: `disk-cleanup`, `model-providers/openrouter`, `security-guidance`
- Defines hook script conventions (`jq -c`, `awk`, SKIP flags)
- Points Hermes runtime hooks/plugins to `~/AppData/Local/hermes/hooks/` and `~/AppData/Local/hermes/plugins/`

### Approvals / Archive state
- No `.github/approvals/` directory present.
- No `.github/archive/` directory present.
- No legacy archive folder present under `.github/`.
- The only "archived" concept observed is `.github/workflows/*.disabled`-style naming in subprojects (`projects/comicwise/.github/workflows/*.disabled`), not under root `.github/`.

---

## 2) Stale path refs from legacy roots

| File | Stale ref | Issue |
|------|-----------|-------|
| `.github/scripts/hook-health-check.sh` | `HOOKS_DIR="${1:-.github/hooks}"` | Defaults to repo-local `.github/hooks`, but live hooks live at `~/AppData/Local/hermes/hooks/`. This script appears to be a health-check stub for local hook dirs, not current repo layout. |
| `.github/workflows/check-plugin-structure.yml` | `plugins/`, `.github/plugin/plugin.json` | Expects a `plugins/` tree and `.github/plugin/plugin.json` in the repo. No such paths exist at repo root. Likely stale md/yml copied from plugin-publish workflow. |
| `.github/workflows/publish.yml` | `eng/materialize-plugins.mjs` | Plugin materialization path assumed; not audited as hook/plugin ref, but indicates external plugin pipeline that may not exist locally. |
| `check-plugin-structure.yml`, `.github/workflows` docs | `plugins/**` glob in other workflows | Further evidence of legacy plugin-materialization assumptions. |

Conclusion: no stale refs from root-level `.github/scripts`/`.github/workflows` into nested `skills/`, `agents/`, or `instructions/` other than the `plugins/` mismatch.

---

## 3) Safe updates vs destructive changes

### Safe updates
- Documentation counts: if counts in `copilot-instructions.md` diverge from filesystem, update text only.
- New canonical assets: add files under `.github/prompts/`, `.github/instructions/`, `.github/agents/`.
- Workflow text/doc fixes: update description strings or markdown workflow docs under `.github/workflows/*.md` without adding compiled YAML changes relevant to plugin materialization.
- Local wrapper scripts: can be copied as-is, but they already delegate to local Hermes install.

### Destructive or high-risk changes
- Bulk deletion of `.github/scripts/*` or `.github/workflows/*` without preserving git history.
- Renaming or moving legacy aliases before confirming no consumer uses them.
- Editing `./config.yaml` via `add_hooks_to_config.py` or `fix_duplicate_hooks.py` affects local Hermes runtime config, not repo artifact safety.
- Removing plugin-materialization workflow content from `check-plugin-structure.yml`/`publish.yml` would alter CI behavior for a plugin pipeline that may or may not be in use; requires explicit confirmation.

---

## 4) Approval requirements per change type

| Change | Approval / Gate |
|--------|-----------------|
| Edit `.github/copilot-instructions.md` | Repo PR review; notes `hooks_auto_accept` is true in Hermes config, but that is separate from repo approval. |
| Add/modify `.github/scripts/*` hook/plugin helpers | Repo PR review. Note: these do NOT modify Hermes runtime config unless executed locally. |
| Edit `.github/workflows/*.yml` affecting plugin/materialization (`check-plugin-structure.yml`, `publish.yml`) | Repo PR review + explicit owner confirmation that plugin pipeline is desired, since no `plugins/` tree exists in repo root. |
| Edit `.github/workflows/validate-agentic-workflows-pr.yml` | Repo PR review; modifying this directly changes what is "forbidden" for contributions. |
| Introduce archive/approvals directories under `.github/` | Repo PR review; need owner approval for new directory semantics. |
| Bulk script deletion/rename | Repo PR review + owner sign-off; consider `.bak`/`.old` forbidden policy in repo. |

---

## Summary
- No repository-local approvals or archive directories are present.
- Live hooks and plugins are local-Hermes-runtime artifacts; repo-side wrappers reference `~/AppData/Local/hermes/...`.
- The clearest stale path is the plugin-materialization workflow assuming `plugins/` + `.github/plugin/plugin.json`, which do not exist in this repo root.
- `validate-agentic-workflows-pr.yml` blocks `.github/**` changes in certain PR flows, so `.github/` edits there need contribution-path awareness.
- Safe updates are documentation and additions; destructive changes are deletion/removal of scripts or workflow plugins logic without confirmation.
