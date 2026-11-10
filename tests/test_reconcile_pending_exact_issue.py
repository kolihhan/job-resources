import sys
from pathlib import Path
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from reconcile_pending_exact_issue import reconcile, issue_role_match

URL="https://jobs.ashbyhq.com/example/11111111-1111-4111-8111-111111111111"

def state():
    return {"version":1,"market":"SG","next_seq":2,"next_unacknowledged_seq":1,
            "last_ingestion":None,"terminal":[],
            "pending":[{"key":"sg:1","seq":1,"state":"UNVERIFIED_INDEX","market":"SG",
                        "company":"Example Inc", "title":"AI Engineer (Graduate)", "url":URL}]}

def issue(number=12, role="AI Engineer (Graduate)", company="Example Inc", url=URL):
    return {"number":number,"state":"closed","title":f"[REJECTED][SG] {company} — {role}",
            "body":f"Official role: {url}"}

class PrivateIssueAckTests(unittest.TestCase):
    def test_exact_url_company_title_are_all_required(self):
        s=state()
        out=reconcile(s,[issue()],checked_at="2026-11-10T12:30:00+00:00")
        self.assertEqual(out["verified_duplicates"],1)
        self.assertEqual(s["pending"],[])
        self.assertEqual(s["terminal"][0]["issue_url"],
                         "https://github.com/kolihhan/job-resources/issues/12")
        self.assertEqual(s["terminal"][0]["state"],"DUPLICATE_CONFIRMED")
        self.assertEqual(s["next_unacknowledged_seq"],s["next_seq"])

    def test_weak_or_sibling_role_never_auto_duplicate(self):
        for i in (issue(url="https://jobs.ashbyhq.com/example/22222222-2222-4222-8222-222222222222"),
                  issue(company="Different Inc"), issue(role="AI Engineer (Senior)"),
                  {"number":10,"title":"[WAIT] Example Inc — AI Engineer (Graduate)","body":"No official role link"}):
            s=state()
            out=reconcile(s,[i])
            self.assertEqual(out["verified_duplicates"],0)
            self.assertEqual(len(s["pending"]),1)

    def test_multiple_matching_issues_remain_pending(self):
        s=state()
        out=reconcile(s,[issue(9),issue(10)])
        self.assertEqual(out["ambiguous"],1)
        self.assertEqual(len(s["terminal"]),0)

    def test_non_issue_and_weak_role_skip(self):
        s=state()
        i=issue()
        i["pull_request"]={"url":"https://github.com/example/pull/12"}
        out=reconcile(s,[i])
        self.assertEqual(out["verified_duplicates"],0)

    def test_same_role_other_platform_only_private_hint_never_terminal(self):
        s = state()
        original = issue(number=640, company="Example Inc",
                         role="AI Engineer (Graduate)",
                         url="https://www.linkedin.com/jobs/view/4478262632")
        out = reconcile(s,[original])
        self.assertEqual(out["verified_duplicates"],0)
        self.assertEqual(out["history_hints_added"],1)
        self.assertEqual(out["possible_cross_platform"],1)
        self.assertEqual(len(s["pending"]),1)
        self.assertEqual(s["terminal"],[])
        self.assertEqual(s["pending"][0]["consumer_review"]["possible_prior_issue"],640)
        again = reconcile(s,[original])
        self.assertEqual(again["history_hints_added"],0)

    def test_cross_platform_hint_does_not_merge_sibling_role(self):
        s=state()
        out=reconcile(s,[issue(number=10,role="AI Engineer (Senior)",
                               url="https://www.linkedin.com/jobs/view/4478262632")])
        self.assertEqual(out["possible_cross_platform"],0)
        self.assertNotIn("consumer_review",s["pending"][0])

    def test_ambiguous_cross_platform_titles_no_hint(self):
        s=state()
        a=issue(number=21,url="https://www.linkedin.com/jobs/view/4478262632")
        b=issue(number=22,url="https://www.linkedin.com/jobs/view/4478262633")
        out=reconcile(s,[a,b])
        self.assertEqual(out["possible_cross_platform"],0)
        self.assertEqual(out["verified_duplicates"],0)
        self.assertNotIn("consumer_review",s["pending"][0])

    def test_different_market_not_a_cross_platform_hint(self):
        s=state()
        i=issue(url="https://www.linkedin.com/jobs/view/4478262632")
        i["title"]=i["title"].replace("[SG]","[MY]")
        out=reconcile(s,[i])
        self.assertEqual(out["history_hints_added"],0)

if __name__=="__main__":
    unittest.main()
