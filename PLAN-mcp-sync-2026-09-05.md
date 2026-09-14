# MCP Server Sync — Implementation Plan

**Generated:** 2026-09-05
**Spec:** `.hermes/SPEC-mcp-sync-2026-09-05.md`
**Workspace:** C:\Users\Alexa\Desktop\SandBox

---

## Phase 1: Fix Sync Script (Critical, 1 file)

**Goal:** Make `scripts/sync-mcp-configs.ps1` actually write to the real Copilot config.

### Step 1.1 — Replace `.copilot/mcp.json` references with `.github/mcp.json`

**File:** `scripts/sync-mcp-configs.ps1`
**Action:** Edit lines 20, 21, 162, 163 to use `.github/mcp.json` instead of `.copilot/mcp.json`.
**Verify:** Re-run the script; confirm `[SYNC]` or `[OK]` line for `.github/mcp.json` and no phantom `.copilot/mcp.json` file is created.

### Step 1.2 — Make sync script idempotent + verbose

**File:** `scripts/sync-mcp-configs.ps1`
**Action:** When the target file does not exist, create it from scratch (instead of failing silently). Add `-Verbose` switch for diagnostic output.
**Verify:** Delete `.github/mcp.json` temporarily, re-run, confirm it's regenerated with the expected schema (`{ "mcpServers": { ... } }`).

---

## Phase 2: Disable Dead Endpoints (5 servers × 4 configs)

**Goal:** Mark `anthropic-resources`, `stripe`, `plaid`, `everart`, `parallel-task` as `enabled: false` everywhere.

### Step 2.1 — Disable in `opencode.json`

**Action:** Edit each of the 5 entries: add `"enabled": false` (4 of them already have it; only `everart` may need the flag). Confirm.
**Verify:** Run `python scripts/validate-mcp-servers.py`; all 5 should now report `disabled`.

### Step 2.2 — Disable in `.codex/mcp.json`

**Action:** Same 5 entries. Note `.codex/mcp.json` does NOT use `enabled`; instead, add to a `disabledServers: []` array at the top level (matching github/mcp.json convention) — OR omit the entry. Decision: add `disabledServers: []` array and move the 5 servers into it (plus `atlassian`, `docs`, `postgres` for parity).
**Verify:** `codex mcp list` should NOT list any of the 5 disabled servers.

### Step 2.3 — Disable in `.github/mcp.json`

**Action:** Add the 5 dead servers to the existing `disabledServers` array.
**Verify:** `copilot mcp list` should NOT list any of the 5 disabled servers.

### Step 2.4 — Disable in `.vscode/mcp.json`

**Action:** VSCode schema does NOT support `enabled: false` or `disabledServers`. The fix is to remove these servers from `.vscode/mcp.json` entirely. But to preserve audit trail, comment them in the `notes` field of the root object.
**Verify:** VSCode should show only enabled servers in its MCP panel.

### Step 2.5 — Disable in `projects/Python-projects/.mcp.json`

**Action:** None required — that file does not list the 5 dead servers.

---

## Phase 3: Replace HEAD Validation with JSON-RPC POST (1 file)

**Goal:** Eliminate false positives in `scripts/validate-mcp-servers.py`.

### Step 3.1 — Replace `_test_remote_server` to use POST initialize

**File:** `scripts/validate-mcp-servers.py`
**Action:** Replace `HEAD` with `POST` of JSON-RPC `initialize` body. Treat any 2xx, plus 401 (needs auth) and 405 (method-specific) as "working" — because real MCP servers respond to POST initialize with a valid handshake or auth challenge.
**Verify:** Run validator; `context7`, `parallel-search`, `tavily`, `honcho`, `neon`, `sentry`, `smithery` should all report `working`.

### Step 3.2 — Skip disabled servers from validation report noise

**Action:** In `validate_all`, skip servers where `enabled: false`.
**Verify:** Disabled servers do NOT appear in the "broken" section of the report.

