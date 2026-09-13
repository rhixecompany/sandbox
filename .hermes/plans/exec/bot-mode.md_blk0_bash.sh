#!/bin/bash
# Auto-extracted from: bot-mode.md
# Source block language: bash
hermes peer add spark --url http://spark.lan:8377 --key <API_SERVER_KEY>
hermes peer list
hermes peer dm spark < /tmp/dm.txt        # message body from a file (nothing shell-interpreted)
hermes peer dm spark/researcher < /tmp/dm.txt   # named profile on a multiplexed peer
hermes peer run spark --idempotency-key ticket-123 < /tmp/long-task.txt
hermes peer status spark run_abc123
hermes peer stop spark run_abc123
