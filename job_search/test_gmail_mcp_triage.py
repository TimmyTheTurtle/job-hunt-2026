from __future__ import annotations

import unittest
from datetime import datetime, timezone

from job_search.gmail_mcp_triage import extract_bodies, extract_job_links, gmail_request, lower_bound, render_report


class GmailMcpTriageTests(unittest.TestCase):
    def test_window_uses_starred_and_exact_boundary(self) -> None:
        now = datetime(2026, 9, 10, 12, tzinfo=timezone.utc)
        start = lower_bound("2026-09-09T12:00:00+00:00", now)
        request = gmail_request(start)
        self.assertEqual(["STARRED"], request["label_ids"])
        self.assertIn("after:2026/09/09", request["query"])

    def test_mcp_decoded_html_recovers_indeed_canonical_url(self) -> None:
        payload = {"mime_type": "text/html", "body": {"content": "<a href='https://www.indeed.com/rc/clk?jk=abc&from=email'>View job</a>"}}
        plain, rich = extract_bodies(payload)
        links = extract_job_links(plain, rich)
        self.assertEqual("https://www.indeed.com/viewjob?jk=abc", links[0]["canonical_url"])

    def test_verified_employer_address_is_rendered_with_provenance(self) -> None:
        url = "https://jobs.lever.co/example/abc"
        report = render_report(
            "2026-09-10",
            datetime(2026, 9, 9, tzinfo=timezone.utc),
            [],
            {
                url: {
                    "canonical_url": url,
                    "source_url": url,
                    "company": "Example Co.",
                    "title": "Applied AI Engineer",
                    "description": "Requirements: Python, APIs, and 3 years of software engineering experience.",
                    "employer_address": {
                        "status": "verified",
                        "address": "1 Example Way, Detroit, MI 48201",
                        "address_type": "headquarters",
                        "source_url": "https://example.com/contact",
                        "verified_at": "2026-09-10",
                    },
                }
            },
        )
        self.assertIn("Employer physical address (headquarters): 1 Example Way", report)
        self.assertIn("https://example.com/contact", report)


if __name__ == "__main__":
    unittest.main()
