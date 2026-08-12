# Prompt Library Maintenance Plan — 2026-08-11

> Generated: 2026-08-11T20:38Z | cwd: `C:\Users\Alexa\Desktop\SandBox` | branch: development
> Invoked skills: /plan /create-implementation-plan /implementation-plan /plans-and-specs /executing-plans /hermes-platform-debugging /hermes-setup /using-superpowers /user-communication-preferences

## Goal

1. Inventory `.github/prompts/` — execute `ls` across 3 depth levels and log output to a file.
2. Discover and load every `/prompt-*` skill; use them to update **all** files found in the inventory; create all missing files (referenced children, missing frontmatter, canonical names).
3. Use `/systematic-debugging` (4-phase root cause) to fix every bug/issue/warning/error found by validators.
4. Sync the updated prompt library to **both Hermes** (`~/AppData/Local/hermes/prompts/`) and **OpenCode** (`~/.config/opencode/`).

## Current Context / Assumptions

- `.github/prompts/` = canonical prompt library: **661 `.md` files** (227 at depth 1, 2 at depth 2, 431 at depth 3 via `templates/`, 0 deeper), plus 29 non-`.md` (`.enhance/` toolkit scripts).
- Subdirs: `.github/prompts/templates/` (per-prompt template dirs + `_shared/`), `.github/prompts/.enhance/` (LF-only fixer scripts).
- Prior plans exist: `2026-07-23-comprehensive-github-prompts-plan.md`, `2026-07-23-migrate-hermes-prompts-to-github-prompts.md` — canonical root is already `.github/prompts/`; do not re-migrate.
- Hermes copy exists at `~/AppData/Local/hermes/prompts/` (mirror). OpenCode config at `~/.config/opencode/opencode.jsonc` (+ `.omo/omo.jsonc`).
- Prompt frontmatter uses YAML with `name`, `description`, `version`, `tags`, `trigger:` (singular), `toolsets:`, `dependencies:`/`skills:`.

## Phase A — Inventory (ls → log file)

1. `shopt -s globstar; ls .github/prompts/*.md .github/prompts/**/*.md .github/prompts/**/**/*.md > .hermes/plans/docs/prompt-inventory.log` (faithful to requested command).
2. Dedupe/sort into canonical working list: `find .github/prompts -type f -name '*.md' | sort` → `.hermes/plans/docs/prompt-files.txt` (661 files).
3. Verify counts: depth1 227 / depth2 2 / depth3 431 / total 661.

## Phase B — Discover + Load /prompt-* Skills

1. Search skills for `/prompt-*` and related: `prompt-library-maintenance`, `prompt-library-lifecycle`, `prompt-library-consolidation`, `prompt-builder`, `prompt-engineering`, `prompt-inventory`, `prompt-repair-frontmatter`, `fix-prompt-frontmatter`, `validate-prompts`, `prompt-fix-metadata`, `prompt-audit-all-cjs`, `prompt-batch-audit`, `boost-prompt`, `enhance-prompt`, `fix-prompts`, `fix-prompts-comprehensive`, `normalize-prompt-actions`, `prompt-source-conversion`, `prompt-management`, `scraped-markdown-to-prompt`.
2. Load each via `skill_view`; follow their workflows.

## Phase C — Audit + Update All Found Files (batches ≤ 7)

1. Run `prompt-library-maintenance` scripts:
   - `verify_prompt_library.py` → baseline `TOTAL=N CLEAN=N WITH_ISSUES=M`
   - `audit_prompt_library.py` → `docs/` reports + dangling refs
   - `fix_prompt_library.py --apply` → deterministic frontmatter repair (name/trigger sync, toolsets, MCP→tool:, DEPS==SKILLS)
2. Run `.enhance/` fixers where applicable (LF-only, idempotent) + `validate_prompt_frontmatter.py` if present.
3. Re-run verifier → drive `WITH_ISSUES` to 0. Independent second verifier required.
4. **Create missing files**: any referenced-but-absent child prompt/template paths (from orchestrators) → meaningful placeholders; any file whose slug has no `.prompt.md` → canonical rename if in-scope.

## Phase D — Systematic Debugging of Remaining Issues

- Phase 1: reproduce each failing check; read validator output carefully; trace root cause (frontmatter corruption? CRLF? name/trigger drift? dead refs?).
- Phase 2: compare against working examples + `.enhance/` repair patterns; identify differences.
- Phase 3: one hypothesis at a time; minimal change; verify.
- Phase 4: implement root-cause fix (targeted patch / whole-file rewrite for duplicate frontmatter); regression re-check via verifier.
- Rule of three: if 3 fixes fail on the same file class → stop and reassess approach.

## Phase E — Sync Hermes + OpenCode

1. Hermes: push canonical `.github/prompts/*.prompt.md` → `~/AppData/Local/hermes/prompts/` (mirror existing pattern; verify counts match or note intentional delta).
2. OpenCode: update prompts/rules referenced by `~/.config/opencode/opencode.jsonc` / `.omo/omo.jsonc` — identify prompt dir used by OpenCode, copy canonical files there, re-verify config references resolve.
3. Verify both destinations: counts + spot diff vs canonical.

## Files Likely to Change

- `.github/prompts/**/*.prompt.md` (frontmatter/name/trigger/toolset fixes, LF normalization)
- `.hermes/plans/docs/prompt-inventory.log`, `prompt-files.txt` (new inventory artifacts)
- `~/AppData/Local/hermes/prompts/*.prompt.md` (Hermes mirror sync)
- `~/.config/opencode/` prompt files (OpenCode sync, if applicable)
- `.github/prompts/templates/_index.md` (if missing-file repair needed)

## Tests / Validation

- `verify_prompt_library.py` → `WITH_ISSUES=0` (or documented impossible items)
- Independent second verifier → `CLEAN=N WITH_ISSUES=0`
- `git status` clean of unintended changes; no `.bak` files
- Hermes + OpenCode destination counts match canonical

## Risks / Tradeoffs / Open Questions

- **Risk**: bulk frontmatter rewrites corrupt YAML → always yaml.safe_load round-trip, never regex; whole-file rewrite for duplicate-frontmatter files.
- **Risk**: `fix_prompt_library.py --apply` may touch 200+ files → batch ≤7, verify after each batch.
- **Open**: what exactly OpenCode consumes (`.prompt.md` vs `AGENTS.md`/rules). Resolve by inspecting `opencode.jsonc` first; do not guess.
- **Open**: whether Hermes mirror should be byte-identical or a filtered subset (e.g. only `.prompt.md`, excluding `templates/`).
