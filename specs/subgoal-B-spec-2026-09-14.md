# Subgoal B Spec — Web-Research + Agent-Browser (OpenRouter Free Models)

## Requirements (verified from user directive)
- Agent-browser (`https://openrouter.ai/models?variant=free`) using `browser_exec` tool.
- Convert HTML → markdown; generate markdown report.
- Execute `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` per model.
- Create/update artifacts: `./plans/subgoal-B-*`, `./specs/subgoal-B-*`, `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` (updated/executed), `results/web-research-subgoal-B-*.md`.
- Approved: all crud batches; best quality; subagent delegation; approvals requested.

## Evidence Requirements (real artifacts — no fabrication)
- Browser execution log / page info (verified by real output).
- Markdown conversion artifact (`.md`) with real file size.
- Markdown report (`.md`) listing real free models (names, URLs, descriptions from page — verified by content match).
- Prompt execution results per model (`results/`) — real response content, verified by file existence/size/content check.
- No synthetic model names / capabilities / rankings.

## Non-Functional Constraints
- .env untouched; identity/DRY preserved; security findings not hidden.
- Communication: concise, table-first, direct, action-first, verification-first.
- Multi-file protocol: sequential execution (B after A complete); approvals before crud execution.

## Subagent Task
1. Execute `agent-browser` (browser_exec) to fetch openrouter.ai free models page.
2. Convert HTML → markdown (`convert-pdf-to-md` or equivalent markdown conversion — verified by real `.md` artifact).
3. Generate markdown report with real model entries (verified by content match with page).
4. Read `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` (verify file exists; update if needed).
5. Execute prompt per model in report; collect real responses.
6. Create/update artifacts; verify file sizes/checksums.
7. Request approvals (clarification / kanban mechanism).
8. Deliver results file (`results/web-research-subgoal-B-*.md`) with verified outputs.
