---
name: profile-skills-enhancement-spec
title: Hermes Profile Skills Enhancement — Specification
description: Specification for enhancing existing and creating missing Hermes profile management skills with DRY principles, best practices, tools, hooks, and quick commands
date: 2026-08-15
status: draft
---

# Hermes Profile Skills Enhancement — Specification

## 1. Overview

Enhance 3 existing profile management skills and create 3 missing ones, forming a complete DRY cross-referenced skill network for Hermes profile lifecycle management. All skills follow SKILL.md best practices with YAML frontmatter, structured workflow, pitfalls, verification checklists, and cross-references.

## 2. Skill Inventory — Current vs Target State

### 2.1 Existing Skills (to enhance)

| Skill | Location | Current State | Target State |
|--------|----------|---------------|--------------|
| `soul-enhancer` | `~/AppData/Local/hermes/skills/devops/soul-enhancer/` | SKILL.md (197L) + `enhance_soul.py` (169L). Validates SOUL.md structure. Has `--check`/`--fix`/`--apply-template`/`--mirror` modes. | Fix REQUIRED_SECTIONS to match actual SOUL.md format. Add `--propagate` mode. Add `--discover-profiles`. Cross-reference `hermes-personality-soul`. Add validation hook. |
| `hermes-profile-sync` | `~/AppData/Local/hermes/skills/development/hermes-profile-sync/` | SKILL.md (115L) + 2 scripts. Config sync only. Hardcoded 13-profile list. | Add dynamic profile discovery. Add memory sync delegation to `hermes-profile-memory-sync`. Add `--dry-run`. Add quick commands. |
| `hermes-profile-memory-sync` | `~/AppData/Local/hermes/skills/hermes-profile-memory-sync/` | SKILL.md (147L) + references. Most comprehensive. Covers memory files + aliases + clone-drift fix. | Add `--dry-run`. Add profile discovery. Add alias creation as documented subcommand. Better integration with `validate_memories.py`. |

### 2.2 Missing Skills (to create)

| Skill | Trigger | Purpose | Target Location |
|--------|---------|---------|-----------------|
| `hermes-personality-soul` | `/hermes-personality-soul` | Persona→tone→traits mapping for all 14 Hermes profiles. Reference for SOUL.md personality sections. | `~/AppData/Local/hermes/skills/profiles/hermes-personality-soul/` |
| `create-missing-souls` | `/create-missing-souls` | Discover profiles missing SOUL.md or with stub SOUL.md. Apply minimal template. Cross-reference personality skill. | `~/AppData/Local/hermes/skills/profiles/create-missing-souls/` |
| `create-missing-memories` | `/create-missing-memories` | Discover profiles missing USER.md/MEMORY.md. Create from root canonical templates. Validate schema. | `~/AppData/Local/hermes/skills/profiles/create-missing-memories/` |

### 2.3 Skills to Leave As-Is (already adequate)

| Skill | Reason |
|--------|--------|
| `profile-maintenance` | Comprehensive standalone skill for USER.md/MEMORY.md/SOUL.md audit. 289 lines. Well-documented. |
| `hermes-profiles` | Thin orchestration wrapper. Will be updated to cross-reference enhanced skills. |

## 3. Skill Specifications

### 3.1 `soul-enhancer` (Enhance)

#### Changes to SKILL.md
- Fix `REQUIRED_SECTIONS` in script: replace `## Architectural Invariants` with the actual section names from the current root SOUL.md format
- Add `## Skills Required` table referencing `hermes-personality-soul`
- Add `## Quick Commands` section with:
  - `python enhance_soul.py --check` — validate all profiles
  - `python enhance_soul.py --fix` — repair headers
  - `python enhance_soul.py --propagate` — propagate root headers to profiles
  - `python enhance_soul.py --discover-profiles` — auto-discover from `hermes profile list`
- Add post-enhancement validation hook reference

#### Changes to `enhance_soul.py`
- Fix `REQUIRED_SECTIONS` list to match actual SOUL.md format
- Add `--propagate` flag: reads root SOUL.md, updates profile SOUL.md `**Profile:**` headers and `**Identity:**` lines
- Add `--discover-profiles` flag: runs `hermes profile list` subprocess to get profile names instead of hardcoding
- Add `propagate_one()` function
- Add post-propagation validation (re-run `check_one` after propagate)

