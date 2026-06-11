#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail

echo
# make clean

# sudo rm -r static volumes
# sudo chown -R $USER:$USER .
docker compose -f docker-compose.local.yml build --pull

docker compose -f docker-compose.local.yml up -d

docker compose -f docker-compose.local.yml logs -f
