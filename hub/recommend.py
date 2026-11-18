"""Read-only integration of deterministic PEOS plans with the versioned prompt catalog.

This module only references existing prompt metadata; it never executes prompts,
changes manifests, or declares editorial/legal release approval.
"""
from __future__ import annotations

import re

from hub import catalog


def _tokens(text: str) -> list[str]:
    return list(dict.fromkeys(re.findall(r"\w+", catalog.normalize(text))))


def recommend(goal: str, limit: int = 10, pmu: str | None = None) -> dict:
    """Compose a PLAN_ONLY workflow and return explainable catalog references.

    Canonical dependencies are derived solely from the selected PMU manifest.
    Related entries are heuristic matches, not semantic or editorial approval.
    """
    if not isinstance(goal, str) or not goal.strip():
        raise ValueError("goal must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 20:
        raise ValueError("limit must be 1..20")

    from tools import peos_engine

    problems = peos_engine.validate()
    if problems:
        raise ValueError("; ".join(problems))
    plan = peos_engine.compose(goal, pmu)
    entries = catalog.entries()
    by_canonical_id = {e["id"]: e for e in entries if e["namespace"] == "canonical"}
    required_ids = [d["id"] for d in plan["canonical_dependencies"]]

    # Dependency references are exact manifest references, never generated text.
    dependencies = [by_canonical_id[ref] for ref in required_ids]
    if any(e["sha256"] != d["sha256"] for e, d in
           zip(dependencies, plan["canonical_dependencies"])):
        raise ValueError("canonical manifest and catalog hashes disagree")

    words = [w for w in _tokens(goal) if len(w) >= 3]
    ranked = []
    for e in entries:
        # PMUs and canonical dependencies are represented separately. A
        # heuristic match must never silently elevate an entry's status.
        if e["namespace"] == "pmu" or (e["namespace"] == "canonical" and e["id"] in required_ids):
            continue
        title = catalog.normalize(e["title"])
        fields = catalog.normalize(" ".join(str(x or "") for x in
                                  [e.get("category"), e.get("group"), " ".join(e.get("tags") or [])]))
        score = sum((3 if word in title else 0) + (1 if word in fields else 0)
                    for word in words)
        if score:
            ranked.append((-score, e["namespace"], e["id"], e))

    matches = [item for _, _, _, item in sorted(ranked)[:limit]]
    return {
        "goal": goal,
        "plan": plan,
        "canonical_references": dependencies,
        "related_catalog_entries": matches,
        "match_method": "deterministic-lexical-heuristic",
        "catalog_count": len(entries),
        "editorial_policy": "PRESERVE_SOURCE_STATUS",
        "publication_gate": "BLOCKED_PENDING_SOURCE_RIGHTS",
        "execution_status": "PLAN_ONLY",
        "permissions": "NO_EXTERNAL_MUTATIONS",
    }