### 3.2 `hermes-personality-soul` (Create)

#### SKILL.md Structure
```markdown
---
name: hermes-personality-soul
title: Hermes Personality & SOUL.md Reference
description: Persona→tone→traits mapping for all 14 Hermes profiles. Reference for SOUL.md personality sections and soul-enhancer persona mapping.
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, profiles, personality, soul, identity]
---

# Hermes Personality & SOUL.md Reference

## Overview
Mapping of all 14 Hermes profiles to their persona, tone, and SOUL.md personality section content.

## Profile Personality Table
(14 rows: profile | persona label | tone | 3 traits | SOUL.md Identity line)

## Persona Mapping (for soul-enhancer)
Same data in script-parseable format.

## SOUL.md Personality Section Template
Minimal template for profile SOUL.md Identity & Tone section.

## Cross-References
- soul-enhancer: uses this for persona mapping
- create-missing-souls: uses this for identity content
- profile-soul-minimal-template: uses this for examples
```

#### Supported Profiles (14)
From `hermes profile list`: default, alexa, code-architect, creative-director, cto, designer, dev, exec-assistant, ops, patient-tutor, pm, qa, research-analyst, security

#### Persona Assignments
From `.hermes.md` profile table + `profile.yaml` descriptions:
- default → General-purpose assistant
- alexa → Operations engineer
- code-architect → Senior software engineer (TDD-first)
- creative-director → Creative director
- cto → Chief technology officer
- designer → Product designer
- dev → Software developer
- exec-assistant → Executive assistant
- ops → Operations engineer
- patient-tutor → Patient tutor
- pm → Product manager
- qa → Quality engineer
- research-analyst → Research analyst
- security → Security engineer

### 3.3 `create-missing-souls` (Create)

#### SKILL.md Structure
```markdown
---
name: create-missing-souls
title: Create Missing Profile SOUL.md Files
description: Discover profiles missing SOUL.md or with stub SOUL.md. Apply minimal template with identity from hermes-personality-soul. Cross-reference personality skill.
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, profiles, soul, create, identity]
---

# Create Missing Profile SOUL.md Files

## Overview
Discovers all Hermes profiles, checks SOUL.md state, creates missing/stub files using the minimal template from hermes-personality-soul.

## Workflow
1. Discover profiles via `hermes profile list`
2. Check each profile's SOUL.md (exists? size? has header? has identity?)
3. For missing/stub: create from `profile-soul-minimal-template.md` + personality data
4. Write with `cross_profile=True`
5. Verify with `validate_memories.py` or manual grep checks

## Quick Commands
- `python create_missing_souls.py --dry-run` — show what would be created
- `python create_missing_souls.py --apply` — create missing files
- `python create_missing_souls.py --profile <name>` — single profile

## Cross-References
- hermes-personality-soul: identity/tone content source
- profile-soul-minimal-template: template source
- soul-enhancer: post-creation validation
- hermes-profile-memory-sync: broader profile memory management
```

### 3.4 `create-missing-memories` (Create)

#### SKILL.md Structure
```markdown
---
name: create-missing-memories
title: Create Missing Profile Memory Files
description: Discover profiles missing USER.md/MEMORY.md. Create from root canonical templates. Validate schema and size limits.
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, profiles, memory, create, user, memories]
---

# Create Missing Profile Memory Files

## Overview
Discovers all Hermes profiles, checks for USER.md/MEMORY.md presence, creates missing files from root canonical templates with per-profile customization.

## Workflow
1. Discover profiles via `hermes profile list`
2. Check each profile's memories/ dir (exists? USER.md? MEMORY.md?)
3. For missing: create MEMORY.md (verbatim from root), create USER.md (per-profile authored)
4. Validate size limits (USER ≤ 2000B, MEMORY ≤ 6000 chars)
5. Verify with `validate_memories.py`

## Quick Commands
- `python create_missing_memories.py --dry-run`
- `python create_missing_memories.py --apply`
- `python create_missing_memories.py --profile <name>`

## Cross-References
- profile-maintenance: schema and audit reference
- hermes-profile-memory-sync: broader memory management
- validate-memories: verification
```

