"""Unit tests for Lead Generator baseline bootstrap."""

import unittest

from lead_generator import get_app_status


class TestAppStatus(unittest.TestCase):
    def test_get_app_status_contains_phase_one_metadata(self) -> None:
        status = get_app_status()

        self.assertEqual(status["name"], "lead-generator")
        self.assertEqual(status["phase"], "Phase 1")
        self.assertEqual(status["status"], "baseline-ready")


if __name__ == "__main__":
    unittest.main()
