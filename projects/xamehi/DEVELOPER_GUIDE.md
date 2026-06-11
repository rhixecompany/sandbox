# Developer Guide — Xamehi

This guide covers setup, development workflow, and contribution process for Xamehi.

## Prerequisites

- Node.js 16+ (recommended: latest LTS)
- npm or yarn
- Git
- RapidAPI key (for Alpha Vantage and Crypto News APIs)

## Project Overview

Xamehi is a full-stack web application combining:
- **Frontend**: React 18 (Create React App)
- **Backend**: Express.js REST API
- **External APIs**: Alpha Vantage (currency), Crypto News Live

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rhixecompany/xamehi.git
cd xamehi
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
REACT_APP_RAPID_API_KEY=your_rapidapi_key_here
```

### 4. Start Development Servers

You need to run two servers simultaneously:

**Terminal 1 — Backend API:**
```bash
npm run server
# Starts nodemon on port 8000
```

**Terminal 2 — React Frontend:**
```bash
npm start
# Starts React dev server (default port 3000)
```

## Project Structure

```
xamehi/
├── index.js          # Express.js backend entry point
├── package.json      # Dependencies and scripts
├── src/              # React frontend source
│   ├── index.js      # React entry point
│   ├── components/   # UI components
│   └── services/     # API service calls
├── public/           # Static assets
└── manage.py         # Django management script (future integration)
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/convert?from_currency=USD&to_currency=EUR` | GET | Currency exchange rate |
| `/news` | GET | Latest crypto news |

## Available Scripts

| Command | Description |
|---------|-------------|
| `npm start` | Start React dev server |
| `npm run server` | Start Express API with nodemon |
| `npm run build` | Build React for production |
| `npm test` | Run React tests |
| `npm run eject` | Eject from CRA (irreversible) |

## Testing

```bash
npm test
```

Tests use Jest and React Testing Library. Write tests for new components and API integrations.

## Code Style

- ESLint configured with `react-app` preset
- Follow existing patterns for component structure
- Use functional components with hooks

## Contribution Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and test locally
4. Commit with Conventional Commits format
5. Push and open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Deployment

- **Frontend**: Build with `npm run build`, deploy static files to Netlify/Vercel/S3
- **Backend**: Deploy Express server to Heroku/Railway/Render
- Set `REACT_APP_RAPID_API_KEY` environment variable in production
