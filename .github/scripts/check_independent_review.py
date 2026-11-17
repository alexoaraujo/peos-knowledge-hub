#!/usr/bin/env python3
"""Read-only PEOS PR review-policy check for solo and team workflows.

Solo-maintainer mode does not require approval; CI and branch rules still apply.
Independent mode remains available if a team adopts mandatory review later.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request


def evaluate(reviews, author, head_sha):
    """Require a latest-HEAD approval from another reviewer with no outstanding change request."""
    if not author or not head_sha:
        return False, "PR author or HEAD SHA missing"
    latest = {}
    for review in reviews:
        user = (review.get("user") or {}).get("login", "")
        state = review.get("state", "")
        if not user or state not in ("APPROVED", "CHANGES_REQUESTED", "DISMISSED"):
            continue
        # GitHub returns reviews in chronological order, with pagination preserved.
        latest[user.lower()] = review
    for username, review in latest.items():
        if username == author.lower():
            continue
        if review["state"] == "CHANGES_REQUESTED":
            return False, f"Unresolved changes requested by {username}"
    valid = [
        username for username, review in latest.items()
        if username != author.lower()
        and review["state"] == "APPROVED"
        and review.get("commit_id") == head_sha
    ]
    if not valid:
        return False, "No independent APPROVED review bound to current PR HEAD SHA"
    return True, "Independent approval on current SHA: " + ", ".join(sorted(valid))


def evaluate_policy(reviews, author, head_sha, mode):
    """Mode-specific review decision. Never claim solo mode is an independent approval."""
    if mode == "solo":
        return True, "Solo-maintainer mode: independent approval not required (no review asserted)"
    if mode == "independent":
        return evaluate(reviews, author, head_sha)
    return False, "Unrecognized review mode; expected solo or independent"


def get_json(url, token):
    if not url.startswith("https://api.github.com/"):
        raise ValueError("Unexpected GitHub API URL")
    request = urllib.request.Request(
        url, headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + token,
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "peos-review-gate",
        }
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    mode = os.environ.get("PEOS_REVIEW_MODE", "solo").strip().lower()
    if mode == "solo":
        _, reason = evaluate_policy([], "", "", mode)
        print("PASS:", reason)
        print("Review status is informational; required CI and branch rules remain enforced")
        return 0
    if mode != "independent":
        print("BLOCKED: unsupported PEOS_REVIEW_MODE", file=sys.stderr)
        return 1
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    token = os.environ.get("GITHUB_TOKEN", "")
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")
    if not repo or not token or not event_path or "/" not in repo:
        print("BLOCKED: missing GitHub context/token", file=sys.stderr)
        return 1
    try:
        with open(event_path, encoding="utf-8") as handle:
            event = json.load(handle)
        number = (event.get("pull_request") or {}).get("number") or event.get("number")
        if not isinstance(number, int) or number < 1:
            print("BLOCKED: event is not a pull request", file=sys.stderr)
            return 1
        base_url = f"https://api.github.com/repos/{repo}/pulls/{number}"
        pr = get_json(base_url, token)
        head_sha = pr["head"]["sha"]
        author = pr["user"]["login"]
        reviews = []
        for page in range(1, 21):
            chunk = get_json(base_url + f"/reviews?per_page=100&page={page}", token)
            if not isinstance(chunk, list):
                raise ValueError("Reviews response must be a list")
            reviews.extend(chunk)
            if len(chunk) < 100:
                break
        else:
            raise ValueError("More than 2,000 reviews: manual review required")
        passed, reason = evaluate_policy(reviews, author, head_sha, mode)
        print(("PASS: " if passed else "BLOCKED: ") + reason)
        print("PR:", number, "HEAD:", head_sha, "review records:", len(reviews))
        return 0 if passed else 1
    except (OSError, ValueError, KeyError, TypeError, urllib.error.URLError) as exc:
        print("BLOCKED: cannot verify independent review:", str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
