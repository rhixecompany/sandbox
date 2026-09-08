---
name: test-providers-models
title: "Test Providers Models"
description: "Comprehensive workflow for testing, ranking, and configuring Hermes LLM providers and models. Use when adding new providers, auditing model performance, or configuring fallback chains."
version: 3.0.0
author: Alexa
license: MIT
tags: [providers, models, testing, configuration, hermes, llm]
metadata:
  hermes:
    tags: [providers, models, testing, configuration]
    related_skills: [web-research-pipeline, executing-plans, subagent-driven-development]
---

# Test Providers Models — Comprehensive Implementation Prompt

## Overview

Automated reasoning and workflow tool for `test-providers-models`. Execute multi-step provider testing with deterministic quality controls and structured outputs.

## Goal

Discover, test, rank, and configure the best free LLM providers and models for Hermes Agent. Produce a ranked top-5 model list, configure Hermes with the primary model, and set up fallback chains with remaining models.

## Subgoals

1. **Inventory** — Capture current Hermes config, auth providers, status, and fallback state
2. **Research** — Web-search all authorized providers for free models (`:free`, `-free` suffixes)
3. **Consolidate** — Deduplicate and migrate all test-providers-models files to canonical location
4. **Test** — Execute standardized test prompts against each discovered model
5. **Rank** — Audit test results and rank top 5 by quality, speed, reliability
6. **Configure** — Set primary model and fallback chain via `hermes config set` / `hermes fallback add`
7. **Verify** — Validate all configuration changes and run prompts-judge on this prompt

## Specs

### specs.md

| Spec ID | Requirement | Acceptance Criteria |
|---------|-------------|---------------------|
| S1 | Capture all authorized providers | `hermes auth list` output parsed, all providers enumerated |
| S2 | Web-research each provider for free models | Documentation URLs extracted, model lists compiled |
| S3 | Consolidate all test-providers-models files | Single canonical location: `.github/prompts/operations/test-providers-models/` |
| S4 | Test up to 10 free models | Each model receives standardized test prompt, results logged |
| S5 | Rank top 5 models | Ranking based on: response quality, latency, context window, capabilities |
| S6 | Configure Hermes primary model | `hermes config set model <provider/model>` |
| S7 | Configure fallback chain | `hermes fallback clear` + `hermes fallback add` for remaining 4 |
| S8 | All artifacts on disk | No duplicates, all files in correct paths |
| S9 | prompts-judge score ≥ 98 | Run `/prompts-judge` on this prompt, fix all issues |

### plans.md

| Phase | Task | Dependencies | Est. Time |
|-------|------|--------------|-----------|
| P1 | Inventory & Research | None | 10 min |
| P2 | Consolidate & Deduplicate | P1 | 5 min |
| P3 | Test Models | P2 | 20 min |
| P4 | Rank & Configure | P3 | 10 min |
| P5 | Verify & Judge | P4 | 5 min |

### goals.md

- **G1**: Comprehensive implementation prompt with all required sections
- **G2**: All test-providers-models files consolidated to canonical location
- **G3**: Top 5 free models identified and ranked
- **G4**: Hermes configured with primary model + 4 fallback models
- **G5**: All judge scores ≥ 98

### subgoals.md

- **SG1**: Execute `hermes config show && hermes auth list && hermes status && hermes insights && hermes fallback list`
- **SG2**: Web-research each provider for free models
- **SG3**: Create test prompts (Provider, Context, max-output, capabilities)
- **SG4**: Execute `hermes chat --provider "X" --model "Y" -q "test" --oneshot` for each model
- **SG5**: Audit all test sessions, rank top 5
- **SG6**: Configure Hermes model and fallback chain
- **SG7**: Run prompts-judge, fix issues, achieve score ≥ 98

### rules.md

1. **MCP-first**: Use MCP servers (fetch, web-search) before native tools
2. **No destructive without approval**: User pre-approved all destructive ops
3. **DRY**: Each fact in one location, cross-reference don't duplicate
4. **Verify before claim**: Test, check, confirm before reporting
5. **Hermes config via CLI**: Always use `hermes config set`, never direct YAML edits
6. **Background execution**: Long commands run in background without timeout
7. **Subagent delegation**: Parallel work via `delegate_task` subagents
8. **Judge threshold**: All artifacts must score ≥ 98 on respective judge skills

### phases.md

