import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_scout_metrics.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_scout_metrics", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def base_record():
    return {
        "market": "SG",
        "run_quality": "PARTIAL_COVERAGE",
        "phase_a_completed": False,
        "phase_b_completed": False,
        "coverage_debt_remaining": 1,
        "coverage_gaps": ["LinkedIn page two inaccessible"],
        "platform_attempts": [{"platform": "LinkedIn"}],
        "source_probes": [
            {
                "platform": "LinkedIn",
                "source_kind": "index",
                "query_family": "LLM",
                "page_key": "query-1",
                "job_refs": ["employer:REQ-1"],
                "end_of_results": False,
            }
        ],
        "freehire_triage": {"manifest_reconciled": False},
    }


class ScoutCompletionGuardTests(unittest.TestCase):
    def test_single_page_partial_is_honest(self):
        self.assertEqual(load_validator().validate(base_record()), [])

    def test_single_page_cannot_be_complete(self):
        record = base_record()
        record.update({
            "run_quality": "COMPLETE",
            "phase_a_completed": True,
            "phase_b_completed": True,
            "coverage_debt_remaining": 0,
            "coverage_gaps": [],
            "platform_attempts": [{"platform": f"source-{i}"} for i in range(4)],
            "freehire_triage": {"manifest_reconciled": True},
        })
        self.assertTrue(load_validator().validate(record))

    def test_four_deeply_scanned_sources_can_be_complete(self):
        record = base_record()
        record.update({
            "run_quality": "COMPLETE",
            "phase_a_completed": True,
            "phase_b_completed": True,
            "coverage_debt_remaining": 0,
            "coverage_gaps": [],
            "platform_attempts": [{"platform": f"source-{i}"} for i in range(4)],
            "source_probes": [],
            "freehire_triage": {"manifest_reconciled": True},
        })
        for i in range(4):
            for pg in range(2):
                record["source_probes"].append({
                    "platform": f"source-{i}",
                    "source_kind": "native",
                    "query_family": "LLM",
                    "page_key": str(pg + 1),
                    "job_refs": [f"employer-{i}:REQ-{pg*10+k}" for k in range(10)],
                    "end_of_results": False,
                })
        self.assertEqual(load_validator().validate(record), [])

    def test_no_phase_b_cannot_be_complete(self):
        record = base_record()
        record.update({"run_quality": "COMPLETE", "phase_a_completed": True})
        errors = load_validator().validate(record)
        self.assertTrue(any("phase_b_completed=true" in e for e in errors))

    def test_unverified_zero_is_not_complete(self):
        record = base_record()
        record.update({
            "run_quality": "COMPLETE",
            "phase_a_completed": True,
            "phase_b_completed": True,
            "coverage_debt_remaining": 0,
            "coverage_gaps": [],
            "platform_attempts": [{"platform": f"source-{i}"} for i in range(4)],
            "source_probes": [],
            "freehire_triage": {"manifest_reconciled": True},
        })
        self.assertTrue(any("no page/query/source evidence" in e for e in load_validator().validate(record)))


if __name__ == "__main__":
    unittest.main()
