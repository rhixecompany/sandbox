# Provider Workflow Implementation Strategy

**Date:** 2026-08-16  
**Status:** draft  

---

## Environment Summary

| Dimension | State |
|-----------|-------|
| Hermes | v0.20.1, 105 skills, 21 MCP servers, 14 profiles |
| OpenCode | v1.18.13, NO config, NO auth |
| VS Code | v1.132.0, .vscode/mcp.json with 21 MCP servers, NO MCP extensions |
| Copilot | v1.0.80 CLI, auth TBD |
| Codex | v0.146.1, NOT on PATH, auth TBD |
| Disk | 98% full (6.3G free of 237G) |
| .github/skills | 311 items, 294 SKILL.md files |
| Hermes skills | 105 items |

---

## Provider Workflow Template (from openrouter-workflow-plan.md)

Each provider gets the same 7-task workflow:

1. **Verify Credentials** — Check API key/env var exists, test connectivity
2. **Verify Model Selection** — List models, confirm defaults, test responsiveness
3. **Verify Provider Routing** — Review config.yaml routing settings
4. **Verify Fallback Chain** — Confirm position in fallback_providers
5. **Verify Auxiliary Model Offload** — Check auxiliary task routing
6. **MCP Compatibility** — Test MCP servers with provider
7. **Compile Workflow Report** — Aggregate findings

---

## Implementation Phases

### Phase 1: Create Provider Workflow Plans
For each of the 8 providers, create a `.hermes/plans/<provider>-workflow.md` implementation plan based on the openrouter-workflow-plan.md template. Each plan adapts the 7-task template to the provider's specific auth mechanism, model catalog, and config structure.

### Phase 2: Execute Provider Workflows
Execute each provider's implementation plan. For each task, run the specified CLI commands, capture output, and write results to `.hermes/plans/results/<provider>-<task>.txt`.

### Phase 3: Skill Implementation

#### 3a. Disk Cleanup Skills
- **disk-cleanup** (devops/): Enable as Hermes plugin, create SKILL.md
- **disk-space-cleanup** (devops/): Create comprehensive SKILL.md with workflow
- **cleanup-disk** (development/): Create wrapper SKILL.md

#### 3b. MCP Server Skills
For each MCP server that doesn't have a skill in `.github/skills/`:
- Create SKILL.md with proper frontmatter
- Include reference documentation
- Include helper scripts where applicable

#### 3c. Cross-Cutting Skills
- **mcp-sequential-thinking**: Already loaded, verify completeness
- **brainstorming**: Already loaded, verify completeness  
- **plans-and-specs**: Already loaded, verify completeness
- **verification-before-completion**: Already loaded, verify completeness

### Phase 4: Hook Implementation
For each MCP server and platform, create/verify hooks:
- Session logging hooks
- Pre-exec validation hooks
- Post-exec state logging hooks

### Phase 5: Quick Commands
Document and create quick commands for each platform.

### Phase 6: Cross-Platform Sync
Create `.github/skills/` entries for skills that should be available across platforms.

### Phase 7: Verification
Test each provider workflow, each skill, each hook, each quick command.

---

## Provider-Specific Adaptations

### opencode-zen (primary, fill_first)
- Auth: OPENCODE_ZEN_API_KEY (vault) + zen-backup (manual)
- 2 credentials in pool — both must be verified
- Config: model.base_url = https://opencode.ai/zen/v1
- Models: deepseek-v4-flash-free (active), laguna-s-2.1-free, nemotron-3-ultra-free
- Special: fill_first strategy means both keys tried before fallback

### openrouter (fallback #2, fill_first)
- Auth: OPENROUTER_API_KEY (env var)
- 1 credential — no pool backup
- Config: response_cache=true, TTL=300s, min_coding_score=0.65
- Models: 400+ across 70+ providers
- Special: Provider routing (sort, only, ignore, order), fallback chains, auxiliary offload

