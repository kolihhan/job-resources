import unittest
from datetime import datetime, timezone, timedelta
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_review_dispatch import build_dispatch, allowed_ats_url, classify_track

NOW = datetime(2026, 11, 9, 12, tzinfo=timezone.utc)


def pending(market, seq, title, company="NTU", stage="FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW",
            complete=True, checked="2026-11-09T08:00:00Z"):
    return {"market":market, "seq":seq, "key":market + ":" + str(seq),
            "company":company, "title":title,
            "source":"ntu:official-cxs:SG" if market=="SG" else "gen-digital:official-ashby:MY",
            "url": "https://ntu.wd3.myworkdayjobs.com/Careers/job/Role_R0000" + str(seq).zfill(4),
            "first_seen_at":"2026-11-07T00:00:00Z",
            "consumer_review":{"stage":stage,"checked_at":checked,"full_jd_complete":complete,
              "jd_sha256":"a" * 64, "review_flags":[],"signals":["agent"]}}


def ats(market, n, title, company, key=None, evidence="full_jd", lane="AI"):
    jid=f"5a5a5a5a-0000-4000-8000-{n:012d}"
    return {"market":market, "key": key or f"{company}|ashby|{jid}",
            "job_id": jid, "company":company,"title":title,
            "location":market, "evidence":evidence, "lane":lane,
            "first_seen_at":"2026-11-09T01:00:00Z",
            "url":f"https://jobs.ashbyhq.com/{company.lower().replace(' ','-')}/{jid}"}


