import importlib.util
from datetime import datetime,timezone
from pathlib import Path
import unittest
p=Path(__file__).resolve().parents[1]/"scripts"/"report_job_pipeline_health.py"
s=importlib.util.spec_from_file_location("pipeline_health",p)
h=importlib.util.module_from_spec(s)
s.loader.exec_module(h)
NOW=datetime(2026,11,7,12,tzinfo=timezone.utc)

class HealthTests(unittest.TestCase):
    def test_source_concentration_not_falsely_market_coverage(self):
        q={"version":1,"market":"SG","next_unacknowledged_seq":1,
           "pending":[
             {"seq":1,"source":"ntu:official-cxs:SG","first_seen_at":"2026-11-06T12:00:00Z",
              "consumer_review":{"stage":"FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW"}},
             {"seq":2,"source":"ntu:official-cxs:SG","first_seen_at":"2026-11-07T08:00:00Z"},
             {"seq":3,"source":"devglobal:public-api:SG","first_seen_at":"2026-11-07T08:00:00Z",
              "consumer_review":{"stage":"FETCH_OR_IDENTITY_RETRY"}}],
           "terminal":[{"seq":0}],"last_ingestion":{"at":"2026-11-07T09:00:00Z",
             "source":"ntu:official-cxs:SG"}}
        r=h.measure_queue(q,NOW)
        self.assertEqual(r["pending"],3)
        self.assertEqual(r["jd_verified_awaiting_fit"],1)
        self.assertEqual(r["unreviewed"],1)
        self.assertEqual(r["retry_needed"],1)
        self.assertEqual(r["oldest_pending_age_hours"],24)
        self.assertAlmostEqual(r["high_concentration"],2/3)
        self.assertEqual(r["hours_since_ingestion"],3)
    def test_scheduled_not_claimed_from_push_success(self):
        runs=[{"name":"SG Conservative Queue Consumer","event":"push",
            "created_at":"2026-11-07T11:00:00Z","conclusion":"success",
            "html_url":"https://github.com/example/1"}]
        r=h.measure_runs(runs,NOW)
        sg=r["SG Conservative Queue Consumer"]
        self.assertEqual(sg["latest_conclusion"],"success")
        self.assertFalse(sg["scheduled_execution_observed_in_last_100"])
        self.assertIsNone(sg["last_scheduled_conclusion"])
    def test_schedule_proof_and_report(self):
        runs=[{"name":"MY TOP Conservative First-Party JD Consumer","event":"schedule",
            "created_at":"2026-11-07T11:30:00Z","conclusion":"success",
            "html_url":"https://github.com/example/2"}]
        r=h.measure_runs(runs,NOW)
        key="MY TOP Conservative First-Party JD Consumer"
        self.assertTrue(r[key]["scheduled_execution_observed_in_last_100"])
        s=h.summarize({"queues":[{"market":"MY","pending":1,"jd_verified_awaiting_fit":1,
              "unreviewed":0,"retry_needed":0,"oldest_pending_age_hours":4}],
               "workflows":r})
        self.assertIn("Scheduled run seen?",s)
        self.assertIn("CN consumer is not covered",s)
if __name__=="__main__":unittest.main()
