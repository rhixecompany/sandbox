# Skills Audit & Remediation Plan

> Generated: 2026-06-29T07:48 | Profile: default (deepseek-v4-flash-free/opencode-zen)
> Strict sequential — each phase completes before next begins.

**Goal:** Full skills pipeline: audit → debug → list → judge → remediate to ≥90 score.

---

## Phase 1: Initial Audit (Capture Baseline)

**Entry check:** If `docs/skills-audit.md` exists with complete stats → skip.

**Commands:**
1. `hermes skills audit > docs/skills-audit.md` — full skill health audit
2. `hermes skills check > docs/skills-check.md` — check for issues
3. `hermes skills update > docs/skills-update.md` — apply available updates

**Verification:**
- All 3 files exist in `docs/` and are non-empty
- Count findings per file

---

## Phase 1.5: Debug & Fix Issues

**Entry check:** Only after Phase 1 completes.

**Actions:**
1. Read all 3 audit files from Phase 1
2. For each issue found: diagnose root cause
3. Install/uninstall any dependencies needed
4. Apply fixes — one issue at a time
5. Re-run `hermes skills audit` to confirm fix

**Verification:**
- All issues from Phase 1 resolved
- No install/uninstall errors

---

## Phase 2: List Local Skills

**Entry check:** Only after Phase 1.5 completes.

**Commands:**
1. `hermes skills list-modified > docs/skills-modified.md`
2. `hermes skills list --source local > docs/local-skills.md`

**Verification:**
- Both files exist in `docs/` with content
- `docs/local-skills.md` contains the full local skill inventory

---

## Phase 3: Judge All Local Skills

**Entry check:** Only after Phase 2 completes.

**Action:** Run `skill-judge` workflow on every skill listed in `docs/local-skills.md`.

**Process:**
1. Read `docs/local-skills.md` to extract skill names
2. For each skill, run skill-judge evaluation (5 dimensions, score 0-100)
3. Write individual reports to `judge_results/skill_<name>_assessment.md`
4. Write aggregate summary to `judge_results/summary.md`

**Verification:**
- Every skill in local-skills.md has a corresponding report
- Aggregate summary presents scores and distribution
- No skill skipped

---

## Phase 4: Remediate All Skills to ≥90

**Entry check:** Only after Phase 3 completes.

**Action:** For each skill scoring <90, apply targeted fixes to reach ≥90.

**Fix priority per skill:**
1. **High** — Missing frontmatter fields (name, title, description, version, author, license, tags), placeholder text, missing verification checklist
2. **Medium** — Over-length SKILL.md (>250 lines → move detail to references/), missing Skills Required table, missing pitfalls, missing phased workflow
3. **Low** — Reference file gaps, formatting, minor DRY issues

**Process:**
1. Order skills by score (lowest first)
2. For each sub-90 skill: read, patch, re-verify
3. Re-judge after fix to confirm ≥90

**Verification:**
- All skills score ≥90 on re-judge
- `judge_results/summary.md` reflects final scores

---

## Files Likely Changed

| Path | Purpose |
|------|---------|
| `docs/skills-audit.md` | Audit output |
| `docs/skills-check.md` | Check output |
| `docs/skills-update.md` | Update output |
| `docs/skills-modified.md` | Modified list |
| `docs/local-skills.md` | Local skill inventory |
| `judge_results/skill_*.md` | Per-skill judge reports |
| `judge_results/summary.md` | Aggregate scores |
| `~/.hermes/skills/*/SKILL.md` | Remediated skills |

## Risks & Open Questions

- **Available score range**: The skill-judge reference says after remediation avg is 72.5/100, with only 12.4% at ≥80. Reaching ≥90 for ALL skills may not be feasible in one session. If a skill stalls at 85-89 after all reasonable patches, note it and move on.
- **Context limits**: Large batch (potentially 100+ skills) — process in batches of 7, write results after each batch.
- **Hermes CLI availability**: All commands use `hermes skills` subcommands — ensure CLI is responsive.
- **Destructive operations**: Patches to SKILL.md files are reversible via git; no `rm -rf` operations planned.
