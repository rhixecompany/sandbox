# Common Optimization Patterns

> Extracted from `power-bi-dax-optimization.prompt.md`.

## Common Optimization Patterns

### Performance Optimizations:

- **Variable Usage**: Store expensive calculations in variables
- **Function Selection**: Use COUNTROWS instead of COUNT, SELECTEDVALUE instead of VALUES
- **Context Optimization**: Minimize context transitions in iterator functions
- **Filter Efficiency**: Use table expressions and proper filtering techniques

### Readability Improvements:

- **Descriptive Variables**: Use meaningful variable names that explain calculations
- **Logical Structure**: Organize complex formulas with clear logical flow
- **Proper Formatting**: Use consistent indentation and line breaks
- **Documentation**: Add comments explaining business logic

### Error Handling:

- **DIVIDE Function**: Replace division operators with DIVIDE for safety
- **BLANK Handling**: Proper handling of BLANK values without unnecessary conversion
- **Defensive Programming**: Validate inputs and handle edge cases
