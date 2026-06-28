---
name: verification-before-completion
title: "Verification Before Completion"
description: "Use when about to claim work is complete, fixed, or passing. Requires running verification commands before committing or creating PRs."
version: 1.0.0
author: Alexa
license: MIT
tags: [imported]
---
## Goal
Use when about to claim work is complete, fixed, or passing. Requires running verification commands before committing or creating PRs.


## Description

Use when about to claim work is complete, fixed, or passing, before committing or creating PRs. Requires running verification commands and confirming output before making success claims.

## When to Use

- Before claiming work is complete
- Before committing changes
- Before creating pull requests
- Before merging to main
- Verifying bug fixes
- Confirming test passes
- **Verifying plan/remediation execution** — checking that documented issues and fix batches were actually applied on disk
- **Cross-referencing planning artifacts** — confirming alignment between issue reports, fix plans, and execution summaries

## When NOT to Use

- Work in progress
- Exploratory code
- Quick verification without rigor
- Non-critical work

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Structured debugging for complex issues |
| `requesting-code-review` | Pre-commit review workflow |

## Workflow

### Phase 1: Identify Verification Needs

- Determine what needs verification
- List all verification steps
- Plan verification approach
- Gather tools needed

### Phase 2: Run Verification

- Execute all verification commands
- Capture output
- Verify results
- Document findings

### Phase 3: Confirm Success

- Review all verification results
- Confirm against requirements
- Verify no regressions
- Document evidence

### Phase 4: Proceed with Confidence

- Commit changes
- Create pull request
- Merge to main
- Archive verification results


## Techniques

### Plan Execution Verification (Cross-Reference Pattern)

Use when confirming that a multi-batch remediation or fix plan was fully applied.

**Process:**

1. **Read all artifacts** — Collect all related docs (list, issues, plan, summary, fix-specs). Understand the full document lifecycle — some documents may be superseded by newer ones.

2. **Build a cross-reference matrix** — Map each documented issue/fix batch onto a checklist. Note which documents reference each item.

3. **Verify both directions:**
   - **Forward** (issues → fixes): For each documented issue, check the actual file on disk for the fix.
   - **Backward** (fix batches → disk): For each plan batch, confirm every listed file was modified as described.

4. **Run automated checks** — Use available linters/syntax checkers:
   - Shell: `shellcheck -f gcc <files>` (install via `npm install -g shellcheck` if missing)
   - Check for errors (exit code, grep for `error:`), warnings, and notes separately.
   - Module structure: verify expected files exist with `ls` and `wc -l`.

5. **Handle environment gaps** — When type-check or lint tools fail because `node_modules` aren't installed or configs are stale, note it as "pre-existing / unrelated" rather than blocking the verification.

6. **Update summary** — Append a Phase 5 verification section with:
   - Shellcheck error/warning/note counts per area
   - On-disk cross-check results per issue category
   - Any pre-existing environment issues (skipped, not scoped)
   - Module/file structure verification results

7. **Handle overlapping documents** — When multiple plan docs exist (e.g., `fix-issues-context.md` from plan A, `prompt.md` from plan B), verify both independently. Items from superseded plans should still be on disk.

8. **If late fixes happen after initial verification**, append a short addendum to the verification artifact, re-read the changed files, and re-run the targeted checks before claiming the work is finished.

**Signals that triggered this technique:**
- User asks to "implement remaining steps" of a prompt with explicit phases/tasks/subtasks/actions
- Multiple planning artifacts exist (list, issues, plan, summary) with overlapping scope
- A comprehensive fix plan was authored but verification state is unknown

**Pitfall:** Do not treat the first completion summary as final if you later patch files during the same session; refresh the verification artifact so the document trail matches the latest on-disk state.

**Script reference:** See `references/shellcheck-verification-patterns.md` for reusable shellcheck command patterns.

### Scripted File Write Pattern

Use when programmatically generating or trimming file content via Python/script.

**Process:**

1. **Generate new content in memory first** — Build the new content string before opening the output file for writing. Never open-for-write-then-generate.
2. **Validate non-empty** — Check `len(new_content) > 0` before writing. A zero-length write destroys the file.
3. **Validate structure** — For markdown: check it has expected headings (`## `). For JSON: parse it. For YAML: parse it.
4. **Check expected section count** — If the original had 10 `## ` sections and the new content has 0, the extraction/detection failed. Abort.
5. **Write only after validation passes** — If validation fails, print diagnostics and abort. Do not write a broken file.
6. **Restore if accidentally wiped** — Immediately restore from last good known content (prior read, git, or backup). Report the incident.

**Pitfall:** The most common cause of a wiped file is failed regex or heading detection that produces 0 results. Always validate detection output before using it to reconstruct content.

## Tools & References

- **Related Skills**: systematic-debugging, requesting-code-review
- **Verification**: Tests, linting, type checking
- **Evidence**: Captured output and logs

## Best Practices

- Run all verification steps
- Capture verification output
- Document evidence
- Verify against requirements
- Check for regressions
- Get peer verification
- Archive verification results

## Pitfalls

- **Assuming summary = reality**: A completion summary that says "all fixed" may be aspirational. Always cross-check a sample of issues against actual files on disk.
- **Single-direction check**: Verifying only "issues → fixes" misses items that were listed in fix batches but never tracked in the issues doc. Always verify both forward and backward.
- **Ignoring shellcheck errors**: Treat warnings/notes as pre-existing style, but zero errors must be confirmed before claiming completion.
- **Environment confusion**: Distinguish between "verification failed because the fix wasn't applied" and "verification failed because tooling/deps aren't available in this environment." The latter is pre-existing — note it, don't block on it.
- **Document lifecycle overlap**: When plans are authored at different times, the newer document may not reference every batch from the older one. Verify against ALL planning artifacts, not just the newest.


## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