#### Phase 1: Inventory & Research
- Execute Hermes diagnostic commands in background
- Parse authorized providers from auth list
- Web-research each provider for free models
- Extract documentation URLs and model specifications

#### Phase 2: Consolidate & Deduplicate
- Find all test-providers-models files across filesystem
- Migrate to `.github/prompts/operations/test-providers-models/`
- Delete duplicates and stale copies
- Verify single canonical location

#### Phase 3: Test Models
- Create standardized test prompts
- Execute `hermes chat` for each discovered model
- Log all results with Provider, Context, max-output, capabilities
- Handle rate limits and retries

#### Phase 4: Rank & Configure
- Audit all test sessions
- Score and rank top 5 models
- Configure primary model via `hermes config set`
- Configure fallback chain via `hermes fallback add`

#### Phase 5: Verify & Judge
- Validate Hermes configuration
- Run `/prompts-judge` on this prompt
- Fix all issues, warnings, errors
- Achieve score ≥ 98

### steps.md

| Step | Action | Command/Tool | Output |
|------|--------|--------------|--------|
| 1 | Get Hermes config | `hermes config show` | Config state |
| 2 | Get auth providers | `hermes auth list` | Provider list |
| 3 | Get system status | `hermes status` | Status info |
| 4 | Get usage insights | `hermes insights` | Model usage |
| 5 | Get fallback config | `hermes fallback list` | Fallback state |
| 6 | Web-research providers | `web_search` + `web_extract` | Free model lists |
| 7 | Consolidate files | `search_files` + `terminal` | Single location |
| 8 | Create test prompts | `write_file` | Test prompt files |
| 9 | Execute model tests | `hermes chat --oneshot` | Test results |
| 10 | Rank results | Subagent analysis | Top 5 ranking |
| 11 | Configure primary | `hermes config set model` | Config updated |
| 12 | Configure fallbacks | `hermes fallback add` | Fallback set |
| 13 | Verify config | `hermes config show` | Validation |
| 14 | Run prompts-judge | `/prompts-judge` | Score report |
| 15 | Fix and re-judge | Patch + re-run | Score ≥ 98 |

### tasks.md

- [ ] Execute all Hermes diagnostic commands
- [ ] Parse and enumerate all authorized providers
- [ ] Web-research each provider for free models
- [ ] Extract documentation URLs for all free models
- [ ] Create free-suffix-catalog markdown file
- [ ] Find all test-providers-models files across filesystem
- [ ] Consolidate to `.github/prompts/operations/test-providers-models/`
- [ ] Delete all duplicate/stale copies
- [ ] Create standardized test prompts
- [ ] Execute `hermes chat` for each model (up to 10)
- [ ] Log all test results
- [ ] Audit and rank top 5 models
- [ ] Create ranking markdown file
- [ ] Configure Hermes primary model
- [ ] Clear existing fallback chain
- [ ] Add 4 fallback models
- [ ] Verify final configuration
- [ ] Run prompts-judge on this prompt
- [ ] Fix all issues to achieve score ≥ 98

### actions.md

| Action | Trigger | Tool | Expected Result |
|--------|---------|------|-----------------|
| Run diagnostics | Phase 1 | `terminal` (background) | All config/state captured |
| Web research | Phase 1 | `web_search` + `web_extract` | Free model lists per provider |
| Consolidate files | Phase 2 | `search_files` + `terminal` | Single canonical location |
| Test model | Phase 3 | `hermes chat --provider X --model Y -q "..." --oneshot` | Model response logged |
| Rank models | Phase 4 | Subagent analysis | Top 5 ranked list |
| Set primary | Phase 4 | `hermes config set model provider/model` | Config updated |
| Add fallback | Phase 4 | `hermes fallback add provider/model` | Fallback configured |
| Verify | Phase 5 | `hermes config show` | Config validated |
| Judge | Phase 5 | `/prompts-judge` | Score ≥ 98 |

### gates.md

| Gate | Check | Pass Criteria |
|------|-------|---------------|
| G1 | All diagnostics executed | All 5 commands completed |
| G2 | All providers researched | ≥1 free model per authorized provider |
| G3 | Files consolidated | Single location, zero duplicates |
| G4 | Models tested | ≥5 models tested successfully |
| G5 | Ranking complete | Top 5 models identified |
| G6 | Config updated | Primary model set correctly |
| G7 | Fallback configured | 4 fallback models added |
| G8 | Judge score | prompts-judge ≥ 98 |

