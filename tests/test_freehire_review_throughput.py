import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "build_freehire_review_queue.py"


class FreeHireReviewThroughputTests(unittest.TestCase):
    def _load_module(self):
        spec = importlib.util.spec_from_file_location("build_freehire_review_queue", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_default_batch_is_100_and_preserves_remainder(self):
        mod = self._load_module()
        coldstart = {
            "source_generated_at": "2026-11-03T00:00:00Z",
            "candidates": [
                {
                    "market": "CN",
                    "public_slug": f"cn-{i:03d}",
                    "company": f"Company {i}",
                    "title": "AI Engineer",
                }
                for i in range(130)
            ],
        }
        cursors = {
            "SG": {"last_consumed_candidate_seq": 0},
            "CN": {"last_consumed_candidate_seq": 0},
            "MY": {"last_consumed_candidate_seq": 0},
        }

        _, batches = mod.build_batches(coldstart, registry=None, cursors=cursors)

        self.assertEqual(batches["CN"]["batch_size"], 100)
        self.assertEqual(batches["CN"]["candidate_count"], 100)
        self.assertEqual(batches["CN"]["remaining_after_batch"], 30)
        self.assertEqual(batches["CN"]["max_candidate_seq"], 100)


if __name__ == "__main__":
    unittest.main()