### 3.5 `hermes-profile-sync` (Enhance)

#### Changes to SKILL.md
- Replace hardcoded PROFILES list with dynamic discovery
- Add `--dry-run` to all script invocations
- Add memory sync delegation section referencing `hermes-profile-memory-sync`
- Add quick commands section:
  - `python sync_profile_configs.py` — config sync (normal)
  - `python sync_profile_configs.py --force` — config sync (overwrite secrets)
  - `python sync_profile_memories.py` — memory file sync
  - `python profile_discover.py` — discover all profile states
- Add `## Skills Required` table referencing `hermes-profile-memory-sync`

#### Changes to `sync_profile_configs.py`
- Add `--discover` flag: run `hermes profile list` to get profile names
- Keep hardcoded list as fallback

### 3.6 `hermes-profile-memory-sync` (Enhance)

#### Changes to SKILL.md
- Add `--dry-run` to all workflow steps
- Add profile discovery note (always run `hermes profile list` first)
- Add alias creation as explicit subcommand in Quick Commands
- Add `## Skills Required` table referencing `create-missing-souls` and `create-missing-memories`
- Add post-sync verification hook

## 4. Tools to Create

### 4.1 `profile_discover.py`
Location: `~/AppData/Local/hermes/scripts/profile_discover.py`

Purpose: Discover all Hermes profiles and their state (SOUL.md, USER.md, MEMORY.md existence, sizes, header status).

```python
#!/usr/bin/env python3
"""Discover all Hermes profiles and report SOUL.md/USER.md/MEMORY.md state."""
import subprocess, sys, os, yaml
from pathlib import Path

HERMES = os.path.expanduser("~/AppData/Local/hermes")

def discover_profiles():
    """Run `hermes profile list` and parse output."""
    try:
        result = subprocess.run(
            ["hermes", "profile", "list"],
            capture_output=True, text=True, timeout=30
        )
        # Parse table format
        profiles = []
        for line in result.stdout.splitlines():
            if line.strip().startswith("◆") or line.strip().startswith(" ") and not line.startswith("─"):
                parts = line.split()
                if len(parts) >= 2:
                    name = parts[0].replace("◆", "").strip()
                    if name and name != "Profile":
                        profiles.append(name)
        return profiles
    except Exception:
        # Fallback: directory listing
        profiles_dir = Path(HERMES) / "profiles"
        if profiles_dir.exists():
            return sorted(d.name for d in profiles_dir.iterdir() if d.is_dir())
        return []

def check_soul(profile):
    soul_path = Path(HERMES) / "profiles" / profile / "SOUL.md"
    if not soul_path.exists():
        return {"exists": False, "size": 0, "lines": 0, "has_header": False, "has_identity": False}
    text = soul_path.read_text()
    return {
        "exists": True,
        "size": len(text),
        "lines": len(text.splitlines()),
        "has_header": "**Profile:**" in text,
        "has_identity": "**Identity:**" in text,
    }

def check_memories(profile):
    mem_dir = Path(HERMES) / "profiles" / profile / "memories"
    user_path = mem_dir / "USER.md"
    memory_path = mem_dir / "MEMORY.md"
    return {
        "memories_dir": mem_dir.exists(),
        "USER.md": {"exists": user_path.exists(), "size": user_path.stat().st_size if user_path.exists() else 0},
        "MEMORY.md": {"exists": memory_path.exists(), "size": memory_path.stat().st_size if memory_path.exists() else 0},
    }

def main():
    profiles = discover_profiles()
    print(f"Found {len(profiles)} profiles: {', '.join(profiles)}")
    print()
    for p in profiles:
        soul = check_soul(p)
        mem = check_memories(p)
        status = []
        if not soul["exists"]:
            status.append("SOUL:MISSING")
        elif not soul["has_header"]:
            status.append(f"SOUL:NO-HDR({soul['size']}B)")
        elif not soul["has_identity"]:
            status.append(f"SOUL:NO-ID({soul['size']}B)")
        else:
            status.append(f"SOUL:OK({soul['size']}B)")
        if not mem["memories_dir"]:
            status.append("MEM:DIR-MISSING")
        else:
            if not mem["USER.md"]["exists"]:
                status.append("USER:MISSING")
            elif mem["USER.md"]["size"] > 2000:
                status.append(f"USER:OVERSIZE({mem['USER.md']['size']}B)")
            else:
                status.append(f"USER:OK({mem['USER.md']['size']}B)")
            if not mem["MEMORY.md"]["exists"]:
                status.append("MEM:MISSING")
            elif mem["MEMORY.md"]["size"] > 6000:
                status.append(f"MEM:OVERSIZE({mem['MEMORY.md']['size']}B)")
            else:
                status.append(f"MEM:OK({mem['MEMORY.md']['size']}B)")
        print(f"  {p:20s} | {' | '.join(status)}")

if __name__ == "__main__":
    main()
```

