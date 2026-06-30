# Awesome Hermes Agent — Complete File Catalog

**Repo:** `github.com/0xNyk/awesome-hermes-agent`
**Discovered:** 2026-06-05
**Last synced in this workspace:** 2026-06-29
**Total files:** 11 (3 root + 3 pages + 5 sections) + 2 metadata JSON
**Total size:** ~22 KB

---

## File Inventory

### Root (`awesome-hermes-agent/`)

| # | Path | Size | Type | Summary |
|---|------|------|------|---------|
| 1 | `.actions.json` | 1.4 KB | Metadata | 4 workflow actions, all `read_only`, `implementable_locally: false`. Covers: refer to official quickstart, list community skills, open GitHub issue for contributions, CoC enforcement. |
| 2 | `.discovery.json` | 174 B | Metadata | Minimal discovery record: repo name + page list (README, CONTRIBUTING, CODE_OF_CONDUCT). |
| 3 | `index.md` | 6.1 KB | Catalog index | Navigation hub linking to all sub-pages. Lists 4 awesome-list README sections, 3 policy pages, 18 external resource links grouped by priority. |

### Pages (`awesome-hermes-agent/pages/`)

| # | Path | Size | Type | Summary |
|---|------|------|------|---------|
| 4 | `README.md` | 5.2 KB | Main content | Full awesome-list README: Core overview, 3-step getting started, maturity tags table, 9 official resources (Nous-maintained), 5 community skills/plugins. **Duplicate block removed.** |
| 5 | `CONTRIBUTING.md` | 2.3 KB | Policy | Contribution guide: open issues (no direct PRs), 7 quality standards, maturity label guidelines. **Duplicate trailing sections removed.** |
| 6 | `CODE_OF_CONDUCT.md` | 1.9 KB | Policy | Contributor Covenant v2.0. **Duplicate attribution paragraph restored to single copy.** |

### Sections (`awesome-hermes-agent/pages/sections/`)

| # | Path | Size | Type | Summary |
|---|------|------|------|---------|
| 7 | `core-overview.md` | 972 B | Fragment | Hermes Agent capabilities: self-improving loop, Curator (v0.12.0), 7 terminal backends, 18 messaging platforms, cron, MCP, profiles, OpenClaw migration. **Extra `---` separator removed.** |
| 8 | `getting-started-(3-step-path).md` | 1.4 KB | Fragment | 3 steps: follow official quickstart → add skills (wondelai, litprog) → get a GUI (hermes-workspace, mission-control). Maturity tags table. |
| 9 | `official-resources-(nous-research-maintained).md` | 1.7 KB | Fragment | 9 Nous-maintained projects: Core, autonovel, paperclip-adapter, self-evolution, docs, release notes, tinker-atropos, Skills Hub, Discord. |
| 10 | `preamble.md` | 243 B | Fragment | Title + ecosystem status line. **Duplicated status line collapsed to single copy.** |
| 11 | `skills-&-plugins.md` | 968 B | Fragment | 5 community skills (hermes-plugins, skill-factory, litprog-skill, Wizards-of-the-Ghosts, super-hermes) with maturity labels. **Corruption fixed — cut-off sentence and duplicate entries removed.** |

---

## Per-File Content Breakdown

### 1. `.actions.json`
Four parsed actions mapping README resources to actions:
- **readme-getting-started** — points to official docs quickstart URL
- **readme-get-skills** — lists 2 community skill repos (wondelai/skills, litprog-skill)
- **contributing-open-issue** — directs to GitHub Issues for resource recommendations
- **coc-enforcement** — CoC policy notice

All status: `read_only`, no local implementation possible.

### 2. `.discovery.json`
Minimal. `{ discovered_at, pages: [3 filenames], repo: "0xNyk/awesome-hermes-agent" }`. Used internally by the discoverer tool.

### 3. `index.md`
Serves as the table of contents. Lists every extracted section/policy page with:
- Section heading and description
- File path reference
- External resource count per section
- Priority ranking (high/medium/informational)

### 4. `pages/README.md` — The Core Document
**Sections:**
- **Core Overview** — Hermes Agent self-improving loop, 7 backends, 18 platforms, cron/MCP/profiles/OpenClaw migration
- **Getting Started (3-Step Path)** — Install docs → skills → GUI
- **Maturity Tags** — production / beta / experimental definitions
- **Official Resources (Nous Research Maintained)** — 9 repos with descriptions
- **Community Skills** — 5 community projects (2 beta, 2 experimental, 1 unnamed)

### 5. `pages/CONTRIBUTING.md`
**Policy content:**
- Open-issue-only contribution model (no PRs)
- 7 quality standards for resource inclusion
- Maturity label update process
- Repository suggestions process
- Link to Code of Conduct

### 6. `pages/CODE_OF_CONDUCT.md`
Standard Contributor Covenant v2.0. No Hermes-specific content.

### 7. `pages/sections/core-overview.md`
Pure extract of README's "Core Overview" section. Self-contained overview of Hermes capabilities.

### 8. `pages/sections/getting-started-(3-step-path).md`
Extract of the "Getting Started (3-Step Path)" section + maturity tags table.

### 9. `pages/sections/official-resources-(nous-research-maintained).md`
Extract of the "Official Resources" section. Lists all 9 Nous-maintained repos.

### 10. `pages/sections/preamble.md`
Extract of README's preamble (title + ecosystem status).