class DispatchTests(unittest.TestCase):
    def test_title_routing_only_never_claims_candidate_fit(self):
        self.assertEqual(classify_track("Research Engineer II (AI Agents)"), "RES")
        self.assertEqual(classify_track("AI Applied Scientist"), "RES")
        self.assertEqual(classify_track("Machine Learning Engineer"), "ENG")
        self.assertEqual(classify_track("Full-Stack Developer"), "ENG")

    def test_origin_and_jd_proof_distinguished_from_ats_feed(self):
        p=pending("SG", 3, "Research Engineer I")
        a=ats("SG", 1, "LLM Engineer", "A")
        report=build_dispatch({"SG":{"market":"SG","pending":[p],"terminal":[]}},
                              {"SG":{"market":"SG","jobs":[a]}}, {"strong":{"urls":[]}}, now=NOW)
        selected=report["markets"]["SG"]["selected"]
        by_origin={s["origin"]:s for s in selected}
        self.assertEqual(by_origin["official_queue"]["status"],"JD_VERIFIED_FIT_REVIEW_DUE")
        self.assertEqual(by_origin["ats_feed"]["status"],"NEEDS_LIVE_OFFICIAL_JD_AND_FIT")
        self.assertNotIn("full_jd_text",str(selected))
        self.assertNotIn("APPLY", str(selected))
        self.assertEqual(by_origin["official_queue"]["queue_seq"],3)
        self.assertEqual(report["markets"]["SG"]["selected_by_track"],{"ENG":1,"RES":1})

    def test_mixed_tracks_get_reserved_share_when_both_exist(self):
        p=[pending("SG",n, "Research Engineer I",company="University" + str(n)) for n in range(1,7)]
        jobs=[ats("SG",n, "LLM Engineer", "AICompany" + str(n)) for n in range(1,7)]
        result=build_dispatch({"SG":{"market":"SG","pending":p,"terminal":[]}},
                              {"SG":{"market":"SG","jobs":jobs}}, {"strong":{"urls":[]}},
                              now=NOW,limit_per_market=8,min_each_track=3)
        self.assertEqual(len(result["markets"]["SG"]["selected"]),8)
        self.assertGreaterEqual(result["markets"]["SG"]["selected_by_track"]["ENG"],3)
        self.assertGreaterEqual(result["markets"]["SG"]["selected_by_track"]["RES"],3)

    def test_source_diversity_before_same_employer_overflow(self):
        jobs=[ats("MY",n,"AI Engineer", "BJAK") for n in range(1,10)]
        jobs += [ats("MY",10,"AI Engineer","Grab"),ats("MY",11,"AI Engineer","Gen Digital")]
        result=build_dispatch({}, {"MY":{"market":"MY","jobs":jobs}}, {"strong":{"urls":[]}},
                              now=NOW,limit_per_market=5)
        names=[x["company"] for x in result["markets"]["MY"]["selected"]]
        self.assertIn("Grab",names)
        self.assertIn("Gen Digital",names)
        self.assertLessEqual(names.count("BJAK"),3)

    def test_exact_history_suppression_is_advisory_not_fresh_dedupe_proof(self):
        a=ats("SG",2,"LLM Engineer","CompanyX")
        report=build_dispatch({},{"SG":{"market":"SG","jobs":[a]}},
                              {"strong":{"urls":[a["url"]]}},now=NOW)
        self.assertEqual(report["markets"]["SG"]["selected"],[])
        self.assertEqual(report["markets"]["SG"]["suppressed_exact_snapshot_url"],1)
        self.assertIn("snapshot",report["limits"]["dedupe"])

    def test_incomplete_legacy_and_old_jd_cannot_claim_review_ready(self):
        old=(NOW-timedelta(hours=60)).isoformat()
        p1=pending("SG",1,"Research Engineer I",complete=False)
        p2=pending("SG",2,"Research Engineer II",checked=old)
        report=build_dispatch({"SG":{"market":"SG","pending":[p1,p2],"terminal":[]}}, {},
                              {"strong":{"urls":[]}},now=NOW)
        rows=report["markets"]["SG"]["selected"]
        self.assertEqual([x["status"] for x in rows],
                         ["JD_INCOMPLETE_FETCH_DUE","JD_STALE_REVERIFY_DUE"])
        self.assertEqual(report["markets"]["SG"]["verified_waiting_fit"],2)
        self.assertEqual(report["markets"]["SG"]["current_full_jd_for_fit"],0)

    def test_bad_url_ignored_and_missing_feed_not_reported_as_exhausted(self):
        self.assertFalse(allowed_ats_url("https://someblog.net/job/1"))
        self.assertTrue(allowed_ats_url("https://job-boards.eu.greenhouse.io/binance/jobs/12"))
        invalid=ats("CN",1,"AI Engineer","A")
        invalid["url"]="https://evil.example.com/phishing"
        result=build_dispatch({},{"CN":{"market":"CN","jobs":[invalid]}},
                              {"strong":{"urls":[]}},now=NOW)
        self.assertEqual(result["markets"]["CN"]["selected"],[])
        self.assertEqual(result["markets"]["CN"]["bad_source_rows"],1)
        self.assertEqual(result["markets"]["MY"]["ats_snapshot_state"],"UNAVAILABLE")
        self.assertEqual(result["markets"]["MY"]["ats_rows_observed"],None)

    def test_lesser_evidence_and_mature_title_not_falsely_rejected(self):
        a=ats("SG",3,"Senior AI Engineer","Acme")
        b=ats("SG",4,"LLM Engineer","Beta",evidence="listing_only")
        result=build_dispatch({},{"SG":{"market":"SG","jobs":[a,b]}},
                              {"strong":{"urls":[]}},now=NOW)
        rows=result["markets"]["SG"]["selected"]
        self.assertEqual(len(rows),2)
        self.assertTrue(next(x for x in rows if x["title"].startswith("Senior"))["title_maturity_flag"])
        self.assertEqual(next(x for x in rows if x["company"]=="Beta")["status"],
                         "NEEDS_FULL_JD_AND_LIVE_ROUTE")
        self.assertEqual(result["markets"]["SG"]["hard_rejects_this_run"],0)

    def test_ats_same_url_as_official_pending_never_double_counts(self):
        a=ats("SG",1,"LLM Engineer","Acme")
        p=pending("SG",1,"Research Engineer I")
        p["url"]=a["url"]
        result=build_dispatch({"SG":{"market":"SG","pending":[p],"terminal":[]}},
                              {"SG":{"market":"SG","jobs":[a]}}, {"strong":{"urls":[]}}, now=NOW)
        self.assertEqual(result["markets"]["SG"]["unique_review_candidates"],1)
        self.assertEqual(len(result["markets"]["SG"]["selected"]),1)
        self.assertEqual(result["markets"]["SG"]["selected"][0]["origin"],"official_queue")


if __name__ == "__main__":
    unittest.main()
