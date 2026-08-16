# Disk Cleanup Skill Implementation Plan

**Date:** 2026-08-16  
**Goal:** Implement disk-cleanup, disk-space-cleanup, and cleanup-disk skills fully.

---

## Overview

Three related skills for disk cleanup operations in the Hermes ecosystem:

1. **disk-cleanup** (devops/) — Hermes bundled plugin for internal agent artifacts
2. **disk-space-cleanup** (devops/) — Full-sweep cleanup using cleanup_disk.py script
3. **cleanup-disk** (development/) — Wrapper skill for cleanup_disk.py script

---

## Skill 1: disk-cleanup (devops/)

**Current state:** Skill exists but may need full implementation. This is a Hermes bundled plugin.

**SKILL.md requirements:**
- YAML frontmatter with name, description, version, author, license, tags
- Clear trigger conditions (when to use / when NOT to use)
- Workflow phases (≥3 phases with entry/exit checks)
- Commands reference (`/disk-cleanup status`, `dry-run`, `quick`, `deep`, `track`, `forget`)
- Pitfalls section
- Verification checklist
- References to related skills

**Implementation steps:**
1. Read current SKILL.md if it exists
2. Add missing frontmatter fields
3. Add workflow phases with entry/exit checks
4. Add commands reference table
5. Add pitfalls (active log files, Hermes root filtering, temp folder pitfalls)
6. Add verification checklist
7. Add references

---

## Skill 2: disk-space-cleanup (devops/)

**Current state:** Skill exists at `devops/disk-space-cleanup/SKILL.md`. Full-sweep cleanup using `cleanup_disk.py` script.

**Current content (from memory):**
- Trigger: User wants more disk space
- Canonical script: `~/Desktop/SandBox/scripts/cleanup_disk.py`
- Workflow: measure → dry-run → approve → apply → verify
- Categories: deps, archive, cache, logs
- Hermes root: conservative cats only (cache, logs, archive)
- Temp folder: age-based cleanup
- Bloated .git: git gc --prune=now
- App uninstall: winget inventory → approve → uninstall
- Pitfalls: argparse abbreviation, double-counting, Windows path conversion, temp rmtree, Hermes root deps

**Implementation steps:**
1. Read current SKILL.md
2. Verify YAML frontmatter (name, description)
3. Ensure workflow phases are clearly structured with entry/exit checks
4. Verify all commands are accurate and tested
5. Add verification checklist
6. Add cross-references to related skills (cleanup-disk, disk-cleanup)
7. Ensure pitfalls section is comprehensive

---

## Skill 3: cleanup-disk (development/)

**Current state:** Wrapper skill for `cleanup_disk.py` script at `~/AppData/Local/hermes/scripts/cleanup_disk.py`.

**Implementation steps:**
1. Create SKILL.md if missing
2. Add YAML frontmatter
3. Document script location and usage
4. Add workflow phases (setup, run, verify)
5. Add when to use / when NOT to use
6. Add verification checklist
7. Add pitfalls (Python venv, execution policy, etc.)

---

## Cross-Cutting Concerns

### Shared Script: cleanup_disk.py
Location: `~/AppData/Local/hermes/scripts/cleanup_disk.py`

All three skills reference this script. The script:
- Categories: deps, archive, cache, logs
- Dry-run-first approach
- Safe hermes-root filtering
- Windows/MSYS path handling

### Skill Relationships
- `disk-cleanup` (plugin, internal artifacts) → narrow scope
- `disk-space-cleanup` (full-sweep, script-based) → broad scope
- `cleanup-disk` (wrapper, script-focused) → development/ context

### References to Include
- cleanup_disk.py source code reference
- Hermes Agent disk cleanup plugin docs
- Windows/MSYS path handling notes
- Git gc documentation

---

## Implementation Order

1. **disk-space-cleanup** (most comprehensive — anchor skill)
2. **disk-cleanup** (plugin — narrower, builds on disk-space-cleanup concepts)
3. **cleanup-disk** (wrapper — simplest, references the script)

---

## Verification Checklist

- [ ] All three SKILL.md files have valid YAML frontmatter (name, description, version, author, license, tags)
- [ ] All three have ≥3 workflow phases with entry/exit checks
- [ ] All three have pitfalls sections
- [ ] All three have verification checklists
- [ ] Commands are accurate and tested
- [ ] References are cited
- [ ] Progressive disclosure: common workflow first, edge cases later
- [ ] No external dependencies without documentation
- [ ] Cross-references between skills are correct
