# Phase 2: Stale Markdown Files Deletion Catalog

## Root-Level Files (C:\Users\Alexa\Desktop\SandBox\*.md)

### KEEP (Active/Referenced)
| File | Reason |
|------|--------|
| `.hermes.md` | Active project config (highest priority) |
| `AGENTS.md` | Active project context |
| `SESSION_REPORT.md` | Active session rolling summary |
| `PLAN.md` | Active plan (asyncIO debug) |

### DELETE (Stale/Superseded/Unused)
| File | Reason |
|------|--------|
| `HERMES_PROFILE_REPORT.md` | Superseded by hermes-profiles skill |
| `HERMES_SYNC_REPORT.md` | Superseded by hermes-profiles skill |
| `judge_batch_1_results.md` through `judge_batch_28_results.md` (28 files) | Prior audit artifacts, superseded |
| `remediation_verification_2026-06-14.md` | Prior session artifact |
| `skills_audit_final_report.md` | Prior audit, superseded by new audit |
| `sample.prompt.md` | Unclear purpose, not referenced |
| `su.md` | Unclear purpose, not referenced |

**Root deletion count: 33 files**

## Docs-Level Files (C:\Users\Alexa\Desktop\SandBox\docs\*.md)

### KEEP (Active Reference Docs)
| File | Reason |
|------|--------|
| `01-MCP_BEST_PRACTICES_GUIDE.md` | Hermes reference doc |
| `02-HERMES_CONFIGURATION_GUIDE.md` | Hermes reference doc |
| `03-ENVIRONMENT_VARIABLES_REFERENCE.md` | Reference doc |
| `04-DOCKER_MCP_SETUP_GUIDE.md` | Reference doc |
| `05-COMPLETE_SETUP_VERIFICATION.md` | Reference doc |
| `06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md` | Reference doc |
| `07-MCP_SECURITY_BEST_PRACTICES.md` | Reference doc |
| `HERMES_DOCUMENTATION_INDEX.md` | Documentation index |
| `INDEX.md` | Index |
| `QUICK_REFERENCE.md` | Quick reference |
| `agents-cross-reference.md` | Cross-reference doc |
| `agents-cross-reference-registry.md` | Registry |
| `ai-readiness-report.md` | Readiness report |
| `apify.md` | Reference |
| `chroma.md` | Reference |
| `context7.md` | Reference |
| `desktop-commander.md` | Reference |
| `django-mcp-server.md` | Reference |
| `github-official.md` | Reference |
| `gitmcp.md` | Reference |
| `linear.md` | Reference |
| `markdownify-mcp.md` | Reference |
| `markitdown-mcp-server.md` | Reference |
| `mcp-google-map.md` | Reference |
| `mcp-reference-servers.md` | Reference |
| `mcp-server-fetch-typescript.md` | Reference |
| `neo4j-memory.md` | Reference |
| `neon.md` | Reference |
| `nextjs-devtools.md` | Reference |
| `node-js-sandbox.md` | Reference |
| `playwright.md` | Reference |
| `python-interpreter.md` | Reference |
| `scrapegraph.md` | Reference |
| `sentry.md` | Reference |
| `shadcn.md` | Reference |
| `vitest.md` | Reference |
| `youtube-transcripts.md` | Reference |
| `IMPLEMENTATION_PLAN.md` | Implementation plan |
| `implementation-plan.md` | Implementation plan |
| `per-project-research-queries.md` | Research queries |
| `per-repo-implementation-plans.md` | Repo plans |
| `per-repo-plan-execution-report.md` | Execution report |
| `per-repo-research-summary.md` | Research summary |
| `repo-prioritization.md` | Prioritization |
| `repo-normalization-report.md` | Normalization report |
| `repo-migration-complete.md` | Migration report |
| `git-submodules-setup-report.md` | Setup report |
| `doc-symmetry-report.md` | Symmetry report |
| `ecom-django-upgrade-plan.md` | Upgrade plan |
| `rhixecompany-comics-architecture.md` | Architecture doc |
| `rhixecompany-comics-migration-report.md` | Migration report |
| `rhixecompany-comics-plan.md` | Plan |
| `sandbox-projects-consolidation-status.md` | Status |
| `sandbox-migration-final-report.md` | Migration report |
| `sandbox-runbook-fill-guide.md` | Runbook |
| `workspace-consolidation-final-summary.md` | Summary |
| `workspace-consolidation-summary.md` | Summary |
| `categorization-prioritization.md` | Categorization |
| `dev-init-comprehensive-plan.md` | Dev init plan |
| `dev-init-spec.md` | Dev init spec |
| `dev-init-execution-summary.md` | Execution summary |
| `dev-init-implementation-guide.md` | Implementation guide |
| `dev-init-implementation-plan.md` | Implementation plan |
| `dev-init-index.md` | Index |
| `dev-init-completion-report.md` | Completion report |
| `prompt-conversion-enhancement-plan.md` | Enhancement plan |
| `prompts-cross-reference-registry.md` | Registry |
| `prompts-enhancement-report.md` | Enhancement report |
| `prompts-quality-audit-report.md` | Quality audit |
| `research-doc-cross-reference.md` | Cross-reference |
| `sample-prompt-execution-index.md` | Execution index |
| `sample-prompt-execution-summary.md` | Execution summary |
| `skill-consolidation-report.md` | Consolidation report |
| `skill-dedup-final-report.md` | Dedup report |
| `skill-library-triage.md` | Triage |
| `skills-debug-final-report.md` | Debug report |
| `skills-metadata-fix-report.md` | Metadata fix report |
| `soul-audit-verification-report.md` | Audit report |
| `ignore-file-audit-report.md` | Audit report |
| `patch-application-report.md` | Patch report |
| `patch-debug-report.md` | Debug report |
| `patch-dependency-graph.md` | Dependency graph |
| `dirs_to_delete.txt` | Deletion list |
| `dirs_to_delete_v2.txt` | Deletion list |

