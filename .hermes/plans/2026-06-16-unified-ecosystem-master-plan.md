# Unified Hermes Ecosystem Master Plan

**Date:** 2026-06-16
**Mode:** Planning document only
**Scope:** Consolidate all `.hermes/plans/*.md` plans + live hooks/skills/plugins/MCP/tools inventory into one executable master plan.

---

## 1. Session & Environment Context

| Field | Value |
|-------|-------|
| Workspace | `C:\Users\Alexa\Desktop\SandBox` |
| Active profile | `default` |
| Model | `stepfun/step-3.7-flash:free` provider `nous` |
| Hermes data | `C:\Users\Alexa\.hermes\` |
| Profile runtime | `C:\Users\Alexa\AppData\Local\hermes\` |
| Behavior source | `.hermes.md` in workspace |
| `USER.md` / `SOUL.md` | Not found in `~/.hermes\` |

---

## 2. Source Plans Triage

### `2026-06-08_hermes-docs-reimplementation.md`
- Status: claims complete; 12 target docs under `docs/...` total ~88.8 KB / 2,656 lines originally
- Intent: recreate Hermes user-guide from source URLs
- Lemma: no live verification found in current inventory beyond plan references

### `2026-06-08_hermes-docs-verification.md`
- Status: validation plan for the reimplementation plan
- Intent: confirm H1, source URL, code blocks, See Also, sizes, cross-links
- Lemma: plan itself is sound; validation state is unverified

### `2026-06-08_mcp-servers-install-plan.md`
- Status: partially executed draft
- Intent: install ~40+ MCP servers
- Known blockers:
  - `mcp-server-time` 404 as of 2026-06-11
  - `@modelcontextprotocol/server-sqlite` not existing
  - `markdownify-mcp-server` not existing
- Scope reduced to servers with valid/local-runnable forms

### `2026-06-09_official-skills-bulk-install.md`
- Status: completed
- Intent: install official optional skills
- Outcome:
  - Before: 73 skills
  - After: 146 skills
  - Added: 95 official skills
  - Audit: 93 scanned -> 50 safe, 43 blocked
- Lemma: BLOCKED status is informational, not disabling

### `2026-06-11_173000-hermes-profile-restore.md`
- Status: superseded / guidance source only
- Key decision recorded: `.github/plugins/` are Copilot agent configs, NOT Hermes plugins

### `2026-06-11_200000-comprehensive-skills-hooks-plugins-mcp-audit-plan.md`
- Status: supersedes profile-restore; broad workspace audit blueprint
- Covers: skills browse/install/audit, profile/backup schemas, full inventory, full health check

### `2026-06-11_cleanup-skills-hooks-sandbox.plan.md`
- Status: retains as policy; not auto-executed
- Key policy: keep all 337 skills by default; prune disabled/empty only; do not delete current hooks retroactively

### `2026-06-14_143000-skills-audit-pipeline.md`
- Status: pipeline spec
- Outcome: 191 skills inventoried and judged in 28 batches of 7
- Validation criteria: accuracy, completeness, usability, maintainability, safety

### `2026-06-14_remaining-remediation-plan.md`
- Status: in progress
- Focus: re-judge 26 patched skills; fix 51 remaining skills in 4 batches
- 4 verification gates remain open

### `2026-06-15_remediation-plan-v2.md`
- Status: in progress
- Focus: targeted patch for remaining needs-work skills
- Exception: `frontend-design` skipped due to prior write failure

### `2026-06-16-multi-agent-research.md`
- Status: not started
- Intent: `/multi-agent-research` end-to-end with phases 1-6
- Output target: `docs/multi-agent-research/`

---

## 3. Live Inventory

### 3.1 Hooks
| Hook | Runtime location | Workspace stub location | Event behavior |
|------|------------------|-------------------------|----------------|
| `session-logger` | `C:\Users\Alexa\AppData\Local\hermes\hooks\session-logger\hook.sh` | `.github\hooks\session-logger\hook.sh` | session/pre_llm_call/end logging; supports skip flag |
| `session-auto-commit` | `...\session-auto-commit\hook.sh` | `.github\hooks\session-auto-commit\hook.sh` | auto-commit on session end; supports skip flag |
| `governance-audit` | `...\governance-audit\hook.sh` | `.github\hooks\governance-audit\hook.sh` | threat detection on pre_llm_call; supports skip flag |

Artifacts and tests:
- `.hermes\hook-health-check.sh`
- `.hermes\full-health-check.sh`
- `.hermes\e2e-session-test.sh`

Known issue: `hermes hooks list` reports no shell hooks configured in `~/.hermes/config.yaml` while the hook scripts and hook-health-check scripts exist. Do not delete current hooks; treat as a config registration mismatch to verify/fix.

Key rule from cleanup policy: do NOT remove `~/.hermes/hooks` or `.github/hooks` retroactively.

### 3.2 Plugins
Source of truth: bundled plugins discovered via `hermes plugins list`.

Enabled:
- `disk-cleanup`
- `openrouter-provider`
- `security-guidance`
- `memory/honcho`

Disabled selected examples:
- Browser backends: `browser-browser-use`, `browser-browserbase`, `browser-firecrawl`
- Chat platforms: `google_chat-platform`, `mattermost-platform`, `teams-platform`, `irc-platform`, `line-platform`, `photon-platform`, `simplex-platform`
- Image/video: `openai`, `fal`, `xai`, `openai-codex`, `xai` video
- Providers: many model-provider/* plugins are bundled but disabled
- Observability: `langfuse` is disabled
- Home integrations: `spotify`, `homeassistant` disabled

`.github/plugins/` is NOT Hermes plugin inventory; it contains 46 Copilot agent configs and should not be installed into Hermes as plugins.

### 3.3 MCP Servers
Enabled:
- `ast-grep`
- `code-sandbox`
- `fetch`
- `filesystem`
- `github`
- `linear`
- `mcp-docker`
- `memory`
- `playwright`
- `sequential-thinking`

Transport styles present:
- stdio via `npx -y ...`
- HTTP via URL for `linear`

Transport dependency rule: when adding new servers, prefer stdio when possible; match exact package names and auth/token requirements per server.

Blocked/dropped references:
- `mcp-server-time`
- `@modelcontextprotocol/server-sqlite`
- `markdownify-mcp-server`

### 3.4 Tools
Available built-in toolsets:
- Enabled: `web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`, `moa`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`, `clarify`, `delegation`, `cronjob`, `messaging`, `computer_use`
- Disabled: `video`, `video_gen`, `x_search`, `homeassistant`, `spotify`, `yuanbao`

