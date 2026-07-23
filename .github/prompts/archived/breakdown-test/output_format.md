# Output Format

> Extracted from `breakdown-test.prompt.md`.

## Output Format

Create comprehensive test planning documentation:

1. **Test Strategy**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/test-strategy.md`
2. **Test Issues Checklist**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/test-issues-checklist.md`
3. **Quality Assurance Plan**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/qa-plan.md`

### Test Strategy Structure

#### 1. Test Strategy Overview

- **Testing Scope**: Features and components to be tested
- **Quality Objectives**: Measurable quality goals and success criteria
- **Risk Assessment**: Identified risks and mitigation strategies
- **Test Approach**: Overall testing methodology and framework application

#### 2. ISTQB Framework Implementation

##### Test Design Techniques Selection

Create a comprehensive analysis of which ISTQB test design techniques to apply:

- **Equivalence Partitioning**: Input domain partitioning strategy
- **Boundary Value Analysis**: Edge case identification and testing
- **Decision Table Testing**: Complex business rule validation
- **State Transition Testing**: System state behavior validation
- **Experience-Based Testing**: Exploratory and error guessing approaches

##### Test Types Coverage Matrix

Define comprehensive test type coverage:

- **Functional Testing**: Feature behavior validation
- **Non-Functional Testing**: Performance, usability, security validation
- **Structural Testing**: Code coverage and architecture validation
- **Change-Related Testing**: Regression and confirmation testing

#### 3. ISO 25010 Quality Characteristics Assessment

Create a quality characteristics prioritization matrix:

- **Functional Suitability**: Completeness, correctness, appropriateness assessment
- **Performance Efficiency**: Time behavior, resource utilization, capacity validation
- **Compatibility**: Co-existence and interoperability testing
- **Usability**: User interface, accessibility, and user experience validation
- **Reliability**: Fault tolerance, recoverability, and availability testing
- **Security**: Confidentiality, integrity, authentication, and authorization validation
- **Maintainability**: Modularity, reusability, and testability assessment
- **Portability**: Adaptability, installability, and replaceability validation

#### 4. Test Environment and Data Strategy

- **Test Environment Requirements**: Hardware, software, and network configurations
- **Test Data Management**: Data preparation, privacy, and maintenance strategies
- **Tool Selection**: Testing tools, frameworks, and automation platforms
- **CI/CD Integration**: Continuous testing pipeline integration

### Test Issues Checklist

#### Test Level Issues Creation

- [ ] **Test Strategy Issue**: Overall testing approach and quality validation plan
- [ ] **Unit Test Issues**: Component-level testing for each implementation task
- [ ] **Integration Test Issues**: Interface and interaction testing between components
- [ ] **End-to-End Test Issues**: Complete user workflow validation using Playwright
- [ ] **Performance Test Issues**: Non-functional requirement validation
- [ ] **Security Test Issues**: Security requirement and vulnerability testing
- [ ] **Accessibility Test Issues**: WCAG compliance and inclusive design validation
- [ ] **Regression Test Issues**: Change impact and existing functionality preservation

#### Test Types Identification and Prioritization

- [ ] **Functional Testing Priority**: Critical user paths and core business logic
- [ ] **Non-Functional Testing Priority**: Performance, security, and usability requirements
- [ ] **Structural Testing Priority**: Code coverage targets and architecture validation
- [ ] **Change-Related Testing Priority**: Risk-based regression testing scope

#### Test Dependencies Documentation

- [ ] **Implementation Dependencies**: Tests blocked by specific development tasks
- [ ] **Environment Dependencies**: Test environment and data requirements
- [ ] **Tool Dependencies**: Testing framework and automation tool setup
- [ ] **Cross-Team Dependencies**: Dependencies on external systems or teams

#### Test Coverage Targets and Metrics

- [ ] **Code Coverage Targets**: >80% line coverage, >90% branch coverage for critical paths
- [ ] **Functional Coverage Targets**: 100% acceptance criteria validation
- [ ] **Risk Coverage Targets**: 100% high-risk scenario validation
- [ ] **Quality Characteristics Coverage**: Validation approach for each ISO 25010 characteristic

### Task Level Breakdown

#### Implementation Task Creation and Estimation

- [ ] **Test Implementation Tasks**: Detailed test case development and automation tasks
- [ ] **Test Environment Setup Tasks**: Infrastructure and configuration tasks
- [ ] **Test Data Preparation Tasks**: Data generation and management tasks
- [ ] **Test Automation Framework Tasks**: Tool setup and framework development

#### Task Estimation Guidelines

- [ ] **Unit Test Tasks**: 0.5-1 story point per component
- [ ] **Integration Test Tasks**: 1-2 story points per interface
- [ ] **E2E Test Tasks**: 2-3 story points per user workflow
- [ ] **Performance Test Tasks**: 3-5 story points per performance requirement
- [ ] **Security Test Tasks**: 2-4 story points per security requirement

#### Task Dependencies and Sequencing

- [ ] **Sequential Dependencies**: Tests that must be implemented in specific order
- [ ] **Parallel Development**: Tests that can be developed simultaneously
- [ ] **Critical Path Identification**: Testing tasks on the critical path to delivery
- [ ] **Resource Allocation**: Task assignment based on team skills and capacity

#### Task Assignment Strategy

- [ ] **Skill-Based Assignment**: Matching tasks to team member expertise
- [ ] **Capacity Planning**: Balancing workload across team members
- [ ] **Knowledge Transfer**: Pairing junior and senior team members
- [ ] **Cross-Training Opportunities**: Skill development through task assignment

### Quality Assurance Plan

#### Quality Gates and Checkpoints

Create comprehensive quality validation checkpoints:

- **Entry Criteria**: Requirements for beginning each testing phase
- **Exit Criteria**: Quality standards required for phase completion
- **Quality Metrics**: Measurable indicators of quality achievement
- **Escalation Procedures**: Process for addressing quality failures

#### GitHub Issue Quality Standards

- [ ] **Template Compliance**: All test issues follow standardized templates
- [ ] **Required Field Completion**: Mandatory fields populated with accurate information
- [ ] **Label Consistency**: Standardized labeling across all test work items
- [ ] **Priority Assignment**: Risk-based priority assignment using defined criteria
- [ ] **Value Assessment**: Business value and quality impact assessment

#### Labeling and Prioritization Standards

- [ ] **Test Type Labels**: `unit-test`, `integration-test`, `e2e-test`, `performance-test`, `security-test`
- [ ] **Quality Labels**: `quality-gate`, `iso25010`, `istqb-technique`, `risk-based`
- [ ] **Priority Labels**: `test-critical`, `test-high`, `test-medium`, `test-low`
- [ ] **Component Labels**: `frontend-test`, `backend-test`, `api-test`, `database-test`

#### Dependency Validation and Management

- [ ] **Circular Dependency Detection**: Validation to prevent blocking relationships
- [ ] **Critical Path Analysis**: Identification of testing dependencies on delivery timeline
- [ ] **Risk Assessment**: Impact analysis of dependency delays on quality validation
- [ ] **Mitigation Strategies**: Alternative approaches for blocked testing activities

#### Estimation Accuracy and Review

- [ ] **Historical Data Analysis**: Using past project data for estimation accuracy
- [ ] **Technical Lead Review**: Expert validation of test complexity estimates
- [ ] **Risk Buffer Allocation**: Additional time allocation for high-uncertainty tasks
- [ ] **Estimate Refinement**: Iterative improvement of estimation accuracy
