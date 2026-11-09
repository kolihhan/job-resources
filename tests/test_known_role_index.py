import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "build_known_role_index.py"


class KnownRoleIndexTests(unittest.TestCase):
    def _load_module(self):
        self.assertTrue(SCRIPT.exists(), "scripts/build_known_role_index.py is required")
        spec = importlib.util.spec_from_file_location("build_known_role_index", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_normalize_url_drops_tracking_but_preserves_job_identity(self):
        mod = self._load_module()
        normalized = mod.normalize_url(
            "https://jobs.example.com/role/123?job=abc&utm_source=freehire.me#details"
        )
        self.assertEqual(
            normalized,
            "https://jobs.example.com/role/123?job=abc#details",
        )

    def test_build_index_extracts_strong_and_weak_keys_from_all_issue_states(self):
        mod = self._load_module()
        issues = [
            {
                "number": 10,
                "state": "open",
                "title": "[APPLY][SG-ENG] Acme — AI Engineer — Singapore",
                "body": "Official: https://jobs.example.com/role/123?utm_source=linkedin\nFreeHire: https://freehire.me/jobs/acme-ai-123",
            },
            {
                "number": 11,
                "state": "closed",
                "title": "[BLOCKED][CN-RES] LabCo — Research Engineer — Beijing",
                "body": "Exact role: https://careers.lab.example/jobs/RE-77",
            },
        ]

        index = mod.build_index(issues, generated_at="2026-11-03T00:00:00Z")

        self.assertEqual(index["issue_count"], 2)
        self.assertIn("https://jobs.example.com/role/123", index["strong"]["urls"])
        self.assertIn("acme-ai-123", index["strong"]["freehire_slugs"])
        self.assertIn("acme|ai engineer", index["weak"]["company_title"])
        self.assertIn("labco|research engineer", index["weak"]["company_title"])
        self.assertEqual(index["issue_numbers"], [10, 11])

    def test_wait_employer_is_history_hint_not_hard_duplicate(self):
        mod=self._load_module()
        issues=[
            {"number":479, "title":"[WAIT][MY-RES] Gen Digital / MoneyLion — Applied AI Scientist (Generative AI)",
             "body":"User previously submitted an application"},
            {"number":698, "title":"[APPLY][SG-ENG] NTU / AI Singapore — AI Engineer (AIAP)",
             "body":"Not submitted"},
            {"number":901, "title":"[WAIT][SG-RES] NTU DTC — Research Engineer II",
             "body":"User-confirmed applied"},
        ]
        index=mod.build_index(issues,"2026-11-09T00:00:00Z")
        self.assertIn("gen digital moneylion",index["weak"]["wait_employers"])
        self.assertIn("ntu dtc",index["weak"]["wait_employers"])
        self.assertNotIn("ntu ai singapore",index["weak"]["wait_employers"])
        self.assertEqual(index["issue_count"],3)



if __name__ == "__main__":
    unittest.main()
