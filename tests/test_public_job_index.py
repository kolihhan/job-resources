import importlib.util
from pathlib import Path
import unittest
from urllib.parse import quote

P = Path(__file__).parents[1] / "scripts" / "probe_public_job_index.py"
spec = importlib.util.spec_from_file_location("probe_public_job_index", P)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class PublicIndexTests(unittest.TestCase):
    def test_jobstreet_and_linkedin_exact_identity(self):
        self.assertEqual(m.candidate_url("https://my.jobstreet.com/job/98765432?tracking=x","MY"),
                         "https://my.jobstreet.com/job/98765432")
        self.assertEqual(m.candidate_url("https://sg.linkedin.com/jobs/view/ai-engineer-4321098765?trk=foo","SG"),
                         "https://www.linkedin.com/jobs/view/4321098765")
        self.assertIsNone(m.candidate_url("https://sg.jobstreet.com/ai-engineer-jobs","SG"))
        self.assertIsNone(m.candidate_url("https://my.jobstreet.com/job/98765432","SG"))
    def test_search_wrapper(self):
        url = "https://duckduckgo.com/l/?uddg=" + quote("https://my.jobstreet.com/job/12345678?utm=a",safe="")
        self.assertEqual(m.candidate_url(url, "MY"),"https://my.jobstreet.com/job/12345678")
    def test_rss(self):
        rss=b'<rss><channel><item><title>AI Engineer</title><link>https://sg.jobstreet.com/job/12345678</link></item><item><link>https://sg.jobstreet.com/job/12345678?foo=x</link></item><item><link>https://example.com/ai</link></item></channel></rss>'
        self.assertEqual(m.parse_results("bing_rss",rss,"SG"),["https://sg.jobstreet.com/job/12345678"])
    def test_html(self):
        html=b'<a href="https://my.hiredly.com/jobs/ai-research-engineer-1234567">job</a><a href="https://my.hiredly.com/jobs">list</a>'
        self.assertEqual(m.parse_results("ddg_html",html,"MY"),["https://my.hiredly.com/jobs/ai-research-engineer-1234567"])

if __name__=="__main__":
    unittest.main()
