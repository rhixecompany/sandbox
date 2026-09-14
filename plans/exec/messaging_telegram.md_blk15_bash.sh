#!/bin/bash
# Auto-extracted from: messaging/telegram.md
# Source block language: bash
tail -f ~/./logs/gateway.log | grep -iE "telegram|cache"
