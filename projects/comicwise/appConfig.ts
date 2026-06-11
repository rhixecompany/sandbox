/**
 * Application Configuration
 * @description Centralized configuration using environment variables
 * Provides type-safe access to all app configuration
 * Contains Zod schema validation
 */

import { z } from "zod";

/**
 * Environment variable schema definition
 * Validates all 60+ environment variables on app load
 * Uses defaults for optional fields to allow testing without full config
 */
const envSchema = z.object({
  // ========== DATABASE ==========
  DATABASE_URL: z.string().default("postgresql://localhost:5432/comicwise"),
  NEON_DATABASE_URL: z.string().optional(),

  // ========== AUTH ==========
  AUTH_SECRET: z.string().default("dev-secret-32-characters-minimum-ok"),
  AUTH_TRUST_HOST: z
    .string()
    .transform((v) => v === "true")
    .optional(),
  AUTH_REDIRECT_PROXY_URL: z.string().url().optional(),

  // ========== PROVIDERS ==========
  GOOGLE_CLIENT_ID: z.string().default(""),
  GOOGLE_CLIENT_SECRET: z.string().default(""),
  GITHUB_CLIENT_ID: z.string().default(""),
  GITHUB_CLIENT_SECRET: z.string().default(""),
  KEYCLOAK_CLIENT_ID: z.string().optional(),
  KEYCLOAK_CLIENT_SECRET: z.string().optional(),
  KEYCLOAK_ISSUER: z.string().optional(),

  // ========== EMAIL ==========
  RESEND_API_KEY: z.string().optional(),
  EMAIL_FROM: z.string().email().default("test@example.com"),
  NODEMAILER_HOST: z.string().optional(),
  NODEMAILER_PORT: z.string().transform(Number).optional(),
  NODEMAILER_USER: z.string().optional(),
  NODEMAILER_PASS: z.string().optional(),

  // ========== REDIS ==========
  REDIS_HOST: z.string().default("localhost"),
  REDIS_PORT: z.coerce.number().default(6379),
  REDIS_PASSWORD: z.string().optional(),
  UPSTASH_REDIS_REST_URL: z.string().url().optional(),
  UPSTASH_REDIS_REST_TOKEN: z.string().optional(),

  // ========== IMAGE SERVICES ==========
  IMAGEKIT_PUBLIC_KEY: z.string().optional(),
  IMAGEKIT_PRIVATE_KEY: z.string().optional(),
  IMAGEKIT_URL_ENDPOINT: z.string().url().optional(),
  CLOUDINARY_CLOUD_NAME: z.string().optional(),
  CLOUDINARY_API_KEY: z.string().optional(),
  CLOUDINARY_API_SECRET: z.string().optional(),

  // ========== STORAGE ==========
  AWS_ACCESS_KEY_ID: z.string().optional(),
  AWS_SECRET_ACCESS_KEY: z.string().optional(),
  AWS_REGION: z.string().default("us-east-1"),
  AWS_S3_BUCKET: z.string().optional(),

  // ========== MONITORING ==========
  SENTRY_DSN: z.string().optional(),
  SENTRY_AUTH_TOKEN: z.string().optional(),
  SENTRY_ENV: z.enum(["development", "staging", "production", "test"]).default("development"),
  POSTHOG_API_KEY: z.string().optional(),
  POSTHOG_HOST: z.string().optional(),

  // ========== PAYMENT ==========
  STRIPE_SECRET_KEY: z.string().optional(),
  STRIPE_PUBLISHABLE_KEY: z.string().optional(),
  STRIPE_WEBHOOK_SECRET: z.string().optional(),

  // ========== SUPABASE ==========
  SUPABASE_URL: z.string().url().optional(),
  SUPABASE_ANON_KEY: z.string().optional(),
  SUPABASE_SERVICE_KEY: z.string().optional(),

  // ========== API ==========
  NEXT_PUBLIC_API_URL: z.string().optional().default("http://localhost:3000"),
  API_BASE_URL: z.string().url().optional(),

  // ========== DEVELOPMENT ==========
  CUSTOM_PASSWORD: z.string().default("password123"),
  NODE_ENV: z.enum(["development", "staging", "production", "test"]).default("development"),
  ENVIRONMENT: z.enum(["development", "staging", "production", "test"]).default("development"),
  CI: z.string().optional(),

  // ========== FEATURES ==========
  ENABLE_SEEDING: z
    .string()
    .transform((v) => v === "true")
    .pipe(z.boolean())
    .default(false),
  ENABLE_ANALYTICS: z
    .string()
    .transform((v) => v === "true")
    .pipe(z.boolean())
    .default(true),
  ENABLE_ERROR_TRACKING: z
    .string()
    .transform((v) => v === "true")
    .pipe(z.boolean())
    .default(true),

  // ========== LOGGING ==========
  LOG_LEVEL: z.enum(["debug", "info", "warn", "error"]).default("info"),
  DEBUG: z.string().optional(),

  // ========== SECURITY ==========
  ALLOWED_ORIGINS: z.string().default("http://localhost:3000"),
  RATE_LIMIT_WINDOW_MS: z.coerce.number().default(900000),
  RATE_LIMIT_MAX_REQUESTS: z.coerce.number().default(100),

  // ========== JWT ==========
  JWT_SECRET: z.string().default("jwt-secret-32-characters-minimum-ok"),
  JWT_EXPIRY: z
    .string()
    .regex(/^\d+[smhd]$/, "JWT_EXPIRY must be a duration format like '7d', '30m', '3600s', '2h'")
    .default("7d"),
  REFRESH_TOKEN_EXPIRY: z
    .string()
    .regex(/^\d+[smhd]$/, "REFRESH_TOKEN_EXPIRY must be a duration format like '30d', '7d', '3600s', '2h'")
    .default("30d"),

  // ========== FILE UPLOAD ==========
  MAX_FILE_SIZE: z.coerce.number().default(52428800),
  ALLOWED_FILE_TYPES: z.string().default(".jpg,.jpeg,.png,.gif,.webp,.pdf"),

  // ========== SEEDING ==========
  SEED_API_KEY: z.string().optional(),
  SEED_DOWNLOAD_CONCURRENCY: z.coerce.number().min(1).max(20).default(5),
  SEED_MAX_IMAGE_SIZE_BYTES: z.coerce.number().min(1048576).max(104857600).default(5242880),
  SEED_BATCH_SIZE: z.coerce.number().min(10).max(1000).default(100),
  SEED_TIMEOUT_MS: z.coerce.number().min(1000).max(300000).default(30000),

  // ========== CACHE ==========
  CACHE_TTL: z.coerce.number().default(3600),
  CACHE_REDIS_TTL: z.coerce.number().default(86400),
});

