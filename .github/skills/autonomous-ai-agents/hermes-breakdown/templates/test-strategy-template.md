# Test Strategy Template

**Purpose:** Define the test approach for a feature/epic — unit, integration, e2e, acceptance criteria, and quality gates.

---

## Test Strategy: [Feature/Epic Name]

**ID:** TS-XXX  
**Feature:** [Feature Name / FEAT-XXX]  
**Epic:** [Epic Name / EPIC-XXX]  
**Created:** YYYY-MM-DD  
**Author:** [QA Lead / Engineer]  
**Status:** Draft / Reviewed / Approved  

---

### 1. Test Scope

#### In Scope
- [Component 1]
- [Integration point 1]
- [User flow 1]

#### Out of Scope
- [Component X]
- [Legacy system Y]

---

### 2. Test Levels

#### Unit Tests
| Target | Framework | Coverage Target | Location |
|--------|-----------|-----------------|----------|
| [Module A] | pytest/Jest | ≥80% | `tests/unit/` |
| [Module B] | pytest/Jest | ≥80% | `tests/unit/` |
| [Utility fn] | pytest/Jest | ≥90% | `tests/unit/` |

**Patterns:**
- Test pure functions in isolation
- Mock external dependencies
- Name: `test_<function>_<scenario>_<expected>`

#### Integration Tests
| Integration Point | Test Focus | Framework | Location |
|-------------------|------------|-----------|----------|
| [API ↔ DB] | CRUD, transactions | pytest/Testcontainers | `tests/integration/` |
| [Service A ↔ Service B] | Contract, resilience | Pact/pytest | `tests/integration/` |
| [Frontend ↔ Backend] | API contract | Cypress/Playwright | `tests/e2e/` |

#### End-to-End Tests
| User Flow | Priority | Tool | Test Data |
|-----------|----------|------|-----------|
| [Flow 1: Happy path] | P0 | Playwright/Cypress | Synthetic |
| [Flow 2: Edge case] | P1 | Playwright/Cypress | Synthetic |
| [Flow 3: Error handling] | P1 | Playwright/Cypress | Synthetic |

#### Acceptance Tests
| AC ID | Scenario | Given/When/Then | Automation |
|-------|----------|-----------------|------------|
| AC-1 | [Story 1 happy path] | Given X, When Y, Then Z | Y |
| AC-2 | [Story 1 edge case] | Given X, When Y, Then Z | Y |
| AC-3 | [Story 2 happy path] | Given X, When Y, Then Z | N |

---

### 3. Test Environments

| Environment | Purpose | Data | Refresh Cadence |
|-------------|---------|------|-----------------|
| Local | Dev testing | Synthetic | N/A |
| CI | Automated gates | Synthetic | Per run |
| Staging | Integration, UAT | Subset of prod | Daily |
| Production | Canary, monitoring | Real | N/A |

---

### 4. Quality Gates

| Gate | Criteria | Blocking? | Where Enforced |
|------|----------|-----------|----------------|
| Unit coverage | ≥80% (lines, branches) | Yes | CI pipeline |
| Integration pass | 100% critical paths | Yes | CI pipeline |
| E2E pass | P0 flows 100% | Yes | CI/CD pipeline |
| Security scan | No critical/high vulns | Yes | CI pipeline |
| Performance | P95 < 500ms (API) | No | Staging |
| Accessibility | WCAG 2.1 AA | No | Staging |

---

### 5. Test Data Strategy

| Data Type | Source | Masking | Volume |
|-----------|--------|---------|--------|
| User accounts | Synthetic factory | N/A | 1000s |
| Transactions | Generated | N/A | 10000s |
| PII | Faker library | Full | As needed |

---

### 6. Defect Management

| Severity | SLA | Escalation |
|----------|-----|------------|
| Critical (P0) | 2 hours | Page on-call |
| High (P1) | 4 hours | Notify lead |
| Medium (P2) | 24 hours | Sprint triage |
| Low (P3) | Next sprint | Backlog |

---

### 7. Release Criteria

- [ ] All P0/P1 tests passing
- [ ] Unit coverage ≥80%
- [ ] No critical/high security findings
- [ ] Performance benchmarks met
- [ ] Accessibility audit passed
- [ ] Documentation updated
- [ ] Rollback plan validated

---

### 8. Monitoring & Observability (Post-Release)

| Metric | Target | Alert Threshold | Dashboard |
|--------|--------|-----------------|-----------|
| Error rate | <0.1% | >1% | [Link] |
| Latency P95 | <500ms | >1s | [Link] |
| Throughput | >1000 req/s | <500 req/s | [Link] |
| Availability | 99.9% | <99.5% | [Link] |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Lead | | | |
| Engineering Lead | | | |
| Product Owner | | | |

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | | Initial draft |