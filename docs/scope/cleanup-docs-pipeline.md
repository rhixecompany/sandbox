# Scope: Markdown cleanup and docs pipeline feature

A new feature to clean up markdown artifacts and establish the docs pipeline.

**What it builds**: Deletes empty subfolders at repo root, docs/, .github/; trims whitespace in .md files; creates docs/document.md and docs/project-docs/.
**Who it's for**: Workspace maintainers (Alexa) and all agent profiles (default, adminbot, architect, analyst, creative, exec-assistant, tutor, dev, ops, pm, security) that read clean docs.
**Build approach**: Tracer bullet — one vertical slice (cleanup + docs) verified end to end before considering further features.
**Workflow tier**: Alpha — after /develop, verify with `/check verify` (real file checks); no full test suite required since this is cleanup and docs.

## At a glance

|| # | Feature | Phase | Status |
||---|---------|-------|--------|
|| 1 | Markdown cleanup and docs pipeline | Foundation | planned |

## Feature

### 1. Markdown cleanup and docs pipeline · planned

Clean up markdown artifacts across root/docs/.github and establish the docs pipeline.

**Done when:** empty subfolders removed from root/docs/.github (verified by `find`); whitespace trimmed in all .md files in those directories; docs/document.md and docs/project-docs/ exist and are non-empty; audit evidence saved.

- [ ] Design it (spec): /architect markdown cleanup feature
- [ ] Build it: /develop docs artifacts + cleanup
- [ ] Verify it: /check verify markdown cleanup feature

## Deferred
- Per feature design token updates (design-md) out of scope for this pass
- Full profile identity reconciliation deferred (existing scope.md handles it)
- Web verified reference links deferred
