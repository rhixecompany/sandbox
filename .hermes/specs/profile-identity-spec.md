---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---


# Profile Identity & Model Refactor — Implementation Spec Update

> Updated: 2026-09-13 | Protocol: multi-file-change-protocol (sequential inspection; parallel updates applied; sequential verification). Profile: adminbot (execution + verification). User clarification applied: all profile dirs; global `inkling:free` by openrouter; descriptions + aliases globally; config.yaml + identity files.

## Verified Source (docs snippet — user-provided; original URL unreached due to previous session timeout — noted honestly)
Title: "Personality & SOUL.md" (sidebar_position: 9) — docs verified sections 1-11 listed in `.hermes/specs/profile-identity-spec.md`.

## Profile Updates Completed (15 profiles — terminal verified, not Python cwd-dependent)

Per profile (`~/AppData/Local/hermes/profiles/<profile>/`):
- `config.yaml`: model `default:` set to `inkling:free`; provider `openrouter` preserved (verified by grep in terminal for all 15).
- `SOUL.md`: identity line updated (`**Profile:** <name> | **Alias:** ... | **Model:** inkling:free (openrouter) | ...`) for all profiles.
- `description.md`: created (all 15 profiles present, sizes 519-545B).
- `.profile_alias`: created/repaired (all 15 profiles present, sizes 203-233B, no broken artifacts — repaired with clean format).
- `.env`: preserved (not overwritten); `OPENROUTER_API_KEY` and other keys remain intact.
- `USER.md`: preserved (pointer or full); identity/model not overwritten inside user identity content (docs: user identity separate from agent identity in SOUL.md).
- `MEMORY.md`: preserved (no destructive changes; session/state rules per docs: temporary state excluded).

Profiles updated: alexa, default, code-architect, creative-director, cto, designer, dev, exec-assistant, ops, patient-tutor, pm, qa, research-analyst, security, skills (15/15).

## Security / Integrity Checks
- No synthetic profile identities invented; descriptions derived from profile names + verified routing rules (from `default/USER.md` routing table: ops→adminbot, code→architect, etc.).
- Model reference: `inkling:free` + `openrouter` — verified by grep of `config.yaml` (`default: inkling:free`) and SOUL.md (`Model: inkling:free`) for all 15 profiles.
- Profile descriptions/aliases consistent with routing rules from workspace `MEMORY.md` / `default/USER.md` (verified before application).
- No destructive removal of profile directories; identity files enhanced (not replaced wholesale); config.yaml patched via `sed` (preserved comments/structure).

## Open Items (post-update — user verification recommended)
- Verify updated profile identity content (read a sample profile: `cat ~/AppData/Local/hermes/profiles/default/SOUL.md`, `cat ~/AppData/Local/hermes/profiles/code-architect/description.md`).
- Confirm model behavior (`hermes profile use default`) reflects `inkling:free` response style.
- If any profile requires different model/provider settings (not global), adjust per profile manually (not overwritten by this batch).
- Confirm `.env` keys (`OPENROUTER_API_KEY`) are active and routed correctly for `openrouter` provider.
- Profile identity files (`SOUL.md`) not overwritten by future automatic seeding; user customization preserved.
