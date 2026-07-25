# Resume_maker Research Report

## Project Overview
- **Project**: Resume_maker
- **Type**: CLI Document Generator (JSON → Markdown + PDF)
- **Status**: Active

## Technology Stack
- **Runtime**: Bun (latest), Node.js (fallback)
- **Language**: TypeScript ^5 (strict mode)
- **PDF Generation**: markdown-pdf ^11.0.0 (uses PhantomJS - deprecated)
- **Linting/Quality**: ESLint 10.x (flat config), Prettier 3.x, Markdownlint, CSpell
- **Module System**: ES Modules (`"type": "module"`)
- **Entry Point**: `index.ts`

## Key Queries Researched
1. CLI resume generator markdown PDF TypeScript Bun best practices
2. markdown-pdf npm package TypeScript configuration puppeteer options
3. Bun CLI TypeScript strict ESLint Prettier Markdownlint CSpell configuration
4. CLI generator tool TypeScript Bun JSON input markdown output best practices
5. markdown-pdf PhantomJS deprecated alternatives puppeteer
6. Bun CLI TypeScript best practices single executable compilation
7. ESLint 10 flat config TypeScript strict configuration
8. markdownlint markdown linting best practices CSpell spell checking

## Findings

### 1. Similar CLI Resume Generators & Tools
- **awesome-markdown-resumes** (GitHub): Curated list of tools, templates, examples for markdown resumes
  - markdown-resume (Node.js CLI for converting Markdown resumes to various formats)
  - resume-cli (Command-line tool for JSON Resume - can convert from Markdown)
  - md2resume (PHP-based CLI tool to generate HTML and PDF resumes from Markdown)
  - MarkdownResume.app (Online editor with PDF export via Puppeteer)
  - Resumey.Pro (Web-based markdown resume builder with themes)
  - YAMLResume (YAML-based resume with LaTeX/XeTeX PDF generation)

- **md-to-pdf** (npm): Simple CLI using Marked + Puppeteer (modern alternative to markdown-pdf)
- **markdown-pdf** (npm): Uses **deprecated PhantomJS** (since 2018) - major concern
- **JSON Resume ecosystem**: Standardized JSON schema with multiple themes/renderers

### 2. markdown-pdf Critical Issues
- **Uses PhantomJS** which has been **officially deprecated since 2018**
- No longer maintained; security vulnerabilities unpatched
- Alternatives: **md-to-pdf** (uses Puppeteer/headless Chrome), **markdown-pdf-ng**, **md-preview-pdf**
- Migration path: Replace markdown-pdf with md-to-pdf or direct Puppeteer implementation

