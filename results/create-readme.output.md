# create-readme — Execution Report

**Action:** Generated a comprehensive root `README.md` for the `projects/mcp-servers` project (a multi-language MCP server collection).

**Target project:** `C:\Users\Alexa\Desktop\SandBox\projects\mcp-servers`

**Output written:**

- `C:\Users\Alexa\Desktop\SandBox\projects\mcp-servers\README.md` (new, 3.9 KB)
- This report → `C:\Users\Alexa\Desktop\SandBox\results\create-readme.output.md`

**Why this project:** A scan of `projects/` showed every subdirectory either already had a README or was a multi-package repo (e.g. `mcp-servers`, `profile`). `mcp-servers` had 11 language subdirectories each with its own README but **no root README** to orient newcomers — the highest-value gap.

**What the README covers:**

- Project intro + note on shared MCP stdio transport and comparable tool set
- Languages table (11 dirs: TypeScript, Python, Go, Rust, Java, Kotlin, PHP, Ruby, Swift, C#, Copilot Studio)
- Getting started with per-language commands + MCP Inspector tip
- Repository layout, architecture overview, development notes
- GitHub admonitions (`[!NOTE]`, `[!TIP]`, `[!IMPORTANT]`) per prompt guidance
- Deliberately omits LICENSE/CONTRIBUTING/CHANGELOG sections (per rules 4)

**Evidence used (workspace files):**

- `mcp-servers/AGENTS.md`, `architecture.md`, `folder-structure.md`, `tech-stack.md`
- Per-language `README.md` files (read from `typescript/`, `python/`, `go/`, `csharp/`, `rust/`, `java/`, `kotlin/`, `php/`, `ruby/`, `swift/`)

**Skipped references:**

- Prompt template `templates/create-readme/phases.md` — missing (per-prompt templates not present; used inline body which is authoritative).
- Core rules file `prompts/templates/_shared/rules-core.md` — missing; applied standard prompt rules inline.
- Example README URLs in the prompt (Azure-Samples/serverless-*, sinedied/*) — used as structural inspiration only; fetched 2 of them (`run-on-output`, `smoke`) for tone/format reference.

**Verification:** Root README present and well-formed GFM; language table matches actual top-level directories (`typescript`, `python`, `go`, `rust`, `java`, `kotlin`, `php`, `ruby`, `swift`, `csharp`, `copilot-studio`). No unrelated files modified.
