# Output Format

> Extracted from `breakdown-epic-arch.prompt.md`.

## Output Format

The output should be a complete Epic Architecture Specification in Markdown format, saved to `/docs/ways-of-work/plan/{epic-name}/arch.md`.

### Specification Structure

#### 1. Epic Architecture Overview

- A brief summary of the technical approach for the epic.

#### 2. System Architecture Diagram

Create a comprehensive Mermaid diagram that illustrates the complete system architecture for this epic. The diagram should include:

- **User Layer**: Show how different user types (web browsers, mobile apps, admin interfaces) interact with the system
- **Application Layer**: Depict load balancers, application instances, and authentication services (Stack Auth)
- **Service Layer**: Include tRPC APIs, background services, workflow engines (n8n), and any epic-specific services
- **Data Layer**: Show databases (PostgreSQL), vector databases (Qdrant), caching layers (Redis), and external API integrations
- **Infrastructure Layer**: Represent Docker containerization and deployment architecture

Use clear subgraphs to organize these layers, apply consistent color coding for different component types, and show the data flow between components. Include both synchronous request paths and asynchronous processing flows where relevant to the epic.

#### 3. High-Level Features & Technical Enablers

- A list of the high-level features to be built.
- A list of technical enablers (e.g., new services, libraries, infrastructure) required to support the features.

#### 4. Technology Stack

- A list of the key technologies, frameworks, and libraries to be used.

#### 5. Technical Value

- Estimate the technical value (e.g., High, Medium, Low) with a brief justification.

#### 6. T-Shirt Size Estimate

- Provide a high-level t-shirt size estimate for the epic (e.g., S, M, L, XL).
