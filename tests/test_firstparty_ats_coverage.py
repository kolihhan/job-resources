"""Regression checks: exact identity, market isolation, fail-closed source coverage."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from probe_firstparty_ats_coverage import in_market,role,probe

ID="b0c59b18-231e-4a65-8b5c-a0ab65ec3861"

class FirstPartyATSTests(unittest.TestCase):
    def test_market_filter(self):
        self.assertTrue(in_market("SG","Singapore"))
        self.assertFalse(in_market("MY","Singapore"))
        self.assertTrue(in_market("MY","Petaling Jaya"))
        self.assertFalse(in_market("SG","Kuala Lumpur"))
    def test_greenhouse_true_identity(self):
        def get(url):
            if url.endswith("/jobs"):
                return {"jobs":[{"id":123456,"title":"AI Engineer","location":{"name":"Shah Alam, Malaysia"}},
                                {"id":555111,"title":"AI Engineer","location":{"name":"New York"}}]}
            if url.endswith("/123456"):
                return {"id":123456,"content":"Build production AI agents, RAG retrieval and evaluation."}
            raise AssertionError(url)
        x=probe(("MY","New Era Technology","greenhouse","neweratech"),get)
        self.assertEqual(x["status"],"BOUNDED_SOURCE_END")
        self.assertEqual(len(x["items"]),1)
        self.assertTrue(x["items"][0]["jd_verified"])
        self.assertIn("/neweratech/jobs/123456",x["items"][0]["url"])
    def test_ashby_only_listed_local_generic_agent(self):
        def get(url):
            return {"jobs":[
                {"id":ID,"title":"Backend Engineer","location":"Petaling Jaya, Malaysia","descriptionPlain":"Build LLM agents with RAG and retrieval.","isListed":True},
                {"id":"11111111-1111-4111-8111-111111111111","title":"AI Engineer","location":"Singapore","isListed":True},
                {"id":"22222222-2222-4222-8222-222222222222","title":"AI Engineer","location":"Kuala Lumpur","isListed":False}
            ]}
        x=probe(("MY","Bjak","ashby","bjakcareer"),get)
        self.assertEqual(len(x["items"]),1)
        self.assertEqual(x["items"][0]["signal"],"generic_engineering_with_AI_JD")
    def test_generic_backend_without_AI_rejected(self):
        self.assertIsNone(role("MY","Bjak","ashby","bjakcareer",ID,
            "Backend Engineer","Kuala Lumpur","Build ordinary REST APIs and databases."))
    def test_senior_title_is_flag_only(self):
        x=role("SG","NCS","smartrecruiters","NCS3","6000000001234567",
               "Senior AI Engineer","Singapore","Build AI agents and RAG evaluation")
        self.assertTrue(x["senior_title_flag"])
    def test_failure_is_not_reported_as_empty_market(self):
        def failing(_):raise OSError("blocked")
        x=probe(("SG","NCS","smartrecruiters","NCS3"),failing)
        self.assertEqual(x["status"],"SOURCE_ERROR")
        self.assertNotIn("source_rows",x)
    def test_smartrecruiters_detail_failure_is_partial(self):
        def get(url):
            if "offset=0" in url:
                return {"content":[{"id":"6000000001234567","name":"AI Engineer",
                    "location":{"country":"SG","city":"Singapore"}}],"totalFound":1}
            raise ValueError("detail unavailable")
        x=probe(("SG","NCS","smartrecruiters","NCS3"),get)
        self.assertEqual(x["status"],"PARTIAL_COVERAGE")
        self.assertFalse(x["items"][0]["jd_verified"])
        self.assertEqual(len(x["pages"]),1)

if __name__=="__main__":unittest.main()
