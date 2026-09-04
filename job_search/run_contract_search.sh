#!/usr/bin/env bash

set -euo pipefail

cat >&2 <<'EOF'
The direct contracting search is retired.
Use ./job_search/run_gmail_job_report.sh after configuring Gmail job alerts.
If you explicitly need legacy diagnostics, consult the retired workflow only
with the user’s authorization and do not treat its results as active discovery.
EOF
exit 2
