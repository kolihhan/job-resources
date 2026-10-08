import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "freehire_fetch.py"
spec = importlib.util.spec_from_file_location("freehire_fetch", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class FreeHireFetchTests(unittest.TestCase):
    def test_offsets_cover_api_maximum_exactly(self):
        self.assertEqual(mod.page_offsets(max_rows=10000, page_size=100)[0], 0)
        self.assertEqual(mod.page_offsets(max_rows=10000, page_size=100)[-1], 9900)
        self.assertEqual(len(mod.page_offsets(max_rows=10000, page_size=100)), 100)

    def test_fetch_stops_at_reported_total(self):
        calls = []

        def fake_fetch(params):
            calls.append(dict(params))
            offset = params["offset"]
            if offset == 0:
                return {"data": [{"public_slug": "a"}, {"public_slug": "b"}], "meta": {"total": 3, "limit": 2, "offset": 0}}
            return {"data": [{"public_slug": "c"}], "meta": {"total": 3, "limit": 2, "offset": 2}}

        jobs = mod.fetch_market(fake_fetch, country="SG", max_rows=10000, page_size=2)
        self.assertEqual([j["public_slug"] for j in jobs], ["a", "b", "c"])
        self.assertEqual([c["offset"] for c in calls], [0, 2])

    def test_fetch_rejects_ignored_country_filter(self):
        def fake_fetch(params):
            return {"data": [], "meta": {"total": 0, "limit": 100, "offset": 0, "ignored_params": ["countries"]}}

        with self.assertRaisesRegex(RuntimeError, "ignored"):
            mod.fetch_market(fake_fetch, country="CN")

    def test_cheap_screen_keeps_early_career_and_rejects_obvious_mismatch(self):
        jobs = [
            {"public_slug": "good", "title": "AI Engineer", "enrichment": {"seniority": "junior", "experience_years_min": 1, "employment_type": "full_time", "company_type": "product"}},
            {"public_slug": "senior", "title": "Senior AI Engineer", "enrichment": {"seniority": "senior"}},
            {"public_slug": "five", "title": "Backend Engineer", "enrichment": {"experience_years_min": 5}},
            {"public_slug": "agency", "title": "LLM Engineer", "enrichment": {"company_type": "outstaff"}},
            {"public_slug": "intern", "title": "Software Engineer Intern", "enrichment": {"employment_type": "internship"}},
            {"public_slug": "stretch", "title": "Backend Engineer", "enrichment": {"seniority": "middle", "experience_years_min": 3, "company_type": "product"}},
        ]
        kept, rejected = mod.cheap_screen(jobs)
        self.assertEqual([j["public_slug"] for j in kept], ["good", "stretch"])
        self.assertEqual({r["public_slug"] for r in rejected}, {"senior", "five", "agency", "intern"})

    def test_build_params_uses_relevant_categories_and_newest_created_order(self):
        params = mod.build_params(country="CN", offset=0, page_size=100)
        self.assertEqual(params["countries"], "CN")
        self.assertEqual(params["limit"], 100)
        self.assertEqual(params["offset"], 0)
        self.assertEqual(params["sort"], "created_at")
        self.assertEqual(params["order"], "desc")
        self.assertIn("ai_engineering", params["category"])
        self.assertIn("backend", params["category"])


if __name__ == "__main__":
    unittest.main()
