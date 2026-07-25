# Cross-Reference Verification: Skill References in Prompts

After batch-fixing prompt frontmatter, run this cross-reference check to
ensure all `skill:` references in `dependencies:` resolve to real skills.

## The Problem

Prompts declare dependencies via:
```yaml
dependencies:
    - skill:brainstorming
    - skill:plans-and-specs
    - skill:copilot-cli  # BROKEN — actual skill is copilot-cli-quickstart
```

And there's a separate `skills:` field for constraint flags:
```yaml
skills:
    - introspection-only-general  # NOT a skill-loading directive
```

Confusing `skills:` entries with broken `skill:` refs is the #1 pitfall.

## Verification — Two Methods

### Method A: grep-based (quick, may miss hub/plugin skills)

```bash
# Get all actual Hermes skill names from SKILL.md files
grep -rh '^name:' $(find $LOCALAPPDATA/hermes/skills -name 'SKILL.md') \
  | sed 's/^name: *//' | sed 's/^"//;s/"$//' | sort -u > /tmp/actual_skills.txt

# Get all skill: references from dependencies: in prompts
cd ~/Desktop/SandBox/prompts
grep -h 'skill:' *.prompt.md | grep -oP 'skill:[a-zA-Z0-9_-]+' \
  | sed 's/^skill://' | sort -u > /tmp/ref_skills.txt

# Find missing - exclude known non-skills
grep -vf /tmp/actual_skills.txt /tmp/ref_skills.txt \
  | grep -v '^prompt$' | grep -v '^provider$'
```

### Method B: skills_list API (authoritative — catches plugin, hub, deduplicated)

Use from `execute_code` for the definitive set of all skills the runtime knows:

```python
from hermes_tools import tool_call

result = tool_call("skills_list")
actual_skills = {s["name"] for s in result.get("skills", [])}

# Extract from prompt files and diff
ref_skills = set()
# ... collect skill:xxx refs from dependencies: ...
missing = ref_skills - actual_skills
print(f"Unresolved refs: {missing}")
```

## Known Non-Skill Patterns

| Pattern | Reason |
|---------|--------|
| `skill:prompt:xxx.prompt.md` | Regex extracts `prompt` prefix from `prompt:` namespace |
| `skill:provider:hermes-auth` | Regex extracts `provider` prefix from `provider:` namespace |
| `execute_code`, `patch`, `terminal`, `write_file` | These are MCP tools, not skills |

## Detection: Malformed Dependency Prefixes

```bash
# Find skill:prompt:xxx (should be prompt:xxx)
find ~/Desktop/SandBox/prompts -name '*.prompt.md' -exec \
  grep -n 'skill:prompt:\|skill:provider:' {} +

# Extract all dependency refs and cross-reference against real skills
grep -h '\(skill:\|prompt:\|tool:\)' ~/Desktop/SandBox/prompts/*.prompt.md \
  | grep -o '\(skill:\|prompt:\|tool:\)[a-zA-Z0-9_-]\+' | sort -u
```

## Detection: Duplicate Dependency Entries

Prompts may list the same dependency twice:

```bash
for f in prompts/*.prompt.md; do
  dupes=$(grep -oP '(skill|prompt|tool):[a-zA-Z0-9_.-]+' "$f" | sort | uniq -d)
  [ -n "$dupes" ] && echo "$f: DUPLICATES → $dupes"
done
```

Fix by removing the extra entry.

## Detection: Leading `/` in Skill Refs

Some prompts reference skills with a leading `/` (e.g. `/context-map`). These won't resolve:

```bash
grep -rn 'skill:/' prompts/*.prompt.md
grep -rn 'prompt:/' prompts/*.prompt.md
```

Fix: strip the leading `/`.

## Remediation

| Found Pattern | Corrected | Example |
|---------------|-----------|---------|
| `skill:prompt:xxx.prompt.md` | `prompt:xxx` | `skill:prompt:context-map.prompt.md` → `prompt:context-map` |
| `skill:provider:yyy` | (depends) | `skill:provider:hermes-auth` → `skill:test-providers-models` |
| `skill:creating-skills` | `skill:skill-creator` | Rename |
| `/context-map` | `context-map` | Strip leading `/` |
| `/prompt-engineering` | `prompt-engineering` | Strip leading `/` |

## Fix Actions

When a reference is missing:
1. **Rename ref** — skill exists under different name
2. **Create skill** — genuinely missing with documented purpose
3. **Note artifact** — parsing artifact from `skill:prompt:`/`skill:provider:` syntax