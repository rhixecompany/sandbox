import express, { Request, Response, NextFunction } from 'express';
import cors from 'cors';
import * as fs from 'fs';
import * as path from 'path';
import { v4 as uuidv4 } from 'uuid';

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface JsonRpcRequest {
  jsonrpc: '2.0';
  id: string | number | null;
  method: string;
  params?: Record<string, unknown>;
}

interface JsonRpcSuccess {
  jsonrpc: '2.0';
  id: string | number | null;
  result: unknown;
}

interface JsonRpcError {
  jsonrpc: '2.0';
  id: string | number | null;
  error: {
    code: number;
    message: string;
    data?: unknown;
  };
}

type JsonRpcResponse = JsonRpcSuccess | JsonRpcError;

export interface ToolDefinition {
  name: string;
  description: string;
  inputSchema: Record<string, unknown>;
}

export interface ToolResult {
  content: Array<{ type: 'text'; text: string }>;
  isError?: boolean;
}

// ---------------------------------------------------------------------------
// Tool Registry
// ---------------------------------------------------------------------------

export type ToolHandler = (args: Record<string, unknown>) => Promise<ToolResult>;

const tools: Map<string, { definition: ToolDefinition; handler: ToolHandler }> = new Map();

function registerTool(definition: ToolDefinition, handler: ToolHandler): void {
  tools.set(definition.name, { definition, handler });
}

// Register built-in tools
registerTool(
  {
    name: 'search_customers',
    description:
      'Search for customers by name, email, or other criteria. Returns a list of matching customer records with basic contact information.',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Search query to match against customer name, email, or phone',
        },
        limit: {
          type: 'integer',
          description: 'Maximum number of results to return (default: 10, max: 50)',
          default: 10,
        },
        status: {
          type: 'string',
          enum: ['active', 'inactive', 'lead', 'any'],
          description: 'Filter by customer status',
          default: 'any',
        },
      },
      required: ['query'],
    },
  },
  async (args) => {
    const query = String(args.query || '');
    const limit = Math.min(Math.max(Number(args.limit) || 10, 1), 50);
    const status = String(args.status || 'any');

    // Sample customer data
    const sampleCustomers = [
      { id: 'CUST-001', name: 'Acme Corporation', email: 'contact@acme.com', phone: '+1-555-0101', status: 'active', city: 'San Francisco' },
      { id: 'CUST-002', name: 'Globex Industries', email: 'info@globex.com', phone: '+1-555-0102', status: 'active', city: 'New York' },
      { id: 'CUST-003', name: 'Initech Solutions', email: 'support@initech.com', phone: '+1-555-0103', status: 'inactive', city: 'Austin' },
      { id: 'CUST-004', name: 'Hooli Technologies', email: 'hello@hooli.com', phone: '+1-555-0104', status: 'active', city: 'Palo Alto' },
      { id: 'CUST-005', name: 'Stark Enterprises', email: 'admin@stark.com', phone: '+1-555-0105', status: 'lead', city: 'Los Angeles' },
      { id: 'CUST-006', name: 'Wayne Dynamics', email: 'info@wayne.com', phone: '+1-555-0106', status: 'active', city: 'Chicago' },
      { id: 'CUST-007', name: 'Cyberdyne Systems', email: 'research@cyberdyne.com', phone: '+1-555-0107', status: 'inactive', city: 'Detroit' },
      { id: 'CUST-008', name: 'Umbrella Corp', email: 'contact@umbrella.com', phone: '+1-555-0108', status: 'active', city: 'Raccoon City' },
    ];

    const queryLower = query.toLowerCase();
    let results = sampleCustomers.filter(
      (c) =>
        c.name.toLowerCase().includes(queryLower) ||
        c.email.toLowerCase().includes(queryLower) ||
        c.phone.includes(query)
    );

    if (status !== 'any') {
      results = results.filter((c) => c.status === status);
    }

    results = results.slice(0, limit);

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(
            {
              total: results.length,
              query,
              status,
              customers: results,
            },
            null,
            2
          ),
        },
      ],
    };
  }
);