### Step 3.3 — Test local commands properly

**Action:** `_test_local_command` currently only checks that the executable exists. Add a real `--help` invocation with 5s timeout to verify the binary responds.
**Verify:** Each local command (`bunx`, `docker`, `python`) reports `working`.

---

## Phase 4: Sync All Configs (1 run of the fixed sync script)

**Goal:** All 3 workspace configs have the same enabled-server set.

### Step 4.1 — Run the corrected sync script

**Command:** `powershell scripts/sync-mcp-configs.ps1`
**Action:** The script should:
1. Detect 0 new servers in opencode.json (since opencode.json already has the 32 servers).
2. Sync opencode.json → `.github/mcp.json` (will fix any drift).
3. Sync opencode.json → `.codex/mcp.json` (will fix any drift).

**Verify:** Compare server counts and names across all 3 configs. They should be identical.

---

## Phase 5: Verify Runtime via Live Tool Calls

**Goal:** Prove that MCP servers actually work, not just that they're configured.

### Step 5.1 — Test currently-loaded MCP tools via this session

**Action:** Call `mcp__context7__resolve-library-id`, `mcp__tavily__tavily-search`, `mcp__parallel-search__web_search`, and `mcp__sequentialthinking__sequentialthinking` from this hermes session.
**Verify:** Each call returns a valid response (not an error).

### Step 5.2 — Document test results in session

**Action:** Note in the validation report which MCP servers were confirmed-live.

---

## Phase 6: Author Reusable Skill

**Goal:** Capture the workflow in a SKILL.md so future agents can re-run it.

### Step 6.1 — Write `hermes-mcp-sync` skill

**Path:** `C:\Users\Alexa\.opencode\skills\hermes-mcp-sync\SKILL.md` (or workspace `.opencode/skills/`)
**Content:** Frontmatter (name, description, trigger phrases), then sections:
- When to use this skill
- MCP config architecture (4 platforms, schema translation)
- How to run validation
- How to sync configs
- How to add a new MCP server (decision tree)
- Common pitfalls (HEAD probe false positive, sync script path bug)

**Verify:** Skill file exists with valid frontmatter; can be loaded via `skill` tool.

---

## Phase 7: Final Audit and Report

**Goal:** Confirm all acceptance criteria from SPEC §5.

### Step 7.1 — Run final validation

**Command:** `python scripts/validate-mcp-servers.py`
**Verify:** Report saved to `.hermes/mcp-validation-report.md` shows expected server counts.

### Step 7.2 — Compare config files

**Action:** Use a Python script or jq to diff enabled-server sets across all 3 workspace configs.
**Verify:** All 3 configs have identical enabled-server sets.

### Step 7.3 — Update session summary

**Action:** Write `.hermes/mcp-sync-2026-09-05-summary.md` documenting what changed, what was fixed, and what was disabled.

---

## Rollback Strategy

If sync breaks a config:
1. `git checkout opencode.json .github/mcp.json .codex/mcp.json .vscode/mcp.json`
2. Re-run `python scripts/validate-mcp-servers.py` to confirm baseline state.

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Sync script corrupts `.github/mcp.json` schema | Backup via git before first run; verify after run with `python -m json.tool < .github/mcp.json` |
| Validation script false-positives a working server | Acceptable to leave a server marked "broken" if runtime is the only test — but our POST initialize approach should cover all real cases |
| Removing entries from `.vscode/mcp.json` breaks VSCode MCP picker | Add `notes` field documenting the disabled list so VSCode users can re-add manually |
| Hermes store drift | Out of scope — Hermes has its own CLI; document in skill, do not auto-sync |

---

## Definition of Done

All acceptance criteria in SPEC §5 checked, plus:
- [ ] No file outside the 5 listed configs and 2 scripts (`sync-mcp-configs.ps1`, `validate-mcp-servers.py`) was modified
- [ ] All edits pass `python -m json.tool < file` (valid JSON)
- [ ] Git diff reviewed before commit
