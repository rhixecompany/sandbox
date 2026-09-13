#!/bin/bash
# Auto-extracted from: messaging/telegram.md
# Source block language: bash
# default profile
hermes gateway start
hermes gateway status
hermes gateway stop

# named profiles
hermes -p research gateway start
hermes -p research gateway status
hermes -p research gateway stop
