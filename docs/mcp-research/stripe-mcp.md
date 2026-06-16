# Stripe MCP Server

**Source:** https://github.com/stripe/ai/tree/main/tools/modelcontextprotocol  
**Package:** `@stripe/mcp`  
**Official Docs:** https://docs.stripe.com/mcp

## Overview

Stripe's official **Model Context Protocol server** that exposes the Stripe Agent Toolkit to AI agents and frameworks. Allows agents to manage customers, products, payments, invoices, and more via the Stripe API.

## Key Features

- Customer lifecycle management (create, list, update)
- Product and price management
- Payment link and intent creation
- Invoice generation and management
- Balance queries and dispute handling
- Documentation search within Stripe docs
- Hosted remote server at `https://mcp.stripe.com` (OAuth)

## Tools Exposed

| Tool | Description |
|------|-------------|
| `customers.create` | Create a new Stripe customer |
| `customers.read` | Retrieve customer details |
| `products.create` | Create a product in the catalog |
| `prices.create` | Set pricing for a product |
| `payment_links.create` | Generate a shareable payment link |
| `payment_intents.create` | Initiate a payment intent |
| `invoices.create` | Create a new invoice |
| `invoices.send` | Send invoice to customer |
| `balance.retrieve` | Get current account balance |
| `documentation.search` | Search Stripe documentation |

## Installation

### Requirements

- Node.js 18+
- Stripe secret key (use Restricted Keys for least privilege)

### Quick Start (stdio — local testing)

```bash
npx -y @stripe/mcp --tools=all --api-key=sk_test_YOUR_KEY
```

### Specific tools only (recommended for production)

```bash
npx -y @stripe/mcp --tools=customers.create,customers.read,invoices.create \
  --api-key=$STRIPE_SECRET_KEY
```

### Programmatic Installation

```bash
npm install @stripe/agent-toolkit/modelcontextprotocol @modelcontextprotocol/sdk
```

```javascript
import { StripeAgentToolkit } from "@stripe/agent-toolkit/modelcontextprotocol";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new StripeAgentToolkit({
  secretKey: process.env.STRIPE_SECRET_KEY,
  configuration: {}
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Hermes / Claude Desktop Config

```yaml
mcp_servers:
  stripe:
    command: npx
    args: ["-y", "@stripe/mcp", "--tools=all"]
    env:
      STRIPE_SECRET_KEY: "rk_live_..."  # Use Restricted Key
```

## Remote Server (OAuth)

Connect directly via hosted endpoint:
- URL: `https://mcp.stripe.com`
- Auth: OAuth (granular authorization)
- Compatible with Cursor, Claude Desktop, Codex CLI

## Security Notes

- Always use **Restricted API Keys** (`rk_*`) to limit tool permissions
- Never hardcode keys — use environment variables or secrets managers
- Test with **test mode keys** (`sk_test_*`) before production

## Related Resources

- [Stripe MCP Official Docs](https://docs.stripe.com/mcp)
- [GitHub: stripe/ai](https://github.com/stripe/ai/tree/main/tools/modelcontextprotocol)
- [Stripe Agent Toolkit Setup](https://mcpconfig.com/agent-toolkit/)
