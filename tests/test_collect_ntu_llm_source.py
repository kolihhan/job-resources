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
    def test_pagination_cursor_resumes_debt_without_skipping_fresh_head(self):
        calls=[]
        def search(url,payload):
            if payload is None:raise AssertionError("No candidate JDs in generic pages")
            calls.append((payload["searchText"],payload["offset"]))
            return {"jobPostings":[{"title":"Finance Admin","externalPath":"/job/X-_R00020001"} for _ in range(20)]}
        r=s.source_scan(search,False)
        self.assertEqual(r["coverage"],"PARTIAL_COVERAGE")
        self.assertEqual(r["next_offsets"],{"LLM":60,"agent":60})
        calls.clear()
        r2=s.source_scan(search,False,start_offsets=r["next_offsets"])
        self.assertEqual(calls,[("LLM",0),("LLM",60),("LLM",80),
                                ("agent",0),("agent",60),("agent",80)])
        self.assertEqual(r2["next_offsets"],{"LLM":100,"agent":100})

    def test_exact_known_requisition_skips_detail_fetch(self):
        paths=[]
        def f(url,payload):
            if payload is not None:
                return {"jobPostings":[{"title":"Research Engineer I","externalPath":"/job/X-_R00026164-1"}]}
            paths.append(url)
            raise AssertionError("Known req must not be re-opened")
        r=s.source_scan(f,False,known_reqs={"R00026164"})
        self.assertEqual(r["strong_history_id_suppressed"],1)
        self.assertEqual(r["items"],[])
        self.assertEqual(paths,[])

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
