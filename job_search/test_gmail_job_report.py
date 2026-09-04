from __future__ import annotations

import unittest
from datetime import datetime, timezone

from job_search.gmail_job_report import (
    canonicalize_url,
    extract_job_links,
    lower_bound,
)


class GmailJobReportTests(unittest.TestCase):
    def test_lower_bound_uses_shorter_of_last_run_and_fourteen_days(self) -> None:
        now = datetime(2026, 9, 4, 12, tzinfo=timezone.utc)
        recent = "2026-09-03T12:00:00+00:00"
        stale = "2026-08-01T12:00:00+00:00"
        self.assertEqual("2026-09-03T12:00:00+00:00", lower_bound(recent, now).isoformat())
        self.assertEqual("2026-08-21T12:00:00+00:00", lower_bound(stale, now).isoformat())

    def test_initial_run_is_capped_at_fourteen_days(self) -> None:
        now = datetime(2026, 9, 4, 12, tzinfo=timezone.utc)
        self.assertEqual("2026-08-21T12:00:00+00:00", lower_bound(None, now).isoformat())

    def test_indeed_tracking_redirect_becomes_public_job_url(self) -> None:
        url = "https://www.indeed.com/rc/clk?jk=abc123&from=email&tk=secret"
        self.assertEqual("https://www.indeed.com/viewjob?jk=abc123", canonicalize_url(url))

    def test_control_links_are_excluded_and_job_link_is_retained(self) -> None:
        html = """
        <a href='https://cts.indeed.com/v3/job-token'>View job</a>
        <a href='https://cts.indeed.com/v3/bad-token'>This is a bad match</a>
        <a href='https://cts.indeed.com/v3/unsub-token'>Unsubscribe</a>
        """
        links = extract_job_links("", html)
        self.assertEqual(1, len(links))
        self.assertEqual("https://cts.indeed.com/v3/job-token", links[0]["canonical_url"])


if __name__ == "__main__":
    unittest.main()
