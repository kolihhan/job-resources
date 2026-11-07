import importlib.util
from pathlib import Path
import unittest
import urllib.error

SCRIPT = Path(__file__).parents[1] / "scripts" / "probe_source_feasibility.py"


def load():
    spec = importlib.util.spec_from_file_location("source_feasibility", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class FeasibilityTests(unittest.TestCase):
    def test_lever_pagination_distinctness_and_detail(self):
        m = load()
        p1 = [{"id": f"id-{i}", "text": "AI Engineer", "categories": {"location": "Singapore"}, "hostedUrl": f"https://jobs.lever.co/test/{i}"} for i in range(50)]
        p2 = [{"id": f"id-{i}", "text": "Engineer", "categories": {"location": "Kuala Lumpur, Malaysia"}} for i in range(50, 52)]
        calls = []
        def fetch(url):
            calls.append(url)
            if "skip=50" in url:
                return p2
            if "skip=0" in url:
                return p1
            return {"id": "id-0", "description": "AI research"}
        result = m.probe({"id": "lever_test", "kind": "lever", "slug": "test", "markets": ["SG", "MY"]}, fetch)
        self.assertEqual(result["state"], "LIST_AND_DETAIL")
        self.assertEqual(result["pagination"], "PAGE_2_DISTINCT")
        self.assertEqual(result["list_unique_jobs"], 52)
        self.assertEqual(result["market_matches"]["SG"], 50)
        self.assertEqual(result["market_matches"]["MY"], 2)
        self.assertEqual(len(calls), 3)

    def test_gh_full_board_with_detail(self):
        m = load()
        calls = []
        def fetch(url):
            calls.append(url)
            return {"jobs": [{"id": 123, "title": "Research Engineer", "location": {"name": "Singapore"}, "absolute_url": "https://job-boards.greenhouse.io/test/jobs/123"}]} if url.endswith("/jobs") else {"id": 123, "content": "<p>Role description</p>"}
        result = m.probe({"id": "gh", "kind": "greenhouse", "slug": "test", "markets": ["SG"]}, fetch)
        self.assertEqual(result["pagination"], "WHOLE_BOARD_ENDPOINT")
        self.assertEqual(result["market_matches"]["SG"], 1)
        self.assertEqual(result["state"], "LIST_AND_DETAIL")
        self.assertEqual(len(calls), 2)

    def test_smartrecruiters_pagination_is_not_assumed_completed(self):
        m = load()
        base = {"content": [{"id": f"p-{i}", "name": "Data Scientist", "title": "Data Scientist", "location": {"city": "Singapore", "country": "SG"}} for i in range(50)], "totalFound": 51}
        def fetch(url):
            if "offset=50" in url:
                return {"content": [{"id": "p-50", "name": "AI Engineer", "title": "AI Engineer", "location": {"city": "Kuala Lumpur", "country": "MY"}}], "totalFound": 51}
            if "/postings/p-0" in url:
                return {"id": "p-0", "name": "Data Scientist"}
            return base
        result = m.probe({"id": "smart", "kind": "smartrecruiters", "slug": "Test", "markets": ["MY", "SG"]}, fetch)
        self.assertEqual(result["pagination"], "PAGE_2_DISTINCT")
        self.assertEqual(result["list_unique_jobs"], 51)

    def test_blocked_is_not_success(self):
        m = load()
        def blocked(url):
            raise urllib.error.HTTPError(url, 403, "Forbidden", None, None)
        result = m.probe({"id": "blocked", "kind": "greenhouse", "slug": "abc", "markets": ["MY"]}, blocked)
        self.assertEqual(result["state"], "BLOCKED_HTTP")
        self.assertEqual(result["list_unique_jobs"], 0)

    def test_liepin_missing_artifact_is_failure(self):
        m = load()
        out = m.liepin_probe(Path("/does-not-exist-feasibility-output.json"), None)
        self.assertEqual(out["state"], "COLLECTOR_FAILED")


if __name__ == "__main__":
    unittest.main()
