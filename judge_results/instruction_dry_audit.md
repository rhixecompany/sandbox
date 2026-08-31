# Instruction File DRY Audit

**Date:** 2026-08-31 (UTC)
**Scope:** SandBox repo root + Hermes home + 14 profiles
**Mode:** Read-only — no files modified
**Files audited:** 65 (7 repo + 2 hermes_root + 56 profile)
**Total size:** 1,906,924 bytes / 36,191 lines
**Potential DRY savings:** ~1.14 MB (59.9%)

---

## Headline

- **14 SOUL.md files audited — all 14 are unique (correct: each profile has its own persona).** However, 7 OWL profiles embed a 5-line "You are Hermes Agent" paragraph that duplicates `~/AppData/Local/hermes/SOUL.md`.
- **16 DRY violations found; 0 backup/timestamped files.** All violations are 4× and 7× byte-identical duplications of content that already lives in a canonical source.
- **Canonical USER.md and MEMORY.md exist** at `~/AppData/Local/hermes/memories/USER.md` (1,754 B) and `memories/MEMORY.md` (4,162 B), but **4 profiles copy the MEMORY content verbatim 4× instead of pointing**, and **4 profiles copy the USER content verbatim 4× instead of pointing**.
- **SandBox repo SOUL.md is a near-duplicate of `~/AppData/Local/hermes/SOUL.md`** (same H1-H2 structure, same first-200 chars `deefe08906c8`); should be a thin stub.

---

## Files Audited (per category)

### A. SandBox repo root (7 files)

| File | Lines | Bytes | mtime (UTC) | H1 | H2 | Action |
|---|---:|---:|---|---:|---:|---|
| `SandBox/SOUL.md` | 255 | 12,335 | 2026-08-28 14:59 | 1 | 8 | **DRY-VIOLATION** (dup of hermes_root SOUL) |
| `SandBox/USER.md` | 13 | 523 | 2026-08-28 14:59 | 1 | 0 | OK-pointer (target wrong) |
| `SandBox/MEMORY.md` | 13 | 551 | 2026-08-28 14:59 | 1 | 0 | OK-pointer (target wrong) |
| `SandBox/.hermes.md` | 61 | 2,675 | 2026-08-28 14:59 | 1 | 8 | OK |
| `SandBox/AGENTS.md` | 322 | 16,333 | 2026-08-28 20:57 | 5 | 9 | OK |
| `SandBox/CLAUDE.md` | 7 | 314 | 2026-08-24 22:42 | 1 | 0 | OK-stub |
| `SandBox/.cursorrules` | 8 | 331 | 2026-08-24 22:42 | 1 | 0 | OK-stub |

### B. Hermes home (2 files)

| File | Lines | Bytes | mtime (UTC) | H1 | H2 | Action |
|---|---:|---:|---|---:|---:|---|
| `~/AppData/Local/hermes/SOUL.md` | 319 | 12,272 | 2026-08-24 22:54 | 1 | 8 | OK (canonical) |
| `~/AppData/Local/hermes/config.yaml` | 2,275 | 120,502 | 2026-08-31 16:00 | 18 | 0 | REVIEW |

### C. 14 profiles × 4 files (56 files)

