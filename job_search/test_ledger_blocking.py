from __future__ import annotations

import unittest

from job_search.ledger import blocking_urls_for_profile


def transaction(kind: str, profile: str, status: str, url: str) -> dict[str, object]:
    return {
        "kind": kind,
        "metadata": {"profile_name": profile},
        "events": [{"status": status, "job_url": url}],
    }


class LedgerProfileBlockingTests(unittest.TestCase):
    def test_surfaced_results_only_block_the_same_profile(self) -> None:
        rows = [transaction("search_run", "full_time", "surfaced", "https://example.com/job/1")]
        self.assertIn("https://example.com/job/1", blocking_urls_for_profile("full_time", rows))
        self.assertNotIn("https://example.com/job/1", blocking_urls_for_profile("contract", rows))

    def test_decisions_block_every_profile(self) -> None:
        rows = [transaction("decision_update", "", "applied", "https://example.com/job/2")]
        self.assertIn("https://example.com/job/2", blocking_urls_for_profile("full_time", rows))
        self.assertIn("https://example.com/job/2", blocking_urls_for_profile("contract", rows))


if __name__ == "__main__":
    unittest.main()
