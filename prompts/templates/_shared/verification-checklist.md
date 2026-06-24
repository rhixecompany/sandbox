# Shared Template — Verification Checklist

Use this standard verification checklist pattern in prompts.

```markdown
## Verification Checklist

| # | Gate | Criterion |
|---|------|-----------|
| 1 | YAML | Frontmatter parses without errors |
| 2 | Skills | All `dependencies:` and `skills:` reference existing skills |
| 3 | Trigger | Trigger matches filename stem |
| 4 | Execution | All phases completed sequentially |
| 5 | Output | Deliverable file(s) created at expected paths |
```

## Safety Gates Pattern

```markdown
### Safety Gates

1. **Pre-audit** — Extract constraints before transformation
2. **Transformation** — Apply changes following rules
3. **Post-audit** — Verify constraints still preserved
4. **Rollback** — If post-audit fails, revert and report
```
