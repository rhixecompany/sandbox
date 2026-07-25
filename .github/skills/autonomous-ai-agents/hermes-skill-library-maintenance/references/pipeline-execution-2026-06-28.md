# Execute-All-Prompts Pipeline — 2026-06-28 Execution Record

Record of the full `/execute-all-prompts` pipeline execution across 362 skills and 4 phases.

## Pipeline Structure

| Phase | Prompt | Sub-phases | Output |
|-------|--------|------------|--------|
| 1. Audit Skills Judge Fix | `audit-skills-judge-fix.prompt.md` | 7 (inventory → categorize → dedupe → judge → remediate → consolidate → verify) | judge_results/*.tsv, *.md |
| 2. Agents System Prompt Context Fix | `agents-system-prompt-context-fix.prompt.md` | 3 (generate context → audit VS Code → verify) | Architecture docs, VS Code config audit |
| 3. Sync Hermes Copilot Codex | `sync-hermes-copilot-codex.prompt.md` | 4 (inventory instructions → identify roots → sync bidirectionally → verify) | Agents/instructions/skills synced |
| 4. Test Providers & Models | `test-providers-models.prompt.md` | 7 (auth inventory → catalog discovery → free extraction → benchmark → comparison → rate limits → scripts) | Provider status report |

## Phase 1 Results (2026-06-28)

### Before
- Total skills: 381 SKILL.md files
- Duplicates: 9 flat root-level dirs with identical names to category subdir versions
- FAIL (<60): 3 skills (smithery-ai-cli: 43, introspection-only-general: 58, no-net-fetch: 58)

### After
- Total skills: 372 (9 duplicates removed)
- Duplicates: 0 (by-name)
- PASS (≥80): 45 (12.4%)
- WARN (60-79): 317 (87.6%)
- FAIL (<60): 0
- Average score: 72.5/100
- 3 FAIL remediated with targeted patches (added title, version, author, license, tags, pitfalls, workflow sections)

### Key Scripts
- `~/AppData/Local/hermes/scripts/batch_skill_judge.py` — heuristic scorer across 5 dimensions (frontmatter 20pts, structure 20pts, content 20pts, DRY 20pts, references 20pts)
- `~/AppData/Local/hermes/scripts/batch_remediate.py` — adds missing frontmatter fields + sections to <60 skills
- `~/AppData/Local/hermes/scripts/consolidate_skills.py` — keyword-based overlap detection (5097 potential overlaps, 22 thin skills)

### Duplicate Detection Method
```bash
cd $LOCALAPPDATA/hermes/skills
grep -rh "^name:" --include="SKILL.md" . | sort | uniq -d
# 9 duplicates found: stable-diffusion, qdrant, modal, lambda-labs,
# accelerate, here-now, cli, flash-attention, torchtitan
```

Richness comparison (flat vs category subdir):
```bash
wc -l <dir1>/SKILL.md <dir2>/SKILL.md
# Keep the larger/richer one (usually the category-subdir version)
```

### Remediation Pattern for FAIL Skills
Skills scoring <60 typically lack: title, version, author, license, tags frontmatter fields, Pitfalls section, Workflow section, Skills Required table, and Verification Checklist. Adding all of these with substantive content (not placeholders) reliably pushes scores from 40-58 → 60-74. The SKILL.md file should remain under 250 lines; move detailed content to references/.

### Phase 2 Results
- All 20+ subprojects have AGENTS.md
- 59 architecture docs in docs/Project_Architecture/
- Root VS Code config: settings.json, launch.json, mcp.json, tasks.json, extensions.json
- Status: Pre-existing, no changes needed

### Phase 3 Results
- Copilot: ~120 .agent.md files, ~180 .instructions.md files
- Codex: ~150 .toml agent files
- Status: Pre-existing, no changes needed

### Phase 4 Results
- 7 providers inventoried: opencode-zen (active), nous (cooldown), openrouter (cooldown), huggingface (active), ollana-cloud (active), openai-api (active), copilot (rate-limited), xai-oauth (new)
- Active session model: deepseek-v4-flash-free (opencode-zen)
- Status: Verified, no changes needed