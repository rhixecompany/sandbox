# Skills audit & automated fix — reference

This reference documents the batch audit-and-fix workflow used during the session on 2026-05-24. Additions here are intentionally conservative: they are intended to be copy-paste runnable guidance for a future operator, not a one-off narrative.

Summary
- Scope: `.opencode/skills/**/*.md` in-repo SKILL.md and supporting markdown files
- Batch size: 7 files per batch (keeps operations short and reviewable)
- Backups: `docs/skills-backups/` — every file changed MUST have a timestamped backup written here before the edit
- Verification artifacts: `docs/skills-fix-issues-context.md` (per-batch log) and `docs/skills-merge-verify.md` (summary)

Safe automated heuristics (proof-of-concept)
1. Ensure YAML frontmatter exists. If missing, insert minimal frontmatter:
   ---
   name: <derived-from-filename>
   description: Use when (placeholder - update)
   version: 1.0.0
   author: <operator>
   license: MIT
   metadata:
     hermes:
       tags: [imported]
   ---

2. Ensure a top-level title (# Title) immediately follows the closing `---` frontmatter. Derive from frontmatter.name or filename.
3. Insert recommended sections if absent: `## Overview`, `## When to Use`, `## Verification Checklist` with placeholder text.
4. Balance unclosed code fences: if triple-fence count is odd, append a closing ``` at EOF.
5. Normalize bullet markers: convert `* ` to `- ` on leading-list lines.

When to NOT apply automated changes
- Files that are intentionally short reference fragments (e.g. single-file README.md in a subdir) — inspect manually.
- Files that are generated or managed by another toolchain (CI templates, third-party vendored content).
- Files with complex, multi-file cross-references or deeply nested frontmatter — manual review required.

Practical commands (git-friendly, PowerShell-friendly) — examples
- Create backups (PowerShell):
  Get-Content -Raw -Path './.opencode/skills/banking/SKILL.md' | Set-Content -Path './docs/skills-backups/banking__SKILL.md.__20260524.bak'

- Quick validator (POSIX/python):
  python - <<'PY'
  import sys,yaml,pathlib,re
  p = pathlib.Path(sys.argv[1])
  c = p.read_text()
  assert c.startswith('---')
  m = re.search(r"\n---\s*\n", c)
  fm = yaml.safe_load(c[3:m.start()+3])
  assert 'name' in fm and 'description' in fm
  print('ok')
  PY

Rollback
- To revert a single file from backup:
  cp "docs/skills-backups/<safe-name>__TIMESTAMP.bak.md" ".opencode/skills/.../SKILL.md"
- To revert the entire change set, restore files from `docs/skills-backups/` and run `git checkout -- .` on any uncommitted changes you don't want.

Verification checklist (post-change)
- [ ] Every modified file has a backup in docs/skills-backups/
- [ ] Frontmatter present and description ≤ 1024 chars
- [ ] No unbalanced ``` fences
- [ ] Recommended sections present
- [ ] Run `skill_manage` validator or local YAML checks before committing

Notes and user preferences encoded
- Default batch size set to 7 (session convention)
- Never perform destructive Move-Item or git operations without explicit user confirmation; always backup first
- Inserted placeholder frontmatter should use `author: Alexa` when the user requests (policy used during the session)

Reference: this document was created automatically by the agent during an in-repo skill-maintenance session. Update it if your process or conventions change.
