import importlib.util
from pathlib import Path
import unittest

P=Path(__file__).parents[1]/"scripts"/"collect_ntu_llm_source.py"
spec=importlib.util.spec_from_file_location("official_ntu",P)
s=importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)

class OfficialNTUSourceTests(unittest.TestCase):
    def test_two_searches_dedupe_exact_req_and_require_true_apply(self):
        def f(url,payload):
            if url.endswith("/jobs"):
                return {"total":2,"jobPostings":[
                    {"title":"Research Engineer I (Trust Technologies)",
                     "externalPath":"/job/NTU-Main-Campus-Singapore/Research-Engineer-I--Trust-Technologies-_R00026164-1",
                     "postedOn":"Posted 2 Days Ago"},
                    {"title":"Senior Research Engineer","externalPath":"/job/X-_R00026200"}]}
            return {"jobPostingInfo":{"jobReqId":"R00026164","canApply":True,
                "title":"Research Engineer I (Trust Technologies)",
                "jobDescription":"Build LLM-based agents and RAG evaluation pipelines",
                "externalUrl":"https://ntu.wd3.myworkdayjobs.com/Careers/job/NTU-Main-Campus-Singapore/Research-Engineer-I--Trust-Technologies-_R00026164-1",
                "startDate":"2026-10-28","location":"Singapore"}}
        r=s.source_scan(f,False)
        self.assertEqual(r["title_candidates"],1)
        self.assertEqual([x["source_id"] for x in r["items"]],["R00026164"])
        self.assertEqual(r["coverage"],"BOUNDED_QUERY_EXHAUSTED")
        self.assertEqual(r["items"][0]["source_kind"],"official_employer")
    def test_block_mismatched_or_closed_role_without_hiding_query_debt(self):
        def f(url,payload):
            if url.endswith("/jobs"):
                if payload["searchText"]=="agent":raise ConnectionError("one query failed")
                return {"total":1,"jobPostings":[
                    {"title":"Research Associate (AI in Education)",
                     "externalPath":"/job/X-_R00026285-1"}]}
            return {"jobPostingInfo":{"jobReqId":"R00026285","canApply":False,
                "title":"Research Associate (AI in Education)",
                "jobDescription":"LLM agents","externalUrl":"https://ntu.wd3.myworkdayjobs.com/Careers/job/X-_R00026285-1"}}
        r=s.source_scan(f,False)
        self.assertEqual(r["coverage"],"PARTIAL_COVERAGE")
        self.assertEqual(r["items"],[])
        self.assertTrue(any(x["state"]=="SOURCE_FETCH_FAILED" for x in r["list_probes"]))
    def test_fail_closed_on_no_access(self):
        with self.assertRaisesRegex(RuntimeError,"Source not scanned"):
            s.source_scan(lambda url,payload: (_ for _ in ()).throw(ConnectionError("403")),False)
    def test_wrong_req_never_enters_queue(self):
        def f(url,payload):
            if url.endswith("/jobs"):
                return {"jobPostings":[{"title":"Research Engineer II","externalPath":"/job/A-_R00026162-1"}]}
            return {"jobPostingInfo":{"jobReqId":"R00099999","canApply":True,
               "jobDescription":"LLM Agent RAG",
               "externalUrl":"https://ntu.wd3.myworkdayjobs.com/Careers/job/A-_R00026162-1"}}
        r=s.source_scan(f,False)
        self.assertEqual(r["items"],[])
        self.assertEqual(len(r["details_failed"]),1)
        self.assertEqual(r["coverage"],"PARTIAL_COVERAGE")
if __name__=="__main__":unittest.main()
