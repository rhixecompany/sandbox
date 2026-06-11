import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // React Compiler for automatic optimization
  reactCompiler: true,

  experimental: {
    // mcpServer: true,
    // Turbopack caching for faster dev builds
    turbopackFileSystemCacheForDev: true,
    turbopackFileSystemCacheForBuild: false,

    // Type-safe environment variables
    typedEnv: true,
    // Optimized caching strategy
    staleTimes: {
      dynamic: 30,
      static: 180,
    },

    // Static generation optimization
    staticGenerationRetryCount: 3,
    staticGenerationMaxConcurrency: 16,
    staticGenerationMinPagesPerWorker: 25,

    // Package import optimization
    optimizePackageImports: [
      "@radix-ui/react-icons",
      "@radix-ui/react-avatar",
      "@radix-ui/react-dialog",
      "@radix-ui/react-dropdown-menu",
      "@radix-ui/react-select",
      "@radix-ui/react-tabs",
      "@radix-ui/react-accordion",
      "@radix-ui/react-popover",
      "@radix-ui/react-tooltip",
      "@radix-ui/react-label",
      "@radix-ui/react-switch",
      "@radix-ui/react-checkbox",
      "@radix-ui/react-slider",
      "@radix-ui/react-separator",
      "lucide-react",
      "@tabler/icons-react",
      "framer-motion",
      "recharts",
      "date-fns",
    ],

    // Server Actions configuration
    serverActions: {
      bodySizeLimit: "10mb",
      allowedOrigins:
        process.env.NODE_ENV === "production"
          ? ["comicwise.vercel.app", "comicwise.app", "www.comicwise.app"]
          : ["localhost:3000", "localhost:3001"],
    },
  },
  // External packages for server-side
  serverExternalPackages: ["postgres", "libsql/client", "bcryptjs", "sharp", "nodemailer"],

  // Cache React Server Components
  // Component caching is enabled for better performance. If you temporarily disabled
  // this during debugging, re-enable it once dynamic route flags are removed or
  // pages are hardened to avoid runtime Date usage during prerender.
  cacheComponents: true,
  // Image optimization
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "avatars.githubusercontent.com" },
      { protocol: "https", hostname: "lh3.googleusercontent.com" },
      { protocol: "https", hostname: "placehold.co" },
      { protocol: "https", hostname: "m.media-amazon.com" },
      { protocol: "https", hostname: "ik.imagekit.io" },
      { protocol: "https", hostname: "gg.asuracomic.net" },
      { protocol: "https", hostname: "res.cloudinary.com" },
      { protocol: "https", hostname: "localhost" },
      { protocol: "http", hostname: "localhost" },
    ],
    formats: ["image/avif", "image/webp"],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
    minimumCacheTTL: 31536000,
    dangerouslyAllowSVG: true,
    contentDispositionType: "attachment",
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },

  // Enhanced logging
  logging: {
    fetches: {
      fullUrl: true,
    },
  },

  // Type-safe routing
  typedRoutes: true,

  // TypeScript configuration
  typescript: {
    ignoreBuildErrors: false,
  },

  // Development indicators
  devIndicators: {
    position: "bottom-right",
  },

  // Bundle optimization
  bundlePagesRouterDependencies: true,

  // Security headers
  poweredByHeader: false,
  compress: true,

  // Security headers
  headers: async () => [
    {
      source: "/:path*",
      headers: [
        {
          key: "X-DNS-Prefetch-Control",
          value: "on",
        },
        {
          key: "Strict-Transport-Security",
          value: "max-age=63072000; includeSubDomains; preload",
        },
        {
          key: "X-Frame-Options",
          value: "SAMEORIGIN",
        },
        {
          key: "X-Content-Type-Options",
          value: "nosniff",
        },
        {
          key: "Referrer-Policy",
          value: "origin-when-cross-origin",
        },
        {
          key: "X-XSS-Protection",
          value: "1; mode=block",
        },
        {
          key: "Permissions-Policy",
          value: "camera=(), microphone=(), geolocation=()",
        },
      ],
    },
  ],
  webpack: (config: Record<string, unknown>, { isServer }: { isServer: boolean }) => {
    if (!isServer) {
      const resolveConfig = config["resolve"] as Record<string, unknown>;
      resolveConfig["fallback"] = {
        ...(resolveConfig["fallback"] as Record<string, boolean>),
        fs: false,
        net: false,
        tls: false,
        crypto: false,
        stream: false,
        url: false,
        zlib: false,
        http: false,
        https: false,
        assert: false,
        os: false,
        path: false,
      };
    }
    return config;
  },
};

export default nextConfig;
