# Scripts Audit — 2026-09-05 02:21 UTC

Dir: `scripts` | Threshold: 99
Count: 46 | Avg: 83.6 | Passed: 0
Syntax failures: 0
Quick-command registry: PASS

| File | Lang | Score | Rating | Syntax | CLI | Err | Doc | DRY |
|---|---|---|---|---|---|---|---|---|
| `agent-provider-matrix-smokecheck.sh` | bash | 62 | WARN | 20 | 0 | 8 | 14 | 20 |
| `agent_provider_matrix.py` | python | 85 | PASS | 20 | 20 | 20 | 20 | 5 |
| `apply_quick_commands.py` | python | 92 | PASS | 20 | 20 | 12 | 20 | 20 |
| `auth_inventory.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `bulk_fix_plans.py` | python | 88 | PASS | 20 | 20 | 12 | 20 | 16 |
| `bulk_fix_prompts.py` | python | 80 | PASS | 20 | 12 | 12 | 20 | 16 |
| `comprehensive-implementation.py` | python | 74 | PASS | 20 | 12 | 12 | 20 | 10 |
| `disk_cleanup.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `docker_cleanup.py` | python | 88 | PASS | 20 | 20 | 12 | 20 | 16 |
| `fanout.py` | python | 90 | PASS | 20 | 20 | 20 | 20 | 10 |
| `fix_provider_models.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `generate-mcp-skills.py` | python | 62 | WARN | 20 | 0 | 6 | 20 | 16 |
| `git_sync.sh` | bash | 84 | PASS | 20 | 14 | 20 | 14 | 16 |
| `hermes-mcp-manager.py` | python | 70 | PASS | 20 | 0 | 20 | 20 | 10 |
| `hermes_config_audit.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `hermes_diagnostic.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `hermes_doctor.py` | python | 90 | PASS | 20 | 20 | 20 | 20 | 10 |
| `hermes_maintenance.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `hermes_quick_commands.py` | python | 90 | PASS | 20 | 20 | 20 | 20 | 10 |
| `hq.py` | python | 60 | WARN | 20 | 0 | 0 | 20 | 20 |
| `instruction_audit.py` | python | 90 | PASS | 20 | 20 | 20 | 20 | 10 |
| `instruction_fix.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `log_analysis.py` | python | 88 | PASS | 20 | 20 | 12 | 20 | 16 |
| `mcp_audit.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `mcp_sync.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `ollama_wire.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `package_inspector.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `plugins_hooks_audit.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `profile_config_audit.py` | python | 88 | PASS | 20 | 12 | 20 | 20 | 16 |
| `profile_config_fix.py` | python | 82 | PASS | 20 | 12 | 20 | 20 | 10 |
| `prompt_dry_audit.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `prompt_dry_bulk_fields.py` | python | 88 | PASS | 20 | 20 | 12 | 20 | 16 |
| `prompt_dry_fix.py` | python | 88 | PASS | 20 | 20 | 12 | 20 | 16 |
| `provider_executor.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `provider_executor_noninteractive.sh` | bash | 74 | PASS | 20 | 0 | 20 | 14 | 20 |
| `remediate_hooks_score.py` | python | 88 | PASS | 20 | 12 | 20 | 20 | 16 |
| `stage_missing_lsps.sh` | bash | 62 | WARN | 20 | 0 | 8 | 14 | 20 |
| `subagent_dispatcher.py` | python | 82 | PASS | 20 | 20 | 12 | 20 | 10 |
| `submodule_commit.sh` | bash | 66 | WARN | 20 | 0 | 12 | 14 | 20 |
| `sync-mcp-config.ts` | ts | 48 | FAIL | 20 | 0 | 0 | 8 | 20 |
| `sync-mcp-configs.ps1` | ps1 | 50 | WARN | 20 | 0 | 0 | 14 | 16 |
| `validate-mcp-consistency.ts` | ts | 44 | FAIL | 20 | 0 | 0 | 8 | 16 |
| `validate-mcp-servers.py` | python | 88 | PASS | 20 | 12 | 20 | 20 | 16 |
| `validate_maintenance_artifacts.py` | python | 96 | PASS | 20 | 20 | 20 | 20 | 16 |
| `verify-full-implementation.py` | python | 76 | PASS | 20 | 0 | 20 | 20 | 16 |
| `verify_prompt_corpus.py` | python | 88 | PASS | 20 | 12 | 20 | 20 | 16 |
