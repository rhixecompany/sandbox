---
name: discover-mcp-capabilities
description: Inspect and enumerate Hermes MCP capabilities, including configured servers, their exact tool names, and known purposes.
title: Discover Mcp Capabilities
version: 1.0.0
author: Hermes Agent
license: MIT
tags: []
---
# discover-mcp-capabilities

## Purpose

Use this skill when the user wants the exact inventory of configured MCP servers and their tools, not a conversational summary. It is for capability discovery, audit verification, and planning what Hermes can do through MCP.

## Inventory

The inventory is derived from live `hermes mcp list` and each `hermes mcp test <name>` discovery. Cache source of truth there; this skill records the exposed tool names per server for precise lookup later.

## Hermes MCP Servers and Exact Tool Names

### ast-grep
- `dump_syntax_tree`
- `test_match_code_rule`
- `find_code`
- `find_code_by_rule`
- `rewrite_code`
- `analyze-imports`
- `scan-code`

### code-sandbox
- `sandbox_initialize`
- `sandbox_exec`
- `run_js`
- `sandbox_stop`
- `run_js_ephemeral`
- `get_dependency_types`
- `search_npm_packages`

### codex
- `codex`
- `codex-reply`

### fetch
- `get_raw_text`
- `get_rendered_html`
- `get_markdown`
- `get_markdown_summary`

### filesystem
- `read_file`
- `read_text_file`
- `read_media_file`
- `read_multiple_files`
- `write_file`
- `edit_file`
- `create_directory`
- `list_directory`
- `list_directory_with_sizes`
- `directory_tree`
- `move_file`
- `search_files`
- `get_file_info`
- `list_allowed_directories`

### github
- `create_or_update_file`
- `search_repositories`
- `create_repository`
- `get_file_contents`
- `push_files`
- `create_issue`
- `create_pull_request`
- `fork_repository`
- `create_branch`
- `list_commits`
- `list_issues`
- `update_issue`
- `add_issue_comment`
- `search_code`
- `search_issues`
- `search_users`
- `get_issue`
- `get_pull_request`
- `list_pull_requests`
- `create_pull_request_review`
- `merge_pull_request`
- `get_pull_request_files`
- `get_pull_request_status`
- `update_pull_request_branch`
- `get_pull_request_comments`
- `get_pull_request_reviews`

### mcp-docker
- `add_comment_to_pending_review`
- `add_issue_comment`
- `add_reply_to_pull_request_comment`
- `assign_copilot_to_issue`
- `code-mode`
- `convert_time`
- `create_branch`
- `create_or_update_file`
- `create_pull_request`
- `create_repository`
- `delete_file`
- `fetch_generic_documentation`
- `fetch_generic_url_content`
- `fork_repository`
- `get_commit`
- `get_current_time`
- `get_file_contents`
- `get_label`
- `get_latest_release`
- `get_me`
- `get_release_by_tag`
- `get_tag`
- `get_team_members`
- `get_teams`
- `issue_read`
- `issue_write`
- `list_branches`
- `list_commits`
- `list_issue_types`
- `list_issues`
- `list_pull_requests`
- `list_releases`
- `list_tags`
- `match_common_libs_owner_repo_mapping`
- `mcp-activate-profile`
- `mcp-add`
- `mcp-config-set`
- `mcp-create-profile`
- `mcp-exec`
- `mcp-find`
- `mcp-remove`
- `merge_pull_request`
- `pull_request_read`
- `pull_request_review_write`
- `push_files`
- `request_copilot_review`
- `search_code`
- `search_generic_code`
- `search_generic_documentation`
- `search_issues`
- `search_pull_requests`
- `search_repositories`
- `search_users`
- `sub_issue_write`
- `update_pull_request`
- `update_pull_request_branch`

### memory
- `create_entities`
- `create_relations`
- `add_observations`
- `delete_entities`
- `delete_observations`
- `delete_relations`
- `read_graph`
- `search_nodes`
- `open_nodes`

### mindstudio
Use the live `hermes mcp test mindstudio` output for the full exhaustive catalog. Known surfaced context from discovery includes rich external integrations for messaging, calendars, documents, spreadsheets, video, audio, social apps, vector data sources, databases, OAuth connectors, and additional agent APIs.

