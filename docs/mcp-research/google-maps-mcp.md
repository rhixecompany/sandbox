# Google Maps Comprehensive MCP Server

**Source:** https://github.com/vicpeacock/google-maps-comprehensive-mcp

## Overview

**Repository:** `vicpeacock/google-maps-comprehensive-mcp`
**Description:** Complete Google Maps MCP Server with 8 tools including geocoding, places search, directions, elevation data, and more using Google's latest APIs.

## Available Tools (8 Total)

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| **`maps_ping`** | Health check | Returns: `"Google Maps MCP server is alive ✅"` |
| **`maps_geocode`** | Forward geocoding | `address` → `location`, `formatted_address`, `place_id`, `address_components` |
| **`maps_reverse_geocode`** | Reverse geocoding | `latitude`, `longitude` → `formatted_address`, `place_id`, `address_components` |
| **`maps_search_places`** | Places search | `query` → `displayName`, `formattedAddress`, `location`, `types` |
| **`maps_place_details`** | Place details | `place_id` → `name`, `address`, `contact info`, `ratings`, `reviews`, `opening hours`, `photos` |
| **`maps_distance_matrix`** | Distance/duration matrix | `origins`, `destinations`, `mode` (`driving` \| `walking` \| `bicycling` \| `transit`) → `distances`, `durations` |
| **`maps_elevation`** | Elevation data | `locations` (`{ latitude, longitude }`) → `elevation`, `resolution` |
| **`maps_directions`** | Turn-by-turn directions | `origin`, `destination`, `travelMode` (`DRIVE` \| `WALK` \| `BICYCLE` \| `TRANSIT`) → `route steps`, `distance`, `duration`, `polyline` |

## Setup & Installation

### Prerequisites

- **Google Maps API Key** with these APIs enabled:
  - Places API (New)
  - Routes API
  - Geocoding API
  - Elevation API
- [Official API Key Guide](https://developers.google.com/maps/documentation/javascript/get-api-key#create-api-keys)

### Local Installation

```bash
# 1. Install dependencies
npm install

# 2. Build the project
npm run build

# 3. Set environment variable
export GOOGLE_MAPS_API_KEY="your-api-key-here"

# 4. Run locally
npm start
```

### Docker Deployment

```bash
# Build image
docker build -t google-maps-mcp .

# Run container
docker run -e GOOGLE_MAPS_API_KEY="your-api-key" google-maps-mcp

# Or use docker-compose
docker-compose up
```

## MCP Client Configuration

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "google-maps": {
      "command": "node",
      "args": ["/path/to/google-maps-comprehensive-mcp/dist/index.js"],
      "env": {
        "GOOGLE_MAPS_API_KEY": "your-api-key"
      }
    }
  }
}
```

### LM Studio

```json
{
  "mcpServers": {
    "google-maps": {
      "command": "npx",
      "args": ["-y", "google-maps-comprehensive-mcp"],
      "env": {
        "GOOGLE_MAPS_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Docker + Claude Desktop

```json
{
  "mcpServers": {
    "google-maps": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GOOGLE_MAPS_API_KEY", "google-maps-mcp"],
      "env": {
        "GOOGLE_MAPS_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Testing Status

> **All 8 tools tested and working correctly** ✅

## APIs Used

- **Places API (New)** - Place search & details
- **Routes API** - Directions & distance matrix
- **Geocoding API** - Forward & reverse geocoding
- **Elevation API** - Elevation data

## Security Notes

> ⚠️ **Important**: Never commit your API key to the repository. Always use environment variables.

```bash
# Correct approach
export GOOGLE_MAPS_API_KEY="your-key"

# Never do this
# GOOGLE_MAPS_API_KEY="your-key" in source code
```

## Troubleshooting

| Error | Solution |
|-------|----------|
| `"GOOGLE_MAPS_API_KEY environment variable is required"` | Set the env var: `export GOOGLE_MAPS_API_KEY="your-key"` |
| `"Tool not found"` | Rebuild: `npm run build` |
| Docker issues | Clean rebuild: `docker build --no-cache -t google-maps-mcp .` |

## Project Structure

```
google-maps-comprehensive-mcp/
├── src/                    # TypeScript source
├── maps_autocomplete.ts    # Autocomplete functionality
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Compose file
├── package.json            # Dependencies & scripts
├── tsconfig.json           # TypeScript config
└── README.md               # Documentation
```

## Key Notes

- **Language:** TypeScript
- **Runtime:** Node.js
- **Protocol:** MCP (Model Context Protocol)
- **License:** Check repository for details
- **Status:** Actively maintained (7 commits on main)

## Alternative: cablate/mcp-google-map

Another comprehensive implementation with 18 tools:
- GitHub: https://github.com/cablate/mcp-google-map
- Includes: `maps_batch_geocode`, `maps_explore_area`, `maps_weather`, `maps_air_quality`, `maps_static_map`, `maps_search_along_route`, `maps_plan_route`, `maps_compare_places`, `maps_local_rank_tracker`, and more
- See `skills/google-maps/` for agent skill definition

## Hermes Integration

For Hermes Agent (local Node.js build):

```yaml
mcp_servers:
  google-maps:
    command: "node"
    args: ["dist/index.js"]
    env:
      GOOGLE_MAPS_API_KEY: "${GOOGLE_MAPS_API_KEY}"
    tools:
      include: [maps_ping, maps_geocode, maps_reverse_geocode, maps_search_places, maps_place_details, maps_distance_matrix, maps_elevation, maps_directions]
```

For Docker mode:

```yaml
mcp_servers:
  google-maps:
    command: "docker"
    args: ["run", "-i", "--rm", "-e", "GOOGLE_MAPS_API_KEY", "google-maps-mcp"]
    env:
      GOOGLE_MAPS_API_KEY: "${GOOGLE_MAPS_API_KEY}"
    tools:
      include: [maps_ping, maps_geocode, maps_reverse_geocode, maps_search_places, maps_place_details, maps_distance_matrix, maps_elevation, maps_directions]
```

Then run:
```bash
hermes mcp test google-maps
/reload-mcp
```

## References

- GitHub: https://github.com/vicpeacock/google-maps-comprehensive-mcp
- Docker Hub: mcp/google-maps-comprehensive
- Google Maps Platform: https://developers.google.com/maps
- PulseMCP: https://www.pulsemcp.com/servers/modelcontextprotocol-google-maps
- Alternative (18 tools): https://github.com/cablate/mcp-google-map