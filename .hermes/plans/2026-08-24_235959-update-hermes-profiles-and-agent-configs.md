# Implementation Plan: Update, Enhance, and Verify Hermes Profiles & AI Agent Configs

## Overview
This plan outlines the steps to update, enhance, and verify the Hermes default profile and all Hermes profiles' SOUL.md, USER.md, MEMORY.md files, along with all installed AI agents' context files (Hermes, Copilot, OpenCode, Codex). The plan enforces best practices, DRY principles, and uses all Hermes tools, toolsets, and skills for web/research.

## Files to Modify (≥5 files - triggers Multi-File Change Protocol)

### Root Hermes Config Files
1. `C:/Users/Alexa/AppData/Local/hermes/SOUL.md` (root)
2. `C:/Users/Alexa/AppData/Local/hermes/memories/USER.md` (root)
3. `C:/Users/Alexa/AppData/Local/hermes/memories/MEMORY.md` (root)

### Profile-Specific Files (7 profiles: default, alexa, code-architect, creative-director, exec-assistant, patient-tutor, ops, research-analyst)
For each profile:
- `SOUL.md` - Profile identity & tone
- `memories/USER.md` - User preferences
- `memories/MEMORY.md` - Agent notes

### Workspace Context Files (SandBox root)
4. `C:/Users/Alexa/Desktop/SandBox/.hermes.md`
5. `C:/Users/Alexa/Desktop/SandBox/AGENTS.md`
6. `C:/Users/Alexa/Desktop/SandBox/CLAUDE.md`
7. `C:/Users/Alexa/Desktop/SandBox/.cursorrules`
8. `C:/Users/Alexa/Desktop/SandBox/.github/copilot-instructions.md`

### Subproject Context Files (17+ subprojects each with AGENTS.md, copilot-instructions.md, .cursorrules)
- `projects/Bash/AGENTS.md`, `projects/Bash/copilot-instructions.md`
- `projects/Banking/AGENTS.md`, `projects/Banking/.github/copilot-instructions.md`
- `projects/comicwise/AGENTS.md`, `projects/comicwise/.github/copilot-instructions.md`, `projects/comicwise/.cursorrules`
- ...and 14+ more subprojects

### AI Agent Config Files
- OpenCode: `~/.opencode/opencode.json` or `C:/Users/Alexa/.opencode/`
- Codex: `~/.codex/` config files
- Copilot: VS Code settings, GitHub Copilot config

## Current State Analysis

### Issues Identified:
1. **DRY Violations**: Multi-file protocol repeated in every SOUL.md (55 lines each) instead of referencing parent
2. **Inconsistent Model Info**: Some profiles show `deepseek-v4-flash-free`, others show `nemotron-3-ultra-free` as primary
3. **Stale MEMORY.md**: Root MEMORY.md has valuable facts but profile MEMORY.md files are minimal stubs
4. **Profile Routing Inconsistency**: Some profiles reference `ops→alexa` but `alexa` is a profile name, not a routing target
5. **Missing Verification Gates**: No automated verification that all profiles are in sync
6. **Subproject Context Drift**: Subproject AGENTS.md files may not reflect latest workspace conventions
6. **Prompt File**: `.github/prompts/test-providers-models.prompt.md` needs to only use working, tested models

## Phased Implementation Plan

### Phase 1: Audit & Inventory (Week 1, Days 1-2)
**Goal**: Complete inventory of all files, current state, and discrepancies

#### Tasks:
1.1 **Inventory All Profile Files**
- Use `mcp-filesystem` to list all SOUL.md, USER.md, MEMORY.md across profiles
- Document line counts, content hashes, last modified dates
- Identify which profiles exist vs. which are configured in Hermes

1.2 **Inventory Workspace Context Files**
- Scan SandBox root and all subprojects for AGENTS.md, CLAUDE.md, .cursorrules, copilot-instructions.md
- Catalog version, last updated, key differences from root AGENTS.md

1.3 **Inventory AI Agent Configs**
- Check OpenCode config (`opencode.json`, `~/.opencode/`)
- Check Codex config (`~/.codex/`)
- Check Copilot/VS Code settings

1.4 **Analyze test-providers-models.prompt.md**
- Verify it only references working, tested models
- Cross-reference with actual verified models from live probes

**Deliverable**: `audit-report.md` with full inventory matrix

### Phase 2: Design Consolidated Templates (Week 1, Days 3-4)
**Goal**: Create DRY templates that eliminate duplication

#### Tasks:
2.1 **Create SOUL.md Template**
- Base template at `templates/profile-soul.md.template`
- Profile-specific sections as variables (identity, tone, model, profile-specific rules)
- Shared rules reference parent SOUL.md via include directive

2.2 **Create USER.md Template**
- Base template at `templates/profile-user.md.template`
- Profile-specific: name, model preferences, routing
- Shared: execution preferences, multi-file protocol (single source)

2.3 **Create MEMORY.md Template**
- Base template at `templates/profile-memory.md.template`
- Shared facts from root MEMORY.md
- Profile-specific facts only

