# Steps for Create Feature

## Phase 1: Preparation
### Step 1.1: Analyze Requirements
- **Action**: Read spec file and extract requirements
- **Tool**: read_file
- **Output**: Requirements list

### Step 1.2: Create Plan
- **Action**: Generate implementation plan with phases
- **Tool**: create-implementation-plan skill
- **Output**: Plan file in .hermes/plans/

## Phase 2: Execution
### Step 2.1: Write Tests
- **Action**: Create failing tests for each requirement
- **Tool**: write_file, terminal
- **Output**: Test files with failing tests

### Step 2.2: Implement Feature
- **Action**: Write minimal code to pass tests
- **Tool**: write_file, patch, terminal
- **Output": Working implementation
