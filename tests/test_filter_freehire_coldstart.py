import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).parents[1] / "scripts"
SCRIPT = SCRIPTS / "filter_freehire_coldstart.py"
QUEUE_SCRIPT = SCRIPTS / "build_freehire_review_queue.py"


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
            "matched_counts": {"SG": 2, "CN": 1, "MY": 1},
            "raw_counts": {"SG": 200, "CN": 100, "MY": 50},
            "title_hard_drop_counts": {"SG": 20, "CN": 10, "MY": 5},
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
        self.assertEqual(result["raw_counts"], {"SG": 200, "CN": 100, "MY": 50})
        self.assertEqual(result["title_hard_drop_counts"], {"SG": 20, "CN": 10, "MY": 5})
        self.assertEqual(result["machine_candidate_counts"], {"SG": 2, "CN": 1, "MY": 1})
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


class FreeHireReviewQueueTests(unittest.TestCase):
    def _load_module(self):
        self.assertTrue(QUEUE_SCRIPT.exists(), "scripts/build_freehire_review_queue.py is required")
        spec = importlib.util.spec_from_file_location("build_freehire_review_queue", QUEUE_SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_sequences_are_stable_across_reorder_and_batches_follow_market_cursor(self):
        mod = self._load_module()
        coldstart = {
            "source_generated_at": "2026-11-03T00:00:00Z",
            "candidates": [
                {"market": "SG", "public_slug": "sg-a", "company": "A", "title": "AI Engineer"},
                {"market": "SG", "public_slug": "sg-b", "company": "B", "title": "LLM Engineer"},
                {"market": "CN", "public_slug": "cn-a", "company": "C", "title": "Agent Engineer"},
                {"market": "MY", "public_slug": "my-a", "company": "D", "title": "Research Engineer", "known_status": "suspected_known"},
            ],
        }
        cursors = {
            "SG": {"last_consumed_candidate_seq": 0},
            "CN": {"last_consumed_candidate_seq": 0},
            "MY": {"last_consumed_candidate_seq": 0},
        }

        registry, batches = mod.build_batches(coldstart, registry=None, cursors=cursors, batch_size=1)
        self.assertEqual(registry["next_candidate_seq"], 5)
        self.assertEqual(batches["SG"]["candidates"][0]["public_slug"], "sg-a")
        self.assertEqual(batches["SG"]["candidates"][0]["candidate_seq"], 1)
        self.assertEqual(batches["CN"]["candidates"][0]["candidate_seq"], 3)
        self.assertEqual(batches["MY"]["candidates"][0]["known_status"], "suspected_known")

        reordered = dict(coldstart)
        reordered["candidates"] = [
            coldstart["candidates"][1],
            coldstart["candidates"][0],
            coldstart["candidates"][3],
            coldstart["candidates"][2],
        ]
        cursors["SG"]["last_consumed_candidate_seq"] = 1
        registry2, batches2 = mod.build_batches(reordered, registry=registry, cursors=cursors, batch_size=2)

        self.assertEqual(registry2["roles"]["freehire:sg-a"]["candidate_seq"], 1)
        self.assertEqual(registry2["roles"]["freehire:sg-b"]["candidate_seq"], 2)
        self.assertEqual([c["public_slug"] for c in batches2["SG"]["candidates"]], ["sg-b"])
        self.assertEqual(batches2["SG"]["cursor_before"], 1)
        self.assertEqual(batches2["SG"]["max_candidate_seq"], 2)


if __name__ == "__main__":
    unittest.main()
