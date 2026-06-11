#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail

docker stop

docker rm -f $(docker ps -aq)

docker rmi -f $(docker images -q)

# docker volume rm -f $(docker volume ls -q)

# docker system prune -a -f ;
# docker system prune -a -f --volumes ;
# docker system prune --volumes -f
docker system prune -a -f --volumes
