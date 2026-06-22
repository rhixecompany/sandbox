# Code Exemplars — rhixecompany-comics

## Frontend landing page

```tsx
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8">
      <h1 className="text-4xl font-bold tracking-tight">Rhixecompany Comics</h1>
      <p className="mt-4 text-lg text-muted-foreground">
        Coming soon — your comic discovery platform
      </p>
    </main>
  );
}
```

## App layout metadata

```tsx
export const metadata: Metadata = {
  title: "Rhixecompany Comics",
  description: "Discover, read, and track your favorite comics",
};
```

## Next.js remote image config

```ts
const nextConfig = {
  images: {
    remotePatterns: [{ protocol: "https", hostname: "**" }],
  },
};
```

## Django health endpoint

```py
from django.http import JsonResponse


def health(_request):
    return JsonResponse(
        {
            "service": "rhixecompany-comics",
            "status": "ok",
            "layer": "backend",
        }
    )
```

## Django settings pattern

```py
DATABASES = {"default": _database_config()}
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
```
