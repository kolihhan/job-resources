import importlib.util
from pathlib import Path
import unittest
p=Path(__file__).resolve().parents[1]/"scripts"/"probe_gen_digital_ashby.py"
sp=importlib.util.spec_from_file_location("gen_digital_probe",p)
g=importlib.util.module_from_spec(sp)
sp.loader.exec_module(g)
ID="9c88e56f-df1f-4dba-88e8-4620a3be2267"

class GenDigitalTests(unittest.TestCase):
    def test_employer_uuid_market_and_title_required(self):
        jobs=[
            {"id":ID,"title":"Applied AI Scientist (Generative AI)",
             "location":"MYS - Kuala Lumpur","jobUrl":"https://jobs.ashbyhq.com/gen-digital/"+ID,
             "descriptionPlain":"LLM agents and RAG"},
            {"id":"7ac281fe-0b0f-40cc-abce-cdf44dcf013f","title":"Senior Backend Engineer",
             "location":"MYS - Kuala Lumpur"},
            {"id":"1c41c523-3279-4bb1-b29b-19da43629f11","title":"AI Engineer",
             "location":"USA - California"},
            {"id":"broken","title":"AI Engineer","location":"MYS - Kuala Lumpur"}]
        rows=g.parse_jobs({"jobs":jobs})
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]["source_id"],ID)
        self.assertEqual(rows[0]["jd_chars"],18)
    def test_source_error_not_zero_jobs(self):
        r=g.run(lambda:{"message":"no data"})
        self.assertEqual(r["status"],"SOURCE_ERROR")
        self.assertNotIn("technical_my_ids",r)
    def test_positive_feed_has_exact_url_but_not_apply(self):
        r=g.run(lambda:{"jobs":[{"id":ID,"title":"Applied AI Scientist (Generative AI)",
             "location":"MYS - Kuala Lumpur"}]})
        self.assertEqual(r["status"],"OFFICIAL_BOARD_OBSERVED")
        self.assertEqual(r["technical_my_ids"],1)
        self.assertEqual(r["items"][0]["url"],"https://jobs.ashbyhq.com/gen-digital/"+ID)
        self.assertNotIn("canApply",r["items"][0])
if __name__=="__main__":unittest.main()
