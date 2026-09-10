# Boilerplate Patterns Reference

Known template scaffolding patterns that the stripper removes.

## 1. Overview (self-ref)

Broken Windows-path self-reference that provides zero value.

```
## Overview

The Skills\<category>\<name>\skill.md skill provides tools and workflows for managing operations efficiently.
```

## 2. Workflow (generic Phase 1-4)

100% generic — applies to any topic, says nothing specific.

```
## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for X.

### Phase 2: Execution

Run the primary X operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.
```

## 3. When to Use (generic)

Circular definition — tells you to use the skill for its own operations.

```
## When to Use

- When you need to perform X operations or tasks
- When managing X infrastructure or configurations
- When automating or debugging X workflows
- **Triggers**: "X" required for a project
```

## 4. Best Practices (generic 5-item)

The classic template-filler list. Identical text found in 50+ skills.

```
## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
```

## 5. Verification Checklist (generic)

Same 5 items in every skill that has this.

```
## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] X operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable
```

## 6. Stray Path Reference

Inline path fragment inside a When to Use list.

```
- **Triggers**: "Skills\github\...\skill.md", use skills\github\...\skill.md
```
