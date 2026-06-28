# Skill Curation Guidelines (session-captured)

Purpose: capture durable, class-level rules and procedures for curating the Hermes skill
library. This file holds the operational advice agents should follow when auditing,
merging, archiving, or editing skills.

1) ACTIVE update rule
- Every session that performs skill-library work should make at least one meaningful
  skill-level update (patch/refs/scripts). A no-op pass is a missed learning
  opportunity. Meaningful can be: adding a small pitfall, writing a one-line
  references note, adding a verification script, or improving an umbrella's
  'When to Use' guidance.

2) Signals that require action (any one triggers a curation update)
- User corrects style/format/verbosity/tone: embed the preference in the governing
  skill's SKILL.md under a "User preferences" subsection with concrete examples.
- User corrects workflow or step sequence: add a "Pitfalls & Corrected Workflow"
  subsection and a short step-by-step fix.
- New non-trivial technique, fix, or workaround discovered during a session: add
  a concise note under references/<topic>.md and cross-link in the umbrella SKILL.md.
- Skill consulted and found wrong or missing steps: patch that skill immediately
  (small, verified edits). Document the rationale in references/ and include a
  one-line changelog at the top of the SKILL.md.

3) Backup-before-destructive
- Always create an automated backup before deletion/major rewrite. Recommended
  path: %LOCALAPPDATA%\hermes\skills-backup\<UTC-TIMESTAMP>\
- Backup contents: all SKILL.md files that will be changed, plus any references/
  templates/scripts that are adjacent to them. Store a manifest.json listing
  absolute paths and SHA256 checksums.

4) Using-superpowers and safety gates
- The "using-superpowers" skill MUST be invoked and recorded before any bulk
  changes. Add a one-line note to the task in the umbrella's "Preflight" section
  that it was invoked and the timestamp.

5) Archiving vs Deleting
- Prefer archiving (rewrite SKILL.md with ARCHIVED header and pointer to the
  umbrella) rather than deleting. Delete only when the user explicitly authorizes
  removal and after a backup is created.

6) User-preference embedding
- If the user expresses a formatting, tone, or workflow preference, edit the
  governing skill to include a "User preferences" subsection. Example entries:
  - "User prefers concise, non-polite answers; lead with the change/result."
  - "Always ask before destructive edits; create a backup zip before any deletions."
- The skill entry must show a concrete example (copy/paste of expected format).

7) Support file conventions
- references/<topic>.md: session-specific detail, transcripts, provider quirks.
- templates/<name>.<ext>: boilerplate configs or starter files to be copied.
- scripts/<name>.<ext>: verification or backup scripts. Scripts must be idempotent
  and safe to run (non-destructive by default).

8) Rollback & verification
- For any SKILL.md edits: produce a rollback patch (unified diff) and store it in
  backup_dir/rollback-patches/ with a human-friendly README.
- After edits, run the umbrella's verification script (if present) or a simple
  syntax/readability check: ensure frontmatter still valid, no malformed
  headings, and that the 'name:' frontmatter key matches the directory name.

9) Protected skills
- Do NOT delete or archive bundled skills (shipped with Hermes) or hub-installed
  skills. These are editable (patch allowed) but not removable.

10) Minimal change principle
- Prefer small, verifiable patches. When in doubt: write a references/ note and
  add a one-line patch to SKILL.md explaining the rationale.


Created-by: hermes-skill-library-maintenance (session)
Created-at: {timestamp}
