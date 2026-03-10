#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OPENAPI_PATH="$REPO_ROOT/shared/api/openapi.json"

echo "🍀 Generating openapi.json..."
cd "$REPO_ROOT/backend"
PYTHONUTF8=1 uv run python "../scripts/backend/export_openapi.py"

PYTHONUTF8=1 uv run python "../scripts/backend/_serve_openapi.py"
