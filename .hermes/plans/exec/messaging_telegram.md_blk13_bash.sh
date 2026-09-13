#!/bin/bash
# Auto-extracted from: messaging/telegram.md
# Source block language: bash
curl "http://127.0.0.1:8081/bot<YOUR_BOT_TOKEN>/getMe"
# expected response: {"ok":true,"result":{"id":...,"is_bot":true,...}}
