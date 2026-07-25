# CI/CD Best Practices Reference

## Pipeline Structure
1. **Lint** — ESLint, Prettier, type checking
2. **Test** — Unit tests, integration tests
3. **Build** — Compile/bundle the application
4. **Deploy** — Push to staging/production

## Key Patterns
- Cache dependencies between runs
- Use matrix builds for multi-version testing
- Fail fast: fail on first error
- Separate secrets from code (use CI/CD variables)
