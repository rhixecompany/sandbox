---
status: completed
---

# Oh My OpenAgent / Oh My Hermes — Installation & Verification Plan

**Date:** 2026-08-05 | **Status:** Executed | **Owner:** OWL

## Goal

Install, configure, and verify Oh My OpenAgent (OMO, formerly oh-my-opencode) and the Oh My Hermes workflow layer across OpenCode + Hermes, per the official 2026 guide.

## Environment (verified)

- OpenCode CLI **1.18.13** @ `C:\nvm4w\nodejs\opencode.cmd`
- oh-my-openagent **4.19.4** resolvable via `bunx`
- Bun @ `C:\Users\Alexa\.bun\bin\bun`
- Hermes root `C:\Users\Alexa\AppData\Local\hermes` (opencode plugin present)

## Sequence (validated step-by-step)

1. **Prereq check** — opencode ≥ 1.4.0, bun/node. ✅
2. **OMO install** — `bunx oh-my-openagent install` (interactive, already done 4.19.4). ✅
3. **Config** — `~/.config/opencode/oh-my-openagent.jsonc` (agent→model map, categories). Verify presence.
4. **Auth** — `opencode auth login` providers configured (≥1 present).
5. **Non-interactive env flags** — `OPENCODE_DISABLE_*` set (Hermes-driven mode).
6. **Hermes plugin** — opencode tooling registered in Hermes; smoke tests if plugin present.
7. **doctor** — `bunx oh-my-openagent doctor` + custom `scripts/omo_doctor.py`.
8. **Multi-agent smoke** — `opencode agents` lists agents; optional `@sisyphus` orchestration.

## Artifacts

| Artifact | Path                                                                                | Status |
| -------- | ----------------------------------------------------------------------------------- | ------ |
| Script   | `scripts/omo_doctor.py`                                                             | ✅     |
| Skill    | `~/AppData/Local/hermes/skills/autonomous-ai-agents/oh-my-openagent-setup/SKILL.md` | ✅     |
| Plan     | this file `plans/2026-08-05_omo-ohmyhermes-setup-plan.md`                           | ✅     |
| Spec     | `plans/2026-08-05_omo-ohmyhermes-setup-spec.md`                                     | ✅     |
| Prompt   | `.github/prompts/oh-my-openagent-setup.prompt.md`                                   | ✅     |

## Open Items

- `hermes-profiles/` mirror was wiped per user approval → regeneration path: re-run sync tooling (`verify_sync.py` was deleted with it) from hermes root.
- Multi-agent orchestration smoke (`@sisyphus`) runs on-demand; requires live model quota.
