import importlib.util
from pathlib import Path
import unittest

p=Path(__file__).resolve().parents[1]/"scripts"/"probe_grab_smartrecruiters.py"
spec=importlib.util.spec_from_file_location("grab_probe",p)
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

class GrabPublicFeedTest(unittest.TestCase):
    def test_exact_location_and_identity(self):
        good={"id":"744000123456789","name":"AI Engineer","location":{"country":"my","city":"Petaling Jaya"}}
        bad={"id":"744000123456888","name":"AI Engineer","location":{"country":"SG","city":"Singapore"}}
        self.assertEqual(g.filter_listing(good,"MY")["source_id"],"744000123456789")
        self.assertIsNone(g.filter_listing(bad,"MY"))
        self.assertIsNone(g.filter_listing({"id":"xx","name":"AI Engineer","location":{"country":"MY"}},"MY"))
    def test_title_not_generic_bad_fit(self):
        self.assertIsNone(g.filter_listing({"id":"11111111","name":"Sales Associate",
            "location":{"country":"MY"}},"MY"))
        self.assertTrue(g.filter_listing({"id":"11111112","name":"Senior AI Engineer",
            "location":{"country":"SG"}},"SG")["seniority_flag"])
    def test_distinct_role_pages_and_detail(self):
        def fetch(url):
            if "/postings/" in url:
                return {"id":"744000123456789","name":"AI Engineer",
                       "location":{"country":"my","city":"PJ"},"jobAd":"LLM RAG"}
            return {"totalFound":1,"content":[{"id":"744000123456789","name":"AI Engineer",
                "location":{"country":"my","city":"PJ"}}]}
        result=g.scan_market("MY",fetch,False)
        self.assertEqual(result["status"],"BOUNDED_SOURCE_END")
        self.assertEqual(len(result["items"]),1)
        self.assertEqual(result["detail_verified"],1)
    def test_closed_or_schema_error_preserves_debt(self):
        result=g.scan_market("MY",lambda _:{"totalFound":5,"data":[]},False)
        self.assertEqual(result["items"],[])
        self.assertEqual(result["status"],"PARTIAL_OR_UNAVAILABLE")
        self.assertEqual(len(result["errors"]),1)
    def test_detail_country_mismatch_not_verified(self):
        def fetch(url):
            if "/postings/" in url:
                return {"id":"744000123456789","name":"AI Engineer",
                        "location":{"country":"SG"}}
            return {"totalFound":1,"content":[{"id":"744000123456789","name":"AI Engineer",
                "location":{"country":"my"}}]}
        result=g.scan_market("MY",fetch,False)
        self.assertEqual(result["detail_verified"],0)
        self.assertEqual(result["status"],"PARTIAL_OR_UNAVAILABLE")

if __name__=="__main__":unittest.main()
