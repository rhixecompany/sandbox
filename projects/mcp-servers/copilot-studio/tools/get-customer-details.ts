/**
 * get-customer-details.ts
 *
 * Copilot Studio MCP Tool: get_customer_details
 *
 * Retrieves full customer profile by ID, including contact info,
 * account status, account manager, annual revenue, notes, and
 * optionally recent interaction history.
 *
 * This file exports the tool definition and handler for registration
 * with the MCP server. Import it from server.ts and call registerTool().
 */

import { ToolDefinition, ToolHandler } from '../server';

const definition: ToolDefinition = {
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
};

interface Interaction {
  date: string;
  type: string;
  summary: string;
  handled_by: string;
}

interface CustomerProfile {
  id: string;
  name: string;
  email: string;
  phone: string;
  status: string;
  type: string;
  industry: string;
  city: string;
  state: string;
  country: string;
  created_at: string;
  account_manager: string;
  annual_revenue: number;
  notes: string;
  recent_interactions?: Interaction[];
}

const CUSTOMER_DB: Record<string, CustomerProfile> = {
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

const INTERACTIONS: Record<string, Interaction[]> = {
  'CUST-001': [
    { date: '2024-06-20T10:00:00Z', type: 'email', summary: 'Renewal discussion', handled_by: 'Alice Johnson' },
    { date: '2024-06-15T14:30:00Z', type: 'call', summary: 'Product feedback call', handled_by: 'Alice Johnson' },
    { date: '2024-06-10T09:00:00Z', type: 'ticket', summary: 'Support ticket #4521 resolved', handled_by: 'Support Team' },
  ],
  'CUST-002': [
    { date: '2024-06-18T11:00:00Z', type: 'email', summary: 'Premium tier proposal sent', handled_by: 'Bob Chen' },
    { date: '2024-06-12T15:00:00Z', type: 'call', summary: 'Feature demo for new dashboard', handled_by: 'Bob Chen' },
  ],
  'CUST-003': [
    { date: '2024-05-28T08:30:00Z', type: 'email', summary: 'Re-engagement campaign outreach', handled_by: 'Carol Davis' },
  ],
  'CUST-004': [
    { date: '2024-06-22T13:00:00Z', type: 'meeting', summary: 'Quarterly business review', handled_by: 'Alice Johnson' },
    { date: '2024-06-08T10:00:00Z', type: 'email', summary: 'AI/ML integration roadmap', handled_by: 'Alice Johnson' },
    { date: '2024-05-30T16:00:00Z', type: 'ticket', summary: 'API rate limit issue resolved', handled_by: 'Support Team' },
  ],
};

const handler: ToolHandler = async (args) => {
  const customerId = String(args.customer_id || '');
  const includeInteractions = args.include_interactions !== false;

  const customer = CUSTOMER_DB[customerId];

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

  const result: CustomerProfile = { ...customer };

  if (includeInteractions) {
    result.recent_interactions = INTERACTIONS[customerId] || [];
  }

  return {
    content: [
      {
        type: 'text',
        text: JSON.stringify(result, null, 2),
      },
    ],
  };
};

export { definition, handler };
export default { definition, handler };
