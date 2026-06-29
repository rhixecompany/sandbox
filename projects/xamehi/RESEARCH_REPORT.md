# RESEARCH_REPORT.md

## Project: xamehi

**Type:** Full-stack cryptocurrency dashboard (three-service architecture)
**Tech Stack:** React 18 (CRA), Express.js (Node.js), Django 4.0 (Python DRF), PostgreSQL (via Django ORM), RapidAPI (Alpha Vantage + Crypto News)
**Status:** Stale (active Express only; Django scaffolded but not wired)

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| CoinGecko API | https://www.coingecko.com/en/api | Cryptocurrency data API alternative |
| Cryptocurrency Dashboard (GitHub) | https://github.com/topics/cryptocurrency-dashboard | Open-source crypto dashboard examples |

## Key Findings

### Dual-Backend Architecture (2026)
- Express.js acts as API gateway proxy to external RapidAPI services — standard pattern for key abstraction
- Django is scaffolded but not wired into request lifecycle — common starting point for gradual migration
- React 18 CRA patterns remain widely used for SPAs despite Next.js dominance, especially for API-proxy architectures

### Express.js API Proxy Pattern
- Thin proxy pattern keeps API keys server-side, never exposed to client bundle
- Hardcoded port 8000 in index.js conflicts with Django's default port — AGENTS.md flags this
- Missing error responses: `.catch()` only logs to console, no user-facing error state

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Express.js Routing | https://expressjs.com/en/guide/routing.html | Official Docs |
| Django 4.0 | https://docs.djangoproject.com/en/4.0/ | Framework Docs |
| React 18 | https://react.dev/blog/2022/03/29/react-v18 | Release Notes |
| RapidAPI | https://docs.rapidapi.com/docs | API Marketplace Docs |

## Best Practices

1. **Environment variables for API keys** — `REACT_APP_RAPID_API_KEY` keeps keys server-side
2. **Axios for HTTP** — Standard choice for React ↔ Express communication
3. **Functional components with hooks** — Modern React patterns (useState, useEffect)
4. **Dual-backend separation** — Clear separation of concerns (Express = API proxy, Django = future data layer)
5. **Health check endpoint** — Express `/` route enables basic uptime monitoring

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Port conflict (Express+Django both on 8000) | Can't run both locally | Move Express to 5000, Django stays on 8000 |
| No error UI on network failures | Silent failures confuse users | Add error state + user-facing message |
| Hardcoded SECRET_KEY in Django settings | Security vulnerability | Move to environment variable |
| Console.log instrumentation in production | Bloated logs, info leakage | Strip or gate behind DEBUG env var |

## Performance

1. **CRA development server** proxies API calls with hot-reload for fast iteration
2. **Express thin proxy** adds minimal latency (~5ms) vs direct client→API calls
3. **React functional components** with hooks avoid class component overhead
4. **No image/assets optimization** — CRA default Webpack config handles basic minification

## Security

1. **Extract Django SECRET_KEY** to environment variable — currently hardcoded in settings.py
2. **Restrict CORS** in Express production — currently wildcard `cors()` with no origin restrictions
3. **Add error responses to failed API calls** — `.catch()` currently logs only, client gets no feedback
4. **Rate limit RapidAPI calls** to avoid quota exhaustion and unexpected billing
5. **Remove console.log** instrumentation before production deployment

## Related Projects (in workspace)

- **xamehi.tv** — Django DRF + React 17, shares DRF patterns and deployment model
- **ecom** — Django DRF + React 18 + PayPal, similar dual-stack (DRF backend + React frontend)
- **rhixecompany-comics** — Django + Next.js 16, parallels the dual-backend architecture

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Express.js Docs | https://expressjs.com | Node.js web framework |
| Django 4.0 Docs | https://docs.djangoproject.com/en/4.0/ | Python web framework |
| React 18 Docs | https://react.dev | UI library |
| RapidAPI | https://docs.rapidapi.com | API marketplace |
