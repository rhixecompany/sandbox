# Generation Process

> Extracted from `openapi-to-application-code.prompt.md`.

## Generation Process

### Step 1: Analyze the OpenAPI Specification

- Validate the OpenAPI spec for completeness and correctness
- Identify all endpoints, HTTP methods, request/response schemas
- Extract authentication requirements and security schemes
- Note data model relationships and constraints
- Flag any ambiguities or incomplete definitions

### Step 2: Design Application Architecture

- Plan directory structure appropriate for the framework
- Identify controller/handler grouping by resource or domain
- Design service layer organization for business logic
- Plan data models and entity relationships
- Design configuration and initialization strategy

### Step 3: Generate Application Code

- Create project structure with build/package configuration files
- Generate models/DTOs from OpenAPI schemas
- Generate controllers/handlers with route mappings
- Generate service layer with business logic
- Generate repository/data access layer if applicable
- Add error handling, validation, and logging
- Generate configuration and startup code

### Step 4: Add Supporting Files

- Generate appropriate unit tests for services and controllers
- Create README with setup and running instructions
- Add .gitignore and environment configuration templates
- Generate API documentation files
- Create example requests/integration tests
