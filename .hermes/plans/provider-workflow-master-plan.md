# Provider Workflow Master Plan

**Created:** 2026-08-16  
**Status:** in_progress  
**Goal:** Research, plan, and fully implement workflows for each authorized Hermes provider, then apply disk cleanup, then implement all skills.

---

## Environment Snapshot

| Dimension | State |
|-----------|-------|
| Disk (C:) | 237G total, 236G used, **1.3G free (100% full)** |
| SandBox git | 32 modified, 2 untracked |
| Skills | 105 installed (2803 files, 18.3 MB) |
| MCP servers | 21 enabled |
| Profiles | 13 (default + 12 stopped) |
| .env | 28,636 bytes, 197,609 bytes on disk |

---

## Authorized Providers (from config.yaml)

| # | Provider | Primary Model | Auth | Status |
|---|----------|---------------|------|--------|
| 1 | **opencode-zen** | deepseek-v4-flash-free | OPENCODE_ZEN_API_KEY (vault) | Primary, fill_first |
| 2 | **openrouter** | nvidia/nemotron-3-ultra-550b-a55b:free | OPENROUTER_API_KEY | Fallback, fill_first |
| 3 | **gemini** | gemini-2.5-flash | GOOGLE_API_KEY / GEMINI_API_KEY | Fallback, fill_first |
| 4 | **ollama-cloud** | nemotron-3-ultra | OLLAMA_API_KEY | Fallback, fill_first |
| 5 | **xai** | (voxtral-mini-tts-2603 TTS) | XAI_API_KEY | fill_first |
| 6 | **huggingface** | (HF_TOKEN) | HF_TOKEN | fill_first |
| 7 | **deepseek** | (DEEPSEEK_API_KEY) | DEEPSEEK_API_KEY | fill_first |
| 8 | **nous** | (portal OAuth) | hermes auth | Primary base_url |

**Fallback chain:** opencode-zen → openrouter → gemini → ollama-cloud

---

## Workflow Phases

### Phase 1: Brainstorming (in_progress — this document)

For each provider, define:
- What "repeat the openrouter workflow" means concretely
- Which MCP servers, skills, and tools are relevant
- What research is needed
- What implementation artifacts should be produced

### Phase 2: Research & Specs

For each provider, produce:
- A provider workflow specification document
- Research notes from web/search tools
- MCP server compatibility assessment
- Skill inventory for that provider's workflow
- Open questions and decisions needed

### Phase 3: Implementation Plans

For each provider, create a `.hermes/plans/<provider>-workflow.md` plan with:
- Bite-sized tasks (2-5 min each)
- Exact file paths
- Verification steps
- Dependencies

### Phase 4: Execute Provider Workflows

Execute each provider's plan sequentially, with review checkpoints.

### Phase 5: Disk Cleanup

Apply `cleanup_disk.py` across workspace + hermes root.

### Phase 6: Skill Implementation

Implement each skill fully per its specs.

### Phase 7: Verification

Final status sweep, cross-reference verification.

---

## Provider Workflow Definitions

### What "Repeat the OpenRouter Workflow" Means

The OpenRouter workflow for Hermes Agent typically involves:

1. **Credential setup** — `OPENROUTER_API_KEY` in `.env`, validated via `hermes auth` / `hermes doctor`
2. **Model selection** — `hermes model` → choose OpenRouter → pick model
3. **Provider routing config** — `provider_routing` in config.yaml (sort, only, ignore, order)
4. **Fallback chain** — `fallback_providers` list in config.yaml
5. **Auxiliary model offload** — cheap models for vision/web extraction side tasks
6. **MCP server compatibility** — which MCP tools work well with this provider
7. **Rate limit / quota management** — credential pooling, key rotation
8. **Verification** — `hermes doctor`, test chat, tool-calling validation

**For each other provider, the workflow is analogous but provider-specific:**
- Different auth mechanism (API key vs OAuth vs token)
- Different model catalog
- Different rate limits and quotas
- Different MCP compatibility caveats
- Different config.yaml sections

---

## Research Targets

| Provider | Research Focus |
|----------|---------------|
| opencode-zen | API key pool, model catalog (deepseek-v4-flash-free, laguna-s-2.1-free, nemotron-3-ultra-free), credential rotation, known quirks |
| openrouter | Provider routing, fallback chains, auxiliary offload, 400+ models, rate limits, credential pooling |
| gemini | Free tier quotas, API key setup (GOOGLE_API_KEY vs GEMINI_API_KEY), model selection, doctor false positives |
| ollama-cloud | API key, model availability, context window requirements (64K min), pricing |
| xai | Grok models, API key, TTS-only or also chat, rate limits |
| huggingface | HF_TOKEN, inference endpoints, model access, rate limits |
| deepseek | API key, model availability, context window, rate limits |
| nous | Portal OAuth, model catalog, base_url configuration |

---

## Disk Cleanup Targets

| Category | Scope |
|----------|-------|
| deps | node_modules, venv, .venv, __pycache__, dist, build in SandBox and subrepos |
| archive | .archive, backup, *.bak, *.orig, *.rej, *~ |
| cache | .cache, npm-cache in workspace |
| logs | *.log, *.tmp in workspace |
| hermes root | cache, logs, archive ONLY (never deps) |
| temp | C:\Users\Alexa\AppData\Local\Temp — age-based (>3 days) |

---

## Approval Gates

- Phase 3 (implementation plans): review before execution
- Phase 4 (provider workflow execution): review after each provider
- Phase 5 (disk cleanup): **destructive** — requires explicit approval before `--apply`

---

## Artifact Inventory

### Brainstorm Documents (.hermes/plans/brainstorming/)
- provider-workflow-brainstorm.md (master)
- 8 per-provider brainstorm docs

### Workflow Specs (.hermes/plans/specs/)
- 8 per-provider workflow spec documents

### Implementation Plans (.hermes/plans/)
- 8 per-provider implementation plans
- disk-cleanup-implementation-plan.md
- skill-implementation-master-plan.md

### Execution Results (.hermes/plans/results/)
- Per-task result files
- Per-provider workflow reports

---

## Verification Checklist

- [ ] All 8 provider workflow specs created
- [ ] All 8 provider implementation plans created
- [ ] All brainstorm documents created
- [ ] Disk cleanup implementation plan created
- [ ] Skill implementation master plan created
- [ ] Each provider workflow executed and verified
- [ ] Disk cleanup applied with before/after space measurement
- [ ] All skills implemented per specs
- [ ] Final status sweep complete
- [ ] All verification artifacts written
