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
                {"market": "CN", "public_slug": f"cn-{i:03d}", "company": f"Company {i}", "title": "AI Engineer"}
                for i in range(130)
            ],
        }
        cursors = {market: {"last_consumed_candidate_seq": 0} for market in ("SG", "CN", "MY")}

        _, batches = mod.build_batches(coldstart, registry=None, cursors=cursors)

        self.assertEqual(batches["CN"]["batch_size"], 100)
        self.assertEqual(batches["CN"]["candidate_count"], 100)
        self.assertEqual(batches["CN"]["remaining_after_batch"], 30)
        self.assertEqual(batches["CN"]["max_candidate_seq"], 100)

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

        for dropped in ("description_excerpt", "raw_payload", "freehire_url", "identity", "created_at", "event_kind", "event_seq", "public_slug"):
            self.assertNotIn(dropped, candidate)
        for key in (
            "candidate_seq",
            "role_key",
            "market",
            "company",
            "title",
            "location",
            "source",
            "source_url",
            "external_id",
            "known_status",
            "known_match_basis",
            "ai_score",
            "ai_signals",
            "flags",
            "employment_type",
            "posted_at",
        ):
            self.assertIn(key, candidate)

    def test_sharding_is_bounded_by_serialized_bytes_not_only_item_count(self):
        mod = self._load_module()
        candidates = []
        for i in range(100):
            candidates.append(
                {
                    "market": "MY",
                    "public_slug": f"my-{i:03d}",
                    "company": "Example Company " + ("C" * 80),
                    "title": "AI Agent Engineer " + ("T" * 120),
                    "location": "Kuala Lumpur, Malaysia",
                    "source": "workday",
                    "source_url": "https://example.com/jobs/" + ("u" * 350) + str(i),
                    "external_id": f"REQ-{i}",
                    "known_status": "unseen",
                    "known_match_basis": None,
                    "ai_score": 9,
                    "ai_signals": ["title:ai", "title:agent", "jd:llm", "jd:rag", "jd:retrieval"],
                    "flags": [],
                    "employment_type": "full_time",
                    "posted_at": "2026-11-01T00:00:00Z",
                    "description_excerpt": "X" * 50000,
                }
            )
        cursors = {market: {"last_consumed_candidate_seq": 0} for market in ("SG", "CN", "MY")}
        _, batches = mod.build_batches(
            {"source_generated_at": "2026-11-03T00:00:00Z", "candidates": candidates},
            registry=None,
            cursors=cursors,
        )

        manifest, shards = mod.shard_batch(batches["MY"], shard_size=25, max_shard_bytes=8000)

        self.assertEqual(sum(len(shard["candidates"]) for shard in shards), 100)
        self.assertGreater(len(shards), 4)
        self.assertEqual(manifest["max_shard_bytes"], 8000)
        self.assertTrue(all(len(shard["candidates"]) <= 25 for shard in shards))
        for shard in shards:
            encoded = json.dumps(shard, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8")
            self.assertLessEqual(len(encoded), 8000)
            self.assertTrue(all("description_excerpt" not in c for c in shard["candidates"]))


if __name__ == "__main__":
    unittest.main()
