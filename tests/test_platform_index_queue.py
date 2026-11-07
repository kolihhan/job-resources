import importlib.util
from pathlib import Path
import unittest

P = Path(__file__).parents[1] / "scripts" / "platform_index_queue.py"
spec=importlib.util.spec_from_file_location("platform_index_queue",P)
q=importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)

class IndexQueueTests(unittest.TestCase):
    def test_ingest_strong_duplicate_and_pending(self):
        s=q.new_state("MY")
        known={"strong":{"urls":["https://my.jobstreet.com/job/12345678?utm_source=z"]},"weak":{"company_title":["acme|ai engineer"]}}
        payload={"source":"verified-index-pilot","items":[
            {"market":"MY","platform":"JobStreet","url":"https://my.jobstreet.com/job/12345678","title":"AI Engineer","company":"ACME"},
            {"market":"MY","platform":"LinkedIn","url":"https://my.linkedin.com/jobs/view/ai-engineer-4456087297","title":"AI Engineer","company":"ACME"},
            {"market":"MY","platform":"JobStreet","url":"https://my.jobstreet.com/job/12345678","title":"duplicate"},
            {"market":"SG","url":"https://sg.jobstreet.com/job/87654321","title":"cross market"},
            {"market":"MY","url":"https://my.jobstreet.com/ai-engineer-jobs","title":"category"}]}
        s,stat=q.ingest(s,known,payload)
        self.assertEqual(stat["exact_history"],1)
        self.assertEqual(stat["new_pending"],1)
        self.assertEqual(stat["already_seen"],1)
        self.assertEqual(stat["market_mismatch"],1)
        self.assertEqual(stat["invalid_url"],1)
        self.assertEqual(s["pending"][0]["seq"],2)
        self.assertEqual(s["next_unacknowledged_seq"],2)
        q.validate_state(s,"MY")
    def test_reingest_idempotent_and_ack_evidence(self):
        s=q.new_state("SG")
        i={"source":"independent-test","items":[{"url":"https://sg.jobstreet.com/job/95566693","title":"AI Engineer","platform":"JobStreet"}]}
        s,a=q.ingest(s,{"strong":{"urls":[]}},i)
        s,b=q.ingest(s,{"strong":{"urls":[]}},i)
        self.assertEqual(b["already_seen"],1)
        key=s["pending"][0]["key"]
        with self.assertRaisesRegex(ValueError,"evidence"):
            q.ack(s,{"key":key,"action":"HARD_REJECTED"})
        s=q.ack(s,{"key":key,"action":"RETRY","reason":"authoritative employer JD page temporarily unavailable"})
        self.assertEqual(s["next_unacknowledged_seq"],1)
        s=q.ack(s,{"key":key,"action":"HARD_REJECTED","evidence_url":"https://sg.jobstreet.com/job/95566693"})
        self.assertEqual(s["next_unacknowledged_seq"],2)
        self.assertEqual(len(s["pending"]),0)
        q.validate_state(s,"SG")
    def test_issue_claim_requires_structured_proof(self):
        s=q.new_state("MY")
        s,_=q.ingest(s,{},{"source":"test","items":[{"url":"https://my.jobstreet.com/job/98765432"}]})
        key=s["pending"][0]["key"]
        with self.assertRaisesRegex(ValueError,"Issue URL"):
            q.ack(s,{"key":key,"action":"ISSUE_VERIFIED","evidence_url":"https://my.jobstreet.com/job/98765432"})
        with self.assertRaisesRegex(ValueError,"readback"):
            q.ack(s,{"key":key,"action":"ISSUE_VERIFIED","evidence_url":"https://my.jobstreet.com/job/98765432",
                      "issue_url":"https://github.com/kolihhan/job-resources/issues/1234"})
    def test_invalid_queue_is_fail_closed(self):
        s=q.new_state("MY")
        s["next_unacknowledged_seq"]=99
        with self.assertRaisesRegex(ValueError,"unacknowledged"):
            q.validate_state(s,"MY")

if __name__=="__main__":
    unittest.main()
