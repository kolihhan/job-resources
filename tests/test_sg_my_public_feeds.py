import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).parents[1]/"scripts"/"probe_sg_my_public_feeds.py"
spec=importlib.util.spec_from_file_location("feeds_probe",P)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class FeedTests(unittest.TestCase):
    def test_aggregator_response_structured_and_scope_not_inferred(self):
        raw={"jobs":[{"guid":"abc","title":"AI Research Engineer",
              "companyName":"Example","locationRestrictions":["SG"],
              "applicationLink":"https://himalayas.app/companies/example/jobs/abc"}],
             "nextCursor":None}
        rows=m.normalize("himalayas","SG",raw)
        self.assertEqual(len(rows),1)
        self.assertTrue(rows[0]["relevant_title"])
        self.assertEqual(rows[0]["market_filter"],"SG")
        self.assertIn("SG",rows[0]["location"])

    def test_invalid_records_are_not_jobs(self):
        raw={"data":[{"title":"AI Engineer","url":"javascript:alert(1)"},
                     {"title":"AI Engineer","url":"https://example.com/jobs/1"},
                     {"id":"x","company":"X","url":"https://example.com/jobs/x"}]}
        rows=m.normalize("devglobal","MY",raw)
        self.assertEqual(len(rows),1)

    def test_query_urls_are_separate_country_scoped(self):
        self.assertIn("country=sg",m.url_for("devglobal","SG","AI"))
        self.assertIn("country=MY",m.url_for("himalayas","MY","AI"))
        self.assertIn("page=1",m.url_for("himalayas","MY","AI"))

    def test_unsupported_schema_does_not_fabricate_jobs(self):
        self.assertEqual(m.records("devglobal",{"total":750,"message":"none"}),[])
        with self.assertRaisesRegex(ValueError,"unexpected top-level"):
            m.records("himalayas","<html>")

if __name__=="__main__":unittest.main()