registerTool(
  {
    name: 'get_customer_details',
    description:
      'Get detailed information about a specific customer by their ID. Returns full profile including contact info, account status, recent interactions, and notes.',
    inputSchema: {
      type: 'object',
      properties: {
        customer_id: {
          type: 'string',
          description: 'Unique identifier for the customer',
        },
        include_interactions: {
          type: 'boolean',
          description: 'Whether to include recent interaction history',
          default: true,
        },
      },
      required: ['customer_id'],
    },
  },
  async (args) => {
    const customerId = String(args.customer_id || '');
    const includeInteractions = args.include_interactions !== false;

    // Sample customer database
    const customerDb: Record<string, Record<string, unknown>> = {
      'CUST-001': {
        id: 'CUST-001',
        name: 'Acme Corporation',
        email: 'contact@acme.com',
        phone: '+1-555-0101',
        status: 'active',
        type: 'Enterprise',
        industry: 'Manufacturing',
        city: 'San Francisco',
        state: 'CA',
        country: 'USA',
        created_at: '2023-01-15T08:00:00Z',
        account_manager: 'Alice Johnson',
        annual_revenue: 5000000,
        notes: 'Key enterprise account. Multi-year contract renewing Q3.',
      },
      'CUST-002': {
        id: 'CUST-002',
        name: 'Globex Industries',
        email: 'info@globex.com',
        phone: '+1-555-0102',
        status: 'active',
        type: 'Mid-Market',
        industry: 'Technology',
        city: 'New York',
        state: 'NY',
        country: 'USA',
        created_at: '2023-04-20T10:30:00Z',
        account_manager: 'Bob Chen',
        annual_revenue: 1500000,
        notes: 'Growing account, interested in premium tier.',
      },
      'CUST-003': {
        id: 'CUST-003',
        name: 'Initech Solutions',
        email: 'support@initech.com',
        phone: '+1-555-0103',
        status: 'inactive',
        type: 'Small Business',
        industry: 'Software',
        city: 'Austin',
        state: 'TX',
        country: 'USA',
        created_at: '2022-11-05T14:00:00Z',
        account_manager: 'Carol Davis',
        annual_revenue: 250000,
        notes: 'Account on hold pending contract renewal. Contacted for re-engagement.',
      },
      'CUST-004': {
        id: 'CUST-004',
        name: 'Hooli Technologies',
        email: 'hello@hooli.com',
        phone: '+1-555-0104',
        status: 'active',
        type: 'Enterprise',
        industry: 'Technology',
        city: 'Palo Alto',
        state: 'CA',
        country: 'USA',
        created_at: '2023-07-12T09:15:00Z',
        account_manager: 'Alice Johnson',
        annual_revenue: 8000000,
        notes: 'Strategic partner. Exploring AI/ML integration.',
      },
      'CUST-005': {
        id: 'CUST-005',
        name: 'Stark Enterprises',
        email: 'admin@stark.com',
        phone: '+1-555-0105',
        status: 'lead',
        type: 'Startup',
        industry: 'Defense / Technology',
        city: 'Los Angeles',
        state: 'CA',
        country: 'USA',
        created_at: '2024-02-28T16:45:00Z',
        account_manager: 'Bob Chen',
        annual_revenue: 0,
        notes: 'Prospective lead. Initial demo completed. Follow-up scheduled.',
      },
    };

    const customer = customerDb[customerId];

    if (!customer) {
      return {
        isError: true,
        content: [
          {
            type: 'text',
            text: JSON.stringify({ error: `Customer not found: ${customerId}` }, null, 2),
          },
        ],
      };
    }

    const result: Record<string, unknown> = { ...customer };

    if (includeInteractions) {
      result.recent_interactions = [
        { date: '2024-06-20T10:00:00Z', type: 'email', summary: 'Renewal discussion', handled_by: 'Alice Johnson' },
        { date: '2024-06-15T14:30:00Z', type: 'call', summary: 'Product feedback call', handled_by: 'Alice Johnson' },
        { date: '2024-06-10T09:00:00Z', type: 'ticket', summary: 'Support ticket #4521 resolved', handled_by: 'Support Team' },
      ];
    }

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(result, null, 2),
        },
      ],
    };
  }
);

// ---------------------------------------------------------------------------
// Server
// ---------------------------------------------------------------------------

const app = express();
const PORT = parseInt(process.env.PORT || '3121', 10);
const HOST = process.env.HOST || '0.0.0.0';

// Middleware
app.use(cors());
app.use(express.json({ limit: '1mb' }));

// ---------------------------------------------------------------------------
// MCP Protocol Handler
// ---------------------------------------------------------------------------

async function handleMcpRequest(request: JsonRpcRequest): Promise<JsonRpcResponse> {
  const { id, method, params } = request;

  switch (method) {
    // -----------------------------------------------------------------------
    // Initialization
    // -----------------------------------------------------------------------
    case 'initialize':
      return {
        jsonrpc: '2.0',
        id,
        result: {
          protocolVersion: '2025-03-26',
          capabilities: {
            tools: {
              listChanged: true,
            },
            streaming: {
              supported: true,
              modes: ['text', 'sse'],
            },
          },
          serverInfo: {
            name: 'copilot-studio-mcp',
            version: '1.0.0',
          },
        },
      };

    // -----------------------------------------------------------------------
    // Tool listing
    // -----------------------------------------------------------------------
    case 'tools/list':
      return {
        jsonrpc: '2.0',
        id,
        result: {
          tools: Array.from(tools.values()).map((t) => t.definition),
        },
      };

    // -----------------------------------------------------------------------
    // Tool call
    // -----------------------------------------------------------------------
    case 'tools/call': {
      const p = (params || {}) as { name?: string; arguments?: Record<string, unknown> };
      const toolName = p.name || '';
      const toolArgs = p.arguments || {};

      if (!tools.has(toolName)) {
        return {
          jsonrpc: '2.0',
          id,
          error: {
            code: -32602,
            message: `Tool not found: ${toolName}`,
            data: { availableTools: Array.from(tools.keys()) },
          },
        };
      }

      try {
        const result = await tools.get(toolName)!.handler(toolArgs);
        return {
          jsonrpc: '2.0',
          id,
          result,
        };
      } catch (err: unknown) {
        const message = err instanceof Error ? err.message : String(err);
        return {
          jsonrpc: '2.0',
          id,
          error: {
            code: -32603,
            message: `Tool execution failed: ${message}`,
          },
        };
      }
    }

    // -----------------------------------------------------------------------
    // Notifications (no response expected)
    // -----------------------------------------------------------------------
    case 'notifications/initialized':
    case 'notifications/tools/list_changed':
      // Notifications are acknowledged silently
      return {
        jsonrpc: '2.0',
        id: null,
        result: null,
      };

    // -----------------------------------------------------------------------
    // Unknown method
    // -----------------------------------------------------------------------
    default:
      return {
        jsonrpc: '2.0',
        id,
        error: {
          code: -32601,
          message: `Method not found: ${method}`,
        },
      };
  }
}

