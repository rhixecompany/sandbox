# SPEC: Unified Platform Remediation & Optimization

> Consolidates 4 subgoals into one plan. Gate-gated: non-destructive passes run
> first; destructive actions require explicit user approval at checkpoints.

## Goals (in priority order)

1. **Config integrity** — Audit + fix SOUL.md / USER.md / MEMORY.md / .hermes.md
   / AGENTS.md / CLAUDE.md / .cursorrules across repo, hermes root, and all 13
   profiles. DRY, no frontmatter corruption, consistent inheritance chain.
2. **Disk space** — Free space safely (currently 99% full, 2.7 GB free on 237 GB).
   NO bulk app uninstalls. Cache cleanup + large-file inventory + manual review.
3. **Local LLM** — Install Ollama + compact vision+reasoning model; wire into
   Hermes / Codex / OpenCode / Copilot configs with per-target verification gates.
4. **Multi-agent fanout** — Resume from last session: OAuth re-auth, live /models
   capability query, per-provider concurrency, report generation.
5. **Diagnostic sweep** — `hermes doctor && hermes doctor --fix && hermes
   security audit && hermes status && hermes insights && hermes logs {list,errors,desktop,gateway,gui,agent} && bun run check`.
   Fix all new issues.

## Constraints (non-negotiable)

- **No bulk app uninstalls** via winget/choco without explicit approval.
- **No .env / credential files modified** directly — use `hermes config set`.
- **Profile memory files** (USER.md/MEMORY.md/SOUL.md) are NEVER auto-edited
  unless explicitly authorized per-profile; instead produce a remediation spec
  and ask user to approve the `hermes config set` / `hermes profile` commands.
- **Scripts only in `scripts/` dir** — no inline scripts.
- **≥5 files → master plan** with checkpoint gates (this spec).

## Non-Destructive Pass (executes now)

| Phase | Action | Gate |
|-------|--------|------|
| A1 | Full diagnostic sweep | `hermes doctor` == "All checks passed" |
| A2 | Profile config audit script | Exit 0; report lists drift items |
| A3 | MCP server config audit + sync | `python scripts/mcp_sync.py --dry-run` clean |
| A4 | Disk cleanup (caches only) | `df -h` shows regained space |
| A5 | Large-file inventory (>50MB) | Report + manual-review list |
| A6 | Ollama install + model pull | `ollama run <model> "test"` works |

## Destructive Pass (CHECKPOINT — requires user approval)

| Phase | Action | Requirement |
|-------|--------|-------------|
| B1 | Package-manager app uninstalls | User must approve each app list |
| B2 | Profile memory rewrites | User must approve per-profile changes |
| B3 | Ollama wiring to agent configs | Verified one-at-a-time, rollback plan |

## Output Artifacts

- `.hermes/plans/2026-08-28-unified-platform-remediation/SPEC.md` (this file)
- `.hermes/plans/2026-08-28-unified-platform-remediation/PLAN.md` (sequencing)
- `.hermes/plans/2026-08-28-unified-platform-remediation/implementation-plan.md`
- `scripts/profile_config_audit.py` — scans all 13 profiles, detects drift/corruption
- `scripts/disk_cleanup.py` — cache cleanup + large-file inventory
- `scripts/ollama_setup.py` — install + model pull + health check
- `scripts/fanout_provider_audit.py` — re-run multi-agent fanout with fixes
- `.hermes/plans/2026-08-28-unified-platform-remediation/RESULTS.md` — final report

## Verification Gates

V1: `hermes doctor` — all checks passed
V2: `python scripts/profile_config_audit.py` — exit 0, drift report
V3: `python scripts/disk_cleanup.py --dry-run` — shows reclaimable space
V4: `ollama run gemma3:4b "1+1"` — returns "2"
V5: `bun run lint && bun run format:check && bun run markdownlint` — clean
V6: Re-run diagnostic sweep — no new issues
