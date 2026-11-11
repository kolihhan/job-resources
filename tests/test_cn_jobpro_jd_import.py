"""Direct public employer JD evidence -> exact existing CN Pending row, no APPLY."""
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from enrich_pending_public_ats import enrich_cn_jobpro

URL = "https://join.qq.com/post_detail.html?postid=1282707398326592512"
ID = "1282707398326592512"
TITLE = "AI全栈工程师"
WHEN = "2026-11-11T04:00:00+00:00"
NOW = datetime(2026, 11, 11, 4, 15, tzinfo=timezone.utc)
DESC = "负责构建 Agent RAG 检索与评测平台，开发后端和可用性测试，实现可部署的 AI 应用系统。" * 5
REQ = "计算机相关本科或者硕士学位，熟悉 Python 工程实践和大语言模型工具调用，具备团队协作能力。" * 5
FULL = "岗位职责 / Responsibilities\n" + DESC + "\n任职要求 / Requirements\n" + REQ


def state():
    return {"version": 1, "market": "CN", "next_seq": 2,
            "next_unacknowledged_seq": 1, "terminal": [], "last_ingestion": None,
            "pending": [{
                "market": "CN", "key": "cn:test", "seq": 1, "state": "UNVERIFIED_INDEX",
                "source": "jobpro:public-employer-api:CN",
                "url": URL, "title": TITLE, "company": "tencent",
                "ats_key": "jobpro:tencent:" + ID, "source_job_id": ID,
            }]}


def batch():
    return {"version": 1, "source": "jobpro-public-employer-detail",
            "checked_at": WHEN, "attempted": 1, "failed": 0,
            "jobs": [{
                "company_key": "tencent", "job_id": ID,
                "title": TITLE, "url": URL, "checked_at": WHEN,
                "description_text": DESC, "requirements_text": REQ,
                "full_jd_text": FULL, "full_jd_complete": True,
                "description_truncated": False,
                "source": "jobpro-public-employer-detail",
            }]}


class CNPublicJDTests(unittest.TestCase):
    def test_full_matching_first_party_doc_reaches_review_not_apply(self):
        s = state()
        report = enrich_cn_jobpro(s, batch(), now=NOW)
        self.assertEqual(report["full_jd_imported"], 1)
        row = s["pending"][0]
        self.assertEqual(row["consumer_review"]["full_jd_text"], FULL)
        self.assertEqual(row["consumer_review"]["stage"], "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW")
        self.assertFalse(row["consumer_review"]["source_verified_can_apply"])
        self.assertEqual(row["state"], "UNVERIFIED_INDEX")
        self.assertEqual(len(s["terminal"]), 0)
        self.assertEqual(enrich_cn_jobpro(s, batch(), now=NOW)["full_jd_imported"], 0)

    def test_mismatched_requisition_and_title_never_hydrate(self):
        for key,value in (
            ("job_id", "1282707398326592513"),
            ("url", "https://join.qq.com/post_detail.html?postid=1282707398326592513"),
            ("title", "Sales Director"),
            ("company_key", "bytedance"),
            ("description_truncated", True),
            ("full_jd_complete", False),
            ("requirements_text", ""),
        ):
            with self.subTest(field=key):
                s=state()
                doc=batch()
                doc["jobs"][0][key]=value
                result=enrich_cn_jobpro(s,doc,now=NOW)
                self.assertEqual(result["full_jd_imported"],0)
                self.assertNotIn("consumer_review",s["pending"][0])

    def test_stale_and_unverified_source_do_not_modify(self):
        s=state()
        old=batch()
        old["jobs"][0]["checked_at"]=(NOW-timedelta(hours=12)).isoformat()
        self.assertEqual(enrich_cn_jobpro(s,old,now=NOW)["full_jd_imported"],0)
        bad=batch()
        bad["source"]="aggregator-context"
        self.assertEqual(enrich_cn_jobpro(s,bad,now=NOW)["full_jd_imported"],0)
        self.assertNotIn("consumer_review",s["pending"][0])

    def test_prior_issue_and_existing_not_overwritten(self):
        s=state()
        s["pending"][0]["source"]="liepin:native-api:CN"
        self.assertEqual(enrich_cn_jobpro(s,batch(),now=NOW)["full_jd_imported"],0)
        s=state()
        s["pending"][0]["consumer_review"]={"full_jd_complete":True,
                "full_jd_text":"already independently verified"}
        self.assertEqual(enrich_cn_jobpro(s,batch(),now=NOW)["full_jd_imported"],0)


if __name__=="__main__":
    unittest.main()
