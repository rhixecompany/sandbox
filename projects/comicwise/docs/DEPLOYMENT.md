# ComicWise Production Deployment Guide

## Pre-Deployment Checklist

### Code Quality

```bash
✓ pnpm type-check          # 0 TypeScript errors
✓ pnpm lint:fix            # 0 ESLint errors
✓ pnpm test                # All unit tests pass
✓ pnpm build               # Production build succeeds
```

### Environment Configuration

- [ ] DATABASE_URL configured (PostgreSQL or Neon)
- [ ] AUTH_SECRET generated (32+ character random string)
- [ ] NEXTAUTH_URL set to production domain
- [ ] OAuth credentials configured (GitHub, etc.)
- [ ] ImageKit API keys configured (image optimization)
- [ ] Cloudinary API keys configured (user uploads)
- [ ] Redis connection string configured (caching)
- [ ] Sentry DSN configured (error tracking)
- [ ] Email SMTP configured (notifications)

### Database Setup

- [ ] PostgreSQL instance created and accessible
- [ ] All migrations applied (`pnpm db:push` or manual migrations)
- [ ] Schema validated against expected structure
- [ ] Indexes created for performance
- [ ] Backup strategy configured
- [ ] Replica/failover configured (optional)

### Security Verification

- [ ] HTTPS enabled on production domain
- [ ] SSL certificate valid and auto-renewing
- [ ] CORS configured appropriately
- [ ] Rate limiting enabled on APIs
- [ ] DDoS protection enabled (Cloudflare recommended)
- [ ] Security headers configured (CSP, X-Frame-Options, etc.)
- [ ] Sensitive environment variables not committed
- [ ] Database connection uses SSL/TLS

### Monitoring Setup

- [ ] Sentry error tracking configured
- [ ] New Relic or DataDog metrics configured (optional)
- [ ] CloudWatch or equivalent logging configured
- [ ] Performance monitoring enabled
- [ ] Uptime monitoring configured
- [ ] Alert notifications configured
- [ ] Incident response plan documented

---

## Deployment Methods

### Option 1: Vercel (Recommended for Next.js)

**Step 1: Connect Repository**

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel deploy --prod
```

**Step 2: Configure Environment Variables**

1. Go to Vercel Dashboard → Project Settings → Environment Variables
2. Add all required environment variables
3. Set for Production environment

**Step 3: Configure Database**

```bash
# Vercel integrates with Neon PostgreSQL
# Or use external PostgreSQL with connection pooling (PgBouncer)
```

**Step 4: Deploy**

```bash
# Automatic deployment on git push to main
git push origin main
```

### Option 2: Docker + Cloud (AWS, GCP, Azure)

**Step 1: Build Docker Image**

```bash
# Build locally
docker build -t comicwise:latest .

# Tag for registry
docker tag comicwise:latest myregistry/comicwise:latest

# Push to registry
docker push myregistry/comicwise:latest
```

**Step 2: Deploy to Kubernetes**

```yaml
# kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: comicwise
spec:
  replicas: 3
  selector:
    matchLabels:
      app: comicwise
  template:
    metadata:
      labels:
        app: comicwise
    spec:
      containers:
        - name: comicwise
          image: myregistry/comicwise:latest
          ports:
            - containerPort: 3000
          env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: comicwise-secrets
                  key: database-url
            - name: AUTH_SECRET
              valueFrom:
                secretKeyRef:
                  name: comicwise-secrets
                  key: auth-secret
          livenessProbe:
            httpGet:
              path: /api/health
              port: 3000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /api/health
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 5
```

**Step 3: Deploy with kubectl**

```bash
# Create secrets
kubectl create secret generic comicwise-secrets \
  --from-literal=database-url=$DATABASE_URL \
  --from-literal=auth-secret=$AUTH_SECRET

# Deploy
kubectl apply -f kubernetes/deployment.yaml
```

### Option 3: Docker Compose (Development/Small Scale)

**Step 1: Configure Environment**

```bash
cp .env.local.example .env.production
# Edit .env.production with production values
```

**Step 2: Start Services**

```bash
docker-compose -f docker-compose.yml up -d
```

**Step 3: Run Migrations**

```bash
docker-compose exec app pnpm db:push
```

---

## Post-Deployment Validation

### Health Checks

```bash
# Verify API is responding
curl https://api.yourdomain.com/api/health

# Check database connection
curl https://api.yourdomain.com/api/db-health

# Verify authentication
curl https://api.yourdomain.com/api/auth/session
```

### Performance Metrics

```bash
# Check Core Web Vitals
# Use: https://web.dev/measure/

# Performance Dashboard
# Vercel: https://vercel.com/dashboard/project/comicwise
# New Relic: https://one.newrelic.com/

# Error Tracking
# Sentry: https://sentry.io/organizations/yourorg/issues/
```

### Database Verification

```bash
# Connect to production database
psql $DATABASE_URL

