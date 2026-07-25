# Hermes Artifact Deduplication Pattern

## When to Use

When `.github/skills/`, `.github/hooks/`, or `.github/plugins/` in `~/Desktop/SandBox/` contain items that also exist in the hermes root (`~/AppData/Local/{skills,hooks,plugins}/`), the SandBox copies are redundant mirrors. Delete from SandBox, keep hermes root canonical.

## Procedure

```bash
# 1. Compute duplicates (comm is the cleanest tool)
comm -12 <(ls ~/Desktop/SandBox/.github/skills/ | sort) \
         <(ls $LOCALAPPDATA/hermes/skills/ | grep -v '^\.' | sort)

# 2. Delete duplicates one category at a time
# Skills (use Python execute_code for bulk dir removal):
for d in <dup_list>; do rm -rf ~/Desktop/SandBox/.github/skills/$d; done

# Hooks (small, can use terminal):
rm -rf ~/Desktop/SandBox/.github/hooks/<item>

# Plugins (handle Windows file locking):
chmod -R +w ~/Desktop/SandBox/.github/plugins/<plugin>
rm -rf ~/Desktop/SandBox/.github/plugins/<plugin>

# 3. Verify — comm should produce ZERO output after deletion
comm -12 <(ls ~/Desktop/SandBox/.github/skills/ | sort) \
         <(ls $LOCALAPPDATA/hermes/skills/ | grep -v '^\.' | sort)

# 4. Remove empty dirs if possible
rmdir ~/Desktop/SandBox/.github/hooks 2>/dev/null
rmdir ~/Desktop/SandBox/.github/plugins 2>/dev/null  # may fail on Windows busy handles
```

## What to Keep in SandBox

Items only in SandBox `.github/skills/` that do NOT exist in hermes root are SandBox-specific skills or community additions. Preserve them. As of 2026-06-29 these included:
`accelerate`, `baoyu-article-illustrator`, `baoyu-comic`, `cli`, `creative-ideation`, `docker-management`, `flash-attention`, `here-now`, `lambda-labs`, `modal`, `peft`, `pixel-art`, `qdrant`, `simpo`, `stable-diffusion`, `subagent-driven-development`, `torchtitan`, `watchers`

Dotfiles in `.github/skills/` (`.hub/`, `.curator_backups/`, `.curator_state`, `.usage.json`, `.bundled_manifest`) are Hermes internal state, not skills. Never delete these.

## Verification Command (one-shot)

```bash
echo "Skills:" && comm -12 <(ls ~/Desktop/SandBox/.github/skills/ 2>/dev/null | sort) <(ls $LOCALAPPDATA/hermes/skills/ 2>/dev/null | grep -v '^\.' | sort) && echo "(dupes above)" || echo "(clean)"
echo "Hooks:" && comm -12 <(ls ~/Desktop/SandBox/.github/hooks/ 2>/dev/null | sort) <(ls $LOCALAPPDATA/hermes/hooks/ 2>/dev/null | grep -v '^\.' | sort) && echo "(clean)"
echo "Plugins:" && comm -12 <(ls ~/Desktop/SandBox/.github/plugins/ 2>/dev/null | sort) <(ls $LOCALAPPDATA/hermes/plugins/ 2>/dev/null | grep -v '^\.' | sort) && echo "(clean)"
```