# Prompts Audit — Issues Context

## Summary
| Severity | Count |
|----------|-------|
| High (double_fence) | 29 |
| Medium (missing_tags) | 150 |
| Medium (missing_desc) | 1 |
| Low (h1_missing) | 11 |
| Low (trigger_mismatch) | 2 |

## High: Double `---` Fence (29 files)

These files have `---` appearing 3+ times in the first 60 lines. After manual review, the vast majority are **false positives** — the extra `---` are legitimate markdown horizontal rules in the body, not broken frontmatter. The frontmatter itself is well-formed (closing `---` at the correct position).

**True double-fence count after refinement: 0**

Files flagged (all false positives):
- multi-agent-research-template.prompt.md (19 horizontal rules)
- cosmosdb-datamodeling.prompt.md (10 horizontal rules)
- apple-appstore-reviewer.prompt.md, bigquery-pipeline-audit.prompt.md, code-review.prompt.md, documentation.prompt.md, nextjs-tailwind.prompt.md, performance.prompt.md, playwright-typescript.prompt.md, prompts-strict-template.prompt.md, security.prompt.md, setup-enhanced.prompt.md (5 each)
- Others: plan-*.prompt.md, repo*.prompt.md, features.prompt.md, dev-init.prompt.md, Initial.prompt.md (3-4 each)

## Medium: Missing `tags:` Field (150 files)

150 files have no `tags:` in frontmatter. These are the prompt files where tags: [] was originally present but empty, plus files that never had tags at all.

**Fix:** Bulk-add `tags: []` or context-appropriate tags.

## Medium: Missing `description` (1 file)

- Initial.prompt.md — no `description` field

## Low: Body doesn't start with `#` H1 (11 files)

These files start with prose, a quote, or an image instead of a level-1 heading.

## Low: Trigger mismatch (2 files)

Minor trigger/filename misalignment.