# Check schema
\dt

# Check migrations status
SELECT name FROM schema_versions ORDER BY installed_on DESC;
```

---

## Monitoring & Alerts

### Sentry Configuration

```typescript
// src/instrumentation.ts
import * as Sentry from "@sentry/nextjs";

export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await Sentry.init({
      dsn: process.env.SENTRY_DSN,
      environment: process.env.NODE_ENV,
      integrations: [
        new Sentry.Integrations.Http({ tracing: true }),
        new Sentry.Integrations.OnUncaughtException()
      ],
      tracesSampleRate:
        process.env.NODE_ENV === "production" ? 0.1 : 1.0,
      release: process.env.VERCEL_GIT_COMMIT_SHA
    });
  }

  if (process.env.NEXT_RUNTIME === "edge") {
    await Sentry.init({
      dsn: process.env.SENTRY_DSN,
      environment: process.env.NODE_ENV,
      tracesSampleRate: 0.1
    });
  }
}
```

### Health Check Endpoint

```typescript
// src/app/api/health/route.ts
import { NextResponse } from "next/server";
import { db } from "@/database/db";

export async function GET() {
  try {
    // Test database connection
    await db.query.user.findFirst();

    return NextResponse.json({
      status: "healthy",
      timestamp: new Date().toISOString(),
      database: "connected"
    });
  } catch (error) {
    return NextResponse.json(
      {
        status: "unhealthy",
        timestamp: new Date().toISOString(),
        error:
          error instanceof Error ? error.message : "Unknown error"
      },
      { status: 503 }
    );
  }
}
```

### Alert Configuration

**Sentry Alerts:**

- Error rate > 5% in 1 hour → Slack notification
- Performance regression detected → Email notification
- New issue created → Slack notification

**Monitoring Alerts (New Relic/DataDog):**

- CPU usage > 80% → Page/SMS
- Memory usage > 85% → Page/Email
- Database connection pool exhausted → Critical alert
- API response time > 1s → Warning alert

---

## Rollback Procedure

### Vercel Rollback

```bash
# List previous deployments
vercel list

# Rollback to previous version
vercel rollback
```

### Docker Rollback

```bash
# Tag previous image
docker tag myregistry/comicwise:v1.0.0 myregistry/comicwise:latest

# Push
docker push myregistry/comicwise:latest

# Update Kubernetes
kubectl set image deployment/comicwise \
  comicwise=myregistry/comicwise:v1.0.0
```

### Database Rollback

```bash
# Create backup before deployment
pg_dump $DATABASE_URL > backup-$(date +%Y%m%d).sql

# Restore if needed
psql $DATABASE_URL < backup-20240306.sql
```

---

## Scaling Considerations

### Horizontal Scaling

- API is stateless (can run multiple instances)
- Use load balancer (ELB, ALB, or Nginx)
- Share database (PostgreSQL supports multiple connections)
- Use Redis for distributed caching

### Vertical Scaling

- Increase server resources (RAM, CPU)
- Enable database query optimization
- Implement caching layers
- Use CDN for static assets

### Database Optimization

```sql
-- Create indexes for common queries
CREATE INDEX idx_comic_slug ON comic(slug);
CREATE INDEX idx_chapter_comic_id ON chapter(comicId);
CREATE INDEX idx_bookmark_user_comic ON bookmark(userId, comicId);

-- Enable query analysis
EXPLAIN ANALYZE SELECT * FROM comic WHERE slug = 'one-piece';
```

---

## Maintenance Tasks

### Daily

- Monitor error rate in Sentry
- Check API health endpoint
- Review performance metrics

### Weekly

- Analyze slow query logs
- Check backup integrity
- Review user feedback

### Monthly

- Update dependencies (`pnpm update`)
- Security audit
- Performance tuning
- Cost analysis

### Quarterly

- Major version upgrades
- Architecture review
- Capacity planning
- Disaster recovery testing

---

## Troubleshooting

### Common Issues

**1. Database Connection Timeout**

```bash
# Check connection string
echo $DATABASE_URL

# Test connection
psql $DATABASE_URL -c "SELECT 1"

# If using Neon, check connection pooling config
```

**2. Out of Memory**

```bash
# Increase Node.js heap size
NODE_OPTIONS="--max-old-space-size=4096"

# Or in docker-compose.yml
environment:
  NODE_OPTIONS: "--max-old-space-size=4096"
```

**3. Slow Queries**

```sql
-- Find slow queries
SELECT query, mean_exec_time, calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```

**4. High Memory Usage**

```bash
# Check memory leaks
node --inspect server.js

# Use Chrome DevTools: chrome://inspect
```

---

## Success Criteria

✅ Application deployed and accessible ✅ All health checks passing ✅ Error rate < 1% ✅ Average response time < 500ms ✅ Database backups configured ✅ Monitoring and alerts active ✅ Incident response team ready ✅ Documentation updated
