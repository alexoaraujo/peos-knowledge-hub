"""Regression tests for solo PR policy and optional independent review (no GitHub I/O)."""
import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / ".github/scripts/check_independent_review.py"
spec = importlib.util.spec_from_file_location("check_independent_review", MODULE)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
SHA = "a" * 40


def review(login, state="APPROVED", sha=SHA):
    return {"user": {"login": login}, "state": state, "commit_id": sha}


class IndependentReviewGateTests(unittest.TestCase):
    def test_solo_without_reviews_passes(self):
        ok, reason = gate.evaluate_policy([], "author", SHA, "solo")
        self.assertTrue(ok)
        self.assertIn("not required", reason)
        self.assertNotIn("APPROVED", reason)

    def test_solo_does_not_depend_on_old_approval_or_change_request(self):
        old = [review("reviewer", sha="b" * 40), review("other", "CHANGES_REQUESTED")]
        self.assertTrue(gate.evaluate_policy(old, "author", SHA, "solo")[0])

    def test_independent_mode_still_blocks_missing_review(self):
        self.assertFalse(gate.evaluate_policy([], "author", SHA, "independent")[0])

    def test_unsupported_policy_fails_closed(self):
        self.assertFalse(gate.evaluate_policy([], "author", SHA, "unexpected")[0])

    def test_no_reviews_is_blocked(self):
        self.assertFalse(gate.evaluate([], "author", SHA)[0])

    def test_self_approval_is_blocked(self):
        self.assertFalse(gate.evaluate([review("author")], "author", SHA)[0])

    def test_review_on_previous_commit_is_blocked(self):
        self.assertFalse(gate.evaluate([review("reviewer", sha="b" * 40)], "author", SHA)[0])

    def test_independent_approval_on_head_passes(self):
        passed, _ = gate.evaluate([review("reviewer")], "author", SHA)
        self.assertTrue(passed)

    def test_unresolved_changes_request_blocks(self):
        reviews = [review("reviewer"), review("other", state="CHANGES_REQUESTED")]
        self.assertFalse(gate.evaluate(reviews, "author", SHA)[0])

    def test_change_request_resolved_by_same_reviewer_approval(self):
        reviews = [review("reviewer", state="CHANGES_REQUESTED"), review("reviewer")]
        self.assertTrue(gate.evaluate(reviews, "author", SHA)[0])

    def test_revoked_or_dismissed_approval_is_blocked(self):
        reviews = [review("reviewer"), review("reviewer", state="DISMISSED")]
        self.assertFalse(gate.evaluate(reviews, "author", SHA)[0])

    def test_comment_is_not_approval(self):
        self.assertFalse(gate.evaluate([review("reviewer", "COMMENTED")], "author", SHA)[0])

    def test_missing_metadata_fails_closed(self):
        self.assertFalse(gate.evaluate([review("reviewer")], "", SHA)[0])
        self.assertFalse(gate.evaluate([review("reviewer")], "author", "")[0])


if __name__ == "__main__":
    unittest.main()
