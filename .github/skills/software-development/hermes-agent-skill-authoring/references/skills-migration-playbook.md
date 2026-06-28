# Skills Migration Playbook

This playbook captures practical steps and safety checks discovered during migrating `.opencode/skills/*.md` to Hermes in-repo SKILL.md format.

1. Discovery
   - Run: `find .opencode/skills -type f -name '*.md' | sort > /tmp/skills_list.txt` to enumerate files reliably.
   - Use `/tmp/skills_list.txt` as the canonical file list for batching to avoid intermittent search tool inconsistencies.

2. Backup
   - Create timestamped backup directory: `mkdir -p docs/skills-backups/$(date +%Y%m%d-%H%M%S)` and copy the entire tree into it: `cp -r .opencode/skills docs/skills-backups/$TS/`.
   - Verify file counts match: `wc -l /tmp/skills_list.txt` vs `find docs/skills-backups/$TS -type f -name '*.md' | wc -l`.

3. Batching
   - Default batch size: 7 files.
   - Use deterministic ordering (sort) so batch composition is reproducible.

4. Audit
   - For each file in a batch:
     - Read content and detect frontmatter presence.
     - Collect headings, placeholders (TODO/FIXME/TBD), code block languages, and list style usage.
     - Flag missing Overview/When to Use/Verification sections.
     - Generate a one-line suggested_fix and priority (high if placeholders or CI references exist).

5. Duplicate detection
   - Compare titles and the first 200 characters across the whole tree; flag likely duplicates for manual review.

6. Patch generation
   - Prepare V4A format patches for each file change. Keep patches small and per-file when possible.
   - For batch application, write patched files to a staging area (eg. `tmp/skills-patch-staging/batch-<N>/`) so reviewers can inspect before commit.

7. Validation
   - After applying patches to staging, run frontmatter and YAML validation (description ≤1024 chars, name ≤64 chars, file char limit ≤100k).
   - Run `mdspell` or similar linting if available for basic typos.

8. Commit policy
   - Prepare bash and PowerShell commit scripts per batch; do not push without explicit approval.
   - Commit message template: `chore(skills): migrate batch <N> — normalize frontmatter and fix formatting (author: Alexa)`.

9. Rollback
   - If a validation fails post-apply, revert the file from the backup and record the reason in the verification log.

10. Records
   - Keep audit reports and verification logs under `docs/`: `docs/skills-issues-context.md`, `docs/skills-merge-verify.md`, `docs/skills-merge-complete.md`.

11. Human approvals
   - Require explicit human approval before any write to original files or git commits.

Notes
- This playbook should be considered the operational source for the migration workflow and referenced by any SKILL.md that performs bulk skill edits.