2.4 **Create Workspace Context File Templates**
- `.hermes.md.template` - project overrides
- `AGENTS.md.template` - canonical guidance (subprojects inherit)
- `CLAUDE.md.template` - thin stub
- `.cursorrules.template` - thin stub
- `copilot-instructions.md.template` - references AGENTS.md

2.5 **Update test-providers-models.prompt.md**
- Ensure only verified working models from live probes
- Update provider list to match `hermes auth list`
- Verify fallback chain ordering algorithm

**Deliverable**: Template files in `.github/prompts/templates/` or dedicated templates dir

### Phase 3: Implement Root Profile Updates (Week 2, Days 1-3)
**Goal**: Update root Hermes files with consolidated, DRY content

#### Tasks:
3.1 **Update Root SOUL.md**
- Ensure 4 Mandatory Rules are current and match all profiles
- Verify Multi-File Change Protocol references canonical 14 skills
- Add cross-reference to profile-specific SOUL.md files

3.2 **Update Root USER.md**
- Keep as pointer to MEMORY.md (current pattern is correct)
- Verify model info matches live config (`hermes profile list`)
- Ensure profile routing table is accurate

3.3 **Update Root MEMORY.md**
- Preserve all §-delimited facts
- Add any missing facts from profile MEMORY.md files
- Ensure no H1 heading (MD041 compliance)

3.4 **Verify Root Config**
- Run `hermes config check`
- Run `hermes profile list` to confirm model/provider state

### Phase 4: Update All Profile Files (Week 2, Days 4-7)
**Goal**: Apply templates to all 7 profiles with profile-specific customization

#### Tasks (per profile - can parallelize with subagents):
4.1 **For each profile (default, alexa, code-architect, creative-director, exec-assistant, patient-tutor, ops, research-analyst):**
- Generate SOUL.md from template + profile-specific overrides
- Generate USER.md from template + profile-specific overrides  
- Generate MEMORY.md from template + profile-specific overrides
- Verify each file passes frontmatter validation
- Verify cross-references to parent SOUL.md are correct

4.2 **Special handling for `default` profile:**
- Root SOUL.md IS the default profile SOUL.md
- Root USER.md/MEMORY.md are the default profile memories
- Ensure no duplicate files in `profiles/default/`

**Deliverable**: All 24 profile files updated (3 files × 8 profiles)

### Phase 5: Update Workspace Context Files (Week 3, Days 1-3)
**Goal**: Sync SandBox root and subproject context files

#### Tasks:
5.1 **Update SandBox Root Files**
- `.hermes.md` - Ensure profile table references live config
- `AGENTS.md` - Canonical source, verify all sections current
- `CLAUDE.md` - Thin stub, verify deferral to AGENTS.md
- `.cursorrules` - Thin stub, verify deferral to AGENTS.md
- `.github/copilot-instructions.md` - Verify references AGENTS.md + .hermes.md

5.2 **Update Subproject Context Files (Batch via subagents)**
- For each subproject with AGENTS.md: verify it defers to root AGENTS.md for shared rules
- Update copilot-instructions.md to reference correct AGENTS.md
- Add .cursorrules where missing (thin stub pattern)
- Ensure subproject-specific sections are preserved

5.3 **Validation**
- Run markdownlint on all updated files
- Verify no broken cross-references
- Check frontmatter validity on all prompt/instruction files

### Phase 6: Update AI Agent Configs (Week 3, Days 4-5)
**Goal**: Propagate verified working models to all installed agents

#### Tasks:
6.1 **OpenCode Config**
- Update `opencode.json` or `~/.opencode/opencode.json`
- Set model to highest-ranked verified working model from test-providers-models
- Configure fallback chain per verified providers

6.2 **Codex Config**
- Update `~/.codex/config.toml` or equivalent
- Set model and provider to verified working set

6.3 **Copilot/VS Code**
- Update `.vscode/settings.json` for Copilot model preferences
- Ensure workspace settings align with Hermes config

6.4 **Hermes Config Sync**
- Run `hermes config set` for primary model and fallback chain
- Verify `fallback_providers` is YAML list (not string)
- Set each provider's `default_model` to verified working model

### Phase 7: Verification Gates (Week 4, Days 1-3)
**Goal**: Comprehensive verification all changes are correct and consistent

#### Tasks:
7.1 **Automated Verification Script**
Create `scripts/verify-profile-sync.py` that checks:
- All profile SOUL.md have correct 4 mandatory rules
- All profile USER.md have consistent model info
- All profile MEMORY.md have §-delimited format, no H1
- Root files match profile defaults
- Workspace context files reference correct sources
- AI agent configs use only verified working models
- `hermes config check` passes
- `fallback_providers` is valid YAML list

7.2 **Run Verification**
- Execute verification script
- Fix any failures
- Re-run until all gates pass

7.3 **Live Probe Verification**
- Run `test-providers-models` prompt to re-verify model chain
- Confirm Hermes and all agents use working models only

