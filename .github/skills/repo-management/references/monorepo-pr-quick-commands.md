# Quick Commands — Configuring Shell Shortcuts in Hermes

Quick commands (`quick_commands:` in config.yaml) are shell-level shortcuts that bypass the LLM. Type `/name` in CLI, Telegram, or Discord — command fires instantly, zero tokens.

## Config structure

```yaml
quick_commands:
  st:        type: exec;   command: "cd /project && git status --short"
  gc:        type: alias;  target: /commit
```

## Setting via CLI

```bash
hermes config set quick_commands.<name>.type exec
hermes config set quick_commands.<name>.command "<shell command>"
hermes config set quick_commands.<name>.type alias
hermes config set quick_commands.<name>.target /<other-command>
```
