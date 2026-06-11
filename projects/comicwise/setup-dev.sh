#!/bin/bash
# Development Environment Setup Script (Linux/macOS)
# Enhanced with: progress tracking, error handling, colored output
# Usage: bash setup-dev.sh [--skip-db] [--skip-seed]

set -e

# Colored output
BOLD="\033[1m"
GREEN="\033[32m"
YELLOW="\033[33m"
RED="\033[31m"
BLUE="\033[34m"
GRAY="\033[90m"
RESET="\033[0m"

# Logging functions
log_info() {
  echo -e "${BLUE}ℹ${RESET} $1"
}

log_success() {
  echo -e "${GREEN}✓${RESET} $1"
}

log_warn() {
  echo -e "${YELLOW}⚠${RESET} $1"
}

log_error() {
  echo -e "${RED}✗${RESET} $1"
}

log_header() {
  echo ""
  echo -e "${BOLD}${BLUE}━━━ $1 ━━━${RESET}"
  echo ""
}

# Parse arguments
SKIP_DB=false
SKIP_SEED=false
SKIP_INSTALL=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --skip-db) SKIP_DB=true; shift ;;
    --skip-seed) SKIP_SEED=true; shift ;;
    --skip-install) SKIP_INSTALL=true; shift ;;
    *) log_error "Unknown option: $1"; exit 1 ;;
  esac
done

# Main setup
main() {
  log_header "ComicWise Development Environment Setup"

  # Check prerequisites
  log_info "Checking prerequisites..."

  if ! command -v node &> /dev/null; then
    log_error "Node.js not found. Please install Node.js 18+"
    exit 1
  fi
  log_success "Node.js $(node -v)"

  if ! command -v pnpm &> /dev/null; then
    log_warn "pnpm not found. Installing globally..."
    npm install -g pnpm || {
      log_error "Failed to install pnpm"
      exit 1
    }
  fi
  log_success "pnpm $(pnpm -v)"

  # Install dependencies (optional)
  if [ "$SKIP_INSTALL" = false ]; then
    log_header "Installing Dependencies"
    if pnpm install --frozen-lockfile; then
      log_success "Dependencies installed successfully"
    else
      log_error "Failed to install dependencies"
      exit 1
    fi
  else
    log_info "Skipping dependency installation (--skip-install)"
  fi

  # Configure environment
  log_header "Environment Configuration"
  if [ ! -f .env.local ]; then
    log_info "Creating .env.local from template..."
    cp .env.local.example .env.local || {
      log_error "Failed to create .env.local"
      exit 1
    }

    log_warn "Please edit .env.local with your database credentials:"
    log_warn "  DATABASE_URL: PostgreSQL 14+ connection string"
    log_warn "  AUTH_SECRET: Run 'openssl rand -hex 32' to generate"
    log_warn "  AUTH_URL: http://localhost:3000 (local dev)"
  else
    log_success ".env.local already configured"
  fi

  # Type checking
  log_header "Type Safety Check"
  if pnpm type-check; then
    log_success "TypeScript validation passed"
  else
    log_error "TypeScript errors detected. Please fix above."
    exit 1
  fi

  # Database setup (optional)
  if [ "$SKIP_DB" = false ]; then
    log_header "Database Setup"
    if pnpm db:push; then
      log_success "Database schema applied"
    else
      log_error "Database setup failed"
      exit 1
    fi
  fi

  # Seeding (optional)
  if [ "$SKIP_SEED" = false ] && [ "$SKIP_DB" = false ]; then
    log_header "Database Seeding (Validation)"
    if pnpm seed:validate; then
      log_success "Seed validation passed. Proceeding with data insertion..."
      if pnpm seed:all; then
        log_success "Database seeded successfully"
      else
        log_error "Seeding failed"
        exit 1
      fi
    fi
  fi

  # Summary
  log_header "Setup Complete ✅"
  echo ""
  log_info "Development environment ready!"
  echo ""
  echo -e "${BOLD}Next steps:${RESET}"
  echo "  1. Start the dev server: ${BOLD}pnpm dev${RESET}"
  echo "  2. Open in browser: ${BOLD}http://localhost:3000${RESET}"
  echo ""
  echo -e "${GRAY}Useful commands:${RESET}"
  echo "  ${GRAY}pnpm type-check${RESET}    - Validate TypeScript"
  echo "  ${GRAY}pnpm lint:fix${RESET}       - Format and lint code"
  echo "  ${GRAY}pnpm test${RESET}           - Run unit tests"
  echo "  ${GRAY}pnpm test:ui${RESET}        - Run E2E tests"
  echo "  ${GRAY}pnpm db:studio${RESET}      - Open database viewer"
  echo ""
}

main "$@"
echo "========================"
echo ""
echo "Next steps:"
echo "1. Edit .env.local with database credentials"
echo "2. Run: pnpm db:push (to apply migrations)"
echo "3. Run: pnpm dev (to start development server)"
echo ""
