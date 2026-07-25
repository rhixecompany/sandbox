# Prompt Consolidation Pattern

How to replace a group of one-shot, duplicated, or thin-wrapper prompts
with a smaller number of generic, reusable ones.

## When to Use

- A directory has 10+ `plan-*.prompt.md` files with overlapping purpose.
- `execute-plan-*` wrappers duplicate the same 26-line boilerplate.
- Copilot-imported prompts have only `toolsets:` frontmatter (no `name`,
  `title`, `version`).
- You find prompts with broken `skill:plan:xxx` dependencies (from
  migration artifacts).

## Pattern (from Phase 6)

1. **Full inventory** — Every prompt in the target group, with name,
   title, lines, purpose, and frontmatter health.

2. **Categorise** — Three buckets:
   - **Duplicate** — same name/purpose/body → flag for deletion.
   - **Thin wrapper** — <40 lines, single boilerplate pattern,
     references broken deps → flag for deletion.
   - **Copilot orphan** — no `name`/`version`, only `toolsets:` →
     flag for deletion or migration.

3. **Design consolidated set** — Map each distinct purpose to one
   generic prompt. Example mapping:
   | Old (37 prompts)          | New (4 prompts)          |
   |---------------------------|--------------------------|
   | `plan-debugger`           | `plan-generate`          |
   | `plan-features-seed`      | `plan-generate`          |
   | `plan-updateAiAgentSetup` | `plan-generate`          |
   | 14× `execute-plan-*`     | `plan-execute`           |
   | 2× `plan-batch-fix-*`    | `plan-batch-fix`         |
   | 3× `plan-acpx-audit-*`   | `plan-audit`             |

4. **Create new prompts** — Proper frontmatter, DRY references to
   `prompts/templates/_shared/`, full workflow with phases and
   verification gates.

5. **Delete old prompts** — `git rm`, NOT `rm -rf`. Each deletion is
   tracked in git.

6. **Archive orphaned template dirs** — Template dirs whose prompt was
   deleted become orphans. Move them to `.hermes/archived-plan-templates/`
   via `git mv`:
   ```bash
   for d in prompts/templates/*/; do
     base=$(basename "$d")
     [ "$base" = "_shared" ] && continue
     [ -f "prompts/$base.prompt.md" ] || git mv "$d" .hermes/archived-plan-templates/
   done
   ```

7. **Verify** — Run full checklist, then commit.

## Live Example

Session 2026-06-29 consolidated 37 plan prompts into 4:
- Commit `210b5ee5`: "feat: consolidate 37 plan prompts into 4 DRY prompts"
- Files deleted: 37 `plan-*`, `execute-plan-*`, `execute-*plan*` prompts
- Files created: `plan-generate`, `plan-execute`, `plan-batch-fix`, `plan-audit`
- Dirs archived: 20 orphaned template dirs to `.hermes/archived-plan-templates/`

## Verification Checklist

- [ ] All old prompts `git rm`'d
- [ ] Orphan template dirs archived (not hard-deleted)
- [ ] Zero duplicate names in remaining prompt set
- [ ] Zero broken `dependencies:` refs (no `skill:plan:` or `skill:/`)
- [ ] All new prompts have valid frontmatter
- [ ] Single consolidation commit in git log
