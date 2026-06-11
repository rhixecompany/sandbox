#!/bin/bash
# dev.sh - ComicWise Development Environment Launcher
# Checks prerequisites, verifies database connectivity, launches dev server + browser
#
# Usage:
#   ./dev.sh                    # Start dev server and open browser
#   ./dev.sh --no-browser       # Start dev server only
#   ./dev.sh --skip-db-check    # Skip database connectivity check
#
# Exit codes:
#   0  Success
#   1  Prerequisite check failed
#   2  Database connectivity check failed
#   3  .env.local missing

set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Parse arguments
NO_BROWSER=false
SKIP_DB_CHECK=false

for arg in "$@"; do
  case "$arg" in
    --no-browser)
      NO_BROWSER=true
      ;;
    --skip-db-check)
      SKIP_DB_CHECK=true
      ;;
    *)
      echo "Unknown argument: $arg"
      exit 1
      ;;
  esac
done

# Function to print colored output
print_info() {
  echo -e "${CYAN}ℹ️  $1${NC}"
}

print_success() {
  echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
  echo -e "${RED}✗ $1${NC}"
}

print_warning() {
  echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check Node.js version (18+)
print_info "Checking Node.js version..."
NODE_VERSION=$(node --version | sed 's/v//' | cut -d. -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
  print_error "Node.js 18 or higher is required. Current: $(node --version)"
  exit 1
fi
print_success "Node.js v$(node --version | sed 's/v//')"

# Check pnpm version (8+)
print_info "Checking pnpm version..."
if ! command -v pnpm &> /dev/null; then
  print_error "pnpm is not installed. Install with: npm install -g pnpm"
  exit 1
fi
PNPM_VERSION=$(pnpm --version | cut -d. -f1)
if [ "$PNPM_VERSION" -lt 8 ]; then
  print_error "pnpm 8 or higher is required. Current: $(pnpm --version)"
  exit 1
fi
print_success "pnpm $(pnpm --version)"

# Check .env.local exists
print_info "Checking .env.local..."
if [ ! -f ".env.local" ]; then
  print_warning ".env.local not found"
  if [ -f ".env.local.example" ]; then
    print_info "Creating .env.local from .env.local.example..."
    cp .env.local.example .env.local
    print_success "Created .env.local"
    print_warning "Please update .env.local with your actual environment values"
  else
    print_error ".env.local.example not found either. Cannot proceed."
    exit 3
  fi
fi
print_success ".env.local exists"

# Check database connectivity (unless skipped)
if [ "$SKIP_DB_CHECK" = false ]; then
  print_info "Checking database connectivity..."
  if ! pnpm health:db --turbo &> /dev/null; then
    print_warning "Database connectivity check failed"
    print_warning "You may need to: pnpm db:push"
    print_info "Continuing with dev server startup..."
  else
    print_success "Database connected"
  fi
fi

# Clear build artifacts
print_info "Clearing build artifacts..."
pnpm clean &> /dev/null
print_success "Artifacts cleared"

# Start dev server
print_info "Starting development server..."
print_info "Dev server will be available at: ${CYAN}http://localhost:3000${NC}"
echo ""

# Start pnpm dev in the background
pnpm dev 2>&1 &
DEV_PID=$!

# Wait for dev server to be ready
print_info "Waiting for development server to start..."
RETRY_COUNT=0
MAX_RETRIES=30

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
  if curl -s http://localhost:3000 > /dev/null 2>&1; then
    print_success "Development server is ready!"
    break
  fi
  RETRY_COUNT=$((RETRY_COUNT + 1))
  sleep 1
done

if [ $RETRY_COUNT -eq $MAX_RETRIES ]; then
  print_warning "Development server took longer than expected to start"
fi

echo ""

# Open browser (unless --no-browser)
if [ "$NO_BROWSER" = false ]; then
  print_info "Opening browser..."

  # Detect OS and open browser accordingly
  if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open http://localhost:3000
  elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command -v xdg-open &> /dev/null; then
      xdg-open http://localhost:3000
    elif command -v gnome-open &> /dev/null; then
      gnome-open http://localhost:3000
    else
      print_warning "Could not open browser automatically"
    fi
  fi

  print_success "Browser should open shortly"
fi

echo ""
print_success "Development environment ready!"
print_info "Stop the server with: Ctrl+C"
print_info "View logs: pnpm health:all"
echo ""

# Wait for interrupt signal
wait $DEV_PID
