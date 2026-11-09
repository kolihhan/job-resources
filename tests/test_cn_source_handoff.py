import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "build_cn_source_handoff.py"


def load():
    spec = importlib.util.spec_from_file_location("cn_source_handoff", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class SourceHandoffTests(unittest.TestCase):
    def test_source_ids_and_weak_rejects_preserved_in_raw(self):
        m = load()
        jobs = [
            {"sourceId": "101", "title": "大模型应用工程师", "company": "Example",
             "url": "https://www.liepin.com/job/101.shtml?utm_source=test", "location": "深圳", "experience": "1-3年"},
            {"sourceId": "101", "title": "大模型应用工程师", "company": "Example",
             "url": "https://www.liepin.com/job/101.shtml", "location": "深圳"},
            {"sourceId": "102", "title": "销售经理", "company": "Example",
             "url": "https://www.liepin.com/job/102.shtml", "location": "深圳"},
            {"sourceId": "103", "title": "Agent Engineer", "company": "Example",
             "url": "https://www.liepin.com/job/103.shtml", "location": "深圳"},
        ]
        known = {"strong": {"urls": ["https://www.liepin.com/job/101.shtml"]}}
        manifest, shards = m.build_handoff({"jobs": jobs}, {"jobs": []}, known, "123")
        self.assertEqual(manifest["raw_observed_rows"], 4)
        self.assertEqual(manifest["unique_source_identifiers"], 3)
        self.assertEqual(manifest["candidate_count"], 2)
        self.assertEqual(manifest["low_signal_rows_in_raw_artifact"], 1)
        self.assertEqual(manifest["known_url_hints"], 1)
        self.assertEqual(len(shards), 1)
        self.assertEqual(manifest["status"], "AWAITING_VERIFICATION")
        self.assertEqual(manifest["raw_artifact_reference"], "cn-raw-123")

    def test_jobpro_and_sharding_do_not_drop_candidates(self):
        m = load()
        jobs = [{"sourceId": str(i), "title": "AI 后端研发", "company": "Test",
                 "url": f"https://www.liepin.com/job/{i}.shtml", "location": "深圳"}
                for i in range(53)]
        manifest, shards = m.build_handoff({"jobs": jobs}, {"jobs": [
            {"company_key": "testcompany", "post_id": "EMP-1",
             "title": "Research Engineer", "apply_url": "https://company.example/jobs/EMP-1"}]},
            {}, "456")
        self.assertEqual(manifest["candidate_count"], 54)
        self.assertEqual(manifest["shards"], ["cn-source-candidates-01.json", "cn-source-candidates-02.json", "cn-source-candidates-03.json"])
        self.assertEqual(sum(len(s) for s in shards), 54)
        self.assertTrue(all(len(s) <= 25 for s in shards))

    def test_native_liepin_handoff_queues_ai_identity_not_verdict(self):
        m=load()
        roles=[
            {"sourceId":"1960468101","title":"大模型Agent工程师","company":"A",
             "url":"https://www.liepin.com/job/1960468101.shtml?tracking=abc",
             "location":"深圳","experience":"1-3年"},
            {"sourceId":"1960468102","title":"普通后端开发","company":"B",
             "url":"https://www.liepin.com/job/1960468102.shtml","location":"北京"},
        ]
        manifest,shards=m.build_handoff({"jobs":roles},{"jobs":[]},{}, "rr1")
        snapshot=m.native_queue_snapshot(shards)
        self.assertEqual(snapshot["market"],"CN")
        self.assertEqual(len(snapshot["jobs"]),1)
        row=snapshot["jobs"][0]
        self.assertEqual(row["source_platform"],"猎聘")
        self.assertEqual(row["discovery_access"],"NATIVE_API_LISTING")
        self.assertEqual(row["evidence"],"listing_only")
        self.assertNotIn("full_jd_text",row)
        self.assertEqual(row["job_id"],"1960468101")
        self.assertEqual(manifest["candidate_count"],2)

    def test_blank_identity_cannot_enter_queue(self):
        m = load()
        self.assertIsNone(m.project_liepin({"title": "AI Engineer", "url": "https://example.com"}))
        self.assertIsNone(m.project_jobpro({"company_key": "A", "title": "AI Engineer"}))


if __name__ == "__main__":
    unittest.main()