// ---------------------------------------------------------------------------
// Routes
// ---------------------------------------------------------------------------

// Health check
app.get('/mcp/health', (_req: Request, res: Response) => {
  res.json({
    status: 'ok',
    service: 'copilot-studio-mcp',
    protocol: 'mcp',
    version: '1.0.0',
    toolsAvailable: tools.size,
  });
});

// OpenAPI spec
app.get('/mcp/openapi.json', (_req: Request, res: Response) => {
  const specPath = path.join(__dirname, 'apiDefinition.swagger.json');
  const spec = JSON.parse(fs.readFileSync(specPath, 'utf-8'));
  res.json(spec);
});

// MCP POST endpoint — JSON-RPC 2.0
app.post('/mcp', async (req: Request, res: Response) => {
  try {
    // Validate x-ms-agentic-protocol header
    const protocol = req.headers['x-ms-agentic-protocol'];
    if (protocol !== 'mcp' && protocol !== undefined) {
      res.status(400).json({
        jsonrpc: '2.0',
        id: null,
        error: {
          code: -32600,
          message: `Invalid x-ms-agentic-protocol header: ${protocol}. Expected 'mcp'.`,
        },
      });
      return;
    }

    // Accept single request or batch
    const requests: JsonRpcRequest[] = Array.isArray(req.body) ? req.body : [req.body];
    const responses: JsonRpcResponse[] = [];

    for (const request of requests) {
      if (!request || request.jsonrpc !== '2.0') {
        responses.push({
          jsonrpc: '2.0',
          id: request?.id ?? null,
          error: {
            code: -32600,
            message: 'Invalid JSON-RPC 2.0 request',
          },
        });
        continue;
      }

      const response = await handleMcpRequest(request);

      // Skip null-id responses for notifications
      if (response.id !== null) {
        responses.push(response);
      }
    }

    // Determine if client wants streaming
    const accept = req.headers.accept || '';
    const wantsStreaming = accept.includes('text/event-stream') || accept.includes('text/event-stream');

    if (wantsStreaming && responses.length > 0) {
      // SSE streaming response
      res.writeHead(202, {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        Connection: 'keep-alive',
        'X-MS-Agentic-Protocol': 'mcp',
      });

      for (const response of responses) {
        res.write(`data: ${JSON.stringify(response)}\n\n`);
      }

      res.write(`data: [DONE]\n\n`);
      res.end();
    } else {
      // Inline response
      const body = responses.length === 1 ? responses[0] : responses;
      res.setHeader('X-MS-Agentic-Protocol', 'mcp');
      res.json(body);
    }
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : String(err);
    res.status(500).json({
      jsonrpc: '2.0',
      id: null,
      error: {
        code: -32603,
        message: `Internal error: ${message}`,
      },
    });
  }
});

// ---------------------------------------------------------------------------
// Start
// ---------------------------------------------------------------------------

app.listen(PORT, HOST, () => {
  console.log(`\n  🚀 Copilot Studio MCP Server`);
  console.log(`  ───────────────────────────`);
  console.log(`  Service:   copilot-studio-mcp`);
  console.log(`  Protocol:  MCP (Model Context Protocol)`);
  console.log(`  Transport: streamable-http`);
  console.log(`  JSON-RPC:  2.0`);
  console.log(`  ───────────────────────────`);
  console.log(`  Endpoints:`);
  console.log(`    POST   /mcp                MCP JSON-RPC endpoint`);
  console.log(`    GET    /mcp/health         Health check`);
  console.log(`    GET    /mcp/openapi.json   OpenAPI specification`);
  console.log(`  ───────────────────────────`);
  console.log(`  Listening: http://${HOST}:${PORT}`);
  console.log(`  Tools:     ${tools.size} registered`);
  for (const name of tools.keys()) {
    console.log(`    • ${name}`);
  }
  console.log(`\n`);
});
