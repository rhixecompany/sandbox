# Instructions

> Extracted from `refactor-method-complexity-reduce.prompt.md`.

## Instructions

1. **Analyze the current method** to identify sources of cognitive complexity:
   - Nested conditional statements
   - Multiple if-else or switch chains
   - Repeated code blocks
   - Multiple loops with conditions
   - Complex boolean expressions

2. **Identify extraction opportunities**:
   - Validation logic that can be extracted into a separate method
   - Type-specific or case-specific processing that repeats
   - Complex transformations or calculations
   - Common patterns that appear multiple times

3. **Extract focused helper methods**:
   - Each helper should have a single, clear responsibility
   - Extract validation into separate `Validate*` methods
   - Extract type-specific logic into handler methods
   - Create utility methods for common operations
   - Use appropriate access levels (static, private, async)

4. **Simplify the main method**:
   - Reduce nesting depth
   - Replace massive if-else chains with smaller orchestrated calls
   - Use switch statements where appropriate for cleaner dispatch
   - Ensure the main method reads as a high-level flow

5. **Preserve functionality**:
   - Maintain the same input/output behavior
   - Keep all validation and error handling
   - Preserve exception types and error messages
   - Ensure all parameters are properly passed to helpers

6. **Best practices**:
   - Make helper methods static when they don't need instance state
   - Use null checks and guard clauses early
   - Avoid creating unnecessary local variables
   - Consider using tuples for multiple return values
   - Group related helper methods together