Direct operational tools:
- `terminal`
- `read_file`
- `write_file`
- `patch`
- `search_files`
- `session_search`
- `skill_view`
- `skill_manage`

### 3.5 Skills
Reference totals:
- discovery returned 308 skill summaries
- prior audit judged 191 skills in 28 batches
- classification counts:
  - 113 skills AI-ready (≥70)
  - 51 skills needs work
  - 26 skills already patched
- bulk-install plan raised total to 146 installed skills; repository artifacts also reference 289/200+/100+ skills depending on source

Priority skills for completion work:
- `skill-judge`
- `skill-crever`
- `plans-and-specs`
- `executed-plans`
- `subagent-driven-development`
- `systematic-debugging`
- `verification-before-completion`

### 3.6 Prompts / Plan Artifacts
Under docs/superpowers/plans/ and `.hermes/plans/`:
- docs plan templates
- multi-agent-research master prompt plan
- MCP server plan
- bulk-install final report
- cleanup plan
- profile restore plan
- comprehensive audit plan
- skills audit pipeline plan
- remaining remediation plan
- remediation-plan-v2

Relevant prompt/workflow references:
- `docs/superpowers/plans/2026-06-16-multi-agent-research.md`
- `.github/prompts/multi-agent-research-template.prompt.md` referenced by that plan
- `.hermes/hook-health-check.sh`
- `.hermes/full-health-check.sh`
- `.hermes/e2e-session-test.sh`

---

## 4. Known Work Remaining

| Area | Current state | Next concrete action |
|------|--------------|----------------------|
| Skills audit | 191 judged; 26 patched; 51 pending | Complete Batch B/C/D patches, then re-judge |
| Hooks | scripts present; config registration unclear | verify `~/AppData/Local/hermes/config.yaml` hook registration and runtime activation |
| MCP server plan | many removed/dropped as invalid | re-test installed 10 servers before expanding |
| Docs reimplementation | plan claims 88.8 KB produced | verify by file existence/size/link checks |
| Multi-agent research | not executed | start from docs/superpowers/plans/2026-06-16-multi-agent-research.md |

---

## 5. Master Plan Execution Order

### Phase 1: Verify state before editing
1. Verify `.hermes/plans/` inventory matches decisions above
2. Verify skills audit report artifacts
3. Verify hook script paths and config registration
4. Verify MCP connectivity and tool discovery
5. Verify docs reimplementation outputs

