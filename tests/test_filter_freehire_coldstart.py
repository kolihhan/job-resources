import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).parents[1] / "scripts"
SCRIPT = SCRIPTS / "filter_freehire_coldstart.py"


class FreeHireColdStartFilterTests(unittest.TestCase):
    def _load_module(self):
        self.assertTrue(SCRIPT.exists(), "scripts/filter_freehire_coldstart.py is required")
        sys.path.insert(0, str(SCRIPTS))
        try:
            spec = importlib.util.spec_from_file_location("filter_freehire_coldstart", SCRIPT)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        finally:
            sys.path.pop(0)

    def test_exact_keys_drop_but_weak_matches_remain_for_review(self):
        mod = self._load_module()
        coldstart = {
            "generated_at": "2026-11-03T00:00:00Z",
            "count": 4,
            "counts": {"SG": 2, "CN": 1, "MY": 1},
            "candidates": [
                {
                    "market": "SG",
                    "public_slug": "known-slug",
                    "company": "Acme",
                    "title": "AI Engineer",
                    "source_url": "https://jobs.acme.com/1",
                },
                {
                    "market": "CN",
                    "public_slug": "other-slug",
                    "company": "ByteCo",
                    "title": "Agent Engineer",
                    "source_url": "https://jobs.byteco.com/role/22?utm_source=freehire.me",
                },
                {
                    "market": "MY",
                    "public_slug": "weak-only",
                    "company": "MaybeCo",
                    "title": "Research Engineer",
                    "source_url": "https://jobs.maybe.com/new",
                },
                {
                    "market": "SG",
                    "public_slug": "new-role",
                    "company": "FreshCo",
                    "title": "LLM Engineer",
                    "source_url": "https://jobs.fresh.com/99",
                },
            ],
        }
        known = {
            "strong": {
                "urls": ["https://jobs.byteco.com/role/22"],
                "freehire_slugs": ["known-slug"],
            },
            "weak": {
                "company_title": ["maybeco|research engineer"],
            },
        }

        result = mod.filter_coldstart(coldstart, known, generated_at="2026-11-03T00:10:00Z")

        self.assertEqual(result["source_count"], 4)
        self.assertEqual(result["known_exact_count"], 2)
        self.assertEqual(result["suspected_known_count"], 1)
        self.assertEqual(result["unseen_count"], 1)
        self.assertEqual(len(result["candidates"]), 2)
        by_slug = {item["public_slug"]: item for item in result["candidates"]}
        self.assertEqual(by_slug["weak-only"]["known_status"], "suspected_known")
        self.assertEqual(by_slug["new-role"]["known_status"], "unseen")
        self.assertEqual(result["markets"]["SG"]["known_exact"], 1)
        self.assertEqual(result["markets"]["SG"]["unseen"], 1)
        self.assertEqual(result["markets"]["CN"]["known_exact"], 1)
        self.assertEqual(result["markets"]["MY"]["suspected_known"], 1)


if __name__ == "__main__":
    unittest.main()
