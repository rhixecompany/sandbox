# Personality Commands Reference

## SOUL.md Management
```bash
# Edit global personality
nvim ~/.hermes/SOUL.md  # or your editor

# Verify current SOUL.md
cat ~/.hermes/SOUL.md
```

## Built-in Personalities
```bash
/personality              # List available
/personality concise      # Switch to concise
/personality technical    # Switch to technical
/personality teacher      # Switch to teacher
/personality creative     # Switch to creative
/personality kawaii       # Switch to kawaii
/personality catgirl      # Switch to catgirl
/personality pirate       # Switch to pirate
/personality shakespeare  # Switch to shakespeare
/personality surfer       # Switch to surfer
/personality noir         # Switch to noir
/personality uwu          # Switch to uwu
/personality philosopher  # Switch to philosopher
/personality hype         # Switch to hype
/personality helpful      # Switch to helpful (default)
```

## Custom Personalities
```yaml
# In ~/.hermes/config.yaml
agent:
  personalities:
    codereviewer: >
      You are a meticulous code reviewer. Identify bugs, security issues,
      performance concerns, and unclear design choices. Be precise and constructive.
    mycustom: |
      Your custom personality here.
```
Usage: `/personality codereviewer`

## Quick Reference
| Task | Command |
|------|---------|
| Edit global personality | `nvim ~/.hermes/SOUL.md` |
| List built-in personalities | `/personality` |
| Switch personality (session) | `/personality <name>` |
| Add custom personality | Edit `config.yaml` → `agent.personalities` |
| View current personality | `/personality` (shows active) |