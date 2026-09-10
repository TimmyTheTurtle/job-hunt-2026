from __future__ import annotations

import unittest

from job_search.alert_cleanup import build_plan, classify_subject, render_overlay


PROFILE = {
    "resume_path": "resumes/resume_fde_applied_ai_systems.docx",
    "location_policy": {"remote_anywhere": True, "onsite_countries": ["Canada", "United States"]},
    "target_alerts": [{"label": "Forward Deployed Engineer", "query": "Forward Deployed Engineer"}],
    "platforms": {"dice": {"sender_domains": ["dice.com"]}, "linkedin": {"sender_domains": ["linkedin.com"]}},
    "legacy_patterns": ["adas", "junior c++"],
}


class AlertCleanupTests(unittest.TestCase):
    def test_classifies_legacy_and_aligned_subjects(self) -> None:
        self.assertEqual("legacy", classify_subject('Results from your "ADAS Software Engineer" job alert.', PROFILE))
        self.assertEqual("aligned", classify_subject("Forward Deployed AI Engineer at Example", PROFILE))

    def test_plan_groups_sender_domains_and_marks_legacy(self) -> None:
        plan = build_plan({"messages": [
            {"from": "Dice <dice@connect.dice.com>", "subject": 'Results from your "ADAS Software Engineer" job alert.'},
            {"from": "LinkedIn <jobalerts-noreply@linkedin.com>", "subject": "Forward Deployed Engineer at Example"},
        ]}, PROFILE)
        self.assertEqual("replace_legacy", plan[0]["status"])
        self.assertEqual("retune", plan[1]["status"])

    def test_overlay_is_temporary_and_contains_the_target_query(self) -> None:
        overlay = render_overlay([], PROFILE)
        self.assertIn("dorian-alert-guide", overlay)
        self.assertIn("Forward Deployed Engineer", overlay)
        self.assertIn("guide.remove()", overlay)


if __name__ == "__main__":
    unittest.main()
