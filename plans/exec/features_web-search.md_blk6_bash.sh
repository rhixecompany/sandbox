#!/bin/bash
# Auto-extracted from: features/web-search.md
# Source block language: bash
docker cp ~/searxng/searxng/settings.yml searxng:/etc/searxng/settings.yml
docker restart searxng
