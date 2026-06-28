---
author: Hermes Agent
description: Use when designing, building, or optimizing Microsoft Fabric Lakehouse
  solutions, including schemas, shortcuts, security, performance optimization, and
  query integration.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: fabric-lakehouse
tags: null
title: Fabric Lakehouse
version: 1.0.0

---
# Fabric Lakehouse

## Overview

Use this skill when working with Microsoft Fabric Lakehouse concepts and implementation guidance. It covers data components, organization, access control, performance optimization, query integration, and related coding and reference materials.

## When to Use

- Designing or building Lakehouse structures in Microsoft Fabric
- Creating schemas, tables, files, shortcuts, or materialized/spark views
- Optimizing query performance for Delta and non-tabular data
- Configuring access control and shortcode-based integration patterns

## When NOT to Use

- Non-Fabric data platforms without Lakehouse patterns
- Pure operational monitoring without data engineering context
- Environments where OneLake or Fabric tenancy is unavailable

## Skills Required

| Skill | Purpose |
|-------|---------|
| `project-docs` | Document Lakehouse design and ownership |
| `context-map` | Map data flows and Lakehouse component boundaries |

## Core Concepts

### What is a Lakehouse?

A Lakehouse in Microsoft Fabric stores tabular and non-tabular data together. It combines data lake flexibility with warehouse management capabilities.

Key properties include:

- Unified storage in OneLake
- Delta format for ACID behavior and time travel
- SQL analytics endpoint for T-SQL queries
- Semantic model support for reporting workloads

### Key Components

- Delta Tables
- Files
- SQL Endpoint
- Shortcuts
- Materialized Views

### Tabular Data and Schemas

- Tables use Delta by default; CSV or Parquet may be used for other scenarios
- Internal tables live under the Tables folder
- External tables reference data stored outside the Lakehouse
- Schemas organize tables as folders under Tables

### Files in a Lakehouse

- Files are stored under the Files folder
- Any format can be stored in Lakehouse
- Organize files with folders and subfolders when appropriate

### Security and Access Control

- Workspace roles control access
- OneLake security uses Entra ID and role-based access control
- Column-level and row-level security are supported for tables

## Lakehouse Shortcuts

### Types of Shortcuts

- Internal
- ADLS Gen2
- Amazon S3
- Dataverse
- Google Cloud Storage

## Performance Optimization

### V-Order Optimization

Enable V-Order for faster reads when using semantic models on Delta tables.

### Table Optimization

Use optimization and cleanup commands to improve query performance and reclaim storage.

## Verification Checklist

- [ ] Lakehouse structure documented
- [ ] Schema and shortcut design reviewed
- [ ] Access requirements mapped to OneLake security model
- [ ] Performance optimization options identified

## Pitfalls

- Shortcuts across tenants require valid permissions and network access
- Column-level and row-level security must be tested with actual workloads
- Optimization commands should be scheduled according to ingestion cadence
- External references should be reviewed before production use
