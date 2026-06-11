---
name: project-docs-template
description: "Documentation Templates"
version: 1.0.0
author: Alexa
---
     1|# Documentation Templates
     2|
     3|This file contains comprehensive templates for all project documentation files. Each template has variants for different contexts (Python/Go, OpenSource/Internal, project types).
     4|
     5|## Template Selection Guide
     6|
     7|### By Language
     8|
     9|- **Python**: Use `uv`, `pytest`, `ruff`, `pyproject.toml` references
    10|- **Go**: Use `go.mod`, `go test`, `golangci-lint` references
    11|
    12|### By Context
    13|
    14|- **OpenSource**: Include badges, CODE_OF_CONDUCT, security policy, community guidelines
    15|- **Internal/Work**: Include team chat channels, issue tracker references, internal tooling, compliance notes
    16|
    17|### By Project Type
    18|
    19|- **AI Agent**: MCP architecture, tool integrations, prompt patterns
    20|- **Microservice**: API schemas, service dependencies, health checks
    21|- **CLI Tool**: Installation methods, command examples, subcommands
    22|- **Infrastructure**: Terraform/K8s setup, deployment procedures, DR plans
    23|- **Library**: API reference, usage examples, integration guides
    24|
    25|## Template Variants Reference
    26|
    27|This table shows all language-specific variants available in this file:
    28|
    29|| Section | Python Variant | Go Variant | Location |
    30|| --- | --- | --- | --- |
    31|| README Quick Start | `PYTHON_QUICKSTART` | `GO_QUICKSTART` | Lines 70-117 |
    32|| User Guide Installation | `PYTHON_INSTALLATION` | `GO_INSTALLATION` | Lines 555-587 |
    33|| Developer Guide Setup | `PYTHON_DEV_SETUP` | `GO_DEV_SETUP` | Lines 954-978 |
    34|| Test Examples | `PYTHON_TEST_EXAMPLE` | `GO_TEST_EXAMPLE` | Lines 932-1004 |
    35|| Style Guidelines | `PYTHON_STYLE` | `GO_STYLE` | Lines 1236-1385 |
    36|| Documentation Format | Python Docstrings | Go Comments | In style sections |
    37|
    38|**How to use**: Each main template section uses placeholder tags like `[PYTHON_QUICKSTART or GO_QUICKSTART]`. The variants below provide the actual content to insert based on detected language.
    39|
    40|---
    41|
    42|## README.md Template
    43|
    44|### Structure (All Projects)
    45|
    46|```markdown
    47|# {PROJECT_NAME}
    48|
    49|{ONE_LINE_DESCRIPTION}
    50|
    51|[BADGES - OpenSource only] [![Build Status](link)](link) [![Coverage](link)](link) [![License](link)](link) [![Version](link)](link)
    52|
    53|## Overview
    54|
    55|{2-3 sentences explaining what the project does, why it exists, and who it's for}
    56|
    57|## Features
    58|
    59|- Feature 1 with brief explanation
    60|- Feature 2 with brief explanation
    61|- Feature 3 with brief explanation
    62|
    63|## Quick Start
    64|
    65|[PYTHON_QUICKSTART or GO_QUICKSTART]
    66|
    67|## Documentation
    68|
    69|- [Architecture](docs/ARCHITECTURE.md) - System design and components
    70|- [User Guide](docs/USER_GUIDE.md) - Usage examples and configuration
    71|- [Developer Guide](docs/DEVELOPER_GUIDE.md) - Development setup and contribution
    72|- [Contributing](docs/CONTRIBUTING.md) - Contribution guidelines
    73|
    74|## [CONTEXT_SPECIFIC_SECTIONS]
    75|
    76|[For OpenSource: ## Community, ## Security, ## License] [For Internal: ## Support, ## Compliance, ## Internal Resources]
    77|
    78|## License
    79|
    80|{LICENSE_INFO}
    81|```
    82|
    83|### Python Quick Start Variant
    84|
    85|````markdown
    86|## Quick Start
    87|
    88|### Installation
    89|
    90|```bash
    91|# Using uv (recommended)
    92|uv pip install {package_name}
    93|
    94|# Or using pip
    95|pip install {package_name}
    96|```
    97|````
    98|
    99|### Basic Usage
   100|
   101|```python
   102|from {package_name} import {main_class}
   103|
   104|# Example usage
   105|{example_code}
   106|```
   107|
   108|For more examples, see the [User Guide](docs/USER_GUIDE.md).
   109|
   110|````
   111|
   112|### Go Quick Start Variant
   113|
   114|```markdown
   115|## Quick Start
   116|
   117|### Installation
   118|
   119|```bash
   120|go install github.com/{org}/{project}@latest
   121|````
   122|
   123|### Basic Usage
   124|
   125|```go
   126|package main
   127|
   128|import "{module_path}"
   129|
   130|func main() {
   131|    // Example usage
   132|    {example_code}
   133|}
   134|```
   135|
   136|For more examples, see the [User Guide](docs/USER_GUIDE.md).
   137|
   138|````
   139|
   140|### OpenSource Additional Sections
   141|
   142|```markdown
   143|## Community
   144|
   145|- [Code of Conduct](CODE_OF_CONDUCT.md)
   146|- [Security Policy](SECURITY.md)
   147|- [Discussion Forum](link)
   148|- [Issue Tracker](link)
   149|
   150|## Contributing
   151|
   152|We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.
   153|
   154|## Support
   155|
   156|- Documentation: [docs/](docs/)
   157|- Issues: [GitHub Issues](link)
   158|- Discussions: [GitHub Discussions](link)
   159|````
   160|
   161|### Internal/Work Additional Sections
   162|
   163|```markdown
   164|## Support
   165|
   166|- Team Chat: #{team_channel}
   167|- Issue Tracker: [{PROJECT_KEY}](issue_tracker_link)
   168|- On-call: [Rotation schedule](link)
   169|
   170|## Compliance
   171|
   172|- DORA compliance: ✓
   173|- Security review: [Review #{number}](link)
   174|- Data classification: {classification}
   175|
   176|## Internal Resources
   177|
   178|- [Architecture Decision Records](docs/adr/)
   179|- [Runbooks](docs/runbooks/)
   180|- [Cloud Console](https://console.cloud.provider.com/project={project_id})
   181|```
   182|
   183|---
   184|
   185|## ARCHITECTURE.md Template
   186|
   187|### Structure (All Projects)
   188|
   189|````markdown
   190|# Architecture
   191|
   192|## Overview
   193|
   194|{High-level description of the system architecture in 2-3 paragraphs}
   195|
   196|## System Context
   197|
   198|[DIAGRAM - can be Mermaid, ASCII art, or reference to external diagram]
   199|
   200|```mermaid
   201|graph TD
   202|    A[External System 1] --> B[This Project]
   203|    B --> C[External System 2]
   204|    B --> D[Database]
   205|```
   206|````
   207|
   208|## Components
   209|
   210|### Component 1: {Name}
   211|
   212|**Purpose**: {What this component does}
   213|
   214|**Responsibilities**:
   215|
   216|- Responsibility 1
   217|- Responsibility 2
   218|
   219|**Technology**: {Language, framework, key libraries}
   220|
   221|**Interfaces**: {APIs, events, data formats}
   222|
   223|### Component 2: {Name}
   224|
   225|{Repeat structure}
   226|
   227|## Data Flow
   228|
   229|{Explain how data moves through the system}
   230|
   231|[DIAGRAM showing data flow]
   232|
   233|## [PROJECT_TYPE_SPECIFIC_SECTIONS]
   234|
   235|[For AI Agents: ## MCP Architecture, ## Tool Integrations, ## RAG Pipeline] [For Microservices: ## Service Dependencies, ## API Contracts, ## Event Schemas] [For Infrastructure: ## Cloud Resources, ## Network Architecture, ## Deployment Model]
   236|
   237|## Key Design Decisions
   238|
   239|### Decision 1: {Title}
   240|
   241|**Context**: {Why this decision was needed}
   242|
   243|**Decision**: {What was decided}
   244|
   245|**Rationale**: {Why this approach was chosen}
   246|
   247|**Alternatives Considered**: {What else was considered and why it wasn't chosen}
   248|
   249|### Decision 2: {Title}
   250|
   251|{Repeat structure}
   252|
   253|## Technology Stack
   254|
   255|- **Language**: {Language and version}
   256|- **Framework**: {Framework and version}
   257|- **Database**: {Database type and version}
   258|- **Infrastructure**: {Cloud provider, key services}
   259|- **Key Dependencies**: {Critical libraries}
   260|
   261|## Non-Functional Requirements
   262|
   263|- **Performance**: {Performance targets and characteristics}
   264|- **Scalability**: {How the system scales}
   265|- **Reliability**: {Availability targets, failure handling}
   266|- **Security**: {Security measures, authentication, authorization}
   267|
   268|## Deployment Architecture
   269|
   270|[DIAGRAM of deployment]
   271|
   272|{Description of how the system is deployed}
   273|
   274|## Monitoring & Observability
   275|
   276|- **Metrics**: {Key metrics and where they're tracked}
   277|- **Logs**: {Logging strategy and aggregation}
   278|- **Tracing**: {Distributed tracing approach if applicable}
   279|- **Alerts**: {Critical alerts and thresholds}
   280|
   281|## Future Considerations
   282|
   283|{Known limitations, planned improvements, technical debt}
   284|
   285|````
   286|
   287|### AI Agent Architecture Additions
   288|
   289|```markdown
   290|## MCP Architecture
   291|
   292|### MCP Servers
   293|
   294|```mermaid
   295|graph LR
   296|    A[Claude] --> B[MCP Server 1]
   297|    A --> C[MCP Server 2]
   298|    B --> D[Tool 1]
   299|    B --> E[Tool 2]
   300|    C --> F[Tool 3]
   301|````
   302|
   303|**Server 1: {Name}**
   304|
   305|- Purpose: {What it provides}
   306|- Tools: {List of tools}
   307|- Resources: {List of resources}
   308|
   309|### Tool Integrations
   310|
   311|| Tool   | Purpose   | MCP Server | Configuration    |
   312|| ------ | --------- | ---------- | ---------------- |
   313|| tool_1 | {Purpose} | {Server}   | {Config details} |
   314|
   315|## RAG Pipeline
   316|
   317|[If applicable]
   318|
   319|```mermaid
   320|graph TD
   321|    A[User Query] --> B[Embedding]
   322|    B --> C[Vector Search]
   323|    C --> D[Vertex AI Vector Search]
   324|    D --> E[Retrieved Docs]
   325|    E --> F[Context Assembly]
   326|    F --> G[LLM Response]
   327|```
   328|
   329|**Components**:
   330|
   331|- **Embedding Model**: {Model name and version}
   332|- **Vector Database**: {Vertex AI Vector Search, index details}
   333|- **Chunking Strategy**: {How documents are chunked}
   334|- **Retrieval**: {Top-k, similarity threshold}
   335|
   336|## Prompt Patterns
   337|
   338|Key prompts used in the agent:
   339|
   340|### Pattern 1: {Name}
   341|
   342|```
   343|{Prompt template with variables}
   344|```
   345|
   346|**When Used**: {Context for this prompt} **Variables**: {Description of variables}
   347|
   348|````
   349|
   350|### Microservice Architecture Additions
   351|
   352|```markdown
   353|## Service Dependencies
   354|
   355|```mermaid
   356|graph TD
   357|    A[API Gateway] --> B[Service 1]
   358|    A --> C[Service 2]
   359|    B --> D[Database]
   360|    C --> D
   361|    B --> E[Message Queue]
   362|    C --> E
   363|````
   364|
   365|## API Contracts
   366|
   367|### Service 1 API
   368|
   369|**Base URL**: `/api/v1/service1`
   370|
   371|**Endpoints**:
   372|
   373|#### GET /resource
   374|
   375|Request:
   376|
   377|```json
   378|{
   379|  "field": "value"
   380|}
   381|```
   382|
   383|Response:
   384|
   385|```json
   386|{
   387|  "data": {},
   388|  "status": "success"
   389|}
   390|```
   391|
   392|## Inter-Service Communication
   393|
   394|- **Synchronous**: REST APIs via internal load balancer
   395|- **Asynchronous**: Pub/Sub for events
   396|- **Protocol**: gRPC for high-throughput internal calls
   397|
   398|## Health Checks
   399|
   400|- **Liveness**: `/health/live` - Pod is running
   401|- **Readiness**: `/health/ready` - Pod can accept traffic
   402|- **Startup**: `/health/startup` - Pod has initialized
   403|
   404|````
   405|
   406|### Infrastructure Architecture Additions
   407|
   408|```markdown
   409|## Cloud Resources
   410|
   411|### Cloud Provider Resources
   412|
   413|- **Project ID**: {project_id}
   414|- **Region**: {primary_region}
   415|- **Zones**: {zones}
   416|
   417|**Compute**:
   418|- Kubernetes Clusters: {cluster details}
   419|- Serverless Functions: {function details}
   420|
   421|**Storage**:
   422|- Cloud SQL: {database details}
   423|- GCS Buckets: {bucket purposes}
   424|
   425|**Networking**:
   426|- VPC: {vpc details}
   427|- Subnets: {subnet configuration}
   428|- Firewalls: {firewall rules}
   429|
   430|## Terraform Structure
   431|
   432|````
   433|
   434|terraform/ ├── environments/ │ ├── prod/ │ ├── staging/ │ └── dev/ ├── modules/ │ ├── gke/ │ ├── cloudsql/ │ └── networking/ └── global/
   435|
   436|```
   437|
   438|## Deployment Model
   439|
   440|- **Infrastructure**: Terraform
   441|- **Applications**: Helm charts on GKE
   442|- **CI/CD**: CI/CD platform with automated deployments
   443|- **GitOps**: ArgoCD for declarative deployments
   444|```
   445|
   446|---
   447|
   448|## USER_GUIDE.md Template
   449|
   450|````markdown
   451|# User Guide
   452|
   453|## Introduction
   454|
   455|{What users can accomplish with this project}
   456|
   457|## Getting Started
   458|
   459|### Prerequisites
   460|
   461|{List of required tools, accounts, permissions}
   462|
   463|### Installation
   464|
   465|[PYTHON_INSTALLATION or GO_INSTALLATION]
   466|
   467|### Configuration
   468|
   469|{How to configure the application}
   470|
   471|**Environment Variables**:
   472|
   473|| Variable | Description   | Required | Default   |
   474|| -------- | ------------- | -------- | --------- |
   475|| VAR_1    | {Description} | Yes      | -         |
   476|| VAR_2    | {Description} | No       | {default} |
   477|
   478|**Configuration File**:
   479|
   480|```yaml
   481|# config.yaml
   482|setting1: value1
   483|setting2: value2
   484|```
   485|````
   486|
   487|## Basic Usage
   488|
   489|### Use Case 1: {Name}
   490|
   491|{Description of what this accomplishes}
   492|
   493|```bash
   494|# Command example
   495|{command}
   496|```
   497|
   498|**Expected Output**:
   499|
   500|```
   501|