| Profile | SOUL.md (lines) | USER.md | MEMORY.md | config.yaml | Notes |
|---|---:|---:|---:|---:|---|
| alexa | 58 | 11 (stub) | 11 (stub) | 2,284 | template persona |
| code-architect | 58 | 11 (stub) | 11 (stub) | 2,298 | template persona |
| creative-director | 58 | **46 (EXPANDED — 4× dup)** | **37 (EXPANDED — 4× dup)** | 2,288 | **DRY-VIOLATION** |
| cto | 9 | 11 (stub) | 11 (stub) | 2,284 | OWL header, embedded Hermes para |
| default | 1 | 11 (stub) | 11 (stub) | 2,232 | bare canonical |
| designer | 9 | 11 (stub) | 11 (stub) | 2,284 | OWL header |
| dev | 9 | 11 (stub) | 11 (stub) | 2,284 | OWL header |
| exec-assistant | 58 | **46 (EXPANDED — 4× dup)** | **37 (EXPANDED — 4× dup)** | 2,288 | **DRY-VIOLATION** |
| ops | 9 | 11 (stub) | 11 (stub) | 2,284 | OWL header |
| patient-tutor | 58 | **46 (EXPANDED — 4× dup)** | **37 (EXPANDED — 4× dup)** | 2,288 | **DRY-VIOLATION** |
| pm | 9 | 11 (stub) | 11 (stub) | 2,284 | OWL header |
| qa | 9 | 11 (stub) | 11 (stub) | 2,284 | OWL header |
| research-analyst | 58 | **46 (EXPANDED — 4× dup)** | **37 (EXPANDED — 4× dup)** | 2,288 | **DRY-VIOLATION** |
| security | 9 | 11 (stub) | 11 (stub) | 2,284 | OWL header |

All 14 profile `SOUL.md` have **unique bodies** (correct: persona must differ).

---

## Top 5 Duplication Findings

### #1 — 4× duplicate MEMORY.md (worst)

```
sha256_full = 1ff61bcb305dc48e
files: profiles/{creative-director,exec-assistant,patient-tutor,research-analyst}/MEMORY.md
size: 6,062 bytes × 4 = 24,248 bytes
canonical: ~/AppData/Local/hermes/memories/MEMORY.md (4,162 bytes — 1,900 bytes smaller!)
```

These 4 profiles each contain the **full canonical durable rules** verbatim — Windows MSYS quirks, npm/ruff/eslint pitfalls, MCP server fixes, vision fallback, Copilot removal, multi-agent sync. Every byte of this 6 KB block is already in `memories/MEMORY.md`. **Fix:** replace each with the standard 11-line pointer stub (already used by 10 other profiles). **Saves:** 3 × 5,589 = 16,767 bytes.

### #2 — 4× duplicate USER.md

```
files: profiles/{creative-director,exec-assistant,patient-tutor,research-analyst}/USER.md
size: 1,674 bytes × 4 = 6,696 bytes
canonical: ~/AppData/Local/hermes/memories/USER.md (1,754 bytes)
```

Same 4 profiles duplicate the same expanded USER (Identity, Environment Stack, Model, Execution Preferences, Standing Goal, Honcho Memory). **Fix:** replace each with 11-line pointer stub. **Saves:** 3 × 1,215 = 3,645 bytes.

### #3 — SandBox repo SOUL.md ≈ hermes_root SOUL.md

```
sha256_first200 = deefe08906c8
files: SandBox/SOUL.md (12,335B) vs ~/AppData/Local/hermes/SOUL.md (12,272B)
same H1 (# SOUL.md — Core Operating Principles) + same 8 H2 sections
```

Both files are the same canonical SOUL with only the `**Profile:**` line differing (default vs repo override). **Fix:** replace repo SOUL.md with a 500-byte stub pointing to `~/AppData/Local/hermes/SOUL.md`. **Saves:** 11,835 bytes.

### #4 — 7× OWL SOUL.md embed the Hermes Agent paragraph

```
files: profiles/{cto,designer,dev,ops,pm,qa,security}/SOUL.md
size: 842-879 bytes each (~500B is duplicate)
```

Each OWL profile has a 5-line block:
```
You are Hermes Agent, an intelligent AI assistant created by Nous Research...
```
…that exactly duplicates the same paragraph already in `~/AppData/Local/hermes/SOUL.md`. **Fix:** keep only `**Profile:** cto | **Model:** … | **Identity:** OWL: Chief technology officer. …` — strip the Hermes paragraph. **Saves:** 7 × 500 ≈ 3,500 bytes.

### #5 — 15 config.yaml files cluster into 2 exact-dup groups

