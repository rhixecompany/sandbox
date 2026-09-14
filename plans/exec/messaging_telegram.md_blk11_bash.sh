#!/bin/bash
# Auto-extracted from: messaging/telegram.md
# Source block language: bash
docker compose up -d tg-bot-api
docker logs --tail 20 tg-bot-api
