import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from intake_official_ats import candidate, choose, process_market, run
from platform_index_queue import canonical, new_state, validate_state


def job(market, n, company, title, provider="ashby"):
    rid = f"e8d71da1-0000-4000-8000-{n:012d}"
    if provider == "ashby":
        url = f"https://jobs.ashbyhq.com/{company.lower().replace(' ', '-')}/{rid}"
    elif provider == "greenhouse":
        url = f"https://job-boards.greenhouse.io/{company.lower()}/jobs/{5000000000+n}"
    else:
        url = f"https://jobs.smartrecruiters.com/{company.replace(' ','')}/7440000{n:08d}"
    return {
        "market": market, "ats": provider, "company": company,
        "job_id": rid if provider == "ashby" else str(n),
        "key": f"source:{company}:{n}", "title": title, "url": url,
        "location": market, "evidence": "full_jd", "lane": "AI",
        "triage_priority": "HIGH", "description_excerpt": "Build LLM RAG evaluation",
    }


class OfficialATSIntakeTests(unittest.TestCase):
    def test_vendor_paths_canonical_and_untrusted_pages_rejected(self):
        self.assertEqual(canonical(job("CN", 1, "Abound", "AI Engineer")["url"],"CN"),
                         job("CN", 1, "Abound", "AI Engineer")["url"])
        self.assertEqual(canonical("https://job-boards.greenhouse.io/binance/jobs/5002667101?gh_src=ad","SG"),
                         "https://job-boards.greenhouse.io/binance/jobs/5002667101")
        self.assertEqual(canonical("https://jobs.lever.co/patsnap/79e4620d-10b5-44c4-8954-199811fa9884","SG"),
                         "https://jobs.lever.co/patsnap/79e4620d-10b5-44c4-8954-199811fa9884")
        self.assertEqual(canonical("https://jobs.smartrecruiters.com/NCS3/6000000001339954","SG"),
                         "https://jobs.smartrecruiters.com/NCS3/6000000001339954")
        self.assertEqual(canonical("https://micron.wd1.myworkdayjobs.com/External/job/Fab-10A-Singapore/AI-Engineer_JR111138","SG"),
                         "https://micron.wd1.myworkdayjobs.com/External/job/Fab-10A-Singapore/AI-Engineer_JR111138")
        for url in ("https://evil.example/jobs/123", "http://jobs.ashbyhq.com/abound/id",
                    "https://jobs.ashbyhq.com/abound", "https://jobs.ashbyhq.com/abound/incomplete",
                    "https://jobs.ashbyhq.com@evil.example/abound/80efb9bf-1575-4f0a-8e82-23cd003abac1"):
            with self.subTest(url=url):
                self.assertIsNone(canonical(url,"CN"))

    def test_live_unverified_cn_source_is_queueable(self):
        state=new_state("CN")
        feed={"market":"CN","jobs":[job("CN",1,"Abound","AI Engineer")]}
        out,stats=process_market("CN",feed,state,{"strong":{"urls":[]}},limit=4)
        self.assertEqual(stats["created"],1)
        self.assertEqual(stats["selected_by_track_hint"],{"ENG":1,"RES":0})
        self.assertEqual(out["pending"][0]["state"],"UNVERIFIED_INDEX")
        self.assertEqual(out["pending"][0]["source"],"freehirefetch:official-ats:CN")
        self.assertEqual(out["pending"][0]["source_evidence"],"full_jd")
        self.assertNotIn("full_jd_text",out["pending"][0])
        validate_state(out,"CN")

    def test_previous_wait_is_advisory_not_hard_suppression(self):
        row=job("MY",2,"Gen Digital MoneyLion","AI Applied Scientist")
        state,stats=process_market("MY",{"market":"MY","jobs":[row]},
               new_state("MY"),{"strong":{"urls":[]},"weak":{
                   "wait_employers":["gen digital moneylion"]}})
        self.assertEqual(stats["created"],1)
        self.assertTrue(state["pending"][0]["prior_wait_employer_hint"])
        self.assertEqual(stats["prior_wait_employer_hints"],1)

    def test_known_exact_and_existing_are_suppressed_before_deep_review(self):
        a,b=job("SG",1,"Beta","LLM Engineer"),job("SG",2,"Gamma","Research Engineer")
        known={"strong":{"urls":[a["url"]]}}
        state,first=process_market("SG",{"market":"SG","jobs":[a,b]},
                                   new_state("SG"),known)
        self.assertEqual(first["created"],1)
        self.assertEqual(first["known_exact_history"],1)
        updated,again=process_market("SG",{"market":"SG","jobs":[a,b]},state,known)
        self.assertEqual(again["created"],0)
        self.assertEqual(again["already_in_source_queue"],1)
        self.assertEqual(updated["next_seq"],state["next_seq"])

    def test_company_cap_preserves_diversity_and_both_tracks(self):
        rows=[job("SG",i,"Bjak","AI Engineer") for i in range(1,12)]
        rows.extend([job("SG",20,"Acme","Research Engineer"),
                     job("SG",21,"Beta","Research Associate"),
                     job("SG",22,"Gamma","LLM Engineer")])
        updated,stats=process_market("SG",{"market":"SG","jobs":rows},
                                     new_state("SG"),{},limit=8,company_cap=2)
        self.assertEqual(stats["created"],5)
        self.assertLessEqual(sum(x["company"]=="Bjak" for x in updated["pending"]),2)
        self.assertEqual(stats["selected_by_track_hint"]["RES"],2)
        self.assertEqual(len({x["company"] for x in updated["pending"]}),4)

    def test_failed_source_not_zero_and_does_not_change_queue(self):
        s=new_state("CN")
        original=json.dumps(s,sort_keys=True)
        after,stats=process_market("CN",None,s,{})
        self.assertEqual(json.dumps(after,sort_keys=True),original)
        self.assertIsNone(stats["observed"])
        self.assertIn("ATS_SNAPSHOT_MISSING_NOT_ZERO_JOBS",stats["coverage_gaps"])

    def test_untrusted_url_and_bad_contract_not_imported(self):
        invalid=job("MY",3,"A","AI Engineer")
        invalid["url"]="https://example.org/fake"
        out,stats=process_market("MY",{"market":"MY","jobs":[invalid]},
                                 new_state("MY"),{})
        self.assertEqual(stats["created"],0)
        self.assertEqual(stats["bad_rows"],1)
        with self.assertRaisesRegex(ValueError,"contract mismatch"):
            process_market("MY",{"market":"SG","jobs":[]},new_state("MY"),{})

    def test_run_is_replay_safe_and_does_not_create_extra_tracking_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            snaps=root/"snapshots"; snaps.mkdir()
            (snaps/"CN.json").write_text(json.dumps({
                "market":"CN","jobs":[job("CN",1,"Abound","AI Engineer")]}))
            (root/"discovery-state").mkdir()
            (root/"discovery-state"/"platform-index-my.json").write_text(
                json.dumps(new_state("MY")))
            first=run(root,snaps,{"strong":{"urls":[]}})
            second=run(root,snaps,{"strong":{"urls":[]}})
            self.assertEqual(first["markets"]["CN"]["created"],1)
            self.assertEqual(second["markets"]["CN"]["created"],0)
            self.assertEqual(second["markets"]["SG"]["source"],"UNAVAILABLE")
            self.assertEqual(set(p.name for p in (root/"discovery-state").iterdir()),
                             {"platform-index-my.json","platform-index-cn.json"})


if __name__ == "__main__":
    unittest.main()
