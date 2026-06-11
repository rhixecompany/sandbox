#!/bin/bash
# cleanup.sh - ComicWise Project Cleanup Wrapper
# Safely removes project artifacts, cache, and build directories
#
# Usage:
#   ./cleanup.sh                     # Prompt for confirmation before cleanup
#   ./cleanup.sh --force             # Skip confirmation
#   ./cleanup.sh --dry-run           # Show what would be cleaned without executing
#   ./cleanup.sh --dry-run --force   # Show what would be cleaned (no confirm)
#   ./cleanup.sh --verbose           # Show detailed cleanup information
#
# Exit codes:
#   0  Success
#   1  User cancelled cleanup
#   2  Cleanup failed

set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Parse arguments
FORCE=false
DRY_RUN=false
VERBOSE=false

for arg in "$@"; do
  case "$arg" in
    --force)
      FORCE=true
      ;;
    --dry-run)
      DRY_RUN=true
      ;;
    --verbose)
      VERBOSE=true
      ;;
    *)
      echo "Unknown argument: $arg"
      exit 2
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

print_info "ComicWise Project Cleanup Tool"
echo ""

# Show what will be cleaned
print_info "Cleanup targets:"
echo "  • .next/       (Next.js build cache)"
echo "  • .turbo/      (Turbo cache)"
echo "  • coverage/    (Test coverage)"
echo "  • dist/        (Build output)"
echo "  • build/       (Build artifacts)"
echo "  • .cache/      (General cache)"
echo "  • *.log        (Log files)"
echo "  • *.tmp        (Temporary files)"
echo "  • .DS_Store    (macOS metadata)"
echo ""

# Prompt for confirmation (unless --force)
if [ "$FORCE" = false ]; then
  print_warning "This will remove the above directories and files."
  read -p "Continue? (y/N) " -n 1 -r
  echo ""
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_info "Cleanup cancelled"
    exit 1
  fi
fi

# Build cleanup command
CLEANUP_CMD="pnpm cleanup:project"

if [ "$DRY_RUN" = true ]; then
  CLEANUP_CMD="$CLEANUP_CMD --dry-run"
fi

if [ "$VERBOSE" = true ]; then
  CLEANUP_CMD="$CLEANUP_CMD --verbose"
fi

CLEANUP_CMD="$CLEANUP_CMD --yes"

# Run cleanup
print_info "Running: $CLEANUP_CMD"
echo ""

if eval "$CLEANUP_CMD"; then
  print_success "Project cleanup complete!"
  print_info "Total disk space freed: [reported by cleanup script]"
  print_info "Tip: Run 'pnpm install' to reinstall dependencies if needed"
  exit 0
else
  print_error "Project cleanup failed!"
  exit 2
fi