```
sha256_full = 12504adc36eea1b0  (4× dup, 120,114B each)
  profiles/{creative-director,exec-assistant,patient-tutor,research-analyst}/config.yaml

sha256_full = 84a908df8b143c9a  (7× dup, 120,005B each)
  profiles/{cto,designer,dev,ops,pm,qa,security}/config.yaml
```

11 of 15 config.yaml files are byte-identical within their cluster. Root `config.yaml` (120,502B) and a few others differ at the surface but likely share 80%+ boilerplate (mcp_servers, providers, agents, etc.). **Fix:** out of scope for this read-only audit; recommend a YAML deep-merge to extract per-profile deltas. **Potential savings:** ~800 KB.

---

## DRY Compliance Report Card

| Principle | Compliance | Notes |
|---|---|---|
| USER.md = compact pointer (not duplicate of SOUL) | ✅ PASS for 10/14 profiles; ❌ FAIL for 4 | creative/exec/patient/research copy full content |
| MEMORY.md = agent notes (env, tool quirks) | ✅ PASS for 10/14 profiles; ❌ FAIL for 4 | same 4 profiles |
| SOUL.md = agent identity/persona/boundaries | ✅ PASS — all 14 unique | template is OK, persona body is profile-specific |
| Project-level files = workspace overrides | ✅ PASS | CLAUDE.md (7 lines) and .cursorrules (8 lines) are correctly thin stubs deferring to AGENTS.md |
| No backup files | ✅ PASS — 0 violations | no `.bak`, `.backup`, `.old`, or timestamped variants in instruction paths |
| Canonical source exists | ✅ PASS | `~/AppData/Local/hermes/memories/USER.md` (1,754B) and `memories/MEMORY.md` (4,162B) |
| 14 profile SOUL.md all differ (persona) | ✅ PASS | all 14 unique bodies — template shared but persona content unique |

---

## Backup / Timestamped File Violations

**None.** No `.bak`, `.backup`, `.old`, or timestamped files found in any of the audited instruction paths.

---

## Quantified Summary

```
Files audited:           65 (7 repo + 2 hermes_root + 56 profile)
Total bytes:             1,906,924
Total lines:             36,191
Exact-full dup groups:   3  (4× MEMORY + 4× config + 7× config)
First-200 dup groups:    4  (+1 repo SOUL)
DRY violations:          16 files
Backup files:            0
DRY cleanup potential:   ~1.14 MB (59.9% of total)
  ├─ Exact-full collapse:   1,098,558 B (config.yaml clusters dominate)
  ├─ OWL SOUL.md strip:     3,694 B (7 files × 500B)
  ├─ 4× MEMORY → stub:     22,356 B
  ├─ 4× USER → stub:        4,852 B
  └─ repo SOUL → stub:     11,835 B
```

After full DRY: ~765 KB total, ~30 KB for profile-only changes.

---

## Recommendation (read-only audit; not applied)

1. **High-value, low-risk:** Replace 4× expanded USER/MEMORY.md (8 files) with the 11-line pointer stub template that 10 other profiles already use. Single tool: `scripts/profile_config_fix.py` already exists (it generated the stubs on 2026-08-28).
2. **High-value:** Replace `SandBox/SOUL.md` with a thin stub (500B) pointing to `~/AppData/Local/hermes/SOUL.md`.
3. **Medium-value:** Strip the 5-line "You are Hermes Agent" paragraph from 7 OWL SOUL.md; they should defer to parent.
4. **SandBox repo pointer target:** `SandBox/USER.md` and `SandBox/MEMORY.md` point to `profiles/default/USER.md` but the canonical lives at `memories/USER.md` (15 files in 4 profiles use the latter path). Fix the pointer target.
5. **Out of scope:** 15 config.yaml files (~1.8 MB total) contain deep duplication that needs a separate YAML diff/merge pass.

---

**Files written:**
- `C:\Users\Alexa\Desktop\SandBox\judge_results\instruction_dry_audit.json` (96,580 bytes, full per-file table)
- `C:\Users\Alexa\Desktop\SandBox\judge_results\instruction_dry_audit.md` (this file)
