#!/usr/bin/env python3
"""Deterministic applicant-side source triage, with NO terminal decisions.

The inputs are existing private queue rows. This module NEVER fetches public
batches, runs an LLM, claims applicant eligibility, creates an Issue, or ACKs
Pending. Exact source/Issue history and verified employer JD govern final
decisions. Source snippets and titles are ONLY review signals.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re

MAX_JD_AGE = timedelta(hours=48)
CUE_LIMIT = 6

# Only literal market-compatible source cues; no job-title-only auto rejection.
RESEARCH = re.compile(
    r"\b(?:research (?:assistant|associate|engineer|officer|scientist|fellow)"
    r"|applied scientist|research scientist|ai researcher)\b"
    r"|科研助理|研究助理|研究工程师|助理研究员|研究员", re.I)
CORE = re.compile(
    r"\b(?:llm|genai|agent(?:ic|s)?|rag|nlp|retrieval|rerank(?:ing)?|"
    r"ai(?:[- ]native|[- ]backend|[- ]software|[- ]engineer)?|"
    r"machine learning|evaluation|knowledge graph|"
    r"coding agents?|generative ai|applied ai)\b"
    r"|人工智能|大模型|智能体|知识图谱|检索|模型评测|生成式", re.I)
MATURE = re.compile(
    r"\b(?:staff|principal|lead|director|manager|head|chief|architect|senior)\b"
    r"|架构师|首席|总监|负责人|资深", re.I)
INTERN = re.compile(r"\b(?:intern|internship|trainee)\b|实习|管培生", re.I)
CONTRACT = re.compile(r"\b(?:contract|contractor|temporary|freelance)\b|合同制|短期合同|外包", re.I)
NON_CORE = re.compile(
    r"\b(?:pre[- ]sales|sales engineer|hardware engineer|packaging engineer|"
    r"datacenter (?:design|engineer)|data hall|power engineer|"
    r"electrical systems integration|firmware|robotics|humanoid)\b"
    r"|售前|销售工程师|电源软件|三维重建", re.I)
PREFERENCE = re.compile(
    r"\b(?:preferred|preferably|nice to have|bonus|advantageous|ideally|"
    r"familiarity|exposure|a plus|would be a plus)\b|优先|加分", re.I)
# Deliberately narrow. Years alone (company history / nice-to-haves /
# 3-year SWE stretch / annual planning) never establishes a hard YOE block.
YEARS = re.compile(
    r"\b(?:[4-9]|1[0-9])\s*\+?\s*(?:years?|yrs?)\s+"
    r"(?:of\s+)?(?:relevant\s+|professional\s+|full[- ]time\s+|"
    r"hands[- ]on\s+|industry\s+|commercial\s+|"
    r"software\s+|engineering\s+|machine learning\s+|AI\s+|ML\s+|"
    r"backend\s+|work\s+){0,5}"
    r"(?:experience|work|working|developing|development|engineering)\b", re.I)
PHD_REQUIRED = re.compile(
    r"\b(?:Ph\.?D\.?|doctorate|doctoral degree)\s+(?:is\s+)?"
    r"(?:required|mandatory|essential)\b"
    r"|\b(?:must have|requires?)\s+(?:an?\s+)?(?:Ph\.?D\.?|doctorate)\b"
    r"|必须(?:具有|具备)?博士(?:学位|学历)|博士(?:学位|学历)(?:为必需|必须|及以上)", re.I)
BASE_RESTRICTION = re.compile(
    r"\b(?:candidates?|applicants?|you)\s+(?:must|need(?:s)? to|are required to)\s+"
    r"(?:already\s+)?be\s+(?:currently\s+)?based\s+in\s+"
    r"(?P<place>Singapore|China|Mainland China)\b"
    r"|\bmust\s+(?:already\s+)?be\s+(?:currently\s+)?based\s+in\s+"
    r"(?P<place2>Singapore|China|Mainland China)\b", re.I)
REQUIRED = re.compile(
    r"\b(?:minimum|at least|must|mandatory|required|requires?|"
    r"essential|necessar(?:y|ily)|qualifications?)\b"
    r"|必须|要求|最低|不少于", re.I)
HONG_KONG = re.compile(
    r"\blocation\s*[:：]\s*(?:Hong Kong|香港)(?=[\s,.;—–-]|$)"
    r"|(?:工作地点|办公地点)\s*[:：]\s*香港", re.I)
SOFT_OVERRIDE = re.compile(
    r"\b(?:or equivalent|or comparable|alternatively|other equivalent|"
    r"master'?s (?:or|and) phd|phd (?:or|and) master'?s)\b"
    r"|或同等|硕士或博士|博士或硕士", re.I)


def _dt(s):
    if not isinstance(s, str):
        return None
    try:
        value = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    return value if value.tzinfo else None


def _quote(text, match, width=230):
    """Bounded exact substring to let Scout verify the surrounding context."""
    start = max(0, match.start() - 85)
    end = min(len(text), match.end() + max(0, width - 85 - len(match.group())))
    return text[start:end].strip()


def _fresh_jd(row, now):
    review = row.get("consumer_review") or {}
    checked = _dt(review.get("checked_at"))
    if review.get("stage") != "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW":
        return None
    jd = review.get("full_jd_text")
    if review.get("full_jd_complete") is not True or not isinstance(jd, str) or len(jd) < 300:
        return None
    if checked is None or checked > now + timedelta(minutes=5) or now - checked > MAX_JD_AGE:
        return None
    return jd


def triage(row: dict, market: str, *, now: datetime | None = None) -> dict:
    """Route to reviewers without deciding ineligibility.

    Invariant: no action is ever terminal. The evidence source and literal
    trigger are preserved. Full-JD rules are REVIEW-REQUIRED, not auto-ACK.
    """
    if market not in ("SG", "MY", "CN") or not isinstance(row, dict):
        raise ValueError("invalid market/row")
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    title = str(row.get("title") or "")
    review = row.get("consumer_review") or {}
    evidence = []
    jd = _fresh_jd(row, now)

    def mark(code, basis, quote):
        if len(evidence) < CUE_LIMIT and not any(x["code"] == code for x in evidence):
            evidence.append({"code": code, "basis": basis, "quote": str(quote)[:240]})

    research = bool(RESEARCH.search(title))
    strong = bool(CORE.search(title))
    if MATURE.search(title):
        mark("MATURE_TITLE_VERIFY_SCOPE", "TITLE_HINT", title)
    if INTERN.search(title):
        mark("INTERNSHIP_OR_TRAINEE_TITLE", "TITLE_HINT", title)
    if CONTRACT.search(title):
        mark("RESEARCH_TERM_EXCEPTION_CHECK" if research else "NONPERMANENT_TITLE_CHECK",
             "TITLE_HINT", title)
    if NON_CORE.search(title):
        mark("DOMAIN_OR_NON_CORE_TITLE_CHECK", "TITLE_HINT", title)
    if review.get("possible_prior_issue"):
        mark("POSSIBLE_PRIOR_ISSUE_VERIFY_REQUISITION", "PRIVATE_ISSUE_HINT",
             "Issue #" + str(review["possible_prior_issue"]))

    hard = []
    if jd is not None:
        def strong_cue(code, m):
            if not m:
                return
            mark(code, "FRESH_FIRST_PARTY_JD", _quote(jd, m))
            hard.append(code)
        # Explicit existing residency requirement, not inferred visa policy.
        for match in BASE_RESTRICTION.finditer(jd):
            place = (match.group("place") or match.group("place2") or "").lower()
            if (market == "SG" and place == "singapore") or (
                market == "CN" and place in ("china", "mainland china")):
                strong_cue("CURRENT_LOCAL_RESIDENCY_REQUIREMENT", match)
                break
        for match in PHD_REQUIRED.finditer(jd):
            excerpt = _quote(jd, match, width=300)
            if not PREFERENCE.search(excerpt) and not SOFT_OVERRIDE.search(excerpt):
                strong_cue("EXPLICIT_PHD_REQUIREMENT_REVIEW", match)
                break
        for match in YEARS.finditer(jd):
            # Crucial real-data counterexample: "At least 2–5 years of
            # experience" matched its UPPER endpoint (5 years), turning
            # an early-career-compatible range into a false hard blocker.
            # Never treat upper 4+/5+ as a minimum if lower end <=3.
            left = jd[max(0, match.start() - 18):match.start()]
            if re.search(r"(?:^|[^0-9])(?:[0-3])\s*(?:-|–|—|to)\s*$", left, re.I):
                continue
            context = _quote(jd, match, width=260)
            # A role must not be rejected for bonus/familiarity, historical
            # company tenure, or non-mandatory preferences. Even a flagged
            # requirement is only a HUMAN REVIEW queue signal in V1.
            if (REQUIRED.search(context) and not PREFERENCE.search(context)
                    and not SOFT_OVERRIDE.search(context)):
                strong_cue("EXPLICIT_4PLUS_EXPERIENCE_REVIEW", match)
                break
        if market == "CN":
            strong_cue("OUTSIDE_TARGET_MARKET_HK_LOCATION_REVIEW", HONG_KONG.search(jd))

        # A role may have genuine AI work despite a generic/mature title.
        # Never infer a blocker from an absent keyword in JD or excerpt.
        if CORE.search(jd):
            strong = True
    else:
        if review.get("full_jd_complete") or review.get("stage") == "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW":
            mark("JD_MISSING_OR_STALE_REHYDRATE", "SOURCE_STATE", "Previously verified JD absent or older than 48 hours")
        elif row.get("description_excerpt"):
            mark("LISTING_EXCERPT_NOT_FULL_JD", "SOURCE_STATE", "Partial source description only")

    if jd is not None and hard:
        lane = "HARD_REQUIREMENT_REVIEW"
    elif review.get("possible_prior_issue"):
        lane = "HISTORY_CHECK"
    elif jd is not None:
        lane = "JD_READY" if strong else "SCOPE_REVIEW"
    elif (NON_CORE.search(title) or
          (not research and (CONTRACT.search(title) or INTERN.search(title))) or
          (not strong and MATURE.search(title))):
        # Only lower source-fetch priority. A genuine LLM team may still
        # advertise robotics, client delivery or other adjacent work.
        lane = "LOW_PRIORITY_SOURCE_GAP"
    else:
        lane = "SOURCE_GAP"

    return {
        "lane": lane, "market": market, "has_fresh_full_jd": jd is not None,
        "track_hint": "RES" if research else "ENG",
        "core_signal_hint": bool(strong),
        "evidence": evidence,
        "rule_codes": [x["code"] for x in evidence],
        "auto_reject": False, "auto_ack": False, "applicant_fit": "NOT_DECIDED",
        "reason": ("Review the exact quote, alternatives and applicant evidence before any disposition"
                   if hard else "Review signal only; missing full JD requires source recovery"
                   if jd is None else "Full employer JD available for one-pass Scout review"),
    }


def audit(states: dict, *, now: datetime | None = None) -> dict:
    """Current private queues and historical terminal labels, read-only."""
    now = now or datetime.now(timezone.utc)
    markets = {}
    for market in ("SG", "MY", "CN"):
        state = states.get(market)
        if not isinstance(state, dict) or state.get("market") != market:
            raise ValueError("invalid source state for " + market)
        pending = state.get("pending")
        terminal = state.get("terminal")
        if not isinstance(pending, list) or not isinstance(terminal, list):
            raise ValueError("invalid state rows for " + market)
        rows = [triage(row, market, now=now) for row in pending]
        labels = Counter(str(row.get("state") or "UNKNOWN") for row in terminal)
        counts = Counter(x["lane"] for x in rows)
        historical_missing_reasons = sum(
            1 for x in terminal if x.get("state") in ("HARD_REJECTED", "HARD_REJECT")
            and not str(x.get("reason") or "").strip())
        # Historical ISSUE_VERIFIED is an imperfect positive control: the
        # actual Issue could be APPLY/CHECK/WAIT. Replay only to catch obvious
        # over-flagging, NEVER to certify recall or tune this single snapshot.
        controls = [x for x in terminal if x.get("state") == "ISSUE_VERIFIED"]
        control_lanes = Counter(triage(x, market, now=now)["lane"] for x in controls)
        control_hard = [
            {"key": x.get("key"), "title": x.get("title"),
             "rule_codes": triage(x, market, now=now)["rule_codes"]}
            for x in controls
            if triage(x, market, now=now)["lane"] == "HARD_REQUIREMENT_REVIEW"
        ]
        markets[market] = {
            "pending": len(pending),
            "fresh_full_jds": sum(x["has_fresh_full_jd"] for x in rows),
            "source_gaps": sum(not x["has_fresh_full_jd"] for x in rows),
            "lanes": dict(sorted(counts.items())),
            "historical_terminal_states": dict(sorted(labels.items())),
            "historical_hard_rejects_missing_reason": historical_missing_reasons,
            "issue_verified_imperfect_controls": len(controls),
            "issue_verified_controls_by_lane": dict(sorted(control_lanes.items())),
            "issue_verified_hard_review_counterexamples": control_hard,
            "auto_rejections": 0,
            "auto_acknowledgements": 0,
            "reviewed_rows": [
                {"key": source.get("key"), "title": source.get("title"),
                 "company": source.get("company"), **decision}
                for source, decision in zip(pending, rows)
            ],
        }
    return {
        "version": 1, "mode": "PRIVATE_RULE_TRIAGE_DRY_RUN_NO_MUTATIONS",
        "generated_at": now.isoformat(), "markets": markets,
        "caveat": "Existing Pending queues are bounded/censored; historical labels are noisy and not ground truth. No hard terminal decisions or employer contact.",
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Read-only triage audit of existing Pending sources.")
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    states = {
        m: json.loads((args.repo / "discovery-state" / f"platform-index-{m.lower()}.json").read_text())
        for m in ("SG", "MY", "CN")
    }
    result = audit(states)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    for market, item in result["markets"].items():
        print(market, "pending", item["pending"], "fresh JD", item["fresh_full_jds"],
              "lanes", json.dumps(item["lanes"], ensure_ascii=False),
              "historical unreasoned hard rejects", item["historical_hard_rejects_missing_reason"])
    print("NO APPLY/CHECK/ACK/REJECT decisions made; dry run only")


if __name__ == "__main__":
    main()
