#!/usr/bin/env bash
# Validate and sync PRINCIPLES through the shared Python implementation.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/sync.py" "$@"