### 4.2 `soul_propagate.py`
Location: `~/AppData/Local/hermes/scripts/soul_propagate.py`

Purpose: Propagate root SOUL.md profile headers to all profile SOUL.md files.

```python
#!/usr/bin/env python3
"""Propagate root SOUL.md **Profile:** and **Identity:** headers to profile SOUL.md files."""
import subprocess, sys, os, re
from pathlib import Path

HERMES = os.path.expanduser("~/AppData/Local/hermes")
ROOT_SOUL = Path(HERMES) / "SOUL.md"

PROFILE_RE = re.compile(r"^\*\*Profile:\*\*\s*(\S+)", re.M)
IDENTITY_RE = re.compile(r"^\*\*Identity:\*\*\s*(.+)$", re.M)

def discover_profiles():
    try:
        result = subprocess.run(["hermes", "profile", "list"],
            capture_output=True, text=True, timeout=30)
        profiles = []
        for line in result.stdout.splitlines():
            if line.strip().startswith("◆") or (line.strip() and not line.startswith("─") and not line.startswith("Profile")):
                parts = line.split()
                if parts and parts[0] not in ("Profile", "—", "default"):
                    name = parts[0].replace("◆", "").strip()
                    if name:
                        profiles.append(name)
        return profiles
    except Exception:
        return []

def propagate_one(profile, dry_run=False):
    target = Path(HERMES) / "profiles" / profile / "SOUL.md"
    if not target.exists():
        print(f"  {profile}: SKIP (no SOUL.md)")
        return
    
    text = target.read_text()
    root_text = ROOT_SOUL.read_text()
    
    # Extract root's Profile and Identity
    root_profile = PROFILE_RE.search(root_text)
    root_identity = IDENTITY_RE.search(root_text)
    
    # For profile SOUL.md, we use the profile's own name + a generic identity
    # The profile's identity comes from hermes-personality-soul, not root
    profile_name = profile
    profile_identity = f"OWL: {profile} profile. See parent SOUL.md for shared standards."
    
    changes = []
    
    # Fix Profile header if wrong
    existing_profile = PROFILE_RE.search(text)
    if existing_profile:
        if existing_profile.group(1) != profile_name:
            new_text = PROFILE_RE.sub(f"**Profile:** {profile_name}", text, count=1)
            if not dry_run:
                target.write_text(new_text)
            changes.append(f"fixed Profile header")
    else:
        # Add Profile header after the first line
        first_line_end = text.find("\n")
        if first_line_end > 0:
            new_text = text[:first_line_end] + f"\n**Profile:** {profile_name} |" + text[first_line_end:]
            if not dry_run:
                target.write_text(new_text)
            changes.append(f"added Profile header")
    
    # Fix Identity if missing or stale
    existing_identity = IDENTITY_RE.search(text)
    if not existing_identity:
        # Add after Profile line
        profile_line_end = text.find("\n", text.find("**Profile:**"))
        if profile_line_end > 0:
            new_text = text[:profile_line_end] + f"\n**Identity:** {profile_identity}" + text[profile_line_end:]
            if not dry_run:
                target.write_text(new_text)
            changes.append(f"added Identity line")
        else:
            changes.append(f"could not place Identity (no Profile line found)")
    elif existing_identity.group(1).startswith("OWL:"):
        # Check if it's a stub identity (just says the profile name)
        if existing_identity.group(1).strip() == f"OWL: {profile} profile.":
            changes.append(f"Identity is stub — recommend running create-missing-souls for full identity")
    
    if changes:
        action = "DRY-RUN" if dry_run else "UPDATED"
        print(f"  {profile}: {action} — {', '.join(changes)}")
    else:
        print(f"  {profile}: OK (no changes needed)")

def main():
    dry_run = "--dry-run" in sys.argv
    profile = None
    if "--profile" in sys.argv:
        idx = sys.argv.index("--profile")
        profile = sys.argv[idx + 1]
    
    if profile:
        propagate_one(profile, dry_run)
    else:
        profiles = discover_profiles()
        print(f"Propagating to {len(profiles)} profiles...")
        for p in profiles:
            propagate_one(p, dry_run)
    print("DONE." if not dry_run else "DRY-RUN complete. Remove --dry-run to apply.")

if __name__ == "__main__":
    main()
```

