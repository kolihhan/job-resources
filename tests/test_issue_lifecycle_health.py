import importlib.util
import unittest
from datetime import datetime, timezone
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "scripts" / "report_issue_lifecycle_health.py"
spec = importlib.util.spec_from_file_location("issue_lifecycle_health", path)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

NOW = datetime(2026, 11, 10, 7, tzinfo=timezone.utc)


def issue(number, title, labels=None, created="2026-11-09T07:00:00Z"):
    return {
        "number": number, "title": title,
        "labels": [{"name": name} for name in (labels or [])],
        "created_at": created,
    }


class LifecycleHealthTests(unittest.TestCase):
    def test_exact_label_and_seven_day_open_cohort(self):
        issues = [
            issue(1, "[APPLY][SG] LLM Engineer", ["status:apply", "market:sg"]),
            issue(2, "[WAIT][MY] AI Engineer", ["status:wait"],
                  "2026-10-01T00:00:00Z"),
            issue(3, "[CHECK][CN] RAG Engineer", ["status:check"]),
            issue(4, "[ACTION] Assessment", ["status:action"]),
        ]
        result = audit.count_lifecycle(issues, NOW)
        self.assertEqual(result["open_lifecycle_issues"], 4)
        self.assertEqual(result["by_status"]["APPLY"], 1)
        self.assertEqual(result["currently_open_created_in_last_7d"]["WAIT"], 0)
        self.assertEqual(result["label_mismatch_count"], 0)
        self.assertIn("NOT proof", result["interpretation"])

    def test_missing_duplicate_and_wrong_status_labels(self):
        issues = [
            issue(20, "[APPLY] role", []),
            issue(21, "[WAIT] role", ["status:apply", "status:wait"]),
            issue(22, "[CHECK] role", ["status:apply"]),
        ]
        result = audit.count_lifecycle(issues, NOW)
        self.assertEqual(result["label_mismatch_count"], 3)
        self.assertEqual({r["number"] for r in result["label_mismatches"]},
                         {20, 21, 22})

    def test_skip_pull_requests_and_flag_unclassified(self):
        rows = [
            {**issue(5, "[APPLY] fake PR", []), "pull_request": {"url": "x"}},
            issue(6, "Unknown state", []),
        ]
        result = audit.count_lifecycle(rows, NOW)
        self.assertEqual(result["open_lifecycle_issues"], 0)
        self.assertEqual(result["unclassified_open_issue_numbers"], [6])

    def test_action_event_evidence_no_invented_owner_test(self):
        runs = [
            {"event": "issues", "created_at": "2026-11-10T06:00:00Z",
             "conclusion": "success", "html_url": "https://github.com/example/1"},
            {"event": "issue_comment", "created_at": "2026-10-01T06:00:00Z",
             "conclusion": "success", "html_url": "https://github.com/example/2"},
        ]
        result = audit.measure_event_runs(runs, NOW)
        self.assertEqual(result["issues"]["successful_7d"], 1)
        self.assertFalse(result["issue_comment"]["tested"])
        self.assertEqual(result["issue_comment"]["runs_7d"], 0)

    def test_report_preserves_uncertainty_and_no_private_issue_body(self):
        result = {
            "issues": audit.count_lifecycle([
                issue(42, "[APPLY] Example", [], created="2026-11-09T07:00:00Z")
            ], NOW),
            "event_runs": audit.measure_event_runs([], NOW),
        }
        markdown = audit.render_markdown(result)
        self.assertIn("Label mismatches:** 1", markdown)
        self.assertIn("#42", markdown)
        self.assertIn("untested", markdown)
        self.assertIn("not a submitted application", markdown)


if __name__ == "__main__":
    unittest.main()
