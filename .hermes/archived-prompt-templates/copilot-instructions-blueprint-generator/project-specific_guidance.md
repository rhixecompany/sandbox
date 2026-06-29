# Project-Specific Guidance

> Extracted from `copilot-instructions-blueprint-generator.prompt.md`.

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Match the style and patterns of surrounding code
- When in doubt, prioritize consistency with existing code over external best practices
```

### 2. Codebase Analysis Instructions

To create the copilot-instructions.md file, first analyze the codebase to:

1. **Identify Exact Technology Versions**:
   - ${PROJECT_TYPE == "Auto-detect" ? "Detect all programming languages, frameworks, and libraries by scanning file extensions and configuration files" : `Focus on ${PROJECT_TYPE} technologies`}
   - Extract precise version information from project files, package.json, .csproj, etc.
   - Document version constraints and compatibility requirements

2. **Understand Architecture**:
   - Analyze folder structure and module organization
   - Identify clear layer boundaries and component relationships
   - Document communication patterns between components

3. **Document Code Patterns**:
   - Catalog naming conventions for different code elements
   - Note documentation styles and completeness
   - Document error handling patterns
   - Map testing approaches and coverage

4. **Note Quality Standards**:
   - Identify performance optimization techniques actually used
   - Document security practices implemented in the code
   - Note accessibility features present (if applicable)
   - Document code quality patterns evident in the codebase

### 3. Implementation Notes

The final copilot-instructions.md should:

- Be placed in the .github/copilot directory
- Reference only patterns and standards that exist in the codebase
- Include explicit version compatibility requirements
- Avoid prescribing any practices not evident in the code
- Provide concrete examples from the codebase
- Be comprehensive yet concise enough for Copilot to effectively use

Important: Only include guidance based on patterns actually observed in the codebase. Explicitly instruct Copilot to prioritize consistency with existing code over external best practices or newer language features. "
