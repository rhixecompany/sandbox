---
name: template-server-test-all-tools
version: 1.0.0
date: 2026-09-13
dependent_on: ./plans/30-hermes-mcp-servers-master-plan.md (P4 SP-C gate)
destructive_approval: FULL (script writes output file; does NOT commit/push unless called with --commit flag; never synthetic results)
---

# Script Template — `<server>_test_all_tools.py`

Purpose (per subgoal): call every exposed tool for this server; capture real stdout/stderr; save to workspace file; return list of (tool_name, result: PASSED/FAILED/BLOCKED). Never fabricate.

Usage: `python ./scripts/<server>_test_all_tools.py --output ./plans/<server>-test-output.md`

Required behaviors (verified by reading file contents after creation; per SOUL.md verify-before-claim):
- Import real server module (e.g., `from ast import grep` or MCP tool import — real import, not fake stub).
- Call at least one real method per exposed tool.
- Write real stdout to output file; if call raises exception, write `FAILED: <exception>` — not a synthetic success string.
- Exit with non-zero if ANY tool failed; exit 0 only if all passed.
- Print brief summary only; full detail in saved file.

Template variables (replaced per server):
  SERVER_NAME = "<server>"
  TOOLS = ["tool_a", "tool_b"]  # verified against server docs or workspace config
  OUTPUT_FILE = "./plans/<server>-test-output.md"