## 5. Hooks to Create/Reference

### 5.1 Post-Soul-Enhancement Hook
A lightweight validation hook that runs after soul enhancement operations.

Location: `~/AppData/Local/hermes/hooks/post-soul-enhancement/validate_soul.sh`

```bash
#!/usr/bin/env bash
# Post-soul-enhancement validation hook
# Runs after soul-enhancer --propagate or --fix operations
# Validates that all profile SOUL.md files have correct headers

set -euo pipefail

HERMES="${HERMES_HOME:-$HOME/AppData/Local/hermes}"
FAILURES=0

echo "== Post-soul-enhancement validation =="
for dir in "$HERMES"/profiles/*/; do
  name=$(basename "$dir")
  soul="$dir/SOUL.md"
  if [[ ! -f "$soul" ]]; then
    echo "  WARN: $name has no SOUL.md"
    continue
  fi
  if ! grep -q "^## " "$soul"; then
    echo "  FAIL: $name SOUL.md has no ## sections"
    FAILURES=$((FAILURES + 1))
  fi
  if ! grep -q "**Profile:**" "$soul"; then
    echo "  FAIL: $name SOUL.md missing Profile header"
    FAILURES=$((FAILURES + 1))
  fi
done

if [[ $FAILURES -eq 0 ]]; then
  echo "  All profiles OK"
else
  echo "  $FAILURES failure(s) found"
fi

exit $FAILURES
```

### 5.2 Post-Memory-Creation Hook
Validates memory files after creation.

Location: `~/AppData/Local/hermes/hooks/post-memory-creation/validate_memories.sh`

```bash
#!/usr/bin/env bash
# Post-memory-creation validation hook
# Runs validate_memories.py after create-missing-memories operations

set -euo pipefail

HERMES="${HERMES_HOME:-$HOME/AppData/Local/hermes}"
SCRIPT="$HERMES/skills/devops/validate-memories/scripts/validate_memories.py"

echo "== Post-memory-creation validation =="

if [[ ! -f "$SCRIPT" ]]; then
  echo "  WARN: validate_memories.py not found at $SCRIPT"
  exit 0
fi

python "$SCRIPT"
exit_code=$?

if [[ $exit_code -eq 0 ]]; then
  echo "  All memory files valid"
else
  echo "  Validation failed (exit $exit_code)"
fi

exit $exit_code
```

## 6. Quick Commands

### 6.1 Profile Soul Management
```
# Validate all profile SOUL.md files
python ~/AppData/Local/hermes/scripts/soul_propagate.py --dry-run

# Propagate root headers to all profiles
python ~/AppData/Local/hermes/scripts/soul_propagate.py

# Propagate to single profile
python ~/AppData/Local/hermes/scripts/soul_propagate.py --profile alexa

# Discover all profile states
python ~/AppData/Local/hermes/scripts/profile_discover.py

# Enhance/validate all SOUL.md files
python ~/AppData/Local/hermes/skills/devops/soul-enhancer/scripts/enhance_soul.py --check
python ~/AppData/Local/hermes/skills/devops/soul-enhancer/scripts/enhance_soul.py --fix
```

### 6.2 Profile Memory Management
```
# Sync memory files to all profiles
python ~/AppData/Local/hermes/skills/development/hermes-profile-sync/scripts/sync_profile_memories.py

# Create missing memory files
python ~/AppData/Local/hermes/scripts/create_missing_memories.py --apply

# Validate all memory files
python ~/AppData/Local/hermes/skills/devops/validate-memories/scripts/validate_memories.py
```

