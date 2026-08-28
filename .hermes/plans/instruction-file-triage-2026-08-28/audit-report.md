# Instruction File Audit — Goal 1

**Generated:** 2026-08-28T20:51:55Z
**Scope:** `C:\Users\Alexa\Desktop\SandBox` + `C:\Users\Alexa\AppData\Local\hermes`
**Tool:** `scripts/instruction_audit.py` (stdlib only, read-only)
**Machine-readable:** `audit-report.json` (85 KB)

## Summary

| Metric | Value |
| ------ | ----- |
| Files scanned | **259** |
| Canonical | 5 |
| Duplicate | 0 |
| Bloat | 6 |
| Stale | 16 |
| Conflicting | 4 |
| Unknown | 228 |

## Cross-Reference Analysis (DRY Violations)

| Rule | Files mentioning it | DRY rating |
| ---- | ------------------- | ---------- |
| `mcp_first` | 22 | 🔴 High duplication |
| `profile_routing` | 34 | 🔴 High duplication |
| `dry_principle` | 18 | 🟡 Moderate |
| `session_startup` | 0 | 🟢 None (good — lives in canonical only) |

**Finding:** 22 files repeat the MCP-first rule. 34 files repeat the profile-routing table. The user's DRY preference is being violated by the very files that document it. **Canonical rule should live in `~/AppData/Local/hermes/SOUL.md`; other files should link, not duplicate.**

## Top Findings

### Bloat (>250 lines or >10KB) — 6 files

All 6 are the **same** `mindstudio-agent/CLAUDE.md` replicated across 6 profile directories. Each is 391 lines / 27 KB. Likely a copy-paste during plugin install.

| Path | Lines | Size | Issues |
| ---- | ----- | ---- | ------ |
| `~/AppData/Local/hermes/desktop-plugins/mindstudio-agent/CLAUDE.md` | 391 | 27.0KB | bloat ×2 |
| `~/AppData/Local/hermes/plugins/mindstudio-agent/CLAUDE.md` | 391 | 27.0KB | bloat ×2 |
| `~/AppData/Local/hermes/profiles/creative-director/plugins/mindstudio-agent/CLAUDE.md` | 391 | 27.0KB | bloat ×2 |
| `~/AppData/Local/hermes/profiles/exec-assistant/plugins/mindstudio-agent/CLAUDE.md` | 391 | 27.0KB | bloat ×2 |
| `~/AppData/Local/hermes/profiles/patient-tutor/plugins/mindstudio-agent/CLAUDE.md` | 391 | 27.0KB | bloat ×2 |
| `~/AppData/Local/hermes/profiles/research-analyst/plugins/mindstudio-agent/CLAUDE.md` | 391 | 27.0KB | bloat ×2 |

**Fix strategy:** Keep one canonical `~/AppData/Local/hermes/plugins/mindstudio-agent/CLAUDE.md`; replace the 5 copies with stub files that link to it. Stub = 1-2 lines.

### Conflicting — 4 files

| Path | Issue |
| ---- | ----- |
| `~/AppData/Local/hermes/SOUL.md` | 320 lines; contains "never commit" rule phrasing that audit regex flagged (false positive — user's actual rule is "commit only with explicit ask") |
| `~/AppData/Local/hermes/hermes-agent/AGENTS.md` | 1785 lines / 93.7 KB (upstream hermes-agent source — OUT OF SCOPE per audit filter; should be excluded) |
| `SandBox/AGENTS.md` | 323 lines / 15.9KB; same false-positive + stale `Bash/` path |
| `SandBox/SOUL.md` | 256 lines / 12KB; same false-positive + bloat |

**Fix strategy:** Refine audit regex to avoid false positive; trim SOUL.md/AGENTS.md to point to canonical references/.

### Stale (Bash/, Resume_maker/, deprecated refs) — 16 files

| Type | Count | Sample |
| ---- | ----- | ------ |
| `Bash/` path not migrated | 3 | `SandBox/copilot-instructions.md`, `SandBox/projects/Bash/docs/AGENTS.md`, `SandBox/AGENTS.md` |
| `zen-backup` deprecated reference | 13 | All profile `memories/MEMORY.md` files (adminbot, code-architect, ops, pm, patient-tutor, qa, research-analyst, security, etc.) |

**Fix strategy:** Add whitelist replacements to `templates/whitelist-fixes.json`; run `instruction_fix.py --apply` to repair.

## Top Unknowns (228)

These are project sub-directory instruction files (one per project). Most likely OK (short, scope-local), but not auto-classified as canonical because they live under `projects/*` not at a profile root. **Recommend human review** of the largest unknowns.

## Recommended Repair Order

1. **P1 (now):** Whitelist auto-fix: `Bash/` → `projects/Bash/`, drop `zen-backup` reference. Idempotent.
2. **P2:** Stub-replace the 5 duplicate mindstudio-agent CLAUDE.md copies with links to canonical.
3. **P3:** Refine audit regex to remove false positive on "never commit" rule.
4. **P4:** Human triage of "unknown" category: per-project review of largest files.

## Verification

- ✅ V1: `python scripts/instruction_audit.py` exits 0, 259 files scanned
- ✅ V2: `audit-report.json` valid JSON, all required fields present
- ⏳ V3-V6: pending fix script + skill + prompt
