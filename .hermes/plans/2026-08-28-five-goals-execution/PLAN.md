# PLAN: Five-Goal Platform Remediation

> Strict sequential. Each phase's gate must pass before the next begins.
> Every destructive action is preceded by a successful dry-run.

## Phase 0 — Discovery & Baseline (already complete)

- ✅ Read SESSION_REPORT.md
- ✅ Load 14 required skills
- ✅ `hermes doctor` → clean
- ✅ `hermes profile list` → 14 profiles enumerated
- ✅ `hermes auth list` → 11 credentials / 9 unique providers
- ✅ `hermes mcp list` → 25 servers (22 enabled, 3 disabled)
- ✅ `hermes plugins list` → enabled (browsers, etc.)
- ✅ `hermes hooks list` → 8 hooks (all approved)
- ✅ `hermes insights` → 74 sessions, 261M tokens, last 30 days
- ✅ `python scripts/profile_config_audit.py` → profile gaps identified
- ✅ `python scripts/mcp_audit.py` → 0 FAIL
- ✅ `python scripts/disk_cleanup.py --dry-run` → safe targets identified
- ✅ `python scripts/agent_provider_matrix.py --help` → CLI confirmed
- ✅ Disk: **1.41 GB free** at session start (CRITICAL)
- ✅ Ollama: installed (0.33.1), no models

**Gate 0 → 1:** All discovery checks complete. Disk inventory captured.

## Phase 1 — Context-File Unification (Goal 1)

**Goal:** Every profile has the 7 context files (or a documented waiver).
DRY: skeletons point to canonical sources, no duplication.

### Step 1.1 — Read full audit report
```bash
python scripts/profile_config_audit.py > .hermes/plans/2026-08-28-five-goals-execution/g1-audit.json
```
Inspect: which files are missing in which profiles.

### Step 1.2 — Build `profile_config_fix.py`
Non-mutating on first run (--dry-run). On apply:
- For each profile, for each missing context file:
  - Create a thin pointer file at the canonical location
  - Each file is ≤ 20 lines, points to the source of truth
  - Files: SOUL.md → ~/AppData/Local/hermes/SOUL.md, USER.md → memories/USER.md, etc.
  - Skips files that would duplicate content already in the canonical source
  - Logs every creation with path + sha256 of canonical target

### Step 1.3 — Run fix
```bash
python scripts/profile_config_fix.py --dry-run  # verify target list
python scripts/profile_config_fix.py            # apply
python scripts/profile_config_audit.py          # re-verify
```

**Gate 1 → 2:**
- `python scripts/profile_config_audit.py` reports 0 `file_missing`
  (or all `file_missing` are explicitly waived with rationale)
- `profile-config-fix-report.json` lists every file created
- Each new file is a pointer, not a copy

## Phase 2 — Provider Matrix (Goal 2)

**Goal:** Noninteractive runner executes one request against all 9 providers
+ all 14 profiles, captures result rows with provider, context, max-output,
capabilities.

### Step 2.1 — Read existing artifacts
- `prompts/agent-provider-matrix.prompt.md` (exists from prior session)
- `scripts/agent_provider_matrix.py` (exists)
- `docs/agent-provider-matrix.md` (if exists)

### Step 2.2 — Build the runner skill
Create `~/AppData/Local/hermes/skills/autonomous-ai-agents/agent-provider-matrix-runner/`:
- `SKILL.md` — workflow + verification checklist
- `references/output-schema.md` — row schema
- `templates/prompt.md` — copy of `prompts/agent-provider-matrix.prompt.md`

### Step 2.3 — Execute
```bash
# Dry-run the full matrix
python scripts/agent_provider_matrix.py --dry-run

# Live: at least one cell (limit-cells 1 keeps quota safe)
python scripts/agent_provider_matrix.py --request "Reply with: PROVIDER OK" --limit-cells 1
```

**Gate 2 → 3:**
- Dry-run exits 0, full matrix enumerated
- Live run produces ≥ 1 result row with all 8 fields populated
- `agent-provider-matrix-results.json` exists in `.hermes/plans/results/`

## Phase 3 — MCP Server Sync (Goal 3)

**Goal:** All disk MCP configs (opencode, codex, copilot, vscode) match the
canonical registry. Disabled hermes servers documented.

### Step 3.1 — Re-audit
```bash
python scripts/mcp_audit.py
```

