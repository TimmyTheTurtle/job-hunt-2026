#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [ ! -d "job_search/.venv" ]; then
  python3 -m venv job_search/.venv
fi

source job_search/.venv/bin/activate

if ! python -c "import jobspy" >/dev/null 2>&1; then
  pip install -U pip python-jobspy
fi

python job_search/run_search.py "$@"
