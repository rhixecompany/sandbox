---
name: profile-directive-sync
title: "Profile Directive Sync"
author: Hermes Agent
version: 1.0.0
description: Use when propagating root SOUL.md/USER.md/MEMORY.md changes to all Hermes profiles. Reads root canonical files and adapts them per-profile (header, identity, role), writes to each profile directory.
category: devops
license: MIT
metadata:
  hermes:
    tags: []
---
# profile-directive-sync

Propagates the root `SOUL.md`, `USER.md`, and `MEMORY.md` to all 6 Hermes profiles, adapting only the profile-specific identity header lines.

## Overview

Automated reasoning and workflow tool for `profile-directive-sync`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Workflow

### 1. Read root canonical files
Read `~/AppData/Local/hermes/SOUL.md`, `~/AppData/Local/hermes/memories/USER.md`, `~/AppData/Local/hermes/memories/MEMORY.md`.

### 2. Validate root files first
Before syncing, check size limits and schema compliance:
- **USER.md**: must be ≤ 2000 bytes; must have YAML frontmatter + `## Identity`, `## Model`, `## Execution Preferences` headings. If over limit or missing headings, compact **first** before syncing (see `references/user-md-compaction.md`).
- **MEMORY.md**: must be ≤ 6000 chars (not bytes — Unicode chars). If over limit, compact.
- **SOUL.md**: no hard size limit but `grep -c "^## "` should be ≥ 4 (Persona, Cognitive Style, Execution Frameworks, Standing Rules, Memory Hierarchy).
- If any root file fails, fix it locally before propagating — don't push broken files to profiles.

### 3. Profile adaptations per file

**SOUL.md adaptations:**
- `**Profile:** default` → `**Profile:** <name>`
- `**Identity:** OWL: pragmatic senior engineer...` → `<profile-tagline>`

**USER.md adaptations:**
- `# USER.md — default profile` → `# USER.md — <name> profile`
- `- Profile: default` → `- Profile: <name>`
- Add `| Role: <role>` to the Identity line (e.g., `| Role: Operations`)
- Model line: non-default profiles use their profile-assigned model, not the root's default fallback chain

**MEMORY.md:**
- Same root content for all profiles (universal agent notes)

### 4. Identity taglines map

| Profile | Tagline | Role |
|---------|---------|------|
| alexa | OWL: Operations engineer. Direct, efficient, pragmatic. | Operations |
| code-architect | OWL: Software architect. Deep analysis, clean design, pragmatic trade-offs. | Code architect |
| creative-director | OWL: Creative director. Design thinking, visual polish, brand consistency. | Creative director |
| exec-assistant | OWL: Executive assistant. Structured, thorough, anticipatory. | Executive assistant |
| patient-tutor | OWL: Patient tutor. Explain step-by-step, build understanding, verify comprehension. | Patient tutor |
| research-analyst | OWL: Research analyst. Deep research, evidence-based conclusions, thorough documentation. | Research analyst |

### 5. Execute per profile

For each profile directory under `~/AppData/Local/hermes/profiles/<name>/memories/`:

1. **SOUL.md** — adapt header + identity, write to `profiles/<name>/SOUL.md`
2. **USER.md** — adapt headings + model, compact if needed (≤ 2000B), write to `profiles/<name>/memories/USER.md`
3. **MEMORY.md** — copy verbatim to `profiles/<name>/memories/MEMORY.md`

**Critical**: Write_file calls to non-default profiles require `cross_profile=True` — the tool blocks cross-profile writes by default. Always append this flag or the write silently fails.

```python
# From execute_code or direct tool call
write_file(path="profiles/<name>/memories/USER.md", content=..., cross_profile=True)
```

### 6. Verify — run validate-memories script

After syncing all profiles, run the validator:
```bash
python3 "C:/Users/Alexa/AppData/Local/hermes/skills/devops/validate-memories/scripts/validate_memories.py"
```

Expect exit code 0 with all 21 files passing (7 profiles × SOUL/USER/MEMORY). If any fail, inspect the specific failure message — common causes: missing heading names, size over limit, YAML frontmatter issues.

### 7. Update SESSION_REPORT.md
Log what was synced (which files, which profiles, which root changes triggered the sync).

## Pitfalls

| Pitfall | Mitigation |
|---------|------------|
| **Cross-profile guard blocks writes** | Always pass `cross_profile=True` on write_file calls to non-default profiles. Without it, the tool returns success but the file isn't written. |
| **USER.md heading mismatch** | The validate-memories script checks for literal `## Execution Preferences` heading (not `## Preferences` or `## Execution`). Match exactly or the file fails schema validation even with correct content. |
| **Model line in profile USER.md** | Profile USER.md should show the profile's assigned model (from `hermes profile list`), not the root config default. Root has fallback chain; profiles typically have a single model. |
| **Size limits are byte-oriented** | `wc -c` measures bytes. For ASCII text files bytes ≈ chars, but be precise: USER_LIMIT=2000 (bytes), MEMORY_LIMIT=6000 (chars). Use `python3 -c "len(open(path).read())"` for char count. |
| **Root USER.md model goes stale** | The profile-directive-sync workflow automatically propagates root changes, but if root USER.md itself has stale data (e.g., model from months ago), fix root first before syncing. Cross-check against `hermes config show`. |
| **MEMORY.md anti-bloat rule** | Keep MEMORY.md under 6000 chars. Compact by removing temporal details and verbose explanations. The `|Anti-bloat rule:` header line is a convention marker, not content — keep it. |

## References

- `references/user-md-compaction.md` — Schema-compliant USER.md compaction patterns, heading requirements, and size limit details.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Profile Directive Sync" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## When to Use


- propagating root SOUL
- **Triggers**: ""profile directive sync"" required for a project

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
