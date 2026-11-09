import json
from pathlib import Path
import sys
import tempfile
import unittest
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import collect_market_api as api


URL = "https://jobs.ashbyhq.com/exampleai/12345678-1234-1234-1234-123456789abc"
FREEHIRE = {
    "public_slug": "example-ai-engineer", "title": "AI Engineer - Agent Platform",
    "company": "Example AI", "countries": ["SG"], "location": "Central Region",
    "url": URL+"?utm_source=freehire.me", "description": "Build RAG evaluation",
}
AIDEV = {
    "id": "adv-123", "title": "AI Engineer - Agent Platform",
    "company_name": "Example AI", "location": "Singapore",
    "apply_url": URL+"/application",
    "url": "https://aidevboard.com/job/adv-123",
    "job_type": "full-time", "description": "Build LLM agents and RAG",
}


def fake_api(url):
    parts = urlparse(url)
    params = parse_qs(parts.query)
    if parts.hostname == "freehire.me":
        assert params["countries"] in (["SG"], ["MY"], ["CN"])
        return {"data": [FREEHIRE] if params["countries"] == ["SG"] and
                params.get("offset") == ["0"] else [],
                "meta": {"total": 1 if params["countries"] == ["SG"] else 0,
                         "limit": 50, "offset": int(params.get("offset", ["0"])[0])}}
    if parts.hostname == "aidevboard.com":
        return {"jobs": [AIDEV] if params["location"] == ["Singapore"] and
                params.get("page") == ["1"] else [],
                "has_next": False, "total": 1}
    raise ValueError("unexpected API")


class FreeJobAPIContractTests(unittest.TestCase):
    def test_freehire_country_facet_not_text_location(self):
        self.assertEqual(api.normalize_freehire(FREEHIRE,"SG")["url"],URL)
        self.assertIsNone(api.normalize_freehire(FREEHIRE,"MY"))
        m=dict(FREEHIRE, url="https://www.mycareersfuture.gov.sg/job/123")
        self.assertIsNone(api.normalize_freehire(m,"SG"))
        m=dict(FREEHIRE,countries=["MY"],location="Singapore")
        self.assertIsNone(api.normalize_freehire(m,"SG"))

    def test_aidevboard_ashby_application_suffix_becomes_exact_role(self):
        item=api.normalize_aidevboard(AIDEV,"SG")
        self.assertEqual(item["url"],URL)
        self.assertEqual(item["source"],"aidevboard:public-api:SG")
        self.assertEqual(item["evidence"],"listing_only")
        self.assertIsNone(api.normalize_aidevboard(AIDEV,"CN"))
        self.assertIsNone(api.normalize_aidevboard(dict(AIDEV,title="Sales Manager"),"SG"))
        self.assertIsNone(api.normalize_aidevboard(
            dict(AIDEV,apply_url="https://evil.example/apply"),"SG"))

    def test_merged_providers_dedupe_on_employer_url(self):
        result=api.collect("SG",fetch=fake_api,max_pages=2)
        self.assertEqual(len(result["jobs"]),1)
        self.assertIn(result["jobs"][0]["source"],
                      ("freehire:public-api:SG","aidevboard:public-api:SG"))
        self.assertTrue(all(s["status"]=="COMPLETE"
                            for s in result["providers"].values()))

    def test_api_pagination_and_partial_failure_are_explicit(self):
        pages=[]
        def paged(url):
            p=urlparse(url)
            q=parse_qs(p.query)
            pages.append((p.hostname,q))
            if p.hostname=="freehire.me":
                offset=int(q["offset"][0])
                return {"data":[dict(FREEHIRE,public_slug="a-"+str(offset),
                                     url=URL)] if offset==0 else [],
                        "meta":{"total":51,"limit":50,"offset":offset}}
            if p.hostname=="aidevboard.com":
                if q["page"]==["2"]:
                    raise OSError("simulated page 2 outage")
                return {"jobs":[AIDEV],"has_next":True,"total":51}
        result=api.collect("SG",fetch=paged,max_pages=2)
        self.assertEqual(result["providers"]["aidevboard"]["status"],"PARTIAL")
        self.assertEqual(result["providers"]["freehire"]["status"],"PARTIAL")
        self.assertTrue(any(host=="aidevboard.com" and q["page"]==["2"]
                            for host,q in pages))
        self.assertEqual(len(result["jobs"]),1)

    def test_ignored_country_filter_is_not_accepted(self):
        def ignored(url):
            if "freehire.me" in url:
                return {"data":[FREEHIRE],"meta":{"total":1,"limit":50,
                        "offset":0,"ignored_params":["countries"]}}
            return {"jobs":[],"has_next":False,"total":0}
        result=api.collect("MY",fetch=ignored,max_pages=1)
        self.assertEqual(result["providers"]["freehire"]["status"],"UNAVAILABLE")
        self.assertEqual(len(result["jobs"]),0)

    def test_all_api_errors_preserve_unknown_coverage(self):
        def outage(_):
            raise OSError("no public API")
        report=api.collect("CN",fetch=outage,max_pages=1)
        self.assertEqual(report["providers"]["freehire"]["status"],"UNAVAILABLE")
        self.assertEqual(report["providers"]["aidevboard"]["status"],"UNAVAILABLE")
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(RuntimeError,"All API markets unavailable"):
                api.run(Path(d),fetch=outage,max_pages=1)
            self.assertTrue((Path(d)/"health.json").exists())

    def test_chinese_native_language_role_preserved(self):
        cn=dict(FREEHIRE,public_slug="cn",title="大模型算法工程师",
                countries=["CN"],location="北京，中国")
        self.assertEqual(api.normalize_freehire(cn,"CN")["market"],"CN")
        self.assertIsNone(api.normalize_freehire(cn,"SG"))


if __name__=="__main__":
    unittest.main()
