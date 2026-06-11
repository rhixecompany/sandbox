# Profile State Refresh Checklist

Use this checklist after running `hermes status` or `hermes profile list` to keep USER.md synchronized with actual Hermes configuration.

## Pre-Refresh

- [ ] Run `hermes profile list` — capture output
- [ ] Run `hermes status` — capture output
- [ ] Open `USER.md` in editor
- [ ] Open current SOUL.md reference (for context)

## Identity Section

- [ ] **Name:** Matches profile owner's name (e.g., "Alexa")
- [ ] **OS:** Matches actual OS (Windows 11, macOS, Linux)
- [ ] **Editor/IDE:** Current editor in use (VS Code, Vim, etc.)
- [ ] **Shell:** User's preferred local shell (PowerShell, bash, zsh)
- [ ] **Home:** Correct Hermes installation path

## Active Model & Providers Section

- [ ] **Default Model:** From `hermes status`, first line (`Model: ...`)
- [ ] **Provider:** From `hermes status`, second line (`Provider: ...`)
- [ ] **Configured Providers:** List all with ✓ from hermes status (OpenAI, OpenRouter, Gemini, xAI, etc.)
- [ ] **Auth Status:** Note which are ✓ (logged in) vs ✗ (not set / not logged in)
- [ ] **Gateway:** From hermes status (`Status: stopped` or `Status: running`)

## Profiles Section

- [ ] Active profile marked with ◆ (from `hermes profile list`)
- [ ] All profiles listed with their model (from `hermes profile list`)
- [ ] Status of each profile (active, stopped)

## Execution Preferences Section

- [ ] Reflect actual user preferences (concise/blunt/technical, etc.)
- [ ] Delegation strategy (execute_code vs delegate_task preference)
- [ ] File operations rule (no backups, direct edits, git rollback)
- [ ] Approval requirements (git commits, destructive ops)

## Development Standards Section

- [ ] References SOUL.md for actual standards (no duplication)
- [ ] Lists what SOUL.md covers (code quality, commit style, etc.)

## Notes Section

- [ ] Skill author tag: Alexa (if applicable)
- [ ] Prompt style preference (Hermes-friendly, include ".github/prompts")
- [ ] Any tool-specific quirks (e.g., cron script path relative to ~/AppData/Local/hermes/scripts/)

## Post-Refresh Validation

- [ ] No facts repeated between USER.md and SOUL.md
- [ ] All paths are accurate and Windows-compatible (C:\Users\...)
- [ ] All cross-references to SOUL.md are clear
- [ ] File is concise (no verbose narrative; use bullet points, tables, pipe-delimited headers)
- [ ] Dates updated to current date
- [ ] Git status: ready to commit

## Commit

```bash
git add USER.md
git commit -m "docs: refresh profile state [date]"
```

---

## Shortcuts

**Just active model + gateway status changed?**
→ Update MODEL line in "Active Model & Providers" only. Commit with `docs: update active model`.

**Just added a new provider or auth changed?**
→ Update "Configured Providers" and "Auth Status". Commit with `docs: update provider auth`.

**Major profile overhaul (new profile created)?**
→ Run full checklist. Commit with `docs: add [profile-name] documentation`.