### gemini (fallback #3, fill_first)
- Auth: GOOGLE_API_KEY or GEMINI_API_KEY (env vars)
- 1 credential — no pool backup
- Models: gemini-2.5-flash, gemini-2.5-pro
- Special: Free tier quota risk, doctor false positive bug (#26623), tier detection bug (#21399)

### ollama-cloud (fallback #4/last, fill_first)
- Auth: OLLAMA_API_KEY (env var)
- 1 credential — no pool backup
- Models: nemotron-3-ultra, gpt-oss:120b, glm-4.6:cloud, qwen3-coder:480b-cloud
- Special: Dynamic model discovery, model:tag notation, context window ≥64K required

### xai (fill_first, NOT in fallback chain)
- Auth: XAI_API_KEY (env var) OR SuperGrok OAuth
- 2 credentials — 1 failed (403)
- Models: grok-4.3 (1M context), grok-4.3-fast, grok-4.6, voxtral-mini-tts-2603 (TTS)
- Special: Two auth paths, direct-to-xAI tools (TTS, image, video, transcription, X search), provider aliases

### huggingface (fill_first, NOT in fallback chain)
- Auth: HF_TOKEN (env var)
- 1 credential — no pool backup
- Models: Qwen/Qwen3.5-397B-A17B, deepseek-ai/DeepSeek-V3.2, Llama, Mistral, 100s more
- Special: Routing suffixes (:fastest, :cheapest, :provider_name), HF_BASE_URL override, free tier $0.10/month, backend routing with automatic failover

### deepseek (fill_first, NOT in fallback chain)
- Auth: DEEPSEEK_API_KEY (env var)
- 1 credential — no pool backup
- Models: deepseek-v4-flash-free (via opencode-zen), deepseek-chat, deepseek-coder, DeepSeek-V3.2
- Special: Bug #21725 — api_key in config.yaml IGNORED, must use env var

### nous (OAuth, foundation provider)
- Auth: OAuth via hermes auth (device_code flow)
- 1 credential — OAuth token
- Models: 300+ via Nous Portal, current active: upstage/solar-pro4:free
- Special: Base URL: https://inference-api.nousresearch.com/v1, model catalog: https://hermes-agent.nousresearch.com/docs/api/model-catalog.json

---

## File Structure

### Implementation Plans
```
.hermes/plans/
  opencode-zen-workflow.md
  openrouter-workflow.md
  gemini-workflow.md
  ollama-cloud-workflow.md
  xai-workflow.md
  huggingface-workflow.md
  deepseek-workflow.md
  nous-workflow.md
  disk-cleanup-workflow.md
  provider-workflow-master-plan.md
```

### Results
```
.hermes/plans/results/
  opencode-zen-auth.txt
  opencode-zen-model.txt
  opencode-zen-mcp.txt
  opencode-zen-fallback.txt
  opencode-zen-workflow-report.md
  ... (same pattern for each provider)
  disk-cleanup-report.md
  run-cleanup.py
```

### Skills
```
.github/skills/
  disk-cleanup/SKILL.md
  disk-space-cleanup/SKILL.md
  cleanup-disk/SKILL.md
  mcp-sequential-thinking/SKILL.md (verify)
  brainstorming/SKILL.md (verify)
  plans-and-specs/SKILL.md (verify)
  verification-before-completion/SKILL.md (verify)
  <mcp-server-name>/SKILL.md (for each MCP server)
```

### Hooks
```
.github/hooks/
  <hook-name>.sh
  <hook-name>.py
```

### VS Code
```
.vscode/
  mcp.json (already exists — verify/update)
  settings.json (check for MCP settings)
```

---

## Success Criteria

1. All 8 provider workflow plans created and executed
2. All provider reports written with findings
3. All 3 disk cleanup skills implemented (SKILL.md validated)
4. All MCP server skills created or verified
5. All hooks functional on each supported platform
6. Quick commands documented for each platform
7. VS Code MCP servers verified working
8. OpenCode configured and tested
9. Copilot/Codex configured (if installed)
10. Cross-platform documentation created
11. All SKILL.md files pass frontmatter validation (name, description, version, author, license)
12. All skills follow progressive disclosure principle
