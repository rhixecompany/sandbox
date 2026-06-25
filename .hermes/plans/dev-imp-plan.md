# Dev Imp Plan — 19 Generators × 4 Target Groups

## Scope Overview

| Target Group | Path | # Targets | Type |
|---|---|---|---|
| Root | `./` | 1 | Monorepo root |
| Automation | `./Bash/` | 1 | Bun/TS toolkit |
| Project | `./Resume_maker/` | 1 | Bun/TS job docs |
| Projects | `./projects/*` | 15 | Mixed stack repos |

**Generators:** 8 blueprint (analysis) + 11 MCP server (scaffold)

---

## Phases

### Phase 1: Blueprint Generators — Against All Existing Targets

Run each of the 8 blueprint generators against each target. Blueprint generators analyze an existing project and produce documentation/output. They don't modify source.

| # | Generator | Applies To | Output |
|---|---|---|---|
| 1 | `architecture-blueprint` | All 18 targets | Architecture blueprints (`.md` + diagrams) |
| 2 | `folder-structure-blueprint` | All 18 targets | Folder structure docs |
| 3 | `technology-stack-blueprint` | All 18 targets | Tech stack analysis |
| 4 | `readme-blueprint` | All 18 targets | README generation/enhancement |
| 5 | `code-exemplars-blueprint` | All 18 targets | Code exemplar docs |
| 6 | `copilot-instructions-blueprint` | All 18 targets | Copilot instructions |
| 7 | `project-workflow-analysis-blueprint` | All 18 targets | Workflow analysis |
| 8 | `agents-generator` | All 18 targets | AGENTS.md generation |

**Output location:** `docs/` under each target (or `docs/Project_Architecture/` as convention)

### Phase 2: MCP Server Generators — Scaffold New Projects

Run each of the 11 MCP server generators to create independent MCP server projects. These are self-contained scaffolds.

| # | Generator | Output Location |
|---|---|---|
| 9 | `python-mcp-server` | `./projects/mcp-servers/python/` |
| 10 | `typescript-mcp-server` | `./projects/mcp-servers/typescript/` |
| 11 | `rust-mcp-server` | `./projects/mcp-servers/rust/` |
| 12 | `go-mcp-server` | `./projects/mcp-servers/go/` |
| 13 | `java-mcp-server` | `./projects/mcp-servers/java/` |
| 14 | `kotlin-mcp-server` | `./projects/mcp-servers/kotlin/` |
| 15 | `csharp-mcp-server` | `./projects/mcp-servers/csharp/` |
| 16 | `php-mcp-server` | `./projects/mcp-servers/php/` |
| 17 | `ruby-mcp-server` | `./projects/mcp-servers/ruby/` |
| 18 | `swift-mcp-server` | `./projects/mcp-servers/swift/` |
| 19 | `mcp-copilot-studio-server` | `./projects/mcp-servers/copilot-studio/` |

### Phase 3: Verification

- Verify all blueprint outputs exist at expected paths
- Confirm all MCP server projects scaffold correctly (structure + deps)
- Git status check — no regressions to existing code

### Phase 4: Code Review

- Spot-check blueprint output quality for 3 random targets
- Verify MCP server project structure for each language scaffold
- Check for any unintended side effects

### Phase 5: Report

Generate `dev-imp-report.md` at workspace root with crispy format.

---

## Strict Sequential Gates

1. **Phase 1 complete** ✅ → Phase 2 starts
2. **Phase 2 complete** ✅ → Phase 3 starts
3. **Verification passes** ✅ → Phase 4 starts
4. **Review complete** ✅ → Phase 5 starts
5. **Report written** ✅ = Goal complete

No phase overlap. Each phase must fully complete before the next.

---

## Open Questions

1. **Blueprint output paths** — use `docs/Project_Architecture/` convention (existing) or `docs/blueprints/`?
2. **Already-existing blueprints** — overwrite or skip? Several targets already have architecture docs in `docs/Project_Architecture/`.
3. **MCP server projects** — scaffold under `./projects/mcp-servers/<lang>/` or at workspace root?
4. **Running obsolete generators** — some blueprint generators may produce output that overlaps with existing docs. Accept duplicates or deduplicate?
