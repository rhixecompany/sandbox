# Authentication Options

> Extracted from `typespec-create-api-plugin.prompt.md`.

## Authentication Options

Choose based on API requirements:

1. **No Authentication** (Public APIs)

   ```typescript
   // No @useAuth decorator needed
   ```

2. **API Key**

   ```typescript
   @useAuth(ApiKeyAuth<ApiKeyLocation.header, "X-API-Key">)
   ```

3. **OAuth2**

   ```typescript
   @useAuth(OAuth2Auth<[{
     type: OAuth2FlowType.authorizationCode;
     authorizationUrl: "https://oauth.example.com/authorize";
     tokenUrl: "https://oauth.example.com/token";
     refreshUrl: "https://oauth.example.com/token";
     scopes: ["read", "write"];
   }]>)
   ```

4. **Registered Auth Reference**

   ```typescript
   @useAuth(Auth)

   @authReferenceId("registration-id-here")
   model Auth is ApiKeyAuth<ApiKeyLocation.header, "X-API-Key">
   ```
