"""Fail-closed tests for first-party public ATS enrichment."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from enrich_pending_public_ats import api_url, enrich_market, source_of

ASHBY = "https://jobs.ashbyhq.com/lab-ai/11111111-1111-4111-8111-111111111111"
GH = "https://job-boards.eu.greenhouse.io/alpha/jobs/5000000001"
DESCRIPTION = "We build language model retrieval and agent evaluation systems. " * 18


def queue(market, *entries):
    rows = [{"key":f"{market.lower()}:{i}", "seq":i, "state":"UNVERIFIED_INDEX",
             "market":market, "url":url, "title":title, "company":"Employer"}
            for i, (url,title) in enumerate(entries,1)]
    return {"version":1,"market":market,"pending":rows,"terminal":[],
            "next_seq":len(rows)+1,"next_unacknowledged_seq":1 if rows else 1,
            "last_ingestion":None}


def ashby_job(location="Singapore", title="AI Engineer", listed=True):
    return {"id":"11111111-1111-4111-8111-111111111111",
            "title":title,"location":location,"isListed":listed,
            "descriptionPlain":DESCRIPTION,"employmentType":"FullTime"}


class EnrichTest(unittest.TestCase):
    def test_restricts_endpoint_and_does_not_fetch_queue_url(self):
        self.assertEqual(source_of(ASHBY), ("ashby","lab-ai","11111111-1111-4111-8111-111111111111"))
        self.assertEqual(source_of(GH), ("greenhouse","alpha","5000000001"))
        for url in ("http://jobs.ashbyhq.com/a/1", "https://bad.invalid/job/1",
                    "https://jobs.ashbyhq.com@evil.invalid/x/y",
                    "https://jobs.ashbyhq.com/../../secrets",
                    "https://jobs.ashbyhq.com:444/lab/11111111-1111-4111-8111-111111111111"):
            self.assertIsNone(source_of(url))
        self.assertTrue(api_url("ashby","lab-ai").startswith("https://api.ashbyhq.com/"))
        self.assertTrue(api_url("greenhouse","alpha").startswith("https://boards-api.greenhouse.io/"))

    def test_ashby_verified_exact_title_location_and_full_jd(self):
        s=queue("SG",(ASHBY,"AI Engineer"))
        called=[]
        def fetch(url):
            called.append(url)
            return {"jobs":[ashby_job()]}
        out=enrich_market(s, fetch=fetch, checked_at="2026-11-10T11:00:00+00:00")
        self.assertEqual(out["verified_full_jd"],1)
        self.assertEqual(len(called),1)
        r=s["pending"][0]["consumer_review"]
        self.assertTrue(r["full_jd_complete"])
        self.assertTrue(r["source_verified_can_apply"])
        self.assertIn("HUMAN_FIT", " ".join(r["review_flags"]))
        self.assertEqual(len(s["pending"]),1)
        self.assertEqual(len(s["terminal"]),0)

    def test_wrong_market_or_title_or_unlisted_never_promoted(self):
        for job in (ashby_job(location="Malaysia"),ashby_job(title="Senior Data Scientist"),
                    ashby_job(listed=False)):
            s=queue("SG",(ASHBY,"AI Engineer"))
            out=enrich_market(s,fetch=lambda url: {"jobs":[job]})
            self.assertEqual(out["verified_full_jd"],0)
            self.assertNotIn("consumer_review",s["pending"][0])

    def test_greenhouse_matches_post_id_and_decodes_html(self):
        s=queue("SG",(GH,"LLM Engineer"))
        job={"id":5000000001,"title":"LLM Engineer",
             "location":{"name":"Singapore"},
             "content":"<p>Work on RAG &amp; evaluation.</p><p>"+DESCRIPTION+"</p>"}
        result=enrich_market(s,fetch=lambda url: {"jobs":[job]})
        self.assertEqual(result["verified_full_jd"],1)
        body=s["pending"][0]["consumer_review"]["full_jd_text"]
        self.assertIn("RAG & evaluation",body)
        self.assertNotIn("<p>",body)

    def test_failure_keeps_candidate_and_preserves_source_state(self):
        s=queue("MY",(ASHBY,"AI Engineer"))
        def fail(_): raise TimeoutError("rate limit")
        out=enrich_market(s,fetch=fail)
        self.assertEqual(out["api_errors"],1)
        self.assertEqual(s["pending"][0]["state"],"UNVERIFIED_INDEX")
        self.assertNotIn("consumer_review",s["pending"][0])

    def test_single_board_fetch_and_bounded_processing(self):
        another="https://jobs.ashbyhq.com/lab-ai/22222222-2222-4222-8222-222222222222"
        s=queue("SG",(ASHBY,"AI Engineer"),(another,"LLM Engineer"))
        calls=[]
        def fetch(u):
            calls.append(u)
            return {"jobs":[ashby_job()]}
        out=enrich_market(s,fetch=fetch,max_rows=1)
        self.assertEqual(len(calls),1)
        self.assertEqual(out["verified_full_jd"],1)
        self.assertEqual(out["skipped_budget"],1)

    def test_already_verified_is_preserved(self):
        s=queue("SG",(ASHBY,"AI Engineer"))
        s["pending"][0]["consumer_review"]={"stage":"FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW",
                                             "full_jd_complete":True,"full_jd_text":"Existing"}
        r=enrich_market(s,fetch=lambda _: (_ for _ in ()).throw(RuntimeError("must not fetch")))
        self.assertEqual(r["boards_attempted"],0)
        self.assertEqual(s["pending"][0]["consumer_review"]["full_jd_text"],"Existing")


if __name__=="__main__":
    unittest.main()
