#!/bin/bash
# Auto-extracted from: messaging/telegram.md
# Source block language: bash
sqlite3 ~/./state.db \
  "UPDATE telegram_dm_topic_mode SET enabled = 0
     WHERE profile_name = 'default' AND chat_id = '<your_chat_id>';
   DELETE FROM telegram_dm_topic_bindings
     WHERE profile_name = 'default' AND chat_id = '<your_chat_id>';"
