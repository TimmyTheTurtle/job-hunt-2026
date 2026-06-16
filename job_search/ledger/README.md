# Search Ledger

This folder holds the machine-managed search ledger.

Purpose:
- avoid duplicate search hits across runs
- record dismissals and applications outside `master_tracker.md`
- keep `master_tracker.md` as a supervised/manual artifact for UI submissions

Files:
- `transactions.jsonl`
  Source of truth. Append-only transaction log.
- `state.json`
  Generated materialized state.
- `summary.md`
  Generated human-readable view.

The search runner writes `surfaced` entries here.
Manual or chat-driven review can write `saved`, `dismissed`, and `applied` decisions here.

Archive:
- `archive/2026-06-16_pre_applied_ai_pivot/`
  Previous simulation/C++-oriented search ledger snapshot archived when the
  active search profile pivoted to Applied AI Systems Engineer.