### Phase 2: Complete open remediation pipelines
1. Finish `remediation-plan-v2` last known patch status
2. Run verification gates for `remaining-remediation-plan`
3. Confirm final score ≥ 70 or document exclusions

### Phase 3: Hook / runtime verification
1. Confirm whether hooks are loaded from profile path or workspace path
2. If config mismatch, patch config with approved paths only
3. Run `hermes hooks list`, `hermes plugins list`, `hermes mcp list` again after changes

### Phase 4: Execute multi-agent research workflow
1. Continue from `docs/superpowers/plans/2026-06-16-multi-agent-research.md`
2. Preserve plan order: docs reimplementation completed first

### Phase 5: Aggregate audit and docs
1. Refresh `HERMES_ECOSYSTEM_REPORT_2026-06-11.md` style report if needed
2. Update plan status table above with actual completion dates

---

## 6. Decision Records

- `.github/plugins/` => Copilot configs, not Hermes plugins. Verified across multiple plans; do not re-litigate.
- `.github/hooks/` => source-of-truth stubs; profile runtime contains authoritative scripts.
- Cleanup is NOT a delete-first policy; pruning only after explicit confirmation.

---

## 7. Risks / Blockers

| Risk | Likelihood | Mitigation |
|------|-----------|-----------|
| `hermes hooks list` shows 0 while scripts exist | High | Verify config first |
| Broken MCP package references in plan | Medium | Rely on `hermes mcp list` as source of truth |
| Remediation plan drift across multiple pending plans | High | Use this master plan for next-action priority |
| Docs reimplementation completion may be unverified | Medium | Run file counts/size/checklist before assuming done |

## 8. Verification Checklist

- [ ] All 11 plan files read and classified
- [ ] Skills audit state confirmed from artifacts
- [ ] Hook runtime and config status confirmed
- [ ] MCP tool inventory matches current configuration
- [ ] Prompts and test scripts cataloged above match disk
- [ ] Top 3 next actions decided from this plan
- [ ] Any destructive cleanup deferred until explicit user confirmation

## 9. Approval before implementation

Purpose: Require an explicit approval step tied to owners and dates before executing any actions in this plan that modify hooks, skills, plugins, MCP servers, or delete/prune artifacts. This locks destructive or irreversible steps behind human consent.

Scope: Applies to any plan step that performs one or more of:
- Edits to `~/.hermes/config.yaml` or profile-specific config files
- Registration/deregistration of hooks via `hermes hooks` commands
- `skill_manage(action='delete')` or any skill write operations that remove content
- Installing/uninstalling MCP servers or changing their transport
- Deleting files or directories in `C:\Users\Alexa\AppData\Local\hermes\` or the workspace root
- Bulk plugin enable/disable operations

Required fields for approval request (minimum):
- Requestor: GitHub handle or local username
- Owner(s): list of humans responsible for execution
- Scope: concise list of files/skills/hooks/plugins/MCP servers changed
- Justification: short reason for change
- Rollback plan: explicit commands or steps to revert (git commands, skill_manage reverse ops, config restore path)
- Verification steps: commands to run post-change and expected outputs
- Approval: explicit `+1` from each Owner
- Approval valid until: ISO date (e.g., 2026-07-16)

Procedure:
1. Create an approval request file under `.hermes/approvals/<timestamp>_<short-title>.md` containing all Required fields.
2. Notify Owners (email/Slack/PR) with a link to the approval file.
3. Wait for explicit `+1` confirmations (collect via comments or signed message in the approval file).
4. Once all Owners have approved, execute plan steps. The executor must paste the approval filename into the commit message for traceability.
5. Post-change: run verification steps and append outputs to the approval file.
6. If anything fails, run the Rollback plan and note the remediation in the approval file.

Risks & notes:
- Do not rely on mental approvals. File + recorded `+1` is mandatory.
- Approval files are part of repo history and must not contain secrets.
- Approval step prevents accidental bulk deletions and maintains auditability.

- [ ] All 11 plan files read and classified
- [ ] Skills audit state confirmed from artifacts
- [ ] Hook runtime and config status confirmed
- [ ] MCP tool inventory matches current configuration
- [ ] Prompts and test scripts cataloged above match disk
- [ ] Top 3 next actions decided from this plan
- [ ] Any destructive cleanup deferred until explicit user confirmation
