# Production Dockerfile for ComicWise
# Multi-stage build with aggressive caching and minimal final image

# ─────────────────────────────────────
# Stage 1: Base - Install pnpm globally
# ─────────────────────────────────────
FROM node:22-alpine AS base
RUN npm install -g pnpm@8 && npm cache clean --force
WORKDIR /app

# ─────────────────────────────────────
# Stage 2: Builder - Full install & build
# ─────────────────────────────────────
FROM base AS builder
# Copy dependency files first for better caching
COPY pnpm-lock.yaml pnpm-workspace.yaml package.json ./
RUN pnpm install
# Copy source code
COPY . .
RUN pnpm build

# ─────────────────────────────────────
# Stage 3: Runtime - Minimal production image
# ─────────────────────────────────────
FROM node:22-alpine

# Install only necessary runtime tools
RUN apk add --no-cache dumb-init

# Create non-root user for security
RUN addgroup -g 1001 -S nodejs && adduser -S nextjs -u 1001

WORKDIR /app

# Copy package.json for reference
COPY --chown=nextjs:nodejs package.json ./

# Copy built Next.js app from builder stage
COPY --from=builder --chown=nextjs:nodejs /app/.next ./.next
COPY --from=builder --chown=nextjs:nodejs /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/node_modules ./node_modules

# Set non-root user
USER nextjs

EXPOSE 3000

# Health check using Node.js instead of curl
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/api/health', (r) => {if (r.statusCode !== 200) throw new Error(r.statusCode)})"

ENTRYPOINT ["dumb-init", "--"]
CMD ["node_modules/.bin/next", "start"]
