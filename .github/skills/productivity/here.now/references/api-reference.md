# here.now API Reference

## Authentication Endpoints

### Request Sign-in Code
```bash
curl -sS https://here.now/api/auth/agent/request-code   -H "content-type: application/json"   -d '{"email": "user@example.com"}'
```

### Verify Code & Get API Key
```bash
curl -sS https://here.now/api/auth/agent/verify-code   -H "content-type: application/json"   -d '{"email":"user@example.com","code":"ABCD-2345"}'
```

Response: `{"apiKey": "hk_..."}`

## Site Publishing API

### Create Site (Anonymous)
```bash
curl -sS https://here.now/api/sites   -H "content-type: application/zip"   --data-binary @site.zip
```

Response: `{"slug": "abc123", "claimUrl": "https://here.now/claim?slug=abc123&token=xyz", "expiresAt": "..."}`

### Create Site (Authenticated)
```bash
curl -sS https://here.now/api/sites   -H "Authorization: Bearer YOUR_API_KEY"   -H "content-type: application/zip"   --data-binary @site.zip
```

### Update Site
```bash
curl -sS https://here.now/api/sites/{slug}   -H "Authorization: Bearer YOUR_API_KEY"   -H "content-type: application/zip"   --data-binary @site.zip
```

### List Sites
```bash
curl -sS https://here.now/api/sites   -H "Authorization: Bearer YOUR_API_KEY"
```

## Drive API

### List Drive Contents
```bash
curl -sS "https://here.now/api/drives/{driveId}/files?pathPrefix=notes/"   -H "Authorization: Bearer DRIVE_TOKEN"
```

### Upload File
```bash
curl -sS -X PUT "https://here.now/api/drives/{driveId}/files/notes/today.md"   -H "Authorization: Bearer DRIVE_TOKEN"   -H "content-type: text/markdown"   --data-binary @notes/today.md
```

### Download File
```bash
curl -sS "https://here.now/api/drives/{driveId}/files/notes/today.md"   -H "Authorization: Bearer DRIVE_TOKEN"   -o today.md
```

### Create Scoped Share Token
```bash
curl -sS -X POST https://here.now/api/drives/{driveId}/shares   -H "Authorization: Bearer YOUR_API_KEY"   -H "content-type: application/json"   -d '{"pathPrefix": "notes/", "perms": "write", "ttl": "7d"}'
```

Returns share object with `token` and `apiBase`.

## Webhook Events

Subscribe to events for automated workflows:
- `site.published` — Site created/updated
- `site.deleted` — Site deleted
- `drive.file.uploaded` — File uploaded to Drive
- `drive.file.deleted` — File deleted from Drive

```bash
curl -sS -X POST https://here.now/api/webhooks   -H "Authorization: Bearer YOUR_API_KEY"   -d '{"url": "https://your-server.com/webhook", "events": ["site.published"]}'
```

## Limits & Quotas

| Resource | Anonymous | Authenticated |
|----------|-----------|---------------|
| Sites | 10 | Unlimited |
| Site size | 50 MB | 500 MB |
| Site TTL | 24 hours | Permanent |
| Drive storage | 100 MB | 10 GB |
| API requests/min | 60 | 300 |

## Error Codes

| Code | Meaning |
|------|---------|
| 401 | Invalid/missing API key |
| 403 | Insufficient permissions |
| 404 | Site/Drive not found |
| 413 | Payload too large |
| 429 | Rate limited |
| 500 | Server error |

Always check `error.code` and `error.message` in error responses.