### Step 3.2 — Sync (idempotent)
```bash
python scripts/mcp_sync.py --dry-run  # should show "no change"
python scripts/mcp_sync.py            # apply if drift detected
python scripts/mcp_audit.py           # re-verify
```

### Step 3.3 — Document disabled servers
Append a section to `.hermes/plans/2026-08-28-five-goals-execution/g3-summary.md`:
- atlassian (needs ATLASSIAN_TOKEN)
- docs (disabled, not in registry)
- postgres (disabled, replaced by neon)

**Gate 3 → 4:**
- `mcp_audit.py` → 0 FAIL on all 4 disk configs
- `mcp_sync.py --dry-run` → "no change" (idempotent)
- Disabled servers documented with rationale

## Phase 4 — Disk Cleanup + Ollama (Goal 4)

**Goal:** Free disk; install + verify a small vision+reasoning Ollama model;
wire it into hermes + at least one of copilot/codex/opencode.

### Step 4.1 — Safe disk cleanup (no app uninstalls in this pass)
```bash
python scripts/disk_cleanup.py --dry-run  # verify target list
python scripts/disk_cleanup.py            # apply safe cleanups
```
Reports before/after MB for each cache.

### Step 4.2 — App inventory (no removal in this pass)
```bash
python scripts/disk_cleanup.py --scan-large > .hermes/plans/2026-08-28-five-goals-execution/g4-large-files.json
```
Capture `winget list` + `choco list` to `g4-installed-apps.txt` for user review.

### Step 4.3 — Ollama model selection
Based on post-cleanup free space:
- ≥ 5 GB: pull `gemma3:4b` (~3.3 GB, vision+text, strong reasoning)
- 3-5 GB: pull `qwen2.5vl:3b` (~3.2 GB, vision+reasoning)
- < 3 GB: report blocker, do not pull

### Step 4.4 — Pull + verify
```bash
ollama pull <chosen-model>
echo "Reply with: OLLAMA OK" | ollama run <chosen-model>
curl -s http://localhost:11434/api/tags
```

### Step 4.5 — Wire to agents
- Hermes: `hermes config set model.ollama.<chosen-model> ollama:<chosen-model>`
- OpenCode: edit `opencode.json` (small entry)
- Codex: edit `.codex/config.json` (small entry)
- Copilot: only supports GitHub-hosted models; document limitation

**Gate 4 → 5:**
- `ollama list` shows the model
- `curl localhost:11434/api/tags` returns it
- At least hermes + one of opencode/codex is wired
- Disk free after cleanup reported in `g4-disk-after.txt`

## Phase 5 — Final Verification (Goal 5)

**Goal:** Run all 12 verification commands; catalog and fix every finding.

### Step 5.1 — Commands
```bash
hermes doctor
hermes doctor --fix
hermes security audit
hermes status
hermes insights
hermes logs list
hermes logs errors
hermes logs desktop
hermes logs gateway
hermes logs gui
hermes logs agent
bun run check
```

### Step 5.2 — Triage
Each output → one of:
- **PASS:** recorded, no action
- **WARN:** documented, root cause, decision (fix or accept)
- **FAIL:** must fix before completion

### Step 5.3 — Systematic debug
For every FAIL or unaddressed WARN: apply 4-phase systematic-debugging
(observe → hypothesize → test → confirm root cause → fix → verify).

### Step 5.4 — Final report
`.hermes/plans/2026-08-28-five-goals-execution/FINAL-REPORT.md` with:
- Phase-by-phase summary
- All bugs found, root cause, fix, verification
- Final hermes doctor + bun run check status
- Disk before/after
- Recommendations for next session

**Gate 5 → Done:**
- All phases pass
- FINAL-REPORT.md written
- SESSION_REPORT.md updated

## Execution discipline

- One phase at a time. No skipping.
- Every tool call: parameter pre-flight, output verification, no
  plausible-sounding fabrication.
- Subagents (delegate_task) only for the truly independent parallel work.
  Everything that touches the same config file or shared state stays
  sequential.
- Approval gates for destructive changes (cleanups, MCP sync, app
  uninstalls).

## Success criteria

The pipeline is complete when:
- All 5 goals show PASS in the final report
- All 5 gates (G0..G4 → Done) green
- No outstanding FAIL in any verification command
- Disk free is reported (target: ≥ 2 GB after cleanup)
