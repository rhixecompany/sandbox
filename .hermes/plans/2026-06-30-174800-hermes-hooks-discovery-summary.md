# Hermes Hooks Discovery and Summary Plan

## Goal
Survey `~/AppData/Local/hermes/hooks`, triage/catalog/identify each hook, read their content, and create a Markdown summary at `docs/hermes-hooks-summary.md`.

## Scope
- Source of truth: `~/AppData/Local/hermes/hooks`
- Excluded from this plan: global cleanup of all SandBox plans, full project inventory beyond hooks

## Phases
1. **Discover hook artifacts** — list files under `~/AppData/Local/hermes/hooks` with paths, sizes, and suffixes/types.
2. **Catalog and triage** — classify each hook by type/purpose and note conflicts/issues.
3. **Read hook content** — read each hook script/config to identify commands, references, ports, and assumptions.
4. **Write summary to `docs/hermes-hooks-summary.md`** — catalog table + issues + recommendations.
5. **Verification gate** — confirm summary exists and references every discovered hook.

Done when: summary file is written and every discovered hook has a catalog entry.


## Verified Live State
- `hermes hooks list` was run and confirmed 4 configured shell hooks:
  - `on_session_end`: session-auto-commit (approved)
  - `on_session_end`: session-logger (approved)
  - `on_session_start`: session-logger (approved)
  - `pre_llm_call`: governance-audit (approved)
- Confirmed docs folder: `C:/Users/Alexa/Desktop/SandBox/docs`
