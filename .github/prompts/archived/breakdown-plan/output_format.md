# Output Format

> Extracted from `breakdown-plan.prompt.md`.

## Output Format

Create two primary deliverables:

1. **Project Plan**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`
2. **Issue Creation Checklist**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md`

### Project Plan Structure

#### 1. Project Overview

- **Feature Summary**: Brief description and business value
- **Success Criteria**: Measurable outcomes and KPIs
- **Key Milestones**: Breakdown of major deliverables without timelines
- **Risk Assessment**: Potential blockers and mitigation strategies

#### 2. Work Item Hierarchy

```mermaid
graph TD
    A[Epic: {Epic Name}] --> B[Feature: {Feature Name}]
    B --> C[Story 1: {User Story}]
    B --> D[Story 2: {User Story}]
    B --> E[Enabler 1: {Technical Work}]
    B --> F[Enabler 2: {Infrastructure}]

    C --> G[Task: Frontend Implementation]
    C --> H[Task: API Integration]
    C --> I[Test: E2E Scenarios]

    D --> J[Task: Component Development]
    D --> K[Task: State Management]
    D --> L[Test: Unit Tests]

    E --> M[Task: Database Schema]
    E --> N[Task: Migration Scripts]

    F --> O[Task: CI/CD Pipeline]
    F --> P[Task: Monitoring Setup]
```

#### 3. GitHub Issues Breakdown

##### Epic Issue Template

```markdown
# Epic: {Epic Name}
