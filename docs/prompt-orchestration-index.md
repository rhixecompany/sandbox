# Prompt Orchestration — Artifact Index

> Navigate all files created during the `/prompt-management` workflow orchestration.

---

## 1. Planning Layer (`plan/`)

| File | Size | Description |
|------|------|-------------|
| `plan/prompt-orchestration-comprehensive-plan.md` | 856L | Full spec: executive summary, phase specs, safety gates, risk register, deliverables matrix, rollback procedures |

## 2. Code Layer (`docs/`)

| File | Size | Description |
|------|------|-------------|
| `docs/prompt-orchestration-code-samples.py` | 766L | Production implementation: 6 classes (Phase0Verification, Phase1AuditJudgeFix, Phase2ContextFix, Phase3SyncAgents, Phase4TestProviders, PromptOrchestrator) |
| `docs/prompt-orchestration-implementation-guide.md` | 1,410L | Step-by-step execution: quick start, phase tutorials, shell scripts, checklists, troubleshooting (15 issues), rollback procedures |

## 3. Support Layer (`docs/`)

| File | Size | Description |
|------|------|-------------|
| `docs/prompt-orchestration-execution-summary.md` | ~150L | One-page summary: what was executed, key outcomes, deliverable list |
| `docs/prompt-orchestration-index.md` | (this file) | Full artifact navigator |
| `docs/prompt-orchestration-decision-trees.md` | ~200L | Decision trees for common workflow choices |

## 4. Pipeline Tracking (`docs/`)

| File | Description |
|------|-------------|
| `docs/orchestrator-progress.md` | Phase-level progress tracker (all ✅) |
| `docs/orchestrator-verification.md` | Final verification report (all ✅) |
| `docs/pipeline-result.json` | Machine-readable pipeline result |
| `docs/pipeline-summary.md` | Markdown pipeline summary |

## 5. Phase 1 Artifacts

### Inventory & Reports

| File | Description |
|------|-------------|
| `docs/local-skills.md` | Complete skills inventory (143 dirs, 489+ SKILL.md) |
| `docs/dedupe-report.md` | 9 duplicates identified and removed |
| `docs/consolidation-report.md` | Umbrella skill consolidation |
| `docs/final-verification.md` | Phase 1 final verification |

### Judge Results

| Directory/File | Description |
|----------------|-------------|
| `judge_results/all_results.tsv` | All 350+ skills with scores |
| `judge_results/summary.md` | Aggregate statistics |
| `judge_results/batch_*.md` | 35 per-batch result files |

## 6. Phase 2 Artifacts

| File | Description |
|------|-------------|
| `docs/Project_Architecture/` | 59+ architecture blueprints, folder structures, tech stacks |
| `docs/vscode-validation-report.md` | VS Code JSON validation (112 files, 0 errors) |
| `.vscode/settings.json` | VS Code settings (29 keys) |
| `.vscode/extensions.json` | VS Code extensions |
| `.vscode/launch.json` | Debug launch configs |
| `.vscode/tasks.json` | Task definitions |
| `.vscode/mcp.json` | MCP server config |

## 7. Phase 3 Artifacts

| File | Description |
|------|-------------|
| `docs/sync-drift-report.md` | Zero drift verified for plugins + hooks |
| `.github/instructions/` | 186 instruction files |
| `.github/agents/` | 174 agent files |
| `.github/plugins/` | 4 plugins (synced with Hermes) |
| `.github/hooks/` | 3 hooks (synced with Hermes) |

## 8. Phase 4 Artifacts

| File | Description |
|------|-------------|
| `docs/provider-inventory.md` | Auth methods and status for 7 providers |

## 9. Scripts (`~/AppData/Local/hermes/scripts/`)

| Script | Purpose |
|--------|---------|
| `run-pipeline.sh` | Full pipeline runner (all 5 phases) |
| `batch-judge.sh` | Skill judge in batches of 10 |
| `validate-vscode.sh` | VS Code JSON validation across all projects |
| `check-sync-drift.sh` | Hermes ↔ Copilot drift checker |

## File Tree Summary

```
~/Desktop/SandBox/
├── plan/
│   └── prompt-orchestration-comprehensive-plan.md  ← 1 file
├── docs/
│   ├── prompt-orchestration-code-samples.py         ← 766 lines
│   ├── prompt-orchestration-implementation-guide.md ← 1,410 lines
│   ├── prompt-orchestration-execution-summary.md
│   ├── prompt-orchestration-index.md
│   ├── prompt-orchestration-decision-trees.md
│   ├── orchestrator-progress.md
│   ├── orchestrator-verification.md
│   ├── pipeline-result.json
│   ├── pipeline-summary.md
│   ├── local-skills.md
│   ├── dedupe-report.md
│   ├── consolidation-report.md
│   ├── final-verification.md
│   ├── vscode-validation-report.md
│   ├── sync-drift-report.md
│   ├── provider-inventory.md
│   └── Project_Architecture/                        ← 59+ files
├── judge_results/
│   ├── all_results.tsv
│   ├── summary.md
│   └── batch_*.md                                   ← 35 files
└── .vscode/                                         ← 5 files
```
