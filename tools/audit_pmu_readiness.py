#!/usr/bin/env python3
"""Read-only technical audit of PEOS PMU manifest, original text, workflows and agents.

An automated PASS only demonstrates structural consistency. PMUs remain PROPOSED
and this tool never grants editorial approval, rights or execution permission.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PMU_ID = re.compile(r"^PMU-\d{3}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def audit_records(pmu_doc, workflow_doc, agents_doc, canonical_doc, root):
    """Return immutable-in-memory findings per PMU with detailed error codes."""
    root = Path(root).resolve()
    prompts = pmu_doc.get("prompts", [])
    workflows = workflow_doc.get("workflows", [])
    agents = agents_doc.get("agents", [])
    canonicals = canonical_doc.get("prompts", [])
    canonical_ids = {x.get("id") for x in canonicals if isinstance(x, dict)}
    entries = []
    global_errors = []
    for key, items, expected in (
        ("PMU", prompts, 10), ("WORKFLOW", workflows, 10),
        ("AGENT", agents, 10), ("CANONICAL", canonicals, 659)
    ):
        if not isinstance(items, list) or len(items) != expected:
            global_errors.append("INVALID_" + key + "_COUNT")
    if not isinstance(prompts, list) or not isinstance(workflows, list) or not isinstance(agents, list):
        return {"entries": [], "errors": global_errors, "technical_gate": "FAIL",
                "editorial_gate": "PENDING", "release_gate": "BLOCKED"}
    wf_by_pmu = {w.get("pmu_id"): w for w in workflows if isinstance(w, dict)}
    agent_by_pmu = {a.get("pmu_id"): a for a in agents if isinstance(a, dict)}
    if len(wf_by_pmu) != len(workflows):
        global_errors.append("WORKFLOW_DUPLICATE_PMU")
    if len(agent_by_pmu) != len(agents):
        global_errors.append("AGENT_DUPLICATE_PMU")
    ids = [p.get("id") for p in prompts if isinstance(p, dict)]
    if len(ids) != len(prompts) or len(set(ids)) != len(ids):
        global_errors.append("PMU_DUPLICATE_OR_MISSING_IDS")

    for p in prompts:
        if not isinstance(p, dict):
            global_errors.append("INVALID_PMU_RECORD")
            continue
        ident = p.get("id")
        errors = []
        if not isinstance(ident, str) or not PMU_ID.fullmatch(ident):
            errors.append("INVALID_PMU_ID")
        name, version, goal = (p.get(x, "") for x in ("name", "version", "goal"))
        refs = p.get("refs")
        stages = p.get("stages")
        if p.get("status") != "PROPOSED":
            errors.append("PMU_EDITORIAL_STATE_CHANGED")
        if not isinstance(refs, list) or not refs or len(refs) != len(set(refs)) or any(x not in canonical_ids for x in refs):
            errors.append("INVALID_CANONICAL_REFERENCES")
        if not isinstance(stages, list) or len(stages) != 6 or not all(isinstance(x, str) and x for x in stages):
            errors.append("INVALID_PMU_STAGES")
        inputs = p.get("required_inputs")
        if not isinstance(inputs, list) or not {"OBJETIVO", "PROJETO"}.issubset(inputs):
            errors.append("MISSING_REQUIRED_INPUTS")
        policy = p.get("gate_policy", {})
        if not isinstance(policy, dict) or policy.get("fail_closed") is not True or policy.get("require_evidence") is not True:
            errors.append("PMU_FAIL_CLOSED_DISABLED")
        path = p.get("prompt_path")
        document = ""
        if not isinstance(path, str):
            errors.append("INVALID_PROMPT_PATH")
        else:
            candidate = (root / path).resolve()
            if not candidate.is_relative_to(root / "pmu" / "prompts") or candidate.suffix != ".md":
                errors.append("UNSAFE_PROMPT_PATH")
            elif not candidate.is_file():
                errors.append("PROMPT_FILE_MISSING")
            else:
                raw = candidate.read_bytes()
                if not SHA256.fullmatch(str(p.get("sha256", ""))) or hashlib.sha256(raw).hexdigest() != p.get("sha256"):
                    errors.append("PMU_SHA256_MISMATCH")
                document = raw.decode("utf-8")
        if document:
            if not document.startswith(f"# {ident} — {name}\n"):
                errors.append("PROMPT_TITLE_MISMATCH")
            if f"**Versão:** {version}" not in document:
                errors.append("PROMPT_VERSION_MISMATCH")
            if "**Estado editorial:** PROPOSED" not in document:
                errors.append("PROMPT_EDITORIAL_LABEL_MISSING")
            if f"**Finalidade:** {goal}".casefold() not in document.casefold():
                errors.append("PROMPT_GOAL_MISMATCH")
            if isinstance(refs, list) and f"**Referências canônicas:** {', '.join(refs)}" not in document:
                errors.append("PROMPT_REFS_MISMATCH")
            if isinstance(stages, list):
                for index, stage in enumerate(stages, 1):
                    if f"{index}. **{stage}**" not in document:
                        errors.append("PROMPT_STAGE_MISMATCH")
                        break
            if "Não invente credenciais" not in document or "Não exponha segredos" not in document:
                errors.append("PROMPT_GUARDRAIL_MISSING")
            for inp in ("OBJETIVO", "PROJETO"):
                if f"[{inp}]" not in document:
                    errors.append("PROMPT_INPUT_MISSING")
                    break

        wf = wf_by_pmu.get(ident)
        if not isinstance(wf, dict):
            errors.append("WORKFLOW_MISSING")
        else:
            expected_wf = "WF-" + ident.split("-")[-1]
            if wf.get("id") != expected_wf or wf.get("execution_mode") != "plan-first" or wf.get("production_mutations") != "explicit-authorization-only":
                errors.append("WORKFLOW_POLICY_MISMATCH")
            steps = wf.get("steps")
            if not isinstance(steps, list) or len(steps) != 6 or not isinstance(stages, list) or len(stages) != 6:
                errors.append("WORKFLOW_STEPS_MISMATCH")
            elif any(
                not isinstance(step, dict)
                or step.get("id") != f"S{i:02d}"
                or step.get("name") != stages[i-1]
                or step.get("required_gate") != f"G{i-1}"
                or step.get("evidence_required") is not True
                for i, step in enumerate(steps, 1)
            ):
                errors.append("WORKFLOW_STEPS_MISMATCH")
        agent = agent_by_pmu.get(ident)
        if not isinstance(agent, dict):
            errors.append("AGENT_MISSING")
        elif (
            agent.get("id") != "AGENT-" + ident.split("-")[-1]
            or agent.get("workflow_id") != "WF-" + ident.split("-")[-1]
            or agent.get("status") != "DESIGN_ONLY"
            or agent.get("execution_mode") != "PLAN_ONLY"
            or agent.get("permissions") != []
            or agent.get("requires_human_review") is not True
        ):
            errors.append("AGENT_EXECUTION_POLICY_MISMATCH")
        entries.append({"id": ident, "name": name, "technical_gate": "PASS" if not errors else "FAIL",
                        "editorial_gate": "PENDING", "findings": errors})
    return {
        "entries": entries,
        "errors": global_errors,
        "technical_gate": "PASS" if not global_errors and all(not e["findings"] for e in entries) else "FAIL",
        "editorial_gate": "PENDING",
        "release_gate": "BLOCKED",
        "note": "Technical consistency is not editorial approval or redistribution authorization",
    }


def audit(root=ROOT):
    root = Path(root)
    return audit_records(
        read_json(root / "pmu/manifest.json"),
        read_json(root / "workflows/manifest.json"),
        read_json(root / "agents/manifest.json"),
        read_json(root / "catalog/manifest.json"), root,
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        report = audit(args.root)
    except (OSError, ValueError, UnicodeError, KeyError) as exc:
        print(json.dumps({"technical_gate": "FAIL", "error": type(exc).__name__}))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["technical_gate"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