### 11. `pages/sections/skills-&-plugins.md`
Extract of the "Skills & Plugins" section. Lists 5 community skills with maturity labels.

---

## Consolidated External Resources (Deduplicated)

### Nous Research Official (Maintained by Nous)

| Resource | URL | Type | Maturity |
|----------|-----|------|----------|
| Hermes Agent Core | https://github.com/NousResearch/hermes-agent | Repo | production |
| Official Documentation | https://hermes-agent.nousresearch.com/docs/ | Docs | production |
| Release Notes | https://github.com/NousResearch/hermes-agent/releases | Changelog | production |
| autonovel | https://github.com/NousResearch/autonovel | Repo | production |
| hermes-paperclip-adapter | https://github.com/NousResearch/hermes-paperclip-adapter | Repo | beta |
| hermes-agent-self-evolution | https://github.com/NousResearch/hermes-agent-self-evolution | Repo | experimental |
| tinker-atropos | https://github.com/NousResearch/tinker-atropos | Repo | experimental |
| Skills Hub | https://agentskills.io | Web | production |
| Nous Research Discord | https://discord.gg/NousResearch | Community | production |

### Community Skills & Plugins

| Resource | Author | URL | Maturity |
|----------|--------|-----|----------|
| wondelai/skills | wondelai | https://github.com/wondelai/skills | active (380+ stars) |
| litprog-skill | tlehman | https://github.com/tlehman/litprog-skill | beta (75+ stars) |
| hermes-plugins | 42-evey | https://github.com/42-evey/hermes-plugins | beta |
| hermes-skill-factory | Romanescu11 | https://github.com/Romanescu11/hermes-skill-factory | beta |
| Wizards-of-the-Ghosts | Hmbown | https://github.com/Hmbown/Wizards-of-the-Ghosts | experimental |
| super-hermes | Cranot | https://github.com/Cranot/super-hermes | experimental |

### GUIs & Dashboards

| Resource | Author | URL | Stars |
|----------|--------|-----|-------|
| hermes-workspace | outsourc-e | https://github.com/outsourc-e/hermes-workspace | 500+ |
| mission-control | builderz-labs | https://github.com/builderz-labs/mission-control | 3.7k+ |

---

## Cross-Reference: Current Hermes Skills Inventory

Comparing community skills from the awesome list against the current Hermes skill library:

| Community Resource | Present in Hermes? | Notes |
|-------------------|-------------------|-------|
| wondelai/skills | Partial | Many skills in current library originate from skills-sh org and other sources; likely partial absorption |
| litprog-skill | Not installed | 75 stars, beta — literate programming across Hermes, Claude Code, OpenCode |
| hermes-plugins | Not installed | 4 plugins: goal management, inter-agent bridging, model selection, cost control |
| hermes-skill-factory | Not installed | Meta-skill that auto-generates skills from repeated workflows |
| Wizards-of-the-Ghosts | Not installed | Experimental RPG-themed dev-ops skill pack |
| super-hermes | Not installed | Experimental skill — repo info only, minimal description |
| hermes-workspace GUI | Not installed | 500+ stars, Hermes-native workspace |
| mission-control GUI | Not installed | 3.7k+ stars, broader agent orchestration dashboard |

---

## Scrape Artifact Fixes Applied (2026-06-29)

All 6 affected files were repaired in this session:

| File | Issue Fixed | Severity Was |
|------|-------------|-------------|
| `README.md` | "Community Skills 2" duplicate block removed | Medium |
| `CONTRIBUTING.md` | "Repository Suggestions 2" and "Code of Conduct 2" trailing duplicates removed | Low |
| `CODE_OF_CONDUCT.md` | Duplicate attribution paragraph collapsed to single copy | Low |
| `preamble.md` | Duplicated status line collapsed (243 B → 243 B clean) | Low |
| `skills-&-plugins.md` | Cut-off sentence corruption + 3 duplicated entries removed (1.4 KB → 968 B) | **High** |
| `core-overview.md` | Extra `---` separator line removed | Low |

All files now clean — zero scrape artifacts remaining.

---

## Actionability Matrix

| File | Actionable? | What to do |
|------|-------------|------------|
| `.actions.json` | No | Internal metadata only |
| `.discovery.json` | No | Internal metadata only |
| `index.md` | Reference | Navigation index for docs site |
| `README.md` | Reference | Awesome-list snapshot; no install actions |
| `CONTRIBUTING.md` | No | Policy for upstream repo |
| `CODE_OF_CONDUCT.md` | No | Policy for upstream repo |
| `core-overview.md` | Reference | Hermes capabilities summary |
| `getting-started-(3-step-path).md` | Reference | Points to official docs for install |
| `official-resources-(nous-research-maintained).md` | Reference | Links to Nous repos |
| `preamble.md` | Reference | Title page |
| `skills-&-plugins.md` | **Potentially actionable** | Could install community skills (see cross-reference table) |

**Conclusion:** This directory is a **local mirror/snapshot** of `github.com/0xNyk/awesome-hermes-agent`. All files are reference material except the community skills listed in `skills-&-plugins.md`, which could be installed as external Hermes skills. All 6 scrape-artifact defects have been repaired.

---

*Generated: 2026-06-29 14:45 | Updated: 2026-06-29 (phase-4 fixes applied) | Workspace: ~/Desktop/docs/awesome-hermes-agent/*
