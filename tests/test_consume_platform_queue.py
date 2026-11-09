import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import platform_index_queue as q

spec = importlib.util.spec_from_file_location("consumer", SCRIPTS / "consume_platform_queue.py")
consumer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(consumer)

NOW = datetime(2026, 11, 7, 12, 0, tzinfo=timezone.utc)
ROLE = ("https://ntu.wd3.myworkdayjobs.com/Careers/job/NTU-Main-Campus-Singapore/"
        "Research-Engineer-I--Trust-Technologies-_R00026164-1")
OTHER = ("https://ntu.wd3.myworkdayjobs.com/Careers/job/NTU-Main-Campus-Singapore/"
         "Research-Engineer-II--Trust-Technologies-_R00026159")


def seed(*urls):
    s = q.new_state("SG")
    s, _ = q.ingest(s, {}, {"source": "ntu:official-cxs:SG", "items": [
        {"market": "SG", "url": u, "title": "Research Engineer", "company": "NTU"}
        for u in urls]})
    return s


def jd(req="R00026164", can_apply=True, description="LLM agents and RAG with evaluation"):
    return {"jobPostingInfo": {
        "jobReqId": req, "canApply": can_apply,
        "jobDescription": "<p>" + description + "</p>",
        "timeType": "Full time", "title": "Research Engineer I"}}


