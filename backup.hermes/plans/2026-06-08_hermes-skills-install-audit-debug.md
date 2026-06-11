# Hermes Skills: Browse → Install → Audit → Debug

## Goal
Discover high-value Hermes skills not yet installed, batch-install them with
security scanning, audit the result, then systematically debug any issues.

## Context

- 271 skills already installed across 21 categories (confirmed via `skills_list`)
- Skills Hub has 2,434 browsable skills (122 pages) with 95 official Nous skills
- Previous 5 sessions attempted this workflow but were blocked by:
  - SSH connection failures on `terminal()` calls
  - Context compaction before completion
  - Ambiguous identifiers (multiple skills named `webapp-testing`, `dogfood`, etc.)
- No new skills have been installed yet
- Working directory: `C:\Users\Alexa\Desktop\SandBox`

## Constraints

- Security scan passes before every install
- Only install skills not already in the 271 installed set
- Use `--source all --limit 100 --json` for machine-readable search results
- Prefer `official/` and `skills-sh/` sources; avoid `clawhub` unverified skills

## Step-by-Step Plan

### Phase 1: Inventory (Discovery)

**1.1** Run `skills_list()` with no filter — export full installed list to a temp
file for dedup. Use `skills_list(category=...)` per category to be thorough.

**1.2** Run `hermes skills browse` via `terminal`. Pipe output to a file for
parsing. This lists all 2,434 skills with identifiers.

**1.3** Cross-reference browse output against installed list. Mark every skill
NOT in the installed set as a candidate.

### Phase 2: Selection (Top 30)

**2.1** From the candidate list, filter by priority categories:

| Priority | Categories | Rationale |
|----------|-----------|-----------|
| High | qa, devops, github, security | Direct productivity impact |
| High | software-development, development, mcp | Core tooling |
| Medium | productivity, planning, research | Workflow helper |
| Low | creative, media, gaming, smart-home | Nice-to-have |

**2.2** For each candidate, run `hermes skills inspect <identifier>` to get:
- Full name, description, source, trust level, tags

**2.3** Rank by: official trust > skills-sh trusted > skills-sh community.
Discard anything duplicate or already installed.

**2.4** Lock in exactly 30 candidates. Write list to temp file.

### Phase 3: Search/Filter by Keyword

**3.1** For each of the 30 candidates, run:
```
hermes skills search --source all --limit 20 --json "<skill_name>"
```
This confirms the identifier resolves and finds any related skills.

**3.2** Collect all unique identifiers from search results.

### Phase 4: Install (With Security Scan)

**4.1** For each skill identifier to install:

```
hermes skills inspect <identifier>    # Verify trust + source
hermes skills install <identifier>    # Installs with built-in security scan
```

**4.2** If install fails, log the error and continue to next skill.

**4.3** After each install, verify with `skills_list()` or
`hermes skills inspect <identifier>` to confirm it's live.

**4.4** Keep a running install log: skill name, identifier, status, error (if any).

### Phase 5: Audit

**5.1** Run `skills_list()` post-install — compare count vs pre-install baseline.

**5.2** Run `skill_manage` or check skill directories for:
- Missing frontmatter fields (name, description, version)
- Invalid YAML
- Broken file references (scripts/, templates/, references/ pointing to missing files)

**5.3** Check `$HERMES_HOME/skills/<category>/<name>/SKILL.md` for each
newly installed skill.

**5.4** Produce audit report: installed OK, installed with warnings, failed.

### Phase 6: Systematic Debug

**6.1** For each failed or warning-flagged skill, apply 4-phase debugging:

1. **Understand**: Read the error + inspect the SKILL.md
2. **Isolate**: Identify the broken piece (YAML, reference, missing dep)
3. **Fix**: Patch or remove; if unfixable, uninstall
4. **Verify**: Re-inspect after fix

**6.2** For YAML/syntax errors: use `patch` or `write_file` on the SKILL.md.

**6.3** For missing references: either install the dependency or remove the
broken reference link.

**6.4** For skills that can't be fixed: `hermes skills uninstall <name>`.

## Files Likely to Change

| File/Dir | Change |
|----------|--------|
| `$HERMES_HOME/skills/` | New skill directories created |
| `$HERMES_HOME/skills/<cat>/<name>/SKILL.md` | New skill files |
| `SESSION_REPORT.md` | Created/updated in SandBox |
| `.hermes/plans/` | This plan file |

## Verification

Post-execution checks:
1. `skills_list()` count increased from 271
2. Each installed skill's `SKILL.md` parses cleanly
3. No orphaned partial installs in `$HERMES_HOME/skills/`
4. Audit report written to `SESSION_REPORT.md` or a dedicated log

## Risks & Tradeoffs

| Risk | Mitigation |
|------|-----------|
| SSH connection failures on `terminal()` | Use built-in tools (`skills_list`, `skill_view`, `skill_manage`) instead of `hermes` CLI where possible |
| Context compaction mid-workflow | Write state to temp files between phases so work can resume |
| Ambiguous identifiers | Always use full qualified ID (e.g. `official/security/1password`) |
| Broken community skills | Prefer official/skills-sh trusted; uninstall if unfixable |
| Rate limits on install | Install in small batches (5 at a time) with verification between |

## Open Questions

- Should we install *all* candidates or cap at exactly 30?
- Should we include creative/media/gaming skills or focus on dev/tooling only?
- What's the preferred handling of skills with broken references — fix or skip?