### playwright
- `browser_close`
- `browser_resize`
- `browser_console_messages`
- `browser_handle_dialog`
- `browser_evaluate`
- `browser_file_upload`
- `browser_drop`
- `browser_fill_form`
- `browser_press_key`
- `browser_type`
- `browser_navigate`
- `browser_navigate_back`
- `browser_network_requests`
- `browser_network_request`
- `browser_run_code_unsafe`
- `browser_take_screenshot`
- `browser_snapshot`
- `browser_click`
- `browser_drag`
- `browser_hover`
- `browser_select_option`
- `browser_tabs`
- `browser_wait_for`

### sequential-thinking
- `sequentialthinking`

### smithery
- `code-sentinel.analyze_code`
- `code-sentinel.generate_report`
- `code-sentinel.check_security`
- `code-sentinel.check_deceptive_patterns`
- `code-sentinel.check_placeholders`
- `code-sentinel.analyze_patterns`
- `code-sentinel.analyze_design_patterns`
- `context7-mcp.resolve-library-id`
- `context7-mcp.query-docs`
- `exa.web_search_exa`
- `exa.web_fetch_exa`
- `github.actions_get`
- `github.actions_list`
- `github.actions_run_trigger`
- `github.add_comment_to_pending_review`
- `github.add_issue_comment`
- `github.add_reply_to_pull_request_comment`
- `github.check_dependency_vulnerabilities`
- `github.create_branch`
- `github.create_gist`
- `github.create_or_update_file`
- `github.create_pull_request`
- `github.create_repository`
- `github.delete_file`
- `github.discussion_comment_write`
- `github.dismiss_notification`
- `github.fork_repository`
- `github.get_code_quality_finding`
- `github.get_code_scanning_alert`
- `github.get_commit`
- `github.get_copilot_space`
- `github.get_dependabot_alert`
- `github.get_discussion`
- `github.get_discussion_comments`
- `github.get_file_contents`
- `github.get_gist`
- `github.get_global_security_advisory`
- `github.get_job_logs`
- `github.get_label`
- `github.get_latest_release`
- `github.get_me`
- `github.get_notification_details`
- `github.get_release_by_tag`
- `github.get_repository_tree`
- `github.get_secret_scanning_alert`
- `github.get_tag`
- `github.get_team_members`
- `github.get_teams`
- `github.github_support_docs_search`
- `github.issue_read`
- `github.issue_write`
- `github.label_write`
- `github.list_branches`
- `github.list_code_scanning_alerts`
- `github.list_commits`
- `github.list_copilot_spaces`
- `github.list_dependabot_alerts`
- `github.list_discussion_categories`
- `github.list_discussions`
- `github.list_gists`
- `github.list_global_security_advisories`
- `github.list_issue_fields`
- `github.list_issue_types`
- `github.list_issues`
- `github.list_label`
- `github.list_notifications`
- `github.list_org_repository_security_advisories`
- `github.list_pull_requests`
- `github.list_releases`
- `github.list_repository_collaborators`
- `github.list_repository_security_advisories`
- `github.list_secret_scanning_alerts`
- `github.list_starred_repositories`
- `github.list_tags`
- `github.manage_notification_subscription`
- `github.manage_repository_notification_subscription`
- `github.mark_all_notifications_read`
- `github.merge_pull_request`
- `github.projects_get`
- `github.projects_list`
- `github.projects_write`
- `github.pull_request_read`
- `github.pull_request_review_write`
- `github.push_files`
- `github.request_copilot_review`
- `github.run_secret_scanning`
- `github.search_code`
- `github.search_commits`
- `github.search_issues`
- `github.search_orgs`
- `github.search_pull_requests`
- `github.search_repositories`
- `github.search_users`
- `github.semantic_issue_similarity_search`
- `github.semantic_issues_search`
- `github.star_repository`
- `search_toolbox`
- `execute`
- `get_toolbox_status`
- `remove_server`

## How to Update

Update skill references when:
- `hermes mcp list` shows a new enabled server, or
- `hermes mcp test <name>` discovers a new tool list for an already-enabled server.


## When to Use

- Use when _(describe scenario 1)_
- Use when _(describe scenario 2)_
- Use when _(describe scenario 3)_



## When NOT to Use

- When the task is outside this skill's domain
- When simpler approaches are more effective
- When required dependencies are unavailable



## Workflow

### Phase 1: Preparation

_Set up dependencies, gather inputs, validate the environment._

### Phase 2: Execution

_Run the primary workflow._

### Phase 3: Verification & Cleanup

_Validate results, document outcomes, clean up temporary resources._


## Pitfalls

- **None documented yet.**
- Add common pitfalls, edge cases, and failure modes specific to this skill.

## Verification Checklist

- [ ] All tasks completed
- [ ] Output verified
- [ ] Edge cases handled

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |
