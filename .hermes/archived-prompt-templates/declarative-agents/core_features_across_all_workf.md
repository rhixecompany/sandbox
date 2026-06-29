# Core Features Across All Workflows

> Extracted from `declarative-agents.prompt.md`.

## Core Features Across All Workflows

### Microsoft 365 Agents Toolkit Integration

- **VS Code Extension**: Full integration with `teamsdevapp.ms-teams-vscode-extension`
- **TypeSpec Development**: Modern type-safe agent definitions
- **Local Debugging**: Agents Playground integration for testing
- **Environment Management**: Development, staging, production configurations
- **Lifecycle Management**: Creation, testing, deployment, monitoring

### TypeSpec Examples

```typespec
// Modern declarative agent definition
model MyAgent {
  name: string;
  description: string;
  instructions: string;
  capabilities: AgentCapability[];
  conversation_starters?: ConversationStarter[];
}
```

### JSON Schema v1.5 Validation

- Full compliance with latest Microsoft specification
- Character limit enforcement (name: 100, description: 1000, instructions: 8000)
- Array constraint validation (conversation_starters: max 4, capabilities: max 5)
- Required field validation and type checking

### Available Capabilities (Choose up to 5)

1. **WebSearch**: Internet search functionality
2. **OneDriveAndSharePoint**: File and content access
3. **GraphConnectors**: Enterprise data integration
4. **MicrosoftGraph**: Microsoft 365 service integration
5. **TeamsAndOutlook**: Communication platform access
6. **PowerPlatform**: Power Apps and Power Automate integration
7. **BusinessDataProcessing**: Enterprise data analysis
8. **WordAndExcel**: Document and spreadsheet manipulation
9. **CopilotForMicrosoft365**: Advanced Copilot features
10. **EnterpriseApplications**: Third-party system integration
11. **CustomConnectors**: Custom API and service integration

### Environment Variables Support

```json
{
  "description": "${AGENT_DESCRIPTION}",
  "instructions": "${AGENT_INSTRUCTIONS}",
  "name": "${AGENT_NAME}"
}
```

**Which workflow would you like to start with?** Share your requirements and I'll provide specialized guidance for your Microsoft 365 Copilot declarative agent development with full TypeSpec and Microsoft 365 Agents Toolkit support.