/**
 * Validated environment variables
 * Safe to use throughout the application
 */
let env: null | z.infer<typeof envSchema> = null;

/**
 * Get validated env object (lazy loaded)
 * @returns {z.infer<typeof envSchema>} Validated environment variables
 * @throws {Error} If validation fails
 */
export function getEnv(): z.infer<typeof envSchema> {
  if (env) return env;

  try {
    env = envSchema.parse(process.env);
    return env;
  } catch (error) {
    if (error instanceof z.ZodError) {
      const errors = error.issues.map((e) => `${e.path.join(".")}: ${e.message}`).join("\n");
      const err = new Error(`Environment variable validation failed:\n${errors}`);
      err.cause = error;
      throw err;
    }
    throw error;
  }
}

/**
 * Get app configuration object
 * All values are validated by Zod schema above
 */
export function getAppConfig() {
  const envVars = getEnv();

  return {
    // Database
    database: {
      url: envVars.DATABASE_URL,
      neonUrl: envVars.NEON_DATABASE_URL,
    },

    // Authentication
    auth: {
      secret: envVars.AUTH_SECRET,
      jwtSecret: envVars.JWT_SECRET,
      trustHost: envVars.AUTH_TRUST_HOST,
      redirectProxyUrl: envVars.AUTH_REDIRECT_PROXY_URL,
    },

    // Providers
    providers: {
      google: {
        clientId: envVars.GOOGLE_CLIENT_ID,
        clientSecret: envVars.GOOGLE_CLIENT_SECRET,
      },
      github: {
        clientId: envVars.GITHUB_CLIENT_ID,
        clientSecret: envVars.GITHUB_CLIENT_SECRET,
      },
    },

    // Email
    email: {
      resendApiKey: envVars.RESEND_API_KEY,
      from: envVars.EMAIL_FROM,
      nodemailer: {
        host: envVars.NODEMAILER_HOST,
        port: envVars.NODEMAILER_PORT,
        user: envVars.NODEMAILER_USER,
        pass: envVars.NODEMAILER_PASS,
      },
    },

    // Redis/Caching
    redis: {
      host: envVars.REDIS_HOST,
      port: envVars.REDIS_PORT,
      password: envVars.REDIS_PASSWORD,
      upstash: {
        url: envVars.UPSTASH_REDIS_REST_URL,
        token: envVars.UPSTASH_REDIS_REST_TOKEN,
      },
    },

    // Image Services
    imageKit: {
      publicKey: envVars.IMAGEKIT_PUBLIC_KEY,
      privateKey: envVars.IMAGEKIT_PRIVATE_KEY,
      urlEndpoint: envVars.IMAGEKIT_URL_ENDPOINT,
    },

    cloudinary: {
      cloudName: envVars.CLOUDINARY_CLOUD_NAME,
      apiKey: envVars.CLOUDINARY_API_KEY,
      apiSecret: envVars.CLOUDINARY_API_SECRET,
    },

    // Application
    app: {
      name: "ComicWise",
      url: envVars.NEXT_PUBLIC_API_URL || "http://localhost:3000",
      environment: envVars.NODE_ENV || "development",
      debug: envVars.DEBUG === "true",
    },

    // Feature Flags
    features: {
      seeding: envVars.ENABLE_SEEDING,
      analytics: envVars.ENABLE_ANALYTICS,
      errorTracking: envVars.ENABLE_ERROR_TRACKING,
    },

    // Seeding
    seeding: {
      defaultPassword: envVars.CUSTOM_PASSWORD,
    },

    // JWT
    jwt: {
      secret: envVars.JWT_SECRET,
      expiry: envVars.JWT_EXPIRY,
      refreshTokenExpiry: envVars.REFRESH_TOKEN_EXPIRY,
    },

    // Sentry
    sentry: {
      dsn: envVars.SENTRY_DSN,
      enabled: !!envVars.SENTRY_DSN,
    },
  } as const;
}

