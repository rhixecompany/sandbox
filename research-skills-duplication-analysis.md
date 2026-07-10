# Research Skills: Duplication Analysis & Shared Reference Opportunities

Analyzed 17 skills across the `research/` category plus research-adjacent skills. Below are groups that can share reference files, templates, or consolidate to reduce redundancy.

---

## GROUP 1: Web Content Pipeline (8 skills — HIGHEST consolidation potential)

**Skills:**

- `web-research-pipeline` — orchestrates search→extract→save pipeline
- `firecrawl-search` — web search with content
- `firecrawl-scrape` — URL content extraction
- `firecrawl-map` — URL discovery on sites
- `firecrawl-crawl` — bulk site extraction
- `firecrawl-agent` — AI structured extraction
- `firecrawl-download` — download entire site
- `scrapling` — stealth HTTP/browser scraping (alternative backend)

**Duplication found:**

- Each firecrawl skill has its own `references/overview.md` with *identical* empty boilerplate ("Add quick-start instructions here", "Add usage examples here") — pure waste.
- The escalation pattern (search→scrape→map→crawl→download→agent) is redundantly documented in every firecrawl skill's "see also" section.
- `web-research-pipeline` has a multi-backend fallback chain (mcp-fetch→firecrawl→web_extract→scrapling→playwright) that duplicates extraction patterns across firecrawl skills.
- `scrapling` is already listed as a fallback in `web-research-pipeline`'s backend chain, making its standalone skill partially redundant as a research tool (it's a scraping library, not a workfow orchestrator).

**Shared file candidates:**
| Shared file | Description | Beneficiary skills |
|---|---|---|
| `references/backend-fallback-chain.md` | Single source of truth for extraction backend priority (mcp-fetch → firecrawl → web_extract → scrapling → playwright) | web-research-pipeline, scrapling, repo-research-pipeline |
| `references/escalation-pattern.md` | When to use search vs scrape vs map vs crawl vs agent vs download | All firecrawl skills + web-research-pipeline |
| `references/output-conventions.md` | Shared file naming, slug conventions, metadata headers | All firecrawl skills, web-research-pipeline, scrapling |
| Consolidate firecrawl-* skills | Merge 6 firecrawl skills into 1-2 umbrella skills (e.g. `firecrawl` + `firecrawl-agent`) | Eliminates 5 redundant `references/overview.md` files |

**Rationale:** These 8 skills form a single escalation stack — you never use all 6 firecrawl tools at once. web-research-pipeline already orchestrates them. The fallback chain is identical across all extraction tasks. Consolidating reduces 6 empty `references/overview.md` files and eliminates duplicated escalation documentation.

---

## GROUP 2: OSINT / Public Records Cluster (2 skills — MEDIUM potential)

**Skills:**

- `osint-investigation` — public records OSINT (SEC, contracts, lobbying, sanctions, property, courts, news)
- `domain-intel` — passive domain reconnaissance (DNS, SSL, WHOIS, subdomains)

**Duplication found:**

- osint-investigation already lists domain-intel as a `related_skill` and explicitly defers infrastructure-level OSINT to it.
- Both share the same design philosophy: "Python stdlib only, zero dependencies, no API keys."
- osint-investigation defines a 3-tier confidence system (exact→high, fuzzy→medium, token_overlap→low) that domain-intel could reuse.
- Both use entity resolution (name normalization, suffix/punctuation stripping) with the same matching logic.

**Shared file candidates:**
| Shared file | Description | Beneficiary skills |
|---|---|---|
| `references/confidence-tiering.md` | Standardized confidence levels (exact/high, fuzzy/medium, token_overlap/low) with definitions | osint-investigation, domain-intel |
| `references/entity-resolution-methods.md` | Name normalization, suffix stripping, token-bag matching patterns | osint-investigation, domain-intel |
| `references/rate-limit-best-practices.md` | Retry-After handling, sleep between paginated requests, 429 handling | osint-investigation, domain-intel, scrapling |

**Rationale:** These two skills serve complementary purposes (infrastructure vs. financial/public records OSINT) but share identity resolution, evidence handling, and rate-limit patterns. A shared confidence tiering reference prevents drift between how "fuzzy match" is defined in each skill. Domain-intel's domain availability Python script could also be referenced as a generic "passive probing" utility.

---

## GROUP 3: Pipeline Orchestrators (3 skills — HIGH potential, partial overlap)

**Skills:**

- `repo-research-pipeline` — multi-project research pipeline with MCP tools
- `web-research-pipeline` — single-topic web search→extract→save pipeline
- `content-research-writer` (creative category) — research synthesis for writing

**Duplication found:**

- Both pipeline skills define an MCP tool precedence table (mcp-fetch → mcp-filesystem → mcp-smithery → fallback) — nearly identical.
- Both define the same slugify function, file naming rules, and output directory structure.
- repo-research-pipeline consumes web-research-pipeline as a sub-skill — their output formats should be compatible.
- Both reference the same fallback backend chain (mcp-fetch → firecrawl → web_extract).
- repo-research-pipeline references RESEARCH_REPORT.md templates — these are useful for web-research-pipeline too.

