# Google Flights MCP Server

**Community Implementations:**
- https://github.com/punitarani/fli *(most popular — Python CLI + MCP)*
- https://github.com/HaroldLeo/google-flights-mcp *(9 tools, SerpAPI/fast-flights)*
- https://github.com/pulsemcp/mcp-servers/tree/main/experimental/google-flights *(TypeScript)*
- https://github.com/tistaharahap/google-flights-mcp *(FastMCP + Docker)*

## Overview

**Google Flights MCP servers** enable AI agents to search for flights, compare prices, and retrieve travel information using Google Flights data. Multiple community implementations exist — most use either the `fast-flights` library (no API key needed) or SerpAPI as the data source.

**Note:** Google does not provide an official Google Flights MCP server. All implementations are community-built.

## Key Features

- One-way and round-trip flight search
- Cheapest fare discovery across date ranges
- Airport code lookup
- Multi-passenger support
- Currency and cabin class filtering
- Price history and trend analysis

## Top Implementations

### punitarani/fli (Recommended)

Most active project — Python library, CLI, and MCP server in one.

```bash
pip install fli
```

```bash
# As MCP server
fli mcp

# As CLI
fli search --from JFK --to LAX --date 2025-09-01
```

**MCP Tools exposed:**
- `search_flights` — Search one-way flights
- `search_round_trip` — Search round-trip flights
- `get_cheapest_dates` — Find cheapest travel window
- `search_airports` — Lookup airport codes by city

### HaroldLeo/google-flights-mcp (9 tools)

```bash
git clone https://github.com/HaroldLeo/google-flights-mcp
cd google-flights-mcp
pip install -r requirements.txt
python server.py
```

Optional: Set `SERP_API_KEY` env var for SerpAPI backend (richer results).

### pulsemcp TypeScript

```bash
cd mcp-servers/experimental/google-flights
npm install
npm start
```

No API key required. Supports date-price grid (~60 days lookahead).

## Hermes / Claude Desktop Config

```yaml
mcp_servers:
  google-flights:
    command: fli
    args: ["mcp"]
```

Or with Python server:

```yaml
mcp_servers:
  google-flights:
    command: python3
    args: ["/path/to/google-flights-mcp/server.py"]
    env:
      SERP_API_KEY: "optional_for_richer_results"
```

## Example Agent Prompts

- "Find the cheapest flights from NYC to London in October"
- "Compare prices for JFK to LAX next Friday vs. Saturday"
- "What's the airport code for Heathrow?"
- "Search for round-trip flights from SFO to Tokyo under $800"

## Data Sources

| Source | API Key | Coverage |
|--------|---------|----------|
| `fast-flights` | None required | Real-time Google Flights scraping |
| SerpAPI | Required (paid) | Richer filters, structured JSON |
| Direct scraping | None | Basic fare data |

## Related Resources

- [fli on GitHub](https://github.com/punitarani/fli)
- [HaroldLeo/google-flights-mcp](https://github.com/HaroldLeo/google-flights-mcp)
- [pulsemcp TypeScript implementation](https://github.com/pulsemcp/mcp-servers/tree/main/experimental/google-flights)
- [fast-flights library](https://github.com/AWeirdDev/flights)
