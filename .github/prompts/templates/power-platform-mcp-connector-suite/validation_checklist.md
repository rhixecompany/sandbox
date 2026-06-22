# Validation Checklist

> Extracted from `power-platform-mcp-connector-suite.prompt.md`.

## Validation Checklist

### Technical Compliance

- [ ] `x-ms-agentic-protocol: mcp-streamable-1.0` in MCP endpoint
- [ ] No reference types in any schema definitions
- [ ] All type fields are single types (not arrays)
- [ ] Resources included as tool outputs
- [ ] JSON-RPC 2.0 compliance in script.csx
- [ ] Full URI endpoints throughout
- [ ] Clear descriptions for Copilot Studio agents
- [ ] Authentication properly configured
- [ ] Policy templates for MCP transformations
- [ ] Generative Orchestration compatibility

### CLI Validation

- [ ] **paconn validate**: `paconn validate --api-def apiDefinition.swagger.json` passes without errors
- [ ] **pac CLI ready**: Connector can be created/updated with `pac connector create/update`
- [ ] **Script validation**: script.csx passes automatic validation during pac CLI upload
- [ ] **Package validation**: `ConnectorPackageValidator.ps1` runs successfully

### OAuth and Security Requirements

- [ ] **OAuth 2.0 Enhanced**: Standard OAuth 2.0 with MCP security best practices implementation
- [ ] **Token Validation**: Implement token audience validation to prevent passthrough attacks
- [ ] **Custom Security Logic**: Enhanced validation in script.csx for MCP compliance
- [ ] **State Parameter Protection**: Secure state parameters for CSRF prevention
- [ ] **HTTPS Enforcement**: All production endpoints use HTTPS only
- [ ] **MCP Security Practices**: Implement confused deputy attack prevention within OAuth 2.0

### Certification Requirements

- [ ] **Complete metadata**: settings.json with product and service information
- [ ] **Icon compliance**: PNG format, 230x230 or 500x500 dimensions
- [ ] **Documentation**: Certification-ready readme with comprehensive examples
- [ ] **Security compliance**: OAuth 2.0 enhanced with MCP security practices, privacy policy
- [ ] **Authentication flow**: OAuth 2.0 with custom security validation properly configured
