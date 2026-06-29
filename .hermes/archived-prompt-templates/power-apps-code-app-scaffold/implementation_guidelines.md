# Implementation Guidelines

> Extracted from `power-apps-code-app-scaffold.prompt.md`.

## Implementation Guidelines

### Prerequisites to Mention

- Visual Studio Code with Power Platform Tools extension
- Node.js (LTS version - v18.x or v20.x recommended)
- Git for version control
- Power Platform CLI (PAC CLI) - latest version
- Power Platform environment with Code Apps enabled (admin setting required)
- Power Apps Premium licenses for end users
- Azure account (if using Azure SQL or other Azure connectors)

### PAC CLI Commands to Include

- `pac auth create --environment {environment-id}` - Authenticate with specific environment
- `pac env select --environment {environment-url}` - Select target environment
- `pac code init --displayName "App Name"` - Initialize code app project
- `pac connection list` - List available connections
- `pac code add-data-source -a {api-name} -c {connection-id}` - Add connector
- `pac code push` - Deploy to Power Platform

### Officially Supported Connectors

Focus on these officially supported connectors with setup examples:

- **SQL Server (including Azure SQL)**: Full CRUD operations, stored procedures
- **SharePoint**: Document libraries, lists, and sites
- **Office 365 Users**: Profile information, user photos, group memberships
- **Office 365 Groups**: Team information and collaboration
- **Azure Data Explorer**: Analytics and big data queries
- **OneDrive for Business**: File storage and sharing
- **Microsoft Teams**: Team collaboration and notifications
- **MSN Weather**: Weather data integration
- **Microsoft Translator V2**: Multi-language translation
- **Dataverse**: Full CRUD operations, relationships, and business logic

### Sample Connector Integration

Include working examples for Office 365 Users:

```typescript
// Example: Get current user profile
const profile = await Office365UsersService.MyProfile_V2(
  "id,displayName,jobTitle,userPrincipalName"
);

// Example: Get user photo
const photoData = await Office365UsersService.UserPhoto_V2(
  profile.data.id
);
```

### Current Limitations to Document

- Content Security Policy (CSP) not yet supported
- Storage SAS IP restrictions not supported
- No Power Platform Git integration
- No Dataverse solutions support
- No native Azure Application Insights integration

### Best Practices to Include

- Use port 3000 for local development (required by Power Apps SDK)
- Set `verbatimModuleSyntax: false` in TypeScript config
- Configure vite.config.ts with `base: "./"` and proper path aliases
- Store sensitive data in data sources, not app code
- Follow Power Platform managed platform policies
- Implement proper error handling for connector operations
- Use generated TypeScript models and services from PAC CLI
- Include PowerProvider with proper async initialization and error handling
