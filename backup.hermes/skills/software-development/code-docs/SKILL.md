---
category: software-development
title: Code Docs
name: code-docs
description: "Use when writing Google Style docstrings for Python, Go, or Terraform code, or ensuring consistent documentation standards across projects."
---

## code-docs

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Code Docs operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Description

Google Style documentation for Python, Go, and Terraform. Provides docstring standards, formatting conventions, and best practices for code documentation.

## When to Use

- Writing docstrings for Python functions/classes
- Documenting Go packages and functions
- Creating Terraform module documentation
- Following Google Style documentation standards
- Adding docstrings to existing code
- Ensuring consistent documentation across projects

## When NOT to Use

- Non-Python/Go/Terraform languages
- General prose documentation (use project-docs instead)
- API reference generation (use context7 instead)
- Quick inline comments (use code comments instead)

## Workflow

### Phase 1: Understand Google Style

- Review Google Style Guide for target language
- Identify docstring format (one-line, multi-line, etc.)
- Note parameter and return value conventions

### Phase 2: Write Docstrings

- Add one-line summary (imperative mood)
- Add detailed description if needed
- Document parameters with types
- Document return values
- Include examples for complex functions

### Phase 3: Format Consistently

- Use proper indentation and spacing
- Follow language-specific conventions
- Ensure all public APIs are documented
- Check for consistency across codebase

### Phase 4: Verify & Review

- Validate docstring syntax
- Confirm examples work
- Review for clarity and completeness

## Tools & References

- **Related Skills**: project-docs (full documentation), writing-clearly-and-concisely (clarity)
- **Google Style Guide**: https://google.github.io/styleguide/
- **PEP 257**: Python docstring conventions
- **Godoc**: Go documentation format
- **Terraform Docs**: Module documentation standards

## Best Practices

- Use imperative mood for summaries ("Return X" not "Returns X")
- Include type hints in docstrings
- Provide examples for complex functions
- Document exceptions and edge cases
- Keep docstrings concise but complete
- Update docstrings when code changes
