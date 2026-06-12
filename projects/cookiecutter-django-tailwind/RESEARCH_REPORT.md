# RESEARCH_REPORT.md

## Project: cookiecutter-django-tailwind

**Type:** Django project generator / starter template
**Tech Stack:** Python 3.12+, Django 5.x, Tailwind CSS, pytest, pre-commit, ruff, mypy, Black, djlint, Django REST Framework (optional), Celery (optional), Sentry
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| profile | `projects/profile` | Django + Tailwind content site with form/editor concerns. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Uses generated Django model in production backend. |

---

## Key Findings

### Django 5 + Tailwind CSS
- `django-tailwind` is preferred over static asset pipelines for generated starter applications because it stays inside Python/Django workflows and avoids separate Node build drift.
- Keep generated `static/` and compiled Tailwind artifacts out of version control; commit only app source and `tailwind.config.js`.

### Quality Tooling
- `pre-commit` with `ruff`, `mypy`, `black`, and `djlint` remains the strongest generator quality gate.
- Keep requirements split between `base.txt`, `local.txt`, and `production.txt` so generated repositories have safe upgrade paths.

### Cookiecutter Maintenance
- The generator itself should only depend on maintained packages; document minimum supported versions for Django, Node, and Python.
- Test generated output against multiple OS + Python combinations because cookiecutter consumers will hit Windows aliases first.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Cookiecutter | https://cookiecutter.readthedocs.io | Docs |
| django-tailwind | https://django-tailwind.readthedocs.io | Docs |
| Django 5 release notes | https://docs.djangoproject.com/en/5.x/releases/5.0/ | Docs |
| pre-commit | https://pre-commit.com | Docs |
| django-allauth | https://docs.allauth.org | Docs |

---

## Best Practices
1. **Deterministic output** — pin cookiecutter dependencies used to generate projects.
2. **Minimal defaults** — enable optional integrations only when consumers ask for them.
3. **Type-check generation** — include `mypy` configs so generated projects can validate immediately.
4. **Documentation-first** — generated README and docs should explain the generated directory layout.
5. **Security defaults** — preconfigure `SECRET_KEY` loading from environment and include `.env` guidance.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unpinned optional addons | Template drift over time | Pin optional extras to stable releases. |
| Windows path mismatches | Generator fails on Windows | Test on Windows using git-bash and venv activation paths. |
| Moving compiled Tailwind files | Merge conflicts | Keep generated files under ignore rules and document them. |
| Forgetting migration reset flow | Consumer project breakage | Provide `makemigrations --merge` guidance. |

---

## Performance
1. Cache compiled Tailwind outputs during template rendering; never recompile when no input changed.
2. Provide optional Celery configuration only as a separate generated addon path.
3. Keep default database in SQLite for instant start; provide Postgres instructions only for production migrations.

---

## Security
1. Never hardcode secrets in generated settings; cookied output should fail closed if env vars are missing.
2. Include preconfigured security checklist in generated `docs/`.
3. Use Django's `check --deploy` command in generated CI workflow before marking a generated app production-ready.
4. Keep `ALLOWED_HOSTS` in generated settings but commented as placeholder requiring project-specific values.

---

## Related Projects (in workspace)

- **profile** — Django project with user content that can plug into generated app patterns
- **rhixecompany-comics** — production backend that matches generated Django conventions
- **cookiecutter-django-tailwind** — should be marked as template project in cross-references from consumer repos

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Cookiecutter docs | https://cookiecutter.readthedocs.io | Official docs |
| django-tailwind docs | https://django-tailwind.readthedocs.io | Tailwind integration |
| Django 5 docs | https://docs.djangoproject.com/en/5.x | Framework docs |
| Two Scoops of Django | https://www.feldroy.com/books/two-scoops-of-django | Production patterns |
| Pre-commit docs | https://pre-commit.com | Git hook management |