**Shared file candidates:**
| Shared file | Description | Beneficiary skills |
|---|---|---|
| `references/mcp-tool-precedence.md` | Single authoritative table: which MCP tool for which task, fallback order | repo-research-pipeline, web-research-pipeline |
| `references/slug-conventions.md` | Unified slugify rules, file naming, collision handling, Windows path limits | repo-research-pipeline, web-research-pipeline |
| `references/report-template.md` | RESEARCH_REPORT.md template with methodology section and cross-ref section | repo-research-pipeline, web-research-pipeline |

**Rationale:** Both pipelines do the same thing at different scales. Their overlapping conventions (slugify, output structure, MCP fallback chain) should come from shared files so changes propagate to both. The RESEARCH_REPORT.md template belongs in a shared reference rather than being embedded in one skill.

---

## GROUP 4: Scholarly Knowledge Management (3 skills — MEDIUM potential)

**Skills:**

- `research-toolkit` — arXiv search, blog monitoring (blogwatcher), paper writing
- `llm-wiki` — persistent markdown knowledge base
- `dspy` (mlops/research) — declarative LM programming

**Duplication found:**

- research-toolkit already subsumes what were previously standalone `arxiv`, `blogwatcher`, and `research-paper-writing` skills — consolidation is already done.
- llm-wiki's SCHEMA.md defines frontmatter conventions, tagging taxonomy, and provenance markers that could be referenced by research-toolkit for paper reading notes.
- research-toolkit's paper writing pipeline has a full literature review phase; the findings naturally feed into llm-wiki.
- dspy is orthogonal (it optimizes LM programs) but could be referenced from the "experiments" phase of research-toolkit's paper writing pipeline.

**Shared file candidates:**
| Shared file | Description | Beneficiary skills |
|---|---|---|
| `references/frontmatter-conventions.md` | Standard frontmatter schema (title, created, updated, sources, confidence) for research notes | research-toolkit, llm-wiki |
| `references/provenance-markers.md` | How to trace claims back to sources (^[raw/article.md] pattern from llm-wiki) | research-toolkit, llm-wiki, osint-investigation |

**Rationale:** research-toolkit finds papers → llm-wiki stores them as persistent knowledge → research-toolkit's paper writing consumes them. The frontmatter and provenance conventions from llm-wiki are portable patterns that research-toolkit should adopt to unify how research findings are recorded across both skills.

---

## GROUP 5: Parallel CLI Redundancy (IMMEDIATE fix)

**Skills:**

- `parallel-cli` — full vendor CLI wrapper (search, extract, research, enrich, findall, monitor)
- `parallel-cli-web-research` — subset focused on extract, findall, monitor only

**Duplication found:**

- `parallel-cli-web-research` is a strict subset of `parallel-cli`. All its commands (extract, findall, monitor) exist in the parent skill with more documentation.
- The web-research variant has no unique content, no additional examples, and no linked files beyond what parallel-cli provides.
- Both have identical installation and auth instructions.

**Recommendation:** **Merge into single `parallel-cli` skill and delete `parallel-cli-web-research`.** The parent skill already covers all three subcommands with richer documentation, error handling tables, and usage patterns.

---

## GROUP 6: Standalone Skills (LOW overlap — keep separate)

**Skills with minimal duplication potential:**

- `gitnexus-explorer` — codebase knowledge graph. Unique tool (GitNexus), no overlap with other research skills.
- `polymarket` — prediction market data. Unique API, no overlap.
- `drug-discovery` — pharmaceutical research. Domain-specific (ChEMBL, PubChem, OpenFDA). No shared patterns.
- `dspy` — LM programming framework. Different domain entirely (ML research frameworks).

These are correctly standalone. No consolidation or shared references recommended.

---

## Summary of Waste Identified

| Waste type | Count | Details |
|---|---|---|
| Empty `references/overview.md` files | 6 | firecrawl-* skills each have identical empty boilerplate |
| Fully redundant skill | 1 | `parallel-cli-web-research` is a strict subset of `parallel-cli` |
| Duplicated escalation pattern | 6+ | "search→scrape→map→crawl→download→agent" documented in every firecrawl skill |
| Duplicated fallback chain | 2 | repo-research-pipeline and web-research-pipeline define the same mcp-fetch→firecrawl→web_extract→scrapling→playwright chain independently |

## Priority Actions

1. **Merge `parallel-cli-web-research` into `parallel-cli`** — immediate, no content loss, strictly additive.
2. **Create shared `references/backend-fallback-chain.md`** — stop duplicating the extraction backend priority in web-research-pipeline and repo-research-pipeline.
3. **Create shared `references/mcp-tool-precedence.md`** — unify MCP-first tables across both pipeline skills.
4. **Create shared `references/confidence-tiering.md`** — unify evidence confidence definitions across osint-investigation and domain-intel.
5. **Clean up 6 firecrawl `references/overview.md`** files — either populate or remove the empty boilerplate.
6. **Consider firecrawl umbrella consolidation** — merge 6 firecrawl skills into `firecrawl` + `firecrawl-agent` to eliminate 5 empty overview files and deduplicate the escalation pattern.
