# Cross-Platform Asset Sync (Skills/Plugins/Hooks)

Companion to `cross-platform-agent-inventory.md`. Covers the **sync** step after inventory — synchronizing skills, plugins, and hooks across Hermes, Copilot (.github), and Codex agent platforms.

## When to Use

- After running cross-platform agent inventory and identifying drift
- When skills are added to Hermes library and need mirroring in `.github/skills/`
- When verifying plugins/hooks parity between active Hermes and reference `.github/` copies
- Between major Hermes skill library maintenance sessions

## Platform Asset Map

| Asset | Hermes | Copilot (.github) | Codex |
|-------|--------|-------------------|-------|
| Skills root | `~/AppData/Local/hermes/skills/` | `workspace/.github/skills/` | `~/.codex/skills/` |
| Plugins root | `~/AppData/Local/hermes/plugins/` | `workspace/.github/plugins/` | `~/.codex/plugins/` |
| Hooks root | `~/AppData/Local/hermes/hooks/` | `workspace/.github/hooks/` | (none) |
| Agents | Hermes profiles | `workspace/.github/agents/*.agent.md` | `~/.codex/agents/*.toml` |
| Instructions | — | `workspace/.github/instructions/*.instructions.md` | — |

## Sync Workflow

### Step 1: Inventory all three platforms

```bash
# Skill counts
hermes_skills=$(ls -d $LOCALAPPDATA/hermes/skills/*/ | wc -l)
copilot_skills=$(ls -d workspace/.github/skills/*/ | wc -l)
codex_skills=$(ls -d ~/.codex/skills/*/ 2>/dev/null | wc -l)

# Plugin counts
hermes_plugins=$(ls -d $LOCALAPPDATA/hermes/plugins/*/ | wc -l)
copilot_plugins=$(ls -d workspace/.github/plugins/*/ | wc -l)

# Hook files
hermes_hooks=$(find $LOCALAPPDATA/hermes/hooks/ -type f | wc -l)
copilot_hooks=$(find workspace/.github/hooks/ -type f | wc -l)
```

### Step 2: Identify drift between Hermes and Copilot

```bash
# Export sorted skill lists
cd $LOCALAPPDATA/hermes/skills && ls -d */ | sed 's|/$||' | sort > /tmp/hermes_skills.txt
cd workspace/.github/skills && ls -d */ | sed 's|/$||' | sort > /tmp/copilot_skills.txt

# Find skills missing from Copilot
echo "=== Missing from .github ==="
comm -23 /tmp/hermes_skills.txt /tmp/copilot_skills.txt

# Find skills only in Copilot (reverse drift)
echo "=== Only in .github ==="
comm -13 /tmp/hermes_skills.txt /tmp/copilot_skills.txt
```

### Step 3: Sync skills (Hermes → Copilot)

When Hermes has skills not in `.github/skills/`, copy them:

```bash
cd $LOCALAPPDATA/hermes/skills
for skill in $(comm -23 /tmp/hermes_skills.txt /tmp/copilot_skills.txt); do
  if [ -d "$skill" ]; then
    echo "Syncing: $skill"
    cp -r "$skill" "/path/to/workspace/.github/skills/$skill"
  fi
done
```

**Note:** Copy from Hermes → Copilot only. Hermes is the canonical skills library; `.github/skills/` is the mirror for Copilot/VS Code consumption.

### Step 4: Verify plugins parity

Plugins are typically stable and need only a count/layout check:

```bash
diff <(ls $LOCALAPPDATA/hermes/plugins/) <(ls workspace/.github/plugins/)
```

If drift is found, investigate before syncing — plugins may intentionally differ per platform.

### Step 5: Verify hooks parity

`.github/hooks/` is a **reference-only copy** of active Hermes hooks. Verify but do NOT overwrite active hooks:

```bash
diff -rq $LOCALAPPDATA/hermes/hooks/ workspace/.github/hooks/
```

If the reference copy is stale, sync from active → reference (never reference → active).

### Step 6: Codex note

Codex (OpenAI Codex CLI) uses a fundamentally different architecture:
- **144+ agents** in TOML format at `~/.codex/agents/*.toml`
- **Skills** at `~/.codex/skills/` — typically a `hermes-auto/` bundle with skill subdirectories and a `find-skills` symlink
- Direct skill mirroring from Hermes is NOT applicable; Codex queries its own agent marketplace

If a `hermes-auto` skill exists under Codex, verify it's not stale by spot-checking a few sub-skills against the Hermes originals, but treat Codex as a separate ecosystem.

## Pitfalls

- **Hermes is canonical for skills:** `.github/skills/` is a mirror — sync one direction only (Hermes → .github)
- **Hooks path note:** Active hooks live at `~/AppData/Local/hermes/hooks/` — never overwrite from `.github/hooks/`
- **Codex ≠ direct mirror:** Codex uses TOML agents with `developer_instructions`, not markdown skill files. Don't force Hermes skills into `~/.codex/agents/`
- **Plugin differences may be intentional:** A plugin that's in Hermes but not in `.github/` may be Hermes-specific (e.g., `hermes-achievements`). Check before syncing.
- **File counts can differ from expected:** 140 skill dirs, 4 plugins, 20 hook files is the reference post-sync state. If counts diverge, run drift detection before syncing.