## Workflow

### Phase 1: Inventory & Research

```bash
# Execute in background without timeout
hermes config show && hermes auth list && hermes status && hermes insights && hermes fallback list
```

Parse output for:
- Authorized providers (from auth list)
- Current model configuration
- Existing fallback chain
- Rate limit status per provider

Then web-research each provider:
```
web_search: "<provider name> free models API documentation 2026"
web_extract: <documentation_urls>
```

### Phase 2: Consolidate & Deduplicate

```bash
# Find all test-providers-models files
find . -name "*test-providers*" -type f 2>/dev/null
find . -name "*free-suffix-catalog*" -type f 2>/dev/null
```

Migrate all to: `.github/prompts/operations/test-providers-models/`

Delete duplicates in:
- `.github/prompts/development/test-providers-models/`
- `.github/prompts/testing/test-providers-models/`
- `.github/prompts/test-providers-models-free-suffix-catalog.md`
- `.github/prompts/operations/test-providers-models-free-suffix-catalog.md`
- `.hermes/plans/*test-providers*`
- `.hermes/specs/*test-providers*`
- `.hermes/reports/*test-providers*`

### Phase 3: Test Models

Create standardized test prompts covering:
- Provider identification
- Context window capabilities
- Max output length
- Reasoning capabilities
- Instruction following

Execute for each model:
```bash
hermes chat --provider "<provider>" --model "<model>" -q "<test_prompt>" --oneshot
```

### Phase 4: Rank & Configure

Rank by:
1. Response quality (accuracy, coherence)
2. Latency (response time)
3. Context window size
4. Max output tokens
5. Instruction following

Configure:
```bash
hermes config set model <top_provider>/<top_model>
hermes fallback clear
yes | hermes fallback add <provider2>/<model2>
yes | hermes fallback add <provider3>/<model3>
yes | hermes fallback add <provider4>/<model4>
yes | hermes fallback add <provider5>/<model5>
```

### Phase 5: Verify & Judge

```bash
hermes config show
hermes fallback list
```

Then run:
```
/prompts-judge .github/prompts/operations/test-providers-models/test-providers-models.prompt.md
```

Fix all issues and re-run until score ≥ 98.

## Tools & References

| Tool | Purpose |
|------|---------|
| `terminal` | Execute Hermes CLI commands |
| `web_search` | Research provider free models |
| `web_extract` | Extract documentation content |
| `search_files` | Find and consolidate files |
| `delegate_task` | Parallel model testing |
| `write_file` | Create/update artifacts |
| `patch` | Targeted edits to files |

## Pitfalls

- **Rate limits**: Many free models have strict rate limits; space requests
- **Provider auth**: Some providers may have expired or rate-limited credentials
- **Model availability**: Free models may be deprecated; verify before testing
- **Config corruption**: Always use `hermes config set`, never edit YAML directly
- **Duplicate files**: Stale copies in prompts_backup, .hermes/plans, .hermes/specs
- **Timeout**: Long-running `hermes chat` commands need background execution

## Verification Checklist

- [ ] All Hermes diagnostics executed
- [ ] All authorized providers enumerated
- [ ] Web research completed for each provider
- [ ] Free model catalog created
- [ ] All files consolidated to canonical location
- [ ] No duplicate files remain
- [ ] Test prompts created and executed
- [ ] All test results logged
- [ ] Top 5 models ranked
- [ ] Hermes primary model configured
- [ ] Fallback chain configured (4 models)
- [ ] Configuration verified
- [ ] prompts-judge score ≥ 98

## Best Practices

1. **Background execution**: Run long commands in background without timeout
2. **Subagent parallelism**: Delegate model testing to subagents
3. **Incremental verification**: Check each phase before proceeding
4. **CLI-only config**: Never edit Hermes YAML directly
5. **DRY artifacts**: Single source of truth for each file
6. **Judge-driven quality**: Run judge skills early and often

## Output Artifacts

| Artifact | Path |
|----------|------|
| Main prompt | `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` |
| Free model catalog | `.github/prompts/operations/test-providers-models/test-providers-models-free-suffix-catalog.md` |
| Ranking results | `.github/prompts/operations/test-providers-models/test-providers-models-ranking.md` |
| Test probe script | `.github/prompts/operations/test-providers-models/scripts/test-providers-probe.py` |
