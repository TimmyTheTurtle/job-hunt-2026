#!/usr/bin/env bash

set -euo pipefail

cat >&2 <<'EOF'
The direct JobSpy job-board search is retired.
Use ./job_search/run_gmail_job_report.sh after configuring Gmail job alerts.
If you explicitly need legacy diagnostics, run job_search/run_search.py directly
with the user’s authorization and do not treat its results as active discovery.
EOF
exit 2