### 3. Bun CLI Best Practices (from official docs & community)
- **Argument parsing**: Use `util.parseArgs` (built-in) or `meow`/`commander` for complex CLIs
- **Shebang**: `#!/usr/bin/env bun` at entry point
- **Single executable compilation**: `bun build ./cli.ts --compile --outfile mycli`
- **Cross-platform**: Can target different OSes via `--target` flag
- **Type checking**: Run `bun run typecheck` separately (Bun transpiles but doesn't type-check)
- **ES Modules**: Native support, use `"type": "module"` in package.json

### 4. TypeScript Strict Configuration (tsconfig.json)
Current config is solid but could add:
```json
{
  "strict": true,
  "noUncheckedIndexedAccess": true,
  "exactOptionalPropertyTypes": true,
  "noImplicitOverride": true,
  "noFallthroughCasesInSwitch": true,
  "noUnusedLocals": true,    // Consider enabling
  "noUnusedParameters": true // Consider enabling
}
```

### 5. ESLint 10 Flat Config Best Practices
- Use `typescript-eslint` configs: `tseslint.configs.strict` for strict mode
- Target only TypeScript files: `{ files: ['**/*.ts'] }`
- Disable `no-unused-vars` (base) in favor of `@typescript-eslint/no-unused-vars`
- Use `eslint.config.js` (ESM) not `.eslintrc.json`

### 6. Markdownlint Configuration Best Practices
Current config is comprehensive. Key rules:
- **MD007**: Indent 2 spaces for lists
- **MD013**: Line length 500 (relaxed for tables)
- **MD022**: Headers surrounded by blank lines
- **MD024**: Allow duplicate headers (disabled)
- **MD033**: Allow specific HTML elements (well configured)
- **MD040**: Fenced code blocks must have language
- Consider enabling MD024 (duplicate headers) for stricter docs

### 7. CSpell Configuration Best Practices
- Create `cspell.json` at project root (not in `.vscode/`)
- Add custom dictionary for domain terms (e.g., "markdown-pdf", "Bun", "TypeScript")
- Ignore patterns: code blocks, inline code, proper nouns
- Use `cspell.json` with version field: `{"version": "0.2"}`
- Run via `cspell "**/*.{md,ts}"` in package.json scripts

### 8. PDF Generation Alternatives (Modern)
| Tool | Engine | Status | Notes |
|------|--------|--------|-------|
| markdown-pdf | PhantomJS | ❌ Deprecated | Security risks, no updates since 2018 |
| md-to-pdf | Puppeteer | ✅ Active | Simple CLI, programmatic API |
| md-to-pdf-ng | Puppeteer | ✅ Active | Fork with enhancements |
| md-preview-pdf | Puppeteer | ✅ Active | Mermaid, math, syntax highlighting |
| Direct Puppeteer | Puppeteer | ✅ Active | Full control, singleton browser pattern |

### 9. Common Pitfalls & Solutions
1. **PhantomJS in markdown-pdf**: Migrate to Puppeteer-based solution
2. **ESLint + Bun**: Run `bun --bun eslint .` or use Node for linting
3. **TypeScript strict mode**: Enable from project start; harder to add later
4. **CLI argument parsing**: Use `util.parseArgs` (stdlib) or `meow` for help/version
5. **PDF generation failure**: Always save Markdown first, then convert (current pattern is good)
6. **Spell check false positives**: Configure ignore patterns for code blocks, proper nouns
7. **Single executable**: Test cross-platform; ESM support still maturing

### 10. Recommended Improvements for Resume_maker
1. **Migrate PDF generation** from markdown-pdf to md-to-pdf or direct Puppeteer
2. **Add cspell.json** configuration file
3. **Enable stricter TypeScript flags** (noUnusedLocals, noUnusedParameters)
4. **Add Bun compile script** for standalone executable distribution
5. **Consider JSON Resume schema** compatibility for interoperability
6. **Add CI/CD pipeline** for lint, typecheck, test on push
7. **Document CLI flags** with `--help` output examples

## Architecture Pattern Validation
The **Pipeline Processing Pattern** (JSON → Validate → Generate → Markdown → PDF) is sound and follows CLI best practices:
- Input validation before processing ✓
- Per-document isolation (one failure doesn't block others) ✓
- Markdown preserved on PDF failure ✓
- Clear separation of concerns ✓

## References
- [Bun CLI Guide](https://bun.com/docs/bundler/executables)
- [How to Build CLI with Bun](https://oneuptime.com/blog/post/2026-01-31-bun-cli-applications/view)
- [TypeScript Strict Config](https://www.reddit.com/r/typescript/comments/1ixh398/recommendations_for_a_full_strict_type_tsconfig)
- [ESLint Flat Config](https://eslint.org/docs/latest/use/configure/configuration-files)
- [markdownlint Rules](https://github.com/DavidAnson/markdownlint)
- [CSpell Configuration](https://cspell.org/docs/configuration/)
- [awesome-markdown-resumes](https://github.com/markdownresume/awesome-markdown-resumes)
- [md-to-pdf (modern alternative)](https://github.com/simonhaenisch/md-to-pdf)
- [PhantomJS Deprecation](https://smali-kazmi.medium.com/from-phantomjs-to-puppeteer-building-a-modern-html-to-pdf-converter-987def3caf1f)