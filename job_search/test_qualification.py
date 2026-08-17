from __future__ import annotations

import unittest
from pathlib import Path

from job_search.qualification import evaluate_qualifications, load_candidate_profile, qualification_recommendation


PROFILE = load_candidate_profile(Path(__file__).with_name("candidate_profile.json"))


def row(title: str, description: str, location: str = "Remote, US", is_remote: bool = True) -> dict[str, object]:
    return {
        "title": title,
        "company": "Example",
        "description": description,
        "location": location,
        "country": "US",
        "is_remote": is_remote,
    }


class QualificationTests(unittest.TestCase):
    def test_candidate_profile_keeps_ai_and_clearance_claims_conservative(self) -> None:
        self.assertEqual(0, PROFILE["skills"]["ai_ml"]["years"])
        self.assertEqual("portfolio", PROFILE["skills"]["llm_rag"]["level"])
        self.assertEqual([], PROFILE["clearance"]["active"])

    def test_missing_description_is_unverified_not_apply_first(self) -> None:
        result = evaluate_qualifications(row("AI Forward Deployed Engineer", ""), PROFILE)
        self.assertEqual("missing", result["description_status"])
        self.assertEqual("unverified", qualification_recommendation(15, False, result))

    def test_active_us_clearance_is_hard_blocker(self) -> None:
        description = """
        Minimum Qualifications:
        Active TS/SCI security clearance required.
        5+ years of software development experience.
        Bachelor's degree in computer science or a related field.
        """
        result = evaluate_qualifications(row("AI Engineer", description), PROFILE)
        self.assertTrue(any("active clearance" in item.lower() for item in result["hard_blockers"]))
        self.assertEqual("skip", qualification_recommendation(10, False, result))

    def test_attainable_dotnet_role_is_apply_first(self) -> None:
        description = """
        Minimum Qualifications:
        5+ years of software development experience.
        3+ years using C# and .NET.
        Experience with SQL Server and relational databases.
        Experience building REST APIs and systems integrations.
        Bachelor's degree in computer science or equivalent experience.
        Responsibilities:
        Build workflow software for operational teams.
        """
        result = evaluate_qualifications(
            row("Software Engineer - Workflow Automation", description, "Troy, Michigan, US", False), PROFILE
        )
        self.assertFalse(result["hard_blockers"])
        self.assertGreaterEqual(result["qualification_score"], 75)
        self.assertEqual("apply_first", qualification_recommendation(8, False, result))

    def test_senior_data_ai_role_with_specific_tenure_is_rejected(self) -> None:
        description = """
        Required Qualifications:
        5+ years of data engineering experience building production data platforms.
        3+ years of professional Python development.
        Production expertise with Databricks, Spark, and Kafka.
        Production experience developing machine learning and generative AI systems.
        Bachelor's degree in computer science.
        """
        result = evaluate_qualifications(row("Senior Data Engineer - Agentic AI", description), PROFILE)
        self.assertTrue(result["hard_blockers"])
        self.assertEqual("skip", qualification_recommendation(20, False, result))

    def test_portfolio_ai_can_be_partial_when_software_requirements_are_met(self) -> None:
        description = """
        Requirements:
        5+ years of software engineering experience.
        Hands-on experience with LLM and RAG applications.
        Experience building REST APIs and workflow integrations.
        Bachelor's degree in computer science or equivalent experience.
        """
        result = evaluate_qualifications(row("Applied AI Application Engineer", description), PROFILE)
        self.assertFalse(result["hard_blockers"])
        self.assertTrue(any(item["key"] == "skill:llm_rag" for item in result["partial"]))
        self.assertIn(qualification_recommendation(12, False, result), {"apply_first", "review"})

    def test_out_of_state_onsite_role_is_hard_mismatch(self) -> None:
        description = """
        Requirements:
        5+ years of software development experience.
        Experience building REST APIs.
        This position is on-site in St. Louis, Missouri.
        """
        result = evaluate_qualifications(row("AI Solutions Engineer", description, "St. Louis, MO", False), PROFILE)
        self.assertTrue(any("location" in item.lower() for item in result["hard_blockers"]))
        self.assertEqual("skip", qualification_recommendation(12, False, result))

    def test_missing_description_does_not_hide_location_blocker(self) -> None:
        result = evaluate_qualifications(row("Systems Engineer", "", "Boston, MA", False), PROFILE)
        self.assertTrue(result["hard_blockers"])
        self.assertEqual("skip", qualification_recommendation(8, False, result))

    def test_inline_markdown_heading_and_spelled_years_are_parsed(self) -> None:
        description = """
        **Required Qualifications*** Bachelor's degree in Computer Science or a related discipline.
        * Six or more years of professional software development experience.
        * Advanced proficiency in Python for production services.
        * Strong SQL and relational database experience.
        **Preferred Qualifications*** Experience with Docker and Kubernetes.
        """
        result = evaluate_qualifications(row("Senior Python Engineer", description), PROFILE)
        labels = {item["label"] for item in result["matched"] + result["partial"] + result["gaps"]}
        self.assertIn("6+ years software engineering", labels)
        self.assertTrue(any("Python" in item for item in result["hard_blockers"]))
        self.assertEqual("skip", qualification_recommendation(10, False, result))

    def test_multiple_tenure_requirements_bind_to_the_nearest_skill(self) -> None:
        description = """
        Required Qualifications:
        Eight years of software engineering and three years of Python experience.
        Bachelor's degree in computer science.
        Experience with SQL and relational databases.
        """
        result = evaluate_qualifications(row("Software Engineer", description), PROFILE)
        requirements = {
            item["key"]: item for item in result["matched"] + result["partial"] + result["gaps"]
        }
        self.assertEqual("match", requirements["years:software_engineering:8"]["status"])
        self.assertEqual("gap", requirements["years:python:3"]["status"])

    def test_location_does_not_turn_one_portfolio_requirement_into_apply_first(self) -> None:
        description = """
        Requirements:
        Hands-on experience with LLM and RAG applications.
        Responsibilities include collaborating with product and engineering teams to build, document, test, and improve software workflows for customers. The role involves iterative delivery, clear written communication, and careful operational follow-through.
        """
        result = evaluate_qualifications(row("AI Software Engineer", description), PROFILE)
        self.assertEqual(1, result["substantive_required_count"])
        self.assertEqual("unverified", qualification_recommendation(20, False, result))

    def test_indirect_role_title_cannot_be_apply_first(self) -> None:
        description = """
        Requirements:
        5+ years of software engineering experience.
        Experience with SQL and relational databases.
        Experience building REST APIs and systems integrations.
        Bachelor's degree in computer science.
        """
        result = evaluate_qualifications(row("Software Engineer, Digital Workplace", description), PROFILE)
        self.assertEqual("review", qualification_recommendation(20, False, result, "indirect"))


if __name__ == "__main__":
    unittest.main()
