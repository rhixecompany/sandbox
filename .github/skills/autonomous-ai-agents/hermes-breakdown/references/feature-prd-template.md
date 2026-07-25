# Feature PRD Template

**Purpose:** Define a single feature within an epic — user stories, acceptance criteria, dependencies, and technical approach.

---

## Feature: [Feature Name]

**Epic:** [Epic Name / EPIC-XXX]  
**ID:** FEAT-XXX  
**Status:** Draft / Ready / In Progress / Review / Done  
**Priority:** P0 / P1 / P2 / P3  
**Owner:** [Feature Owner]  
**Created:** YYYY-MM-DD  
**Target Sprint/Release:** [Sprint X / Release Y]  

---

### 1. Problem Statement

> What user problem does this solve? Why now?

[2-3 sentences describing the problem, user pain point, or opportunity]

---

### 2. User Stories

| ID | User Story | Acceptance Criteria | Priority |
|----|------------|---------------------|----------|
| US-1 | As a [role], I want to [action], so that [benefit] | 1. [Criterion 1]<br>2. [Criterion 2] | P0 |
| US-2 | As a [role], I want to [action], so that [benefit] | 1. [Criterion 1]<br>2. [Criterion 2] | P1 |
| US-3 | As a [role], I want to [action], so that [benefit] | 1. [Criterion 1]<br>2. [Criterion 2] | P2 |

---

### 3. User Flows / UX

**Happy Path:**
1. [Step 1]
2. [Step 2]
3. [Step 3] → Success

**Edge Cases:**
- [Edge case 1]: [Handling]
- [Edge case 2]: [Handling]

**Wireframes/Mocks:** [Link to Figma/designs]

---

### 4. Technical Approach

**Architecture:**
- [Component 1]: [Responsibility]
- [Component 2]: [Responsibility]
- [Integration]: [External systems]

**Data Model Changes:**
- [Table/Collection]: [New fields / changes]
- [Migration]: [Strategy]

**API Contract:**
```json
// Request
{
  "field1": "type",
  "field2": "type"
}

// Response
{
  "field1": "type",
  "field2": "type"
}
```

---

### 5. Dependencies

| Dependency | Type | Owner | Status | Blocker? |
|------------|------|-------|--------|----------|
| [Dep 1] | Internal/External | [Team] | [Status] | Y/N |
| [Dep 2] | Internal/External | [Team] | [Status] | Y/N |

---

### 6. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Action] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Action] |

---

### 7. Rollout Plan

| Phase | Scope | Audience | Criteria |
|-------|-------|----------|----------|
| Canary | [Subset] | [Internal/Beta] | [Success criteria] |
| Gradual | [Percentage] | [Segment] | [Success criteria] |
| Full | 100% | All | [Success criteria] |

**Rollback Plan:** [How to revert if issues]

---

### 8. Acceptance Criteria Summary (for QA)

| Test ID | Scenario | Expected Result | Automation |
|---------|----------|-----------------|------------|
| TC-1 | [Happy path] | [Result] | Y/N |
| TC-2 | [Edge case] | [Result] | Y/N |
| TC-3 | [Error case] | [Result] | Y/N |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | | | |
| Engineering Lead | | | |
| QA Lead | | | |

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | | Initial draft |