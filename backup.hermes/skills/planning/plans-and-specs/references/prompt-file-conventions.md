# Prompt File Conventions (.prompt.md)

Frontmatter template, section templates, and naming conventions for `.prompt.md` files in `.github/prompts/` and `Prompts/` directories.

## Frontmatter Template

```yaml
---
title: <Display Name> — <Short Descriptor>
trigger: /<kebab-case-name>
tags: [hermes, copilot, <domain>, <category>]
---
```

### Fields

| Field | Required | Convention |
|---|---|---|
| `title` | Yes | `Name — Description`. Use em-dash separator. Capitalized words. |
| `trigger` | Yes | `/kebab-case` — must match filename stem (e.g. `context-map.prompt.md` → `/context-map`) |
| `tags` | Yes | Array of lowercase kebab-case tags. Always include `hermes`, `copilot`, plus domain tags. |

### Real Examples from SandBox

```yaml
# .github/prompts/context-map.prompt.md
title: context-map
trigger: /context-map
tags: [hermes, copilot, opencode, analysis, dependencies, planning]

# Prompts/agents-fix.prompts.md
title: Agents Fix — Sync Agents Across Platforms
trigger: /agents-fix
tags: [hermes, copilot, opencode, agents, migration, sync]
```

## Section Templates

### Description / Goal (opening blockquote)

```
> One-sentence summary of what this prompt does.
```

### Skills Required Table

```
## Skills Required

| Skill | Purpose |
|---|---|
| `skill-name` | What the skill contributes (dependency mapping, structured authoring) |
```

### Phased Workflow

Each phase follows this pattern:

```
### Phase N: Title

**Goal:** One-line goal statement.

**Steps:**
1. Action step with detail
2. Next step

#### Tasks
- Bullet checklist items
- Cross-reference requirements
```

### Verification Checklist

```
## Verification Checklist

- [ ] Criteria 1
- [ ] Criteria 2
```

## File Naming Conventions

| Location | Suffix | Example |
|---|---|---|
| `.github/prompts/` | `.prompt.md` | `context-map.prompt.md` |
| `Prompts/` | `.prompts.md` (expanded) | `agents-fix.prompts.md` |
| `Prompts/` | `.prompts.txt` (source draft) | `agents-fix.prompts.txt` |

## Conversion Path: `.txt` → `.prompts.md`

1. Read the `.txt` as the source of truth for intent and scope
2. Create frontmatter from the first-line summary (or infer from content)
3. Expand into sections: Description → Skills Required → Phases (1-4) → Verification
4. Write to `.prompts.md` (overwriting if it exists — `.txt` is the source)
5. Verify frontmatter validity and section completeness

### Which files get which suffix

- **`.prompts.txt`**: Short-form source draft. 1-10 lines. The "brain dump" version.
- **`.prompts.md`**: Expanded version with full structure. Paired 1:1 with a `.txt` source.
- **`.prompt.md`** (no 's'): Production-ready prompt under `.github/prompts/`. Full spec with inputs, outputs, rules, and tool references.

## Pitfalls

- **Don't skip frontmatter**: Every `.prompt.md`/`.prompts.md` needs valid YAML frontmatter. Tools and agents depend on the `trigger` field.
- **Trigger mismatch**: `trigger: /foo` in frontmatter must match the filename stem (`foo.prompt.md`). Inconsistent triggers confuse agent routing.
- **Missing Skills Required**: Without an explicit skills table, agents don't know which Hermes skills to preload.
- **Flat phases**: Phase sections should contain sub-steps (numbered or tabular), not just a single paragraph.
- **Overwriting `.prompts.md` from `.txt`**: The convert-plaintext-to-md methodology uses the existing `.prompts.md` content as source when it exists (idempotent). To force re-conversion from `.txt`, delete the `.prompts.md` first or pass the `.txt` explicitly.
