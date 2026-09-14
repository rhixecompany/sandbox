# PLAN: Unified Platform Remediation — Sequential Execution

> Strict sequential: each phase must PASS its gate before next begins.
> Gate G1 (diagnostics) is GREEN per SESSION_REPORT.md + fresh sweep below.

## Phase A: Non-Destructive Audit & Preparation (NOW)

### A1 — Diagnostic Sweep (✅ DONE)
- `hermes doctor` → ✅ All checks passed
- `hermes status` → ✅ Gateway running, config v39
- `bun run check` → ⚠️ 234 cspell issues, all in pre-existing generated JSON
- **Conclusion:** baseline is clean; no new issues introduced by this session so far.

### A2 — Profile Config Audit (NEXT)
Build `scripts/profile_config_audit.py` to scan all 13 profiles for:
- Missing SOUL.md / USER.md / MEMORY.md
- YAML frontmatter corruption (collapsed arrays, duplicated keys)
- Inheritance-chain violations (USER.md → SOUL.md → MEMORY.md)
- Cross-profile drift in provider/model routing tables
**Gate:** exit 0 + `audit-report.json` written

### A3 — MCP Config Drift Audit (carry-over from prior session)
Use existing `scripts/mcp_audit.py` + `scripts/mcp_sync.py` to verify all 4
disk configs (opencode/codex/copilot/vscode) match `.mcp/registry.json`.
**Gate:** `--dry-run` reports "no change" on all targets.

### A4 — Safe Disk Cleanup
Clean caches only (NO app uninstalls):
- Winget cache: `winget --clear-cache` (if cache dir exists)
- VS Code cache: clear `AppData/Roaming/Code/Cache` (~7.7 MB)
- npm cache: `npm cache clean --force` (0 MB, but ensures hygiene)
- Temp: list `AppData/Local/Temp/*` older than 30 days for manual review
**Gate:** `df -h /c` shows regained space.

### A5 — Large-File Inventory
Scan Downloads/VSCode/caches for files >50 MB. Write inventory to
`.hermes/plans/2026-08-28-unified-platform-remediation/large-files.json`.
**Gate:** report written, no deletions performed.

### A6 — Ollama Setup
1. Install Ollama via winget: `winget install Ollama.Ollama`
2. Pull compact vision+reasoning model: `ollama pull gemma3:4b` (2.9 GB) OR
   `qwen2.5-vl:7b` (4.6 GB) — choose based on remaining disk after A4/A5.
   **Decision point:** if < 6 GB free, skip pull, report blocker.
3. Health check: `echo "1+1=?" | ollama run gemma3:4b`
**Gate:** `ollama list` shows model; health check returns valid response.

## Phase B: Agent Config Wiring (one-at-a-time)

### B1 — Hermes → Ollama
- `hermes config set provider.ollama.base_url http://localhost:11434`
- `hermes config set model.default gemma3:4b` (or chosen model)
- Verify: `hermes doctor` still passes; `hermes run "hello"` uses local model.

### B2 — OpenCode → Ollama
- Edit `opencode.json` → add ollama provider entry
- Verify: `OPENCODE_MODEL=gemma3:4b opencode run "echo test"` works

### B3 — Codex → Ollama
- Edit `.codex/config.json` → add ollama provider
- Verify: `CODEX_MODEL=gemma3:4b codex "echo test"` works

### B4 — Copilot → Ollama
- `gh copilot model set gemma3:4b` (if supported) OR document limitation.

## Phase C: Multi-Agent Fanout Resume

### C1 — OAuth Re-auth
- `hermes auth login nous` (device flow)
- `hermes auth login openai-codex` (device flow)
- `hermes auth login xai-oauth` (device flow)
**Gate:** `hermes auth list` shows all 3 active.

### C2 — Live /models Query
- Add provider-specific /models endpoint calls to `scripts/fanout.py`
- Refresh static capability tables with live data.

### C3 — Concurrency
- Switch fanout from sequential to 4-way concurrent (respecting rate limits).

**Gate:** Full 11-cell matrix runs in <30s, report written.

## Phase D: Final Verification

- Re-run: `hermes doctor && hermes doctor --fix && hermes security audit`
- Re-run: `hermes logs errors && bun run check`
- Confirm: V1–V6 gates all pass.

**Checkpoint:** If any gate fails, pause and report before proceeding.
