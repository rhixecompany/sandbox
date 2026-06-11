---
agent: Debug Mode Instructions
model: GPT-5 mini (copilot)
description: Batch Fix All Errors, Warnings, and Deprecations.
tools: [vscode, execute, read, agent, edit, search, web, 'github/*', 'github/*', 'io.github.upstash/context7/*', 'io.github.vercel/next-devtools-mcp/*', 'neondatabase/mcp-server-neon/*', vscode.mermaid-chat-features/renderMermaidDiagram, cweijan.vscode-postgresql-client2/dbclient-getDatabases, cweijan.vscode-postgresql-client2/dbclient-getTables, cweijan.vscode-postgresql-client2/dbclient-executeQuery, github.vscode-pull-request-github/issue_fetch, github.vscode-pull-request-github/suggest-fix, github.vscode-pull-request-github/searchSyntax, github.vscode-pull-request-github/doSearch, github.vscode-pull-request-github/renderIssues, github.vscode-pull-request-github/activePullRequest, github.vscode-pull-request-github/openPullRequest, ms-azuretools.vscode-azureresourcegroups/azureActivityLog, ms-azuretools.vscode-containers/containerToolsConfig, ms-windows-ai-studio.windows-ai-studio/aitk_get_ai_model_guidance, ms-windows-ai-studio.windows-ai-studio/aitk_get_agent_model_code_sample, ms-windows-ai-studio.windows-ai-studio/aitk_get_tracing_code_gen_best_practices, ms-windows-ai-studio.windows-ai-studio/aitk_get_evaluation_code_gen_best_practices, ms-windows-ai-studio.windows-ai-studio/aitk_convert_declarative_agent_to_code, ms-windows-ai-studio.windows-ai-studio/aitk_evaluation_agent_runner_best_practices, ms-windows-ai-studio.windows-ai-studio/aitk_evaluation_planner, ms-windows-ai-studio.windows-ai-studio/aitk_get_custom_evaluator_guidance, ms-windows-ai-studio.windows-ai-studio/check_panel_open, ms-windows-ai-studio.windows-ai-studio/get_table_schema, ms-windows-ai-studio.windows-ai-studio/data_analysis_best_practice, ms-windows-ai-studio.windows-ai-studio/read_rows, ms-windows-ai-studio.windows-ai-studio/read_cell, ms-windows-ai-studio.windows-ai-studio/export_panel_data, ms-windows-ai-studio.windows-ai-studio/get_trend_data, ms-windows-ai-studio.windows-ai-studio/aitk_list_foundry_models, ms-windows-ai-studio.windows-ai-studio/aitk_agent_as_server, ms-windows-ai-studio.windows-ai-studio/aitk_add_agent_debug, ms-windows-ai-studio.windows-ai-studio/aitk_gen_windows_ml_web_demo, prisma.prisma/prisma-migrate-status, prisma.prisma/prisma-migrate-dev, prisma.prisma/prisma-migrate-reset, prisma.prisma/prisma-studio, prisma.prisma/prisma-platform-login, prisma.prisma/prisma-postgres-create-database, todo]
---

## Plan: Batch Fix All Errors, Warnings, and Deprecations

**TL;DR:**
Batch fix all errors, warnings, and deprecations surfaced by `pnpm install`, `pnpm validate`  . Auto-format, document, and verify all changes, ensuring zero issues remain and all fixes are traceable and standards-compliant.

---

### **Steps**

#### Phase 1: Error & Warning Collection

1. Run all validation/build/test scripts and wait for the scripts to complete:

- `pnpm install`
- `pnpm validate`

2. Collect all errors, warnings, and deprecations from the output.

#### Phase 2: Root Cause Analysis & Documentation

3. For each error/warning:
   - Read the full file(s) involved.
   - Analyze the root cause (import path, missing file, type error, deprecated API, etc.).
   - Search official docs for any third-party package errors/deprecations.
   - Document the error, its root cause, and the fix approach.
   - Include links to relevant documentation for each issue.
   - Prioritize fixes based on severity and impact.
   - Identify any patterns (e.g., multiple errors from the same root cause) to batch fix similar issues together.
   - For deprecations, research the recommended replacement APIs and document the migration path.
   - For warnings, determine if they indicate potential future errors or performance issues and prioritize accordingly.
   - For errors, categorize them by type (e.g., syntax errors, type errors, missing dependencies) to streamline the fixing process.
   - For each issue, note any potential side effects of the proposed fix to ensure comprehensive testing later.
   - Output a structured report (e.g. JSON, file: docs/proposedFixes.MD) with all errors/warnings, their causes, and proposed fixes.

#### Phase 3: Batch Fixes

4. Apply fixes in batch, granularly or systematically as needed:
   - Read docs/proposedFixes.MD for context on proposed fixes.
   - Ensure all fixes adhere to coding standards and best practices.
   - Correct import paths and aliases.
   - Restore or create missing files if required by convention.
   - Update deprecated APIs to supported alternatives.
   - Fix type errors, lint issues, and test failures.
   - Only touch code related to surfaced issues.

#### Phase 4: Auto-format & Standards Enforcement

5. Run `pnpm lint:fix` to auto-format the codebase and fix any remaining style issues.

#### Phase 5: Verification & Iteration

6. Rerun all scripts:
   - `pnpm validate`

7. If any errors/warnings remain, repeat Phases 2–5 until all scripts pass cleanly.

#### Phase 6: Documentation & Reporting

8. For each significant fix:
   - Document before-and-after code snippets.
   - Explain why the change was necessary.
   - Reference relevant docs or resources.
   - Update README, CHANGELOG, and architectural docs if usage/setup/architecture changed.
   - Add inline comments for non-obvious fixes.

#### Phase 7: Commit & Final Verification

9. Commit all fixes in a single batch with a clear, comprehensive summary.
10. Cross-verify that all scripts complete successfully with zero errors and zero warnings.

---

### **Relevant Files**

- All files surfaced by the validation/build/test scripts (see previous error logs for specifics).

---

### **Verification**

- All scripts (`pnpm install`, `pnpm validate`, `pnpm lint:fix`, ) complete with zero errors and zero warnings.
- All fixes are documented and traceable.
- Codebase remains consistent with project standards and conventions.

---

### **Decisions & Constraints**

- No unrelated refactoring or new features.
- Only fix issues surfaced by validation/build/test/deprecation output.
- Any allowed warnings must be documented and justified.

---

**Next:**
Begin by running all validation scripts, collecting the current errors/warnings, and then proceed stepwise through the plan above. You will receive a detailed report and all code changes as the process completes.

---
