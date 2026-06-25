/**
 * search-customers.ts
 *
 * Copilot Studio MCP Tool: search_customers
 *
 * Searches the customer database by name, email, or phone number.
 * Supports filtering by account status and pagination via limit.
 *
 * This file exports the tool definition and handler for registration
 * with the MCP server. Import it from server.ts and call registerTool().
 */

import { ToolDefinition, ToolHandler } from '../server';

const definition: ToolDefinition = {
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
};

interface Customer {
  id: string;
  name: string;
  email: string;
  phone: string;
  status: string;
  city: string;
}

const SAMPLE_CUSTOMERS: Customer[] = [
  { id: 'CUST-001', name: 'Acme Corporation', email: 'contact@acme.com', phone: '+1-555-0101', status: 'active', city: 'San Francisco' },
  { id: 'CUST-002', name: 'Globex Industries', email: 'info@globex.com', phone: '+1-555-0102', status: 'active', city: 'New York' },
  { id: 'CUST-003', name: 'Initech Solutions', email: 'support@initech.com', phone: '+1-555-0103', status: 'inactive', city: 'Austin' },
  { id: 'CUST-004', name: 'Hooli Technologies', email: 'hello@hooli.com', phone: '+1-555-0104', status: 'active', city: 'Palo Alto' },
  { id: 'CUST-005', name: 'Stark Enterprises', email: 'admin@stark.com', phone: '+1-555-0105', status: 'lead', city: 'Los Angeles' },
  { id: 'CUST-006', name: 'Wayne Dynamics', email: 'info@wayne.com', phone: '+1-555-0106', status: 'active', city: 'Chicago' },
  { id: 'CUST-007', name: 'Cyberdyne Systems', email: 'research@cyberdyne.com', phone: '+1-555-0107', status: 'inactive', city: 'Detroit' },
  { id: 'CUST-008', name: 'Umbrella Corp', email: 'contact@umbrella.com', phone: '+1-555-0108', status: 'active', city: 'Raccoon City' },
];

const handler: ToolHandler = async (args) => {
  const query = String(args.query || '');
  const limit = Math.min(Math.max(Number(args.limit) || 10, 1), 50);
  const status = String(args.status || 'any');

  const queryLower = query.toLowerCase();
  let results = SAMPLE_CUSTOMERS.filter(
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
        text: JSON.stringify({ total: results.length, query, status, customers: results }, null, 2),
      },
    ],
  };
};

export { definition, handler };
export default { definition, handler };
