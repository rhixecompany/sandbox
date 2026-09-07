# Steps

## Step 1 — Build Inventory and Role Classification

1. Walk `.github/prompts/` and collect all files matching `*generator*.prompt.md` and `*mcp*server*.prompt.md`.
2. Match against the exact 11 prompts declared in the orchestrator prompt's Subagents section.
3. Confirm exactly 11. If mismatched, produce an **inventory_drift** error and halt.
4. Classify each into: **Analysis**, **Documentation**, or **Code-generation**.
5. For each, extract `name`, `title`, `tags`, `dependencies`, and `toolsets` from frontmatter.

## Step 2 — Normalize Inputs Using Deterministic Defaults

1. If `mode` is not provided, set to `full`.
2. If `validation-level` is not provided, set to `strict`.
3. If `include-code-generation` is not provided, derive from mode:
   - `full` → `true`
   - `quick` → `false`
4. For `custom` mode, validate provided stage list against known stages A-E; auto-inject any missing prerequisites.

## Step 3 — Execute Stage A (Parallel)

1. Run `technology-stack-blueprint-generator.prompt.md` — detects programming languages, frameworks, versions, build tools.
2. Run `folder-structure-blueprint-generator.prompt.md` — maps project tree and naming conventions.
3. **Gate A:** Both must produce Markdown output with `## Stack Summary` (or equivalent) and `## Folder Structure` sections. If either fails, retry once with `validation-level=stricter`. If retry fails, record degraded warning.

## Step 4 — Execute Stage B (Gated, Dependency Order)

1. Run `architecture-blueprint-generator.prompt.md` — reads stack + folder outputs to produce architecture docs.
2. Run `project-workflow-analysis-blueprint-generator.prompt.md` — reads stack + arch outputs to document workflows.
3. Run `code-exemplars-blueprint-generator.prompt.md` — reads stack + folder outputs to find exemplars.
4. **Gate B:** All three must exist and reference only Stage A outputs. No forward references. Architecture must have a diagram section; workflow must have a data-flow section.

## Step 5 — Execute Stage C (Gated)

1. Run `copilot-instructions-blueprint-generator.prompt.md` — reads Stage A + Stage B artifacts.
2. Run `readme-blueprint-generator.prompt.md` — reads all prior artifacts.
3. **Gate C:** Cross-link validation — the project name, stack, and framework versions must be consistent across ALL Stage A, B, and C outputs. Any mismatch = hard gate failure. Emit targeted remediation.

## Step 6 — Execute Stage D (Conditional)

1. Check detected stack from Stage A for technology indicators.
2. For each detected technology, run the corresponding MCP generator:
   - TypeScript detected → `typescript-mcp-server-generator.prompt.md`
   - Python detected → `python-mcp-server-generator.prompt.md`
   - Swift detected → `swift-mcp-server-generator.prompt.md`
   - Copilot Studio / Power Platform detected → `mcp-copilot-studio-server-generator.prompt.md`
3. If no MCP language is detected and `include-code-generation=true`, run TypeScript as default safe fallback.
4. **Gate D:** Each MCP output must have a valid `package.json` / `pyproject.toml` / `Package.swift` equivalent and at least one tool definition.

## Step 7 — Execute Stage E (Final Consolidation)

1. **Consistency validation:** Compare stack, project name, version, and key terms across ALL artifacts from ALL stages. Flag every inconsistency.
2. **Manifest generation:** Write `orchestrator-manifest.json` listing: run mode, stages executed, prompts invoked, per-prompt status (success/fail/degraded), gate results.
3. **Validation report:** Write `orchestrator-validation-report.md` with per-gate pass/fail, warnings, and remediation checklist.
4. **Handoff decision:** If no hard failures → PASS. If any hard failure (cross-doc inconsistency, gate A/B/C fail after retry) → FAIL with remediation checklist.