// Export for convenience
export const appConfig = getAppConfig();

export default appConfig;

// Re-export individual typed env vars for convenience
export const {
  DATABASE_URL,
  AUTH_SECRET,
  AUTH_TRUST_HOST,
  GOOGLE_CLIENT_ID,
  GOOGLE_CLIENT_SECRET,
  GITHUB_CLIENT_ID,
  GITHUB_CLIENT_SECRET,
  RESEND_API_KEY,
  EMAIL_FROM,
  REDIS_HOST,
  REDIS_PORT,
  REDIS_PASSWORD,
  UPSTASH_REDIS_REST_URL,
  UPSTASH_REDIS_REST_TOKEN,
  IMAGEKIT_PUBLIC_KEY,
  IMAGEKIT_PRIVATE_KEY,
  IMAGEKIT_URL_ENDPOINT,
  CLOUDINARY_CLOUD_NAME,
  SENTRY_DSN,
  STRIPE_SECRET_KEY,
  NEXT_PUBLIC_API_URL,
  NODE_ENV,
  CUSTOM_PASSWORD,
  ENABLE_SEEDING,
  ENABLE_ANALYTICS,
  SEED_API_KEY,
  SEED_DOWNLOAD_CONCURRENCY,
  SEED_MAX_IMAGE_SIZE_BYTES,
  SEED_BATCH_SIZE,
  SEED_TIMEOUT_MS,
} = getEnv();
