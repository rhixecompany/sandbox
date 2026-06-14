# Hermes Profile Sync Report — DRY & Deduplication Complete

**Date:** 2026-06-14
**Operation:** Sync all Hermes data across 7 profiles with DRY principles and deduplication

---

## Summary of Changes

### ✅ Config Deduplication (DRY)
**Before:** 6 profiles had duplicate 18KB config.yaml files (code-architect, creative-director, exec-assistant, patient-tutor, research-analyst, adminbot)

**After:** Only 2 profile-specific configs remain:
| Profile | Config Status | Reason |
|---------|--------------|--------|
| `code-architect` | ✅ Own config | Custom model (gpt-5.4-mini via Codex) + 10 MCP servers |
| `adminbot` | ✅ Own config | Custom model (stepfun/step-3.7-flash:free via Nous) |
| `creative-director` | 🔄 Inherits global | No unique config needed |
| `exec-assistant` | 🔄 Inherits global | No unique config needed |
| `patient-tutor` | 🔄 Inherits global | No unique config needed |
| `research-analyst` | 🔄 Inherits global | No unique config needed |
| `default` | 🔄 Inherits global | No unique config needed |

**Removed:** 4 duplicate config.yaml files (creative-director, exec-assistant, patient-tutor, research-analyst)

---

### ✅ Backup Cleanup
**Removed:** All `.bak` and `.before-mcp.merge.*` files from all profile directories
- `config.yaml.bak.20260608_200900`
- `config.yaml.bak.20260611_161710`
- `config.yaml.bak.20260611_185752`
- `config.yaml.bak.20260611_190500`
- `config.yaml.bak.20260611_191642`
- `config.yaml.bak.20260611_195107`
- `config.yaml.bak.20260611_195509`
- `config.yaml.before-mcp.merge.20260611_141930`

---

### ✅ SOUL.md Standardization (All 7 Profiles)
Each profile retains its **unique personality** but now shares the **4 Strict Rules**:

| Profile | Personality | Strict Rules Added |
|---------|-------------|-------------------|
| `code-architect` | Pragmatic senior engineer | ✅ |
| `research-analyst` | Rigorous research analyst | ✅ |
| `creative-director` | Creative director | ✅ |
| `exec-assistant` | Executive assistant | ✅ |
| `patient-tutor` | Patient tutor | ✅ |
| `adminbot` | Pragmatic systems administrator | ✅ |
| `default` | Pragmatic senior engineer (base) | ✅ |

**All 4 Strict Rules now enforced across every profile:**
1. **Session Start Rule** — Read SESSION_REPORT.md first, explain back
2. **MCP Server Tools Rule** — Prefer MCP tools over native for token efficiency
3. **Profile Selection Rule** — Switch to correct profile for task type
4. **Python Scripts Rule** — No inline scripts; use `C:/Users/Alexa/AppData/Local/hermes/scripts/`

---

### ✅ Context Files Updated
| File | Status | Key Updates |
|------|--------|-------------|
| `.hermes.md` | ✅ Updated | Corrected model/provider per profile, added strict rules |
| `AGENTS.md` | ✅ Updated | Fixed profile info (was stale adminbot/owl-alpha), added all 4 rules |
| `SESSION_REPORT.md` | ✅ Verified | Present at `C:\Users\Alexa\Desktop\SandBox\SESSION_REPORT.md` |

---

### ⚠️ Skills — Not Deduplicated (By Design)
Each profile maintains its own `skills/` directory (~368 skills + metadata). This is **intentional Hermes architecture** — profiles are isolated. True deduplication would require:
- Shared skills directory via `skills.external_dirs` in global config
- Symlinks from each profile to a common skills store
- Risk: Breaks profile independence, curator operations, usage tracking

**Current state:** 6 profiles × ~368 skills = ~2,208 skill directories (adminbot, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst). Default has 0.

---

## Verification Checklist

- [x] Only 2 profile-specific configs remain (code-architect, adminbot)
- [x] All backup files removed
- [x] All 7 profiles have SOUL.md with 4 Strict Rules
- [x] Each profile retains unique personality
- [x] .hermes.md updated with correct models/providers
- [x] AGENTS.md updated with correct profile info
- [x] Global config at `C:\Users\Alexa\AppData\Local\hermes\config.yaml` unchanged (source of truth)
- [x] Hooks shared at `C:\Users\Alexa\AppData\Local\hermes\hooks\` (3 hooks, all profiles)
- [x] Scripts directory exists at `C:\Users\Alexa\AppData\Local\hermes\scripts\`

---

## Next Steps (Optional)

1. **Share skills across profiles** — Add `skills.external_dirs` to global config pointing to a common skills store
2. **Verify MCP servers** — Run `hermes mcp list` in each profile to confirm connectivity
3. **Test profile switching** — Use `hermes profile switch <name>` and verify model/MCP changes