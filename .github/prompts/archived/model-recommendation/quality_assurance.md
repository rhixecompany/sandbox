# Quality Assurance

> Extracted from `model-recommendation.prompt.md` for DRY templating.

## Quality Assurance

### Validation Steps

- [ ] File successfully read and parsed
- [ ] Frontmatter extracted correctly (or noted if missing)
- [ ] Task complexity accurately categorized (Simple/Moderate/Complex/Advanced)
- [ ] Primary task category identified from 8 options
- [ ] Model recommendation aligns with decision tree logic
- [ ] Multiplier cost explained for user's subscription tier
- [ ] Alternative models provided with clear trade-off explanations
- [ ] Auto-selection guidance included (recommended/not recommended/situational)
- [ ] Deprecated model warnings included if applicable
- [ ] Frontmatter update example provided (valid YAML)
- [ ] Tool alignment verified (model capabilities match specified tools)
- [ ] Context7 used when verification needed for latest model information
- [ ] Report includes all required sections (summary, analysis, recommendation, implementation)

### Success Criteria

- Recommendation is justified by specific file characteristics
- Cost impact is clear and appropriate for subscription tier
- Alternative models cover different priority factors (speed vs. quality vs. cost)
- Frontmatter update is ready to copy-paste (no placeholders)
- User can immediately act on recommendation (clear steps)
- Report is readable and scannable (good structure, tables, emoji markers)

### Failure Triggers

- File path is invalid or unreadable → Stop and request valid path
- File is not `.agent.md` or `.prompt.md` → Stop and clarify file type
- Cannot determine task complexity from content → Request more specific file or clarification
- Model recommendation contradicts documented capabilities → Use Context7 to verify current info
- Subscription tier is invalid (not Free/Pro/Pro+) → Default to Pro and note assumption
