---
status: "in_progress"
---

# Implementation Plan — All Profile SOUL.md Refactor + Model Set

Task: For every Hermes profile (15 profiles), refactor/enhance/verify SOUL.md, add description/alias, create missing files, and set model to `inkling:free` via openrouter.

## Profiles (15)

1. alexa 2. code-architect 3. creative-director 4. cto 5. default 6. designer 7. dev 8. exec-assistant 9. ops 10. patient-tutor 11. pm 12. qa 13. research-analyst 14. security 15. skills

## Per-Profile Requirements

- Refactor/enhance SOUL.md (structure, identity, model line, profile routing, rules)
- Verify description in profile.yaml; create/update alias/description
- If profile.yaml missing (skills profile): create it with description + alias
- Set model line in SOUL.md to: `**Model:** inkling:free (openrouter) | ...`
- Verify USER.md / MEMORY.md presence (create stub if missing and needed)
- Set config.yaml model defaults to reference openrouter / inkling:free (or document)
- Add profile-specific alias/identity tag

## Execution Mode

Sequential (data dependency per profile — same workflow applied 15x). Each profile: load → patch → verify.

## Gates

- [ ] Every profile has SOUL.md enhanced with `inkling:free (openrouter)`
- [ ] Every profile.yaml has description + alias set
- [ ] Skills profile has profile.yaml created
- [ ] Every profile's identity line verified in SOUL.md
- [ ] Final aggregate verification passes (count = 15, all have enhanced SOUL.md)
