# Migration Monitoring

> Extracted from `generate-custom-instructions-from-codebase.prompt.md`.

## Migration Monitoring

### Tracking Metrics
- Percentage of code automatically migrated
- Number of manual validations required
- Error rate of automatic transformations
- Average migration time per file

### Error Reporting
How to report incorrect transformations to Copilot:
- Feedback patterns to improve rules
- Exceptions to document
- Adjustments to make to instructions

\`\`\`

### Phase 3: Contextual Examples Generation

${GENERATE_EXAMPLES == "true" ?
  "#### Transformation Examples
   For each identified pattern, generate:

   \`\`\`
   // BEFORE (${SOURCE_REFERENCE})
   [OLD_CODE_EXAMPLE]

   // AFTER (${TARGET_REFERENCE})
   [NEW_CODE_EXAMPLE]

   // COPILOT INSTRUCTIONS
   When you see this pattern [TRIGGER], transform it to [NEW_PATTERN] following these steps: [STEPS]
   \`\`\`" : ""}

### Phase 4: Validation and Optimization

#### Instructions Testing
- Apply instructions on test code
- Verify transformation consistency
- Adjust rules based on results
- Document exceptions and edge cases

#### Iterative Optimization
${AUTOMATION_LEVEL == "Aggressive" ?
  "- Refine rules to maximize automation
   - Reduce false positives in detection
   - Improve transformation accuracy
   - Document lessons learned" : ""}

### Final Result

Migration instructions that enable GitHub Copilot to:
1. **Automatically apply** the same transformations during future modifications
2. **Maintain consistency** with newly adopted conventions
3. **Avoid obsolete patterns** by automatically proposing alternatives
4. **Accelerate future migrations** by capitalizing on acquired experience
5. **Reduce errors** by automating repetitive transformations

These instructions transform Copilot into an intelligent migration assistant, capable of reproducing your technology evolution decisions consistently and reliably.
"
```