### 6.3 Full Profile Sync
```
# Sync configs (normal)
python ~/AppData/Local/hermes/skills/development/hermes-profile-sync/scripts/sync_profile_configs.py

# Sync configs (force overwrite)
python ~/AppData/Local/hermes/skills/development/hermes-profile-sync/scripts/sync_profile_configs.py --force

# Full profile refresh (config + memory + SOUL headers)
python ~/AppData/Local/hermes/scripts/profile_discover.py && \
python ~/AppData/Local/hermes/scripts/soul_propagate.py && \
python ~/AppData/Local/hermes/skills/development/hermes-profile-sync/scripts/sync_profile_memories.py
```

## 7. Verification Criteria

### 7.1 Skill Verification
- [ ] All 6 skills have valid YAML frontmatter (name, title, description, version, author, license, tags)
- [ ] All 6 skills have ≥3 workflow phases
- [ ] All 6 skills have Pitfalls section
- [ ] All 6 skills have Verification Checklist
- [ ] All 6 skills have Skills Required table (cross-referencing related skills)
- [ ] All 6 skills are < 250 lines (move detail to references/)
- [ ] All 6 skills reference shared templates where applicable

### 7.2 Script Verification
- [ ] `profile_discover.py` runs without errors, discovers all 14 profiles
- [ ] `soul_propagate.py --dry-run` shows correct profile states
- [ ] `soul_propagate.py` (without --dry-run) correctly updates profile headers
- [ ] `enhance_soul.py --check` passes after fixes
- [ ] `sync_profile_configs.py` discovers profiles dynamically

### 7.3 Hook Verification
- [ ] `validate_soul.sh` runs and reports correctly
- [ ] `validate_memories.sh` runs validate_memories.py correctly

### 7.4 Integration Verification
- [ ] `hermes profile list` shows all 14 profiles
- [ ] All profile SOUL.md files have `**Profile:**` header matching profile name
- [ ] All profile SOUL.md files have `**Identity:**` line
- [ ] All profile memories/ dirs have USER.md and MEMORY.md
- [ ] `validate_memories.py` reports 42/42 passing

## 8. Cross-Reference Matrix

| Skill | References | Referenced By |
|-------|-----------|---------------|
| `soul-enhancer` | `hermes-personality-soul`, `profile-soul-minimal-template.md`, `validate_memories.py` | `create-missing-souls`, `hermes-profiles` |
| `hermes-personality-soul` | `profile-soul-minimal-template.md`, `profile.yaml` descriptions | `soul-enhancer`, `create-missing-souls` |
| `create-missing-souls` | `hermes-personality-soul`, `profile-soul-minimal-template.md`, `sync_profile_memories.py`, `soul_propagate.py` | `hermes-profiles`, `hermes-profile-memory-sync` |
| `create-missing-memories` | `profile-maintenance`, `validate_memories.py`, `sync_profile_memories.py` | `hermes-profile-memory-sync`, `hermes-profiles` |
| `hermes-profile-sync` | `hermes-profile-memory-sync`, `sync_profile_configs.py`, `sync_profile_memories.py`, `profile_discover.py` | `hermes-profiles` |
| `hermes-profile-memory-sync` | `create-missing-souls`, `create-missing-memories`, `profile-soul-drift-fix.md`, `validate_memories.py` | `hermes-profiles`, `hermes-profile-sync` |
| `hermes-profiles` | ALL above | — |

## 9. Implementation Order

Due to dependencies, implement in this order:

1. `hermes-personality-soul` (no dependencies — base reference)
2. `profile_discover.py` + `soul_propagate.py` (tools, no skill dependencies)
3. `create-missing-souls` (depends on #1, #2)
4. `create-missing-memories` (depends on #2)
5. `soul-enhancer` enhancement (depends on #1)
6. `hermes-profile-sync` enhancement (depends on #3, #4)
7. `hermes-profile-memory-sync` enhancement (depends on #3, #4)
8. `hermes-profiles` update (depends on all)
9. Hooks (depend on scripts from #2)
10. Block updates (depend on all skills being created)
