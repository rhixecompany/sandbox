#!/bin/bash
# Auto-extracted from: messaging/telegram.md
# Source block language: bash
hermes gateway restart
grep -E "Using custom Telegram base_url|Using Telegram local_mode" ~/.hermes/logs/gateway.log | tail
