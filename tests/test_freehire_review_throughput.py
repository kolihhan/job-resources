import importlib.util
import json
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

    def test_100_candidate_batch_splits_into_four_25_candidate_shards(self):
        mod = self._load_module()
        batch = {
            "version": 1,
            "market": "CN",
            "cursor_before": 0,
            "batch_size": 100,
            "candidate_count": 100,
            "remaining_after_batch": 30,
            "max_candidate_seq": 100,
            "generated_at": "2026-11-03T00:00:00Z",
            "source_generated_at": "2026-11-03T00:00:00Z",
            "candidates": [{"candidate_seq": i} for i in range(1, 101)],
        }

        manifest, shards = mod.shard_batch(batch, shard_size=25)

        self.assertEqual(manifest["candidate_count"], 100)
        self.assertEqual(manifest["shard_count"], 4)
        self.assertNotIn("candidates", manifest)
        self.assertEqual([len(shard["candidates"]) for shard in shards], [25, 25, 25, 25])
        self.assertEqual(shards[0]["min_candidate_seq"], 1)
        self.assertEqual(shards[-1]["max_candidate_seq"], 100)

    def test_hourly_batch_projects_candidates_to_compact_metadata(self):
        mod = self._load_module()
        source = {
            "market": "SG",
            "public_slug": "agent-role-1",
            "company": "Example AI",
            "title": "Agent Engineer",
            "location": "Singapore",
            "source": "workday",
            "source_url": "https://example.com/job/1",
            "freehire_url": "https://freehire.me/jobs/agent-role-1",
            "external_id": "REQ-1",
            "identity": "agent-role-1",
            "known_status": "suspected_known",
            "known_match_basis": "company_title",
            "ai_score": 11,
            "ai_signals": ["title:agent", "jd:rag"],
            "flags": ["senior_hint"],
            "employment_type": "full_time",
            "posted_at": "2026-11-01T00:00:00Z",
            "created_at": "2026-11-02T00:00:00Z",
            "description_excerpt": "VERY-LONG-JD " * 10000,
            "raw_payload": {"also": "must not travel"},
        }
        cursors = {market: {"last_consumed_candidate_seq": 0} for market in ("SG", "CN", "MY")}

        _, batches = mod.build_batches(
            {"source_generated_at": "2026-11-03T00:00:00Z", "candidates": [source]},
            registry=None,
            cursors=cursors,
        )
        candidate = batches["SG"]["candidates"][0]

        self.assertNotIn("description_excerpt", candidate)
        self.assertNotIn("raw_payload", candidate)
        for key in (
            "candidate_seq",
            "role_key",
            "market",
            "public_slug",
            "company",
            "title",
            "location",
            "source",
            "source_url",
            "freehire_url",
            "external_id",
            "identity",
            "known_status",
            "known_match_basis",
            "ai_score",
            "ai_signals",
            "flags",
            "employment_type",
            "posted_at",
            "created_at",
        ):
            self.assertIn(key, candidate)

    def test_shard_size_is_not_driven_by_jd_length(self):
        mod = self._load_module()
        candidates = []
        for i in range(25):
            candidates.append(
                {
                    "market": "MY",
                    "public_slug": f"my-{i:03d}",
                    "company": "Example",
                    "title": "AI Engineer",
                    "location": "Malaysia",
                    "source_url": f"https://example.com/{i}",
                    "ai_score": 8,
                    "ai_signals": ["title:ai", "jd:agent"],
                    "flags": [],
                    "description_excerpt": "X" * 20000,
                }
            )
        cursors = {market: {"last_consumed_candidate_seq": 0} for market in ("SG", "CN", "MY")}

        _, batches = mod.build_batches(
            {"source_generated_at": "2026-11-03T00:00:00Z", "candidates": candidates},
            registry=None,
            cursors=cursors,
        )
        _, shards = mod.shard_batch(batches["MY"], shard_size=25)
        encoded = json.dumps(shards[0], ensure_ascii=False).encode("utf-8")

        self.assertLess(len(encoded), 100_000)
        self.assertTrue(all("description_excerpt" not in c for c in shards[0]["candidates"]))


if __name__ == "__main__":
    unittest.main()
