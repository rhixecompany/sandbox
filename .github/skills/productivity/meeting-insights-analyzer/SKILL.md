---
author: Alexa
description: Use when analyzing meeting transcripts to uncover behavioral patterns,
  communication insights, filler words, and actionable feedback.
license: MIT
name: meeting-insights-analyzer
tags:
- imported
title: Meeting Insights Analyzer
version: 1.0.0

---
## Description

Analyze meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies conflict avoidance, filler words, conversation dominance, and listening opportunities.


## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## When to Use

- Analyzing your own communication patterns
- Preparing performance review examples
- Coaching team members on communication
- Tracking improvement in specific areas
- Identifying behavioral patterns
- Improving listening and facilitation skills

## When NOT to Use

- Single meeting analysis
- Real-time meeting notes
- Non-communication topics
- Confidential or sensitive meetings

## Workflow

### Phase 1: Gather Transcripts

- Collect meeting transcripts with speaker labels
- Include timestamps
- Ensure quality and accuracy

### Phase 2: Analyze Patterns

- Identify communication behaviors
- Note filler words and phrases
- Track speaking time per person
- Identify conflict avoidance

### Phase 3: Extract Insights

- Summarize key patterns
- Identify strengths and weaknesses
- Note improvement opportunities
- Compare across meetings

### Phase 4: Create Action Plan

- Set specific improvement goals
- Plan practice opportunities
- Track progress over time
- Get feedback from others

## Tools & References

- **Related Skills**: humanizer, writing-clearly-and-concisely
- **Formats**: Text, VTT, SRT, DOCX transcripts
- **Metrics**: Speaking time, filler words, interruptions

## Best Practices

- Analyze multiple meetings for patterns
- Focus on specific behaviors
- Get feedback from others
- Track progress over time
- Practice new behaviors
- Record yourself for self-analysis
- Share insights with mentor or coach



## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

