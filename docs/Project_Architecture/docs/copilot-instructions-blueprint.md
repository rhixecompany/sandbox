# GitHub Copilot Instructions — docs

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always respect the Markdown format standards used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our documentation-only repository standards
5. **Code Quality**: Prioritize **clarity, accuracy, and maintainability** in all generated content

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Format**: Markdown only (GitHub-Flavored Markdown)
2. **Tools**: No build system or runtime dependencies
3. **Structure**: Pure documentation repository — no executable code

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: Documentation structure guidelines
- **folder-structure.md**: Content organization guidelines

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar documents to the one being modified or created
2. Analyze patterns for:
   - **Document structure**: Headings, lists, code blocks
   - **Cross-referencing**: Links between documents
   - **Content layout**: How information is organized
   - **Tables**: Format and usage patterns
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write clear, well-structured Markdown
- Use GitHub-Flavored Markdown consistently
- Keep docs DRY — reference rather than duplicate
- Maintain accurate cross-references between documents

## Documentation Requirements

- Follow the exact documentation format found in the codebase
- Match the style and completeness of existing documents
- Document parameters, returns, and exceptions in the same style
- Follow existing patterns for linking to related documentation

## Testing Approach

- No formal test framework — documentation-only repository
- Manual verification of Markdown formatting and cross-references

## Technology-Specific Guidelines

### Markdown
- Use GitHub-Flavored Markdown (GFM)
- Follow existing heading hierarchy patterns
- Use fenced code blocks with language identifiers
- Use relative links for cross-references

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing documentation
- Match organization patterns from similar documents
- Apply consistent formatting throughout
- Reference rather than duplicate content
- Update cross-references when moving or renaming documents

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any content
- Respect existing document structure without exception
- Pure documentation repository — contains no executable code
- Serves as centralized reference for dependency audit findings, research appendices, and architecture blueprints
- Cross-reference with individual project documentation
- VS Code settings in `.vscode/` are shared across workspace
