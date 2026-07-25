# Multi-Target Execution Pattern

When a scope definition lists multiple distinct targets to process, use this pattern for systematic end-to-end execution.

## 5-Phase Execution Model

1. **BRAINSTORM & PLAN** — Create comprehensive plan document with per-target spec, cross-reference matrix
2. **PER-TARGET EXECUTION** — For each target: load current state, apply transformations, check AC
3. **SWEEP VERIFICATION** — Cross-reference sweep: verify ALL targets have complete frontmatter
4. **FIX GAPS** — Patch discrepancies found during sweep
5. **COMMIT & REPORT** — One commit per cycle, summary table

## Acceptance Criteria Template

| Criterion | Check |
|-----------|-------|
| YAML frontmatter | `head -1` contains `---` |
| `trigger:` field | `head -10 \| grep trigger:` |
| `description:` field | `head -10 \| grep description:` |
| `tags:` field | `head -10 \| grep tags:` |
| Source fidelity | Derived file size >= source |

## Subagent-Based Execution

For large-scale multi-target work (10+ targets, or targets requiring individual analysis), use subagent-based execution instead of direct per-target iteration. See `references/dev-imp-pattern.md` for:

- **Multi-Target Subagent Dispatch** — Batch targets into groups of 5-6 per subagent
- **Progress Verification via Filesystem** — Verify via `find`/`stat`, not subagent self-report
- **Stalled Subagent Recovery** — Dispatch fresh subagent for remaining targets
- **Sibling Agent Race Conditions** — Handling concurrent writes from parallel subagents
- **Standing-Goal Subagent Chaining** — Active polling under continuation mode
