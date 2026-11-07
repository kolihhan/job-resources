import importlib.util
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import collect_gen_digital_my as c

class GenDigitalProductionTests(unittest.TestCase):
    def test_senior_roles_do_not_fill_my_top_queue(self):
        source={"status":"OFFICIAL_BOARD_OBSERVED","observed_at":"2026-11-07T00:00:00Z",
                "total_listed":10,"items":[
            {"title":"Lead AI Scientist","source_id":"lead","market":"MY"},
            {"title":"AI Applied Scientist","source_id":"junior","market":"MY"},
            {"title":"MLOps Engineer - MoneyLion","source_id":"mlops","market":"MY"},
            {"title":"Engineering Manager (MLOps)","source_id":"mgr","market":"MY"}]}
        out=c.transform(source)
        self.assertEqual([x["source_id"] for x in out["items"]],["junior","mlops"])
        self.assertEqual(len(out["mature_title_not_enqueued"]),2)
        self.assertEqual(out["source"],"gen-digital:official-ashby:MY")
    def test_bad_source_not_silent_zero_market(self):
        with self.assertRaisesRegex(ValueError,"not readable"):
            c.transform({"status":"SOURCE_ERROR","items":[]})
if __name__=="__main__":unittest.main()
