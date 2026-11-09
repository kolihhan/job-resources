import json
from pathlib import Path
import sys
import tempfile
import unittest
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
import collect_market_api as api


ROLE = {
    "id": "av-job-1", "title": "AI Engineer - Agent Platform",
    "company": {"name": "Example AI"}, "location": "Singapore",
    "applyUrl": "https://jobs.ashbyhq.com/exampleai/12345678-1234-1234-1234-123456789abc",
    "url": "https://activevacancies.com/jobs/exampleai-1",
    "employmentType": "full_time",
}


class APICollectorTests(unittest.TestCase):
    def test_strict_market_and_exact_employer_apply_url(self):
        role = dict(ROLE)
        self.assertEqual(api.normalize(role, "SG")["source"], "activevacancies:public-api:SG")
        self.assertIsNone(api.normalize(role, "CN"))
        role["applyUrl"] = "https://www.mycareersfuture.gov.sg/job/123"
        self.assertIsNone(api.normalize(role, "SG"))
        role["applyUrl"] = "https://example.com/not-employer-job"
        self.assertIsNone(api.normalize(role, "SG"))
        role["applyUrl"] = "https://jobs.ashbyhq.com@evil.example/123"
        self.assertIsNone(api.normalize(role, "SG"))
        role["applyUrl"] = ROLE["applyUrl"]
        role["title"] = "Account Executive"
        self.assertIsNone(api.normalize(role, "SG"))

    def test_pagination_cursor_and_duplicate_job_urls(self):
        seen = []
        def fake(url):
            p = parse_qs(urlparse(url).query)
            seen.append(p)
            if p.get("after") == ["cursor-1"]:
                return {"success": True, "data": [dict(ROLE, id="av-job-2")],
                        "pagination": {"hasNextPage": False}}
            return {"success": True, "data": [ROLE],
                    "pagination": {"hasNextPage": True, "nextCursor": "cursor-1"}}
        result = api.collect("SG", fetch=fake)
        self.assertEqual(result["coverage"], "COMPLETE")
        self.assertEqual(len(result["jobs"]), 1)
        self.assertTrue(any(x.get("after") == ["cursor-1"] for x in seen))
        self.assertEqual(len(seen), 2 * len(api.QUERIES))

    def test_source_failure_is_partial_or_unavailable_never_zero_market(self):
        def outage(_):
            raise OSError("test outage")
        result = api.collect("CN", fetch=outage)
        self.assertEqual(result["coverage"], "UNAVAILABLE")
        self.assertTrue(result["errors"])
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(RuntimeError, "All API markets unavailable"):
                api.run(Path(d), fetch=outage)
            self.assertTrue((Path(d) / "health.json").exists())

    def test_market_job_type_and_chinese_title(self):
        my = dict(ROLE, id="my-1", title="AI Engineer", location="Kuala Lumpur, Malaysia")
        self.assertIsNotNone(api.normalize(my, "MY"))
        self.assertIsNone(api.normalize(my, "SG"))
        my["employmentType"] = "contract"
        self.assertIsNone(api.normalize(my, "MY"))
        cn = dict(ROLE, id="cn-1", title="大模型算法工程师", location="Shenzhen, China")
        self.assertEqual(api.normalize(cn, "CN")["market"], "CN")
        self.assertIsNone(api.normalize(cn, "MY"))


if __name__ == "__main__":
    unittest.main()
