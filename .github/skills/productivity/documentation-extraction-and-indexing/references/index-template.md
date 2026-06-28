# Index.md Catalog Template

## Standard Index Structure

```markdown
# <Source Name> Documentation Index — Phase <N> Extraction

**Generated:** <date>  
**Source:** <source-document> Phase <N> targets  
**Extraction Method:** `web_extract` (primary) + browser fallback  
**Total Pages:** <count>/<expected> ✅

---

## Catalog

| # | File | Source URL | Status | Size (chars) |
|---|------|------------|--------|--------------|
| 1 | [`filename.md`](filename.md) | https://... | ✅ Extracted | ~5000+ |
| 2 | [`filename.md`](filename.md) | https://... | ✅ Extracted | ~8000+ |
| ... | ... | ... | ... | ... |

---

## Topic Clusters

### <Cluster Name>
- **<Feature>** — <description>, <key files>

### <Cluster Name>
- **<Feature>** — <description>, <key files>

---

## Verification

```bash
# Count files
ls docs/<source>/*.md | wc -l
# → <expected>

# Verify source headers
head -3 docs/<source>/*.md
# → All show "# Source: <URL>"

# Check for truncation
grep -r "truncated\|summary" docs/<source>/
# → (empty)
```

---

## Next Phase

**Phase <N+1>:** <Next phase description>  
- <Step 1>
- <Step 2>
- <Reference to plan/doc>
```

## Example: Hermes Docs Index (from this session)

```markdown
# Hermes Agent Documentation Index — Phase 3 Extraction

**Generated:** 2026-06-13  
**Source:** [sample.prompt.md](file:///C:/Users/Alexa/Desktop/SandBox/sample.prompt.md) Phase 3 targets  
**Extraction Method:** `web_extract` (primary) + full content preservation  
**Total Pages:** 12/12 ✅

---

## Catalog

| # | File | Source URL | Status | Size (chars) |
|---|------|------------|--------|--------------|
| 1 | [github.com_0xNyk_awesome-hermes-agent.md](github.com_0xNyk_awesome-hermes-agent.md) | https://github.com/0xNyk/awesome-hermes-agent | ✅ Extracted | ~3000+ |
| 2 | [hermes-agent.nousresearch.com_docs_user-guide_features_skills.md](hermes-agent.nousresearch.com_docs_user-guide_features_skills.md) | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | ✅ Extracted | ~8000+ |
| ... | ... | ... | ... | ... |

---

## Topic Clusters

### Core Features
- **Skills** — Progressive disclosure, SKILL.md format, CLI commands, bundles
- **MCP** — Model Context Protocol integration, server config, tool filtering, WSL2 bridging
...

### Getting Started
- **Quickstart** — Install, provider selection (30+ providers), first chat
- **Learning Path** — Beginner/Intermediate/Advanced tracks
- **Tips & Best Practices** — Prompting, context files, memory vs skills

### Ecosystem
- **Awesome Hermes Agent** — Curated community resources

---

## Verification

```bash
ls docs/hermes/*.md | wc -l  # → 12
head -3 docs/hermes/*.md     # → All have "# Source: <URL>"
```

---

## Next Phase

**Phase 4:** Profiles and Workspace Markdown  
- Research all Markdown files in `docs/*`
- Identify available profiles
- Create profiles with `hermes profile create {name} --clone-all`
```

## Key Principles

1. **Always link to files** — relative paths in catalog table
2. **Include size** — quick truncation check
3. **Group by topic** — not alphabetical
4. **Show verification commands** — runnable proof
5. **Reference next phase** — maintains workflow continuity