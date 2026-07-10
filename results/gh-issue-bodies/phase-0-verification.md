## Objective

Pre-flight verification gate for the Prompt Management Orchestration pipeline. Confirms all 5 target prompts exist and parse, template directories are present, automation scripts exist, the git working tree is clean, and the active Hermes profile is correct — before any execution begins.

## Source Plan

`plan/prompt-orchestration-comprehensive-plan.md` → Phase 0 (§4.1)

## Verification Steps

- [ ] Inventory target prompts (`prompts/*.prompt.md`) — expect 5 files
- [ ] Verify template directories (`prompts/templates/{name}/`)
- [ ] Check shared templates (`prompts/templates/_shared/`) — expect 12 templates
- [ ] Check scripts (`~/AppData/Local/hermes/scripts/`)
- [ ] Check git status (clean working tree, no blocking uncommitted changes)
- [ ] Verify Hermes profile (`hermes profile show`)

## Safety Gate G0

All 5 prompts must exist and parse. Missing prompts = BLOCK (check `.prompts.md` alternate extension). Missing non-shared template dirs = WARNING, not BLOCK.

## Dependencies

None — entry point. Blocks Phase 1.
