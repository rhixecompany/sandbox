# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail
# make clean

# sudo rm -r static volumes
# sudo chown -R $USER:$USER .
docker compose -f docker-compose.production.yml build --pull

docker compose -f docker-compose.production.yml up -d

docker compose -f docker-compose.production.yml logs -f
