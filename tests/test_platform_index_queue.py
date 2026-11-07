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
        s=q.ack(s,{"key":key,"action":"HARD_REJECTED","evidence_url":"https://sg.jobstreet.com/job/95566693","reason":"JD explicitly requires five years experience"})
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
    def test_duplicate_claim_needs_actual_issue_proof(self):
        s=q.new_state("SG")
        s,_=q.ingest(s,{},{"source":"index-test","items":[{"url":"https://sg.jobstreet.com/job/12345678"}]})
        k=s["pending"][0]["key"]
        with self.assertRaisesRegex(ValueError,"Issue URL"):
            q.ack(s,{"key":k,"action":"DUPLICATE_CONFIRMED","evidence_url":"https://sg.jobstreet.com/job/12345678"})
        with self.assertRaisesRegex(ValueError,"readback"):
            q.ack(s,{"key":k,"action":"DUPLICATE_CONFIRMED","issue_url":"https://github.com/kolihhan/job-resources/issues/175",
                     "evidence_url":"https://sg.jobstreet.com/job/12345678"})

    def test_readback_checks_issue_body_canonical_identity(self):
        import io
        from unittest.mock import patch
        class Response(io.BytesIO):
            pass
        issue={"number":123,"body":"exact source https://sg.jobstreet.com/job/12345678?tracking=x"}
        with patch.object(q,"urlopen",return_value=Response(__import__("json").dumps(issue).encode())):
            self.assertTrue(q.verify_issue_readback("https://github.com/kolihhan/job-resources/issues/123",
                          "https://sg.jobstreet.com/job/12345678","token"))
        with patch.object(q,"urlopen",return_value=Response(b'{"number":123,"body":"unrelated listing"}')):
            with self.assertRaisesRegex(ValueError,"exact source identity"):
                q.verify_issue_readback("https://github.com/kolihhan/job-resources/issues/123",
                          "https://sg.jobstreet.com/job/12345678","token")


    def test_idempotent_feed_updates_blank_company_only(self):
        s=q.new_state("SG")
        source={"source":"devglobal:public-api:SG","items":[{"market":"SG","url":"https://devglobaljobs.com/jobs/detail/174081606","title":"Applied AI Engineer, Codex","company":""}]}
        s,a=q.ingest(s,{},source)
        source["items"][0]["company"]="OpenAI"
        s,b=q.ingest(s,{},source)
        self.assertEqual(len(s["pending"]),1)
        self.assertEqual(s["pending"][0]["company"],"OpenAI")
        self.assertEqual(b["already_seen"],1)
        self.assertEqual(s["pending"][0]["seq"],1)

    def test_ntu_first_party_cxs_requisition_links_are_normalized(self):
        a="https://ntu.wd3.myworkdayjobs.com/en-US/careers/job/NTU-Main-Campus-Singapore/Research-Engineer-I--Trust-Technologies-_R00026164-1"
        b="https://ntu.wd3.myworkdayjobs.com/Careers/job/NTU-Main-Campus-Singapore/Research-Engineer-I--Trust-Technologies-_R00026164-1"
        # Valid first-party Workday URL is an actual clickable job link, not
        # a synthetic source key or misleading title-only company match.
        self.assertEqual(q.canonical(a,"SG"),b)
        self.assertEqual(q.canonical(b,"SG"),b)
        self.assertIsNone(q.canonical(a,"MY"))
        self.assertIsNone(q.canonical("https://example.com/job/x_R00026164-1","SG"))

    def test_my_gen_digital_ashby_exact_uuid_source(self):
        u="https://jobs.ashbyhq.com/gen-digital/c35bae67-de6c-45b7-b116-4c30a8c6ac73?utm=x"
        want="https://jobs.ashbyhq.com/gen-digital/c35bae67-de6c-45b7-b116-4c30a8c6ac73"
        self.assertEqual(q.canonical(u,"MY"),want)
        self.assertIsNone(q.canonical(u,"SG"))
        self.assertIsNone(q.canonical("https://jobs.ashbyhq.com/gen-digital/invalid","MY"))
        s=q.new_state("MY")
        payload={"source":"gen-digital:official-ashby:MY","items":[
            {"market":"MY","platform":"Gen Digital official Ashby","url":want,
             "title":"AI Applied Scientist","company":"Gen Digital / MoneyLion"}]}
        s,stats=q.ingest(s,{},payload)
        self.assertEqual(stats["new_pending"],1)
        self.assertEqual(s["pending"][0]["url"],want)
        s,again=q.ingest(s,{},payload)
        self.assertEqual(again["already_seen"],1)

    def test_devglobal_feed_urls_are_explicitly_separate_from_native_board(self):
        self.assertEqual(q.canonical("https://devglobaljobs.com/jobs/detail/174081606?ref=api","SG"),
                         "https://devglobaljobs.com/jobs/detail/174081606")
        self.assertIsNone(q.canonical("https://devglobaljobs.com/jobs","SG"))
        s=q.new_state("SG")
        p={"source":"devglobal:public-api:SG","items":[
           {"market":"SG","platform":"Dev Global Jobs (public aggregator)",
            "url":"https://devglobaljobs.com/jobs/detail/174081606",
            "title":"Applied AI Engineer, Codex","company":"OpenAI"}]}
        s,stats=q.ingest(s,{},p)
        self.assertEqual(stats["new_pending"],1)
        self.assertEqual(s["pending"][0]["source"],"devglobal:public-api:SG")
        self.assertEqual(s["pending"][0]["url"],"https://devglobaljobs.com/jobs/detail/174081606")
        s,stats=q.ingest(s,{},p)
        self.assertEqual(stats["already_seen"],1)

    def test_ntu_workday_issue_readback_by_exact_declared_req(self):
        import io
        from unittest.mock import patch
        class Response(io.BytesIO): pass
        issue={"number":596,"title":"[WAIT][SG] NTU ATMRI — Research Engineer I — R00026053",
               "body":"## Exact role\n- Requisition: `R00026053`\nLocation: Singapore"}
        link="https://ntu.wd3.myworkdayjobs.com/Careers/job/NTU-Main-Campus-Singapore/Research-Engineer-I--Computer-Science---Artificial-Intelligence---Software-Engineering---Information-Systems-_R00026053"
        with patch.object(q,"urlopen",return_value=Response(__import__("json").dumps(issue).encode())):
            self.assertTrue(q.verify_issue_readback("https://github.com/kolihhan/job-resources/issues/596",link,"token"))
        sibling={"number":596,"title":"[WAIT] NTU Research Engineer II R00026162",
                 "body":"## Exact role\n- Requisition: `R00026162`\nRelated earlier role R00026053"}
        with patch.object(q,"urlopen",return_value=Response(__import__("json").dumps(sibling).encode())):
            with self.assertRaisesRegex(ValueError,"exact source identity"):
                q.verify_issue_readback("https://github.com/kolihhan/job-resources/issues/596",link,"token")

    def test_ntu_workday_issue_readback_from_exact_url(self):
        import io
        from unittest.mock import patch
        class Response(io.BytesIO): pass
        link="https://ntu.wd3.myworkdayjobs.com/Careers/job/NTU-Main-Campus-Singapore/AI-Safety---Governance-Engineer--SAGE-_R00025725"
        issue={"number":871,"title":"AI Safety & Governance Engineer R00025725",
               "body":"First party application route: "+link+"\nEvidence: verified"}
        with patch.object(q,"urlopen",return_value=Response(__import__("json").dumps(issue).encode())):
            self.assertTrue(q.verify_issue_readback("https://github.com/kolihhan/job-resources/issues/871",link,"token"))

    def test_invalid_queue_is_fail_closed(self):
        s=q.new_state("MY")
        s["next_unacknowledged_seq"]=99
        with self.assertRaisesRegex(ValueError,"unacknowledged"):
            q.validate_state(s,"MY")

if __name__=="__main__":
    unittest.main()
