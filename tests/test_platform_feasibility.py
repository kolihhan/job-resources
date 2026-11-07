import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "probe_platform_feasibility.py"


def load():
    spec = importlib.util.spec_from_file_location("platform_feasibility", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class PlatformProbeTests(unittest.TestCase):
    def test_jobstreet_distinct_pages_are_proven(self):
        m = load()
        def get(url):
            n = "1" if "page=1" in url else "2"
            return {"state": "HTML_FETCHED", "http_status": 200,
                    "html": f'<html><title>Results</title><a href="/job/1234567{n}?utm=test">AI role</a></html>',
                    "final_url": url}
        spec = {"id": "MY_JOBSTREET", "market": "MY", "host": "jobstreet.com",
                "urls": ["https://my.jobstreet.com/ai-engineer-jobs?page=1",
                         "https://my.jobstreet.com/ai-engineer-jobs?page=2"]}
        result = m.probe_platform(spec, get)
        self.assertEqual(result["coverage"], "TWO_PAGES_WITH_DISTINCT_ROLE_IDS")
        self.assertEqual(result["all_unique_job_identities"], 2)
        self.assertEqual(result["page2_new_identifiable_jobs"], 1)

    def test_js_shell_is_not_a_job(self):
        m = load()
        links, _ = m.recognized_job_links('<html><title>Jobs</title><a href="/jobs">Jobs</a></html>',
                                           'https://my.hiredly.com/jobs', 'hiredly.com')
        self.assertEqual(links, [])

    def test_cross_site_links_not_counted_as_platform_native(self):
        m = load()
        links, _ = m.recognized_job_links(
            '<a href="https://www.linkedin.com/jobs/view/example-1234567890">job</a>'
            '<a href="https://evil.example/job/12345678">job</a>'
            '<a href="/job/12345678?utm_source=tracker">job</a>',
            "https://my.jobstreet.com/ai-engineer-jobs", "jobstreet.com")
        self.assertEqual(links, ["/job/12345678"])

    def test_blocked_native_page_is_not_marked_done(self):
        m = load()
        calls = []
        def blocked(url):
            calls.append(url)
            return {"state": "BLOCKED_HTTP", "http_status": 403}
        r = m.probe_platform(m.PLATFORMS[0], blocked)
        self.assertEqual(r["coverage"], "BLOCKED_FROM_RUNNER")
        self.assertEqual(r["all_unique_job_identities"], 0)
        self.assertEqual(len(calls), 1)

    def test_same_link_on_both_pages_is_insufficient(self):
        m = load()
        def dup(url):
            return {"state": "HTML_FETCHED", "http_status": 200,
                    "final_url": url, "html": '<a href="/job/12345678">same</a>'}
        r = m.probe_platform(m.PLATFORMS[1], dup)
        self.assertEqual(r["coverage"], "ROLE_LINKS_BUT_NEXT_PAGE_UNPROVEN")
        self.assertEqual(r["page2_new_identifiable_jobs"], 0)


if __name__ == "__main__":
    unittest.main()
