import sys
from datetime import datetime,timezone,timedelta
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import platform_index_queue as q
import consume_my_ashby_queue as m

NOW=datetime(2026,11,7,12,tzinfo=timezone.utc)
ID="c35bae67-de6c-45b7-b116-4c30a8c6ac73"
LINK="https://jobs.ashbyhq.com/gen-digital/"+ID

def seed():
    s=q.new_state("MY")
    s,_=q.ingest(s,{},{"source":"gen-digital:official-ashby:MY","items":[
         {"market":"MY","url":LINK,"title":"AI Applied Scientist","company":"Gen Digital / MoneyLion"}]})
    return s

def board():
    return {"jobs":[{"id":ID,"title":"AI Applied Scientist",
      "location":"MYS - Kuala Lumpur","jobUrl":LINK,
      "employmentType":"FullTime",
      "descriptionPlain":"Build LLM and RAG agent systems with evaluation, testing, software engineering and production reliability."*2}]}

class MYConsumerTest(unittest.TestCase):
    def test_firstparty_public_jd_review_is_not_apply(self):
        s,report=m.run(seed(),[{"number":1,"title":"Unrelated role"}],board(),
                       confirm_issue=lambda *_:True,now=NOW)
        self.assertEqual(report["verified_jd"],1)
        self.assertEqual(len(s["pending"]),1)
        review=s["pending"][0]["consumer_review"]
        self.assertEqual(review["stage"],"FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW")
        self.assertEqual(review["source_verified_can_apply"],"NOT_ASSERTED_BY_ASHBY_FEED")
        self.assertTrue(review["full_jd_complete"])
        self.assertEqual(review["full_jd_text"],board()["jobs"][0]["descriptionPlain"])
        self.assertEqual(s["next_unacknowledged_seq"],1)
    def test_exact_source_url_live_issue_readback_acks(self):
        issue={"number":999,"title":"[CHECK][MY] Gen Digital","body":"Official role "+LINK}
        s,report=m.run(seed(),[issue],board(),
                       confirm_issue=lambda i,u:(i.endswith("999") and u==LINK),now=NOW)
        self.assertEqual(report["issue_ack"],1)
        self.assertEqual(len(s["pending"]),0)
        self.assertEqual(s["terminal"][0]["state"],"ISSUE_VERIFIED")
    def test_sibling_role_title_does_not_auto_close(self):
        issue={"number":999,"title":"MoneyLion AI Applied Scientist","body":"Another job in this team."}
        s,report=m.run(seed(),[issue],board(),
                       confirm_issue=lambda *_:True,now=NOW)
        self.assertEqual(report["issue_ack"],0)
        self.assertEqual(report["verified_jd"],1)
    def test_missing_board_job_retains_uncertainty(self):
        s,r=m.run(seed(),[{"number":1,"title":"Other"}],{"jobs":[]},
                   confirm_issue=lambda *_:True,now=NOW)
        self.assertEqual(s["pending"][0]["consumer_review"]["stage"],
                         "NOT_PRESENT_ON_CURRENT_BOARD_RECHECK")
        self.assertEqual(len(s["terminal"]),0)
    def test_wrong_exact_url_fails_closed(self):
        b=board()
        b["jobs"][0]["jobUrl"]="https://jobs.ashbyhq.com/other-org/"+ID
        s,r=m.run(seed(),[{"number":1,"title":"Other"}],b,
                   confirm_issue=lambda *_:True,now=NOW)
        self.assertEqual(s["pending"][0]["consumer_review"]["stage"],"FETCH_OR_IDENTITY_RETRY")
        self.assertEqual(r["verified_jd"],0)
    def test_no_full_issue_history_or_invalid_board_rejected(self):
        with self.assertRaisesRegex(ValueError,"Full GitHub"):
            m.run(seed(),[],board(),confirm_issue=lambda *_:True,now=NOW)
        with self.assertRaisesRegex(ValueError,"complete first-party"):
            m.run(seed(),[{"number":1}],{"message":"blocked"},confirm_issue=lambda *_:True,now=NOW)
    def test_recent_rerun_is_idempotent(self):
        s,_=m.run(seed(),[{"number":1}],board(),confirm_issue=lambda *_:True,now=NOW)
        s,r=m.run(s,[{"number":1}],board(),confirm_issue=lambda *_:True,
                  now=NOW+timedelta(hours=1))
        self.assertEqual(r["considered"],0)
        self.assertEqual(len(s["pending"]),1)
if __name__=="__main__":unittest.main()
