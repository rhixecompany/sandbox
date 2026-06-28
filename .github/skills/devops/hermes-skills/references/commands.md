# Skills Commands Reference

## Discovery
```bash
/skills                      # List installed skills (chat)
hermes skills list           # CLI list
hermes skills view <name>    # View full skill
/skillname                   # Load skill by name
/skillname help              # Load with help prompt
```

## Browsing & Searching the Hub
```bash
hermes skills browse [--page N] [--size N] [--source SOURCE]
  # Sources: all, official, skills-sh, well-known, github, clawhub, lobehub, browse-sh
  # Table truncates long names with "…" and identifiers with line wraps
  # --source official → curated Nous Research optional skills (95 total)
  # --source skills-sh → same official list, different flag

hermes skills search <query> [--source SOURCE] [--limit N] [--json]
  # Search skill registries by keyword
  # --json for scripting (full identifiers)

hermes skills inspect <identifier>
  # Preview a skill without installing (full metadata + SKILL.md preview)
```

## Installation
```bash
/skill install               # Interactive hub picker
hermes skills install <identifier> [--yes] [--force] [--category CAT] [--name NAME]
  # --yes: skip confirmation (use for batch installs)
  # --force: override CAUTION verdicts (does NOT override DANGEROUS)
  # --category: install into a specific category subdirectory
  # --name: override the skill name

# NOTE: Command is "hermes skills install" (plural), NOT "hermes skill install"
```

## Security & Audit
```bash
hermes skills audit [--deep] [name]
  # Re-scan installed hub skills for security issues
  # --deep: AST-level analysis on Python files (slower, more thorough)
  # All installed skills are scanned as "source" = their registry origin
  # RESULTS: ALLOWED (safe), BLOCKED (dangerous/caution)
  # BLOCKED = informational only, does NOT disable the skill
```

## Management
```bash
/skill update                # Check hub updates
hermes skills opt-out        # Stop bundled skill seeding
hermes skills opt-out --remove  # Remove unmodified bundled
hermes skills opt-in --sync  # Re-enable seeding
```