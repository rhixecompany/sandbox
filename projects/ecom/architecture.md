# Ecom — Architecture Overview

## Overview
E-commerce platform built with Django, featuring a REST API backend and frontend interface.

## Key Components
- **ecom/** — Django application package (models, views, URLs, templates)
- **base/** — Base configuration and shared utilities
- **frontend/** — Frontend assets (HTML, CSS, JavaScript)
- **env/** — Virtual environment

## Technology
- Backend: Python 3 / Django
- Database: SQLite (development)
- Additional: appdirs, asgiref, boto3, botocore

## Deployment
- Procfile-based deployment
- systemd service + socket activation

Last updated: 2026-06-28