class ConsumerTests(unittest.TestCase):
    def test_existing_issue_ack_requires_exact_id_in_title_and_verified_readback(self):
        s = seed(ROLE)
        issue = {"number": 869, "title": "[CHECK] NTU R00026164", "body": "Requisition R00026164"}
        called = []
        def confirm(u, role):
            called.append((u, role))
            return True
        def no_detail(url, token):
            raise AssertionError("known requisition should be deduped BEFORE full JD fetch")
        state, report = consumer.run_consumer(s, [issue], get=no_detail,
                                              confirm_issue=confirm, now=NOW)
        self.assertEqual(len(state["pending"]), 0)
        self.assertEqual(state["terminal"][0]["state"], "ISSUE_VERIFIED")
        self.assertEqual(report["issue_ack"], 1)
        self.assertEqual(len(called), 1)
        self.assertEqual(state["next_unacknowledged_seq"], 2)

    def test_body_only_sibling_reference_never_closes_job(self):
        s = seed(ROLE)
        history = [{"number": 596, "title": "[WAIT] NTU R00026053",
                    "body": "Other open role is R00026164"}]
        state, report = consumer.run_consumer(s, history, get=lambda url, token: jd(),
                                             confirm_issue=lambda *_: True, now=NOW)
        self.assertEqual(report["issue_ack"], 0)
        self.assertEqual(report["firstparty_jds_verified"], 1)
        self.assertEqual(state["pending"][0]["consumer_review"]["stage"],
                         "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW")
        self.assertIn("rag", state["pending"][0]["consumer_review"]["signals"])
        review = state["pending"][0]["consumer_review"]
        self.assertEqual(review["full_jd_text"], "LLM agents and RAG with evaluation")
        self.assertTrue(review["full_jd_complete"])
        self.assertEqual(review["jd_chars"], len(review["full_jd_text"]))
        self.assertEqual(state["next_unacknowledged_seq"], 1)

    def test_closed_employer_can_apply_false_requires_exact_req_match(self):
        s = seed(ROLE, OTHER)
        history = [{"number": 1, "title": "Unrelated Issue"}]
        def fetch(url, token):
            if "R00026164" in url:
                return jd(can_apply=False)
            return jd(req="R00000000", can_apply=False)
        state, report = consumer.run_consumer(s, history, get=fetch,
                                             confirm_issue=lambda *_: True, now=NOW)
        self.assertEqual(report["closed_by_employer"], 1)
        self.assertEqual(report["errors"], 1)
        self.assertEqual(len(state["pending"]), 1)
        self.assertEqual(state["pending"][0]["consumer_review"]["stage"],
                         "FETCH_OR_IDENTITY_RETRY")
        self.assertEqual(state["next_unacknowledged_seq"], 2)

    def test_source_unavailable_or_unknown_does_not_disappear(self):
        s = seed(ROLE)
        history = [{"number": 1, "title": "Other requisition"}]
        state, report = consumer.run_consumer(
            s, history,
            get=lambda url, token: (_ for _ in ()).throw(ConnectionError("403")),
            confirm_issue=lambda *_: True, now=NOW)
        self.assertEqual(report["errors"], 1)
        self.assertEqual(len(state["pending"]), 1)
        self.assertEqual(state["pending"][0]["seq"], 1)
        self.assertEqual(state["next_unacknowledged_seq"], 1)

    def test_unsupported_aggregator_requires_employer_canonical(self):
        s = q.new_state("SG")
        s, _ = q.ingest(s, {}, {"source": "devglobal:public-api:SG", "items": [
            {"url": "https://devglobaljobs.com/jobs/detail/168411325", "title": "AI Agent Engineer"}]})
        history = [{"number": 1, "title": "Another Issue"}]
        state, report = consumer.run_consumer(
            s, history, confirm_issue=lambda *_: True, now=NOW)
        self.assertEqual(report["needs_canonical_route"], 1)
        self.assertEqual(len(state["pending"]), 1)
        self.assertEqual(state["pending"][0]["consumer_review"]["stage"],
                         "NEEDS_EMPLOYER_CANONICAL_ROUTE")

    def test_recent_review_not_reprocessed_and_dated_review_resumes(self):
        s = seed(ROLE)
        history = [{"number": 1, "title": "No match"}]
        calls = []
        def fetch(url, token):
            calls.append(url)
            return jd()
        state, report = consumer.run_consumer(
            s, history, get=fetch, confirm_issue=lambda *_: True, now=NOW)
        self.assertEqual(len(calls), 1)
        state, report = consumer.run_consumer(
            state, history, get=fetch, confirm_issue=lambda *_: True,
            now=NOW + timedelta(hours=1))
        self.assertEqual(len(calls), 1)
        self.assertEqual(report["considered"], 0)
        state, report = consumer.run_consumer(
            state, history, get=fetch, confirm_issue=lambda *_: True,
            now=NOW + timedelta(hours=49))
        self.assertEqual(len(calls), 2)
        self.assertEqual(report["firstparty_jds_verified"], 1)

    def test_ambiguous_same_id_is_never_acknowledged(self):
        s = seed(ROLE)
        history = [{"number": 1, "title": "NTU R00026164"},
                   {"number": 2, "title": "NTU R00026164 duplicate"}]
        state, report = consumer.run_consumer(s, history,
                                             confirm_issue=lambda *_: True, now=NOW)
        self.assertEqual(report["errors"], 1)
        self.assertEqual(len(state["pending"]), 1)

    def test_legacy_excerpt_only_verified_jd_refreshes_once_without_waiting_48h(self):
        s = seed(ROLE)
        s["pending"][0]["consumer_review"] = {
            "stage": "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW",
            "checked_at": NOW.isoformat()}
        history = [{"number": 1, "title": "Unrelated"}]
        state, report = consumer.run_consumer(
            s, history, get=lambda url, token: jd(),
            confirm_issue=lambda *_: True, now=NOW + timedelta(hours=1))
        self.assertEqual(report["firstparty_jds_verified"], 1)
        self.assertTrue(state["pending"][0]["consumer_review"]["full_jd_complete"])

    def test_oversized_official_jd_does_not_pretend_to_be_complete(self):
        info = {"jobReqId": "R00026164", "canApply": True,
                "jobDescription": "<p>" + "Agent evaluation " * 2500 + "</p>"}
        review = consumer.review_summary(info, NOW.isoformat())
        self.assertFalse(review["full_jd_complete"])
        self.assertIsNone(review["full_jd_text"])
        self.assertGreater(review["jd_chars"], consumer.MAX_REVIEW_JD_CHARS)
        self.assertEqual(review["stage"], "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW")

    def test_missing_full_history_fails_closed(self):
        s = seed(ROLE)
        with self.assertRaisesRegex(ValueError, "Full GitHub Issue history"):
            consumer.run_consumer(s, [], confirm_issue=lambda *_: True, now=NOW)

    def test_issue_pagination_and_fail_closed_page_cap(self):
        def get(url, token):
            if url.endswith("page=1"):
                return [{"number": i, "title": f"position {i}"} for i in range(100)]
            return [{"number": 101, "title": "position 101"}]
        history = consumer.full_issue_history("token", get=get)
        self.assertEqual(len(history), 101)
        self.assertEqual(consumer.issue_for_req("R00026164", [
            {"number": 1, "title": "R00026053", "body": "R00026164"},
            {"number": 2, "title": "R00026164"}])["number"], 2)


if __name__ == "__main__":
    unittest.main()
