#!/bin/sh
#

pipx install uv
cd /workspaces/ai-dev-tools-zoomcamp/cohorts/2025/01-overview
uv run manage.py runserver