7.4 **Cross-Profile Sync Check**
- Run `multi-agent-sync` skill verify_sync.py (65 checks)
- Confirm parity: root ↔ Codex ↔ OpenCode ↔ mirror ↔ 6 profiles

### Phase 8: Documentation & Handoff (Week 4, Days 4-5)
**Goal**: Document changes, create runbooks for future maintenance

#### Tasks:
8.1 **Update Documentation**
- Update `docs/architecture/profile-sync.md` with sync procedure
- Update `HERMES_PROFILE_REPORT.md` with current state
- Document template locations and update process

8.2 **Create Maintenance Runbook**
- `scripts/profile-maintenance-runbook.md` with:
  - Monthly verification checklist
  - How to add new profile
  - How to update model chain
  - Rollback procedures

8.3 **Commit & Tag**
- Git commit all changes with conventional messages
- Tag release: `profile-sync-2026-08-24`

## Timeline Summary

| Phase | Duration | Start | End | Key Deliverable |
|-------|----------|-------|-----|-----------------|
| 1. Audit & Inventory | 2 days | Day 1 | Day 2 | audit-report.md |
| 2. Design Templates | 2 days | Day 3 | Day 4 | Template files |
| 3. Root Profile Updates | 3 days | Day 5 | Day 7 | Updated root files |
| 4. All Profile Updates | 4 days | Day 8 | Day 11 | 24 profile files |
| 5. Workspace Context Files | 3 days | Day 12 | Day 14 | Root + subproject files |
| 6. AI Agent Configs | 2 days | Day 15 | Day 16 | Agent configs synced |
| 7. Verification Gates | 3 days | Day 17 | Day 19 | All gates passing |
| 8. Documentation | 2 days | Day 20 | Day 21 | Runbook, tagged release |

**Total: ~21 working days (4-5 weeks)**

## Resource Allocation

| Resource | Role | Phases |
|----------|------|--------|
| Primary Agent (exec-assistant) | Orchestration, Phases 1, 2, 3, 7, 8 | All |
| Subagent Pool (4-6 parallel) | Phase 4 (profile files), Phase 5 (subprojects) | 4, 5 |
| Verification Subagent | Phase 7 automated checks | 7 |
| Human (Alexa) | Approval gates, Phase 6 agent config, final verification | 3, 6, 7, 8 |

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Profile config drift during sync | High | Medium | Batch updates, verify after each batch, git commit per phase |
| Subproject context conflicts | Medium | High | Preserve subproject-specific sections, only update shared references |
| Non-working model promoted | Low | High | Live probe verification mandatory before config write |
| YAML corruption in config.yaml | Medium | High | Use `hermes config set` CLI only, never direct edit |
| Skill pollution from duplicate skills | Low | Medium | Audit skills before/after with `skill-judge` |

## Verification Checklist (Phase 7 Gates)

- [ ] `hermes config check` passes
- [ ] `hermes profile list` shows 7 profiles with correct models
- [ ] `fallback_providers` is YAML list ordered by capability
- [ ] Each fallback provider has working free `default_model`
- [ ] All 8 profile SOUL.md have 4 mandatory rules + profile-specific content
- [ ] All 8 profile USER.md have consistent model info + routing table
- [ ] All 8 profile MEMORY.md use §-delimited format, no H1
- [ ] Root SOUL.md = default profile SOUL.md (no duplication)
- [ ] Root USER.md/MEMORY.md = default profile memories
- [ ] SandBox root context files (.hermes.md, AGENTS.md, CLAUDE.md, .cursorrules, copilot-instructions.md) current
- [ ] All subproject AGENTS.md defer to root for shared rules
- [ ] All subproject copilot-instructions.md reference correct AGENTS.md
- [ ] OpenCode config uses verified working models only
- [ ] Codex config uses verified working models only
- [ ] Copilot/VS Code settings aligned
- [ ] `test-providers-models` prompt produces working model chain
- [ ] `multi-agent-sync` verify_sync.py: 65 checks pass
- [ ] No secrets/tokens in any output files
- [ ] Markdownlint passes on all modified files
- [ ] Git status clean with conventional commits

## Approval Gates

1. **Phase 2 Complete** → Review templates with user before Phase 3
2. **Phase 3 Complete** → Verify root files before profile propagation
3. **Phase 4 Complete** → Spot-check 2 profiles before Phase 5
4. **Phase 6 Complete** → Verify agent configs before final verification
5. **Phase 7 Complete** → All gates pass → Tag release

## Success Criteria

1. **Zero DRY violations** - Multi-file protocol defined once, referenced everywhere
2. **Single source of truth** - Model info from `hermes config show` / `hermes profile list`
3. **All agents use working models** - Verified by live probe, not assumption
4. **Consistent profile routing** - code→architect, research→analyst, etc. uniform
5. **Automated verification** - Script catches drift before it propagates
6. **Documented maintenance** - Future updates follow runbook, not ad-hoc

---

*Plan created using `/create-implementation-plan` skill workflow*
*Template: `.github/prompts/templates/workflow.md`*
*Saved to: `.hermes/plans/2026-08-24_235959-update-hermes-profiles-and-agent-configs.md`*