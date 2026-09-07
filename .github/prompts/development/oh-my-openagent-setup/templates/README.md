# oh-my-openagent-setup Template

Prompt: oh-my-openagent-setup.prompt.md
Lines: 165
Templates: 1

## Workflow (phases/steps)

1. **Intake** — read the request, identify scope; locate relevant files/diffs/references.
2. **Execute** — perform work with smallest safe change set; keep steps explicit and reproducible.
3. **Verify** — check result against goal, rules, inputs; confirm output usable and complete.
4. **Hand Off** — return final artifact or findings clearly; stop once the requested result is delivered.

## Verification Checklist

| # | Gate | Criterion |
|| --- | ------ | ----------- ||
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## References

- Shared rules: `templates/_shared/rules-core.md`
- Shared personas: `templates/_shared/personas.md`
- Shared skills table: `templates/_shared/skills-table-core.md`

---

> TODO-to-author: add oh-my-openagent install/verify command sequence when the toolchain pins a version.
