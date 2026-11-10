"""Public upstream batch -> private evidence hydration, never applicant verdict."""
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import enrich_pending_public_ats as source

JOB="https://jobs.ashbyhq.com/example/11111111-1111-4111-8111-111111111111"
OTHER="https://jobs.ashbyhq.com/example/22222222-2222-4222-8222-222222222222"
NOW=datetime(2026,11,10,11,30,tzinfo=timezone.utc)
DOC="Build reliable RAG and AI agent systems with evaluation and provenance. "*12

def state(market="SG", url=JOB, title="AI Engineer"):
    return {"version":1,"market":market,"next_seq":2,
            "next_unacknowledged_seq":1,"terminal":[],"last_ingestion":None,
            "pending":[{"market":market,"key":"sg:identity","seq":1,"state":"UNVERIFIED_INDEX",
                        "url":url,"title":title,"company":"Example"}]}

def batch(market="SG", url=JOB, title="AI Engineer", checked=None):
    return {"version":2,"parts":[{"market":market,"path":market+"-000.json","count":1}],
            "jobs":[{"market":market,"key":"example|ashby|11111111-1111-4111-8111-111111111111",
                     "url":url,"title":title,"part":market+"-000.json",
                     "checked_at":checked or NOW.isoformat(), "description_truncated":False}]}

def chunk(url=JOB, title="AI Engineer", trunc=False, doc=DOC):
    return {"version":1,"jobs":[{"key":"example|ashby|11111111-1111-4111-8111-111111111111",
            "url":url, "title":title,"description_truncated":trunc,
            "description_text":doc}]}

class UpstreamEvidenceTests(unittest.TestCase):
    def test_full_jd_matches_exact_url_key_market_title(self):
        s=state()
        calls=[]
        def read(part):
            calls.append(part)
            return chunk()
        report=source.enrich_market(s,batch(),fetch=read,now=NOW)
        self.assertEqual(report["full_jd_imported"],1)
        self.assertEqual(calls,["SG-000.json"])
        item=s["pending"][0]["consumer_review"]
        self.assertIn("RAG",item["full_jd_text"])
        self.assertEqual(item["source_kind"],"freehirefetch public first-party ATS batch")
        self.assertFalse(item["source_verified_can_apply"])
        self.assertEqual(item["stage"],"FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW")
        self.assertEqual(len(s["pending"]),1)
        self.assertEqual(len(s["terminal"]),0)

    def test_different_title_or_market_or_exact_url_is_not_mixed(self):
        for b in (batch("MY"),batch(title="Data Scientist"),
                  batch(url=OTHER)):
            s=state()
            r=source.enrich_market(s,b,fetch=lambda _:chunk(),now=NOW)
            self.assertEqual(r["full_jd_imported"],0)
            self.assertNotIn("consumer_review",s["pending"][0])

    def test_unmatched_shard_identity_and_truncated_jd(self):
        for payload in (chunk(url=OTHER),chunk(title="Different"),chunk(trunc=True),
                        chunk(doc="too short"),{"version":7,"jobs":[]}):
            s=state()
            r=source.enrich_market(s,batch(),fetch=lambda _:payload,now=NOW)
            self.assertEqual(r["full_jd_imported"],0)
            self.assertNotIn("consumer_review",s["pending"][0])

    def test_stale_or_future_sources_not_promoted(self):
        for t in (NOW-timedelta(days=5),NOW+timedelta(hours=1)):
            s=state()
            r=source.enrich_market(s,batch(checked=t.isoformat()),fetch=lambda _:chunk(),now=NOW)
            self.assertEqual(r["skipped_stale"],1)
            self.assertNotIn("consumer_review",s["pending"][0])

    def test_failed_public_shard_preserves_pending(self):
        s=state()
        def unavailable(_):raise OSError("upstream GitHub unavailable")
        r=source.enrich_market(s,batch(),fetch=unavailable,now=NOW)
        self.assertEqual(r["parts_failed"],1)
        self.assertEqual(s["pending"][0]["state"],"UNVERIFIED_INDEX")
        self.assertEqual(len(s["terminal"]),0)

    def test_existing_verified_jd_preserved(self):
        s=state()
        s["pending"][0]["consumer_review"]={"full_jd_complete":True,"full_jd_text":"existing verified original"}
        r=source.enrich_market(s,batch(),fetch=lambda _: (_ for _ in ()).throw(RuntimeError("must not fetch")),now=NOW)
        self.assertEqual(r["already_complete"],1)
        self.assertEqual(r["parts_fetched"],0)
        self.assertEqual(s["pending"][0]["consumer_review"]["full_jd_text"],"existing verified original")

    def test_allowlist_upstream_path_no_arbitrary_url(self):
        self.assertEqual(source.PART_NAME.fullmatch("SG-000.json").group(),"SG-000.json")
        for path in ("../secrets","https://fake/x.json","SG-001.json?x=1","MY-foo.json"):
            with self.assertRaises(ValueError):
                source.get_public_json(path)
        s=state()
        r=source.enrich_market(s,{"version":1},fetch=lambda _:chunk(),now=NOW)
        self.assertEqual(r["source_state"],"INCOMPATIBLE_BATCH_INDEX")

if __name__=="__main__":
    unittest.main()
