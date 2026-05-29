#!/usr/bin/env bash
# Run Gmail inbox triage. Any agent can invoke this from repo root in WSL.
# First run will prompt for OAuth browser auth; subsequent runs are silent.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

VENV="job_search/.venv"

if [ ! -d "$VENV" ]; then
  python3 -m venv "$VENV"
fi

if ! "$VENV/bin/python" -c "import googleapiclient" >/dev/null 2>&1; then
  "$VENV/bin/pip" install -q -U pip \
    google-auth google-auth-oauthlib google-api-python-client openai
fi

"$VENV/bin/python" job_search/gmail_triage.py "$@"
