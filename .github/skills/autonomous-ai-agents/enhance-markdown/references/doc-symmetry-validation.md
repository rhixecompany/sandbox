# Doc Symmetry Validation

Methodology for verifying that a project's documentation set matches an expected manifest of required artifacts. Detects missing files, extra files, and structural gaps.

## When to Use

After running a generator-orchestrator (11 generators producing docs/project-docs/<name>/) or after any bulk documentation generation. Use symmetry validation to confirm completeness before declaring a project "documented."

## Validation Pattern

### Step 1: Define Expected Manifest

```yaml
# Canonical 11-artifact manifest (from generator-orchestrator)
required:
  - technology-stack.md
  - folder-structure.md
  - architecture.md
  - project-workflow.md
  - code-exemplars.md
  - copilot-instructions.md
  - readme.md
  - artifact-manifest.json
  - cross-linking-report.md
  - validation-report.md
  - execution-summary.md
```

For non-generated docs (manually authored), define a minimal manifest:

```yaml
required:
  - README.md
  - ARCHITECTURE.md
optional:
  - CHANGELOG.md
  - CONTRIBUTING.md
  - DEPLOYMENT_GUIDE.md
  - DEVELOPMENT_GUIDE.md
  - API_REFERENCE.md
  - TESTING_GUIDE.md
  - SETUP_GUIDE.md
  - DATABASE_SCHEMA.md
  - SECURITY.md
```

### Step 2: Compare Actual vs Expected

```bash
# For each project under docs/project-docs/<name>/:
for project_dir in docs/project-docs/*/; do
  name=$(basename "$project_dir")
  echo "=== $name ==="
  for artifact in technology-stack.md folder-structure.md architecture.md project-workflow.md code-exemplars.md copilot-instructions.md readme.md artifact-manifest.json cross-linking-report.md validation-report.md execution-summary.md; do
    if [ -f "${project_dir}${artifact}" ]; then
      echo "  ✅ $artifact"
    else
      echo "  ❌ MISSING: $artifact"
    fi
  done
done
```

### Step 3: Compute Completeness

| Metric | Calculation | Threshold |
|--------|-------------|-----------|
| Completeness ratio | `existing / required` | ≥1.0 for pass |
| Coverage score | `(existing / required) × 100` | ≥73% (8/11) for acceptable |
| Health status | coverage >= 100%: full, >= 73%: partial, < 73%: gap | |

### Step 4: Generate Symmetry Report

```markdown
# Doc Symmetry Report

Generated: 2026-05-27

## Project Completeness Matrix

| Project | README | ARCH | STACK | WORKFLOW | ... | Score | Status |
|---------|--------|------|-------|----------|-----|-------|--------|
| xamehi | ✅ | ✅ | ❌ | ✅ | ... | 9/11 | Partial |
| youtube-downloader | ✅ | ✅ | ❌ | ❌ | ... | 7/11 | Gap |

## Missing Artifacts by Project

| Project | Missing | Recommendation |
|---------|---------|----------------|
| xamehi | technology-stack.md | Run generator-orchestrator Stage A |
| youtube-downloader | technology-stack.md, workflow.md, code-exemplars.md | Run full generator-orchestrator |

## Extra Files (not in manifest)

| Project | Extra File | Notes |
|---------|------------|-------|
| xamehi | SECURITY.md | Bonus — keep |
| youtube-downloader | CHANGELOG.md | Bonus — keep |

## Recommendations

- **Full docs**: Projects with <8/11 — re-run generator-orchestrator
- **Partial docs**: Projects with 8-10/11 — create individual missing artifacts
- **Bonus files**: Extra files are kept; they don't count against the score
```

## Integration with enhance-markdown

Run symmetry validation as a gate before final verification:

1. After documentation is generated/enhanced
2. After all patches are applied
3. Before the final verification report

The symmetry report feeds into:
- AI-readiness scoring — projects with missing docs score lower
- Patch creation — missing documentation can be supplied via new patches
- Final verification checklist

## Tips

- **Bonus files (extra artifacts beyond the manifest) are a positive signal** — they indicate the team added value beyond the template. Never penalize for extra files.
- **Partial coverage is acceptable for tools projects** (e.g., a CLI tool may not need DEPLOYMENT_GUIDE.md if it has no deployment story). Flag but don't block.
- **Re-run generator-orchestrator when coverage < 50%** — the project is under-documented and the generative pipeline is the fastest fix.
- **Use with AI-readiness scoring** — a project with 3/11 docs will likely score <40 on AI-readiness. Fix docs first, then re-score.
