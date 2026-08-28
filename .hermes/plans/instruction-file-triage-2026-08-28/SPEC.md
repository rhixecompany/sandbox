---
title: SPEC — Instruction File Triage System
slug: instruction-triage-spec-2026-08-28
status: approved
created: 2026-08-28T18:30+00:00
---

# SPEC — Instruction File Triage System

## 1. Purpose

Provide a deterministic, DRY, MCP-first system for:
- **Searching/identifying** all instruction-style files (SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules, copilot-instructions.md) across the SandBox workspace and all Hermes profiles
- **Listing** them with per-file metadata (path, size, line count, classification, last-modified)
- **Triaging** each into a category: `canonical`, `duplicate`, `bloat`, `stale`, `conflicting`, `unknown`
- **Debugging** common pathologies (frontmatter corruption, broken links, dead paths)
- **Fixing** with whitelisted auto-repairs (line-cap, dedup pointers, stale-default patches)
- **Enhancing** with DRY cross-references and best-practice structure
- **Verifying** that all gates pass

## 2. Scope

### In scope
- 8 instruction file types × 251 files = ~251 triage entries
- 7 Hermes profiles + 17 sub-projects + root
- All `.md` files matching the 8 patterns; `.cursorrules` is bare (no extension)
- Auto-classify based on:
  - Path (profile root vs project subdir)
  - Size (line count vs cap)
  - Content (presence of known canonical rules)
  - Cross-reference (does it duplicate a rule from canonical SOUL.md?)

### Out of scope
- Files inside `node_modules/`, `.git/`, `cache/`, `spawn-trees/`, `pending/`, `pastes/`, `hermes-agent/` source
- Profile-specific plugin manifests (`plugin.yaml`)
- Skill files themselves (different governance)

## 3. Classification Rules

| Class | Rule |
| ----- | ---- |
| `canonical` | Lives at profile root or workspace root; < 250 lines; unique (not duplicating siblings) |
| `duplicate` | Same file type in same scope (e.g. project has 2 AGENTS.md) OR same rule appears in 3+ files |
| `bloat` | > 250 lines OR > 10 KB OR contains > 5 H1 headings OR has > 30 bullet items in one section |
| `stale` | References a known-retired model/path (e.g. `minimax/minimax-m3:free` as default, or `Bash/` instead of `projects/Bash/`) |
| `conflicting` | Contains a rule that directly contradicts canonical (e.g. "always use PowerShell" vs "always use bash") |
| `unknown` | Doesn't match any other pattern; needs human review |

## 4. Output Schema

```json
{
  "schema_version": 1,
  "generated_at": "2026-08-28T18:35:00Z",
  "scope": "C:/Users/Alexa/Desktop/SandBox + C:/Users/Alexa/AppData/Local/hermes",
  "totals": {
    "files": 251,
    "canonical": 30,
    "duplicate": 12,
    "bloat": 8,
    "stale": 15,
    "conflicting": 2,
    "unknown": 184
  },
  "files": [
    {
      "path": "C:/Users/Alexa/Desktop/SandBox/SOUL.md",
      "type": "SOUL.md",
      "size_bytes": 12345,
      "line_count": 312,
      "classification": "bloat",
      "issues": ["exceeds_250_line_cap"],
      "last_modified": "2026-08-19T12:00:00Z"
    }
  ],
  "cross_refs": {
    "mcp_first_rule": ["SOUL.md", "USER.md", "AGENTS.md", ".hermes.md"],
    "profile_routing_table": ["SOUL.md", "AGENTS.md", ".hermes.md"]
  }
}
```

## 5. Script Architecture

### 5.1 `scripts/instruction_audit.py`
- **Read-only**. Pure stdlib (`pathlib`, `re`, `json`).
- Walks: `C:/Users/Alexa/Desktop/SandBox` + `C:/Users/Alexa/AppData/Local/hermes`
- Skips: `node_modules`, `.git`, `cache`, `spawn-trees`, `pending`, `pastes`, `hermes-agent/` source, `.venv*`, `desktop/dist`
- Emits: `scripts/.runtime/instruction-audit.json` + `.hermes/plans/instruction-file-triage-2026-08-28/audit-report.json` (copy)
- Exit codes: 0 = success, 2 = scan error

### 5.2 `scripts/instruction_fix.py`
- **Whitelist-only auto-fixer**. Stdlib only.
- Flags: `--dry-run` (default), `--apply`, `--type <SOUL.md|...>`, `--path <glob>`
- Whitelisted repairs:
  1. Remove lines with 3+ trailing whitespace (markdownlint MD009)
  2. Replace `minimax/minimax-m3:free` → `nvidia/nemotron-3-ultra-550b-a55b:free` (stale default)
  3. Replace `Bash/` → `projects/Bash/` (path migration)
  4. Replace `Resume_maker/` → `projects/Resume_maker/` (path migration)
  5. Trim trailing newlines > 2 consecutive
- NEVER: merge blocks, change frontmatter structure, rename files, delete content

### 5.3 Skill `instruction-triage` (publishes under `agent-core-architecture/`)
- `SKILL.md` (≤250 lines): workflow + checklist + commands
- `references/classification-rules.md`: detailed rules per class
- `references/whitelist-fixes.md`: exact replacements with rationale
- `references/output-schema.md`: JSON schema
- `scripts/audit.sh`: bash wrapper (calls audit.py)
- `scripts/fix.sh`: bash wrapper (calls fix.py)
- `templates/audit-report.json`: skeleton
- `templates/whitelist-fixes.json`: edit-this-file to add new rules

## 6. Prompt

`.github/prompts/instruction-triage.prompt.md` — human invocation:
- Phase 1: audit (read-only)
- Phase 2: review report
- Phase 3: fix (whitelist only, --dry-run first)
- Phase 4: enhance (manual)
- Phase 5: verify

## 7. Verification Gates (V1-V6)

| Gate | Check |
| ---- | ----- |
| V1 | `python scripts/instruction_audit.py` exits 0, 251 files scanned |
| V2 | `audit-report.json` valid JSON, has all required fields |
| V3 | `instruction_fix.py --dry-run` exits 0, zero files changed |
| V4 | Skill `instruction-triage` in `hermes skills list` |
| V5 | SKILL.md ≤250 lines |
| V6 | No `.bak`, `.backup`, `.old` files created |

## 8. Risk Matrix

| Risk | Severity | Mitigation |
| ---- | -------- | ---------- |
| Auto-fix corrupts frontmatter | High | Whitelist-only, never merge blocks, parse YAML pre/post |
| 251 files too large for one pass | Med | Batch to ≤7 files/run; show progress |
| Stale model references | Low | Static string replace with known-good list |
| User not on board with edits | Med | Default --dry-run, require --apply for mutations |

## 9. Open Questions

- None blocking. Audit report will surface findings for user decision.