### DELETE — Context/Session Artifacts (291 files)
All `*-context.md` files in docs/ top level. These are session artifacts from prior audit/remediation sessions.

### DELETE — Judge Batch Artifacts in docs/
| Pattern | Count |
|---------|-------|
| `*-fix-issues-context.md` | ~30 |
| `*-verify-context.md` | ~30 |
| `*-complete*.md` | ~10 |
| `*-completion*.md` | ~5 |
| `PHASE1-*.md` | ~2 |
| `phase*-*.md` | ~10 |
| `BATCH1-*.md` | ~1 |
| `BOOST-PROMPT-*.md` | ~1 |
| `ENHANCE-MARKDOWN-*.md` | ~1 |
| `FINAL-REPORT-*.md` | ~1 |
| `TASK_COMPLETION_SUMMARY.md` | 1 |
| `WORKFLOW_COMPLETION_REPORT.txt` | 1 |
| `WORKFLOW_FILE_MANIFEST.txt` | 1 |
| `CONTEXT-MAP-COMPLETE-REPORT.md` | 1 |
| `CONTEXT-MAP-WORKFLOW-INDEX.md` | 1 |
| `UPDATE_IMPLEMENTATION_PLAN_INDEX.md` | 1 |
| `SKILLS_FIX_EXECUTION_SUMMARY.md` | 1 |
| `COMPLETION_REPORT.md` | 1 |

### DELETE — Subdir skills-debug-context.md files
All `skills-debug-context.md` files in docs subdirectories (one per skill dir). These are debug artifacts from prior sessions.

**Estimated docs deletion count: ~350-400 files**

## Total Estimated Deletions
- Root: 33 files
- Docs: ~350-400 files
- **Total: ~380-403 files**

## Execution Order
1. Delete root-level stale files (33 files)
2. Delete docs-level context/artifact files (~350 files)
3. Delete subdir skills-debug-context.md files
4. Verify after each batch
