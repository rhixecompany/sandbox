# Tailscale API v2 Reference

## Authentication
All API requests require `Authorization: Bearer <tskey-api-...>` header.
API keys created from: https://login.tailscale.com/admin/settings/keys

## Tailnet Identifier
- **Personal accounts**: user's email (e.g. `alexanderrhixe30@gmail.com`)
- **Business accounts**: `organization.ts.net`
Find it from device MagicDNS name (e.g. `host.tailf146e1.ts.net` → tailnet=`tailf146e1.ts.net`)

## Key Types

| Prefix | Purpose | Created via |
|--------|---------|------------|
| `tskey-api-` | API key — scripted access to API v2 | Admin console |
| `tskey-auth-` | Auth key — join a machine to the tailnet | Admin console or API |

## Common API Response Fields (Device)

```json
{
  "addresses": ["100.x.x.x", "fd7a:..."],
  "id": "nnnn...",           // numeric device ID
  "nodeId": "n3t...CNTRL",   // node identifier
  "user": "user@email.com",
  "name": "host.tailnet.ts.net",
  "hostname": "host",
  "clientVersion": "1.98.9",
  "updateAvailable": false,
  "os": "windows",
  "connectedToControl": true,  // online/offline
  "lastSeen": "2026-07-24T19:17:16Z",
  "expires": "2027-01-20T19:14:59Z",
  "keyExpiryDisabled": false,
  "authorized": true
}
```

## Key Endpoint Details

**List devices:** `GET /api/v2/tailnet/{tailnet}/devices`
Response: `{"devices": [...]}`

**Get ACL:** `GET /api/v2/tailnet/{tailnet}/acl`
Returns current ACL JSON (or default allow-all for personal tailnets).

**Apply ACL:** `POST /api/v2/tailnet/{tailnet}/acl`
Body: full ACL JSON (`{"acls": [...], "tagOwners": {...}}`)
Response: `{"warnings": [...]}` — empty array means clean apply.

**List auth keys:** `GET /api/v2/tailnet/{tailnet}/keys`
Response: `{"keys": [{"id": "k...", "expires": "...", "tags": [...]}]}`

**Disable key expiry:** `PATCH /api/v2/device/{deviceId}/key`
Body: `{"keyExpiryDisabled": true}`
Device ID is the numeric `id` field from the devices list, not `nodeId`.
