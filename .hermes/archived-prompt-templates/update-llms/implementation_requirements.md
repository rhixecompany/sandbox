# Implementation Requirements

> Extracted from `update-llms.prompt.md`.

## Implementation Requirements

### Format Compliance

The updated `llms.txt` file must maintain this exact structure per the specification:

1. **H1 Header**: Single line with repository/project name (required)
2. **Blockquote Summary**: Brief description in blockquote format (optional but recommended)
3. **Additional Details**: Zero or more markdown sections without headings for context
4. **File List Sections**: Zero or more H2 sections containing markdown lists of links

### Content Requirements

#### Required Elements

- **Project Name**: Clear, descriptive title as H1
- **Summary**: Concise blockquote explaining the repository's purpose
- **Key Files**: Essential files organized by category (H2 sections)

#### File Link Format

Each file link must follow: `[descriptive-name](relative-url): optional description`

#### Section Organization

Organize files into logical H2 sections such as:

- **Documentation**: Core documentation files
- **Specifications**: Technical specifications and requirements
- **Examples**: Sample code and usage examples
- **Configuration**: Setup and configuration files
- **Optional**: Secondary files (special meaning - can be skipped for shorter context)

### Content Guidelines

#### Language and Style

- Use concise, clear, unambiguous language
- Avoid jargon without explanation
- Write for both human and LLM readers
- Be specific and informative in descriptions

#### File Selection Criteria

Include files that:

- Explain the repository's purpose and scope
- Provide essential technical documentation
- Show usage examples and patterns
- Define interfaces and specifications
- Contain configuration and setup instructions

Exclude files that:

- Are purely implementation details
- Contain redundant information
- Are build artifacts or generated content
- Are not relevant to understanding the project
