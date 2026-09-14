# Context Files Ownership + Change Matrix
**Date:** 2026-08-24
**Plan:** `.hermes/plans/2026-08-24_update-enhance-verify-context-files.md`

## Canonical Ownership
| Concern | Canonical File | Secondary References |
|---------|----------------|----------------------|
| Identity/boundaries/cognitive style | `~/AppData/Local/hermes/SOUL.md` | `.hermes.md`, subprofile `SOUL.md` → parent pointer only |
| User identity/execution preferences | `~/AppData/Local/hermes/profiles/*/memories/USER.md` | Workspace root `USER.md` pointer only |
| Agent lessons/env facts | `~/AppData/Local/hermes/profiles/*/memories/MEMORY.md` | Workspace root `MEMORY.md` pointer only |
| Workspace toolchain/routing | `AGENTS.md` | `.hermes.md` high-priority overrides only |
| Prompt library guidance | `.github/copilot-instructions.md` | Subproject `copilot-instructions.md` → defer to root |
| IDE-specific rules | `.cursorrules` | `CLAUDE.md` → defer to root |
| Verified provider chain | `.github/prompts/test-providers-models.prompt.md` | `.hermes.md`/`AGENTS.md` provider table |

## Change Matrix
| File | Action | Reason | Risk | Batch |
|------|--------|--------|------|-------|
| `~/AppData/Local/hermes/SOUL.md` | Trim duplicated blocks; keep pointer references | Multi-file protocol block duplicated in profile docs | Low | 1 |
| `.hermes.md` | Replace full multi-file protocol with pointer | DRY; avoids retyping 14-skill stack | Low | 1 |
| `AGENTS.md` | Replace full multi-file protocol with pointer; align provider table to live config | Drift from current profile list/models | Medium | 1 |
| `CLAUDE.md` | Convert to one-liner cross-reference | Already mostly stub; make explicit | Low | 1 |
| `.cursorrules` | Convert to one-liner cross-reference | Already mostly stub; make explicit | Low | 1 |
| `.github/copilot-instructions.md` | Replace duplicated multi-file protocol; verify prompt-category table | DRY + current accuracy | Medium | 1 |
| `.github/prompts/test-providers-models.prompt.md` | Add live verification gates + explicit agent config update steps | User requirement: only working models; propagate to agents | High | 2 |
| Profile `SOUL.md` files | Add parent-pointer line only; remove duplicated protocol blocks | 8 subprofiles currently copy same block | Medium | 2 |
| Profile `USER.md` files | Keep compact; remove any full-rule duplication | Some profiles near pointer format already | Low | 2 |
| Profile `MEMORY.md` files | Keep compact; ensure no H1/title drift | Memory format constraint | Low | 2 |

## Approval
Approved for phased execution with verification after each batch.
