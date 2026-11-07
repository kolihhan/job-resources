#!/usr/bin/env python3
"""MY TOP feed: Gen Digital/MoneyLion official Ashby, early-career signal lane.

Full official board is kept as a short-lived artifact. Only non-mature technical
titles enter the machine queue. This does not certify employer eligibility or
create GitHub Issues. Previously skipped titles remain visible in the artifact.
"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
from probe_gen_digital_ashby import run

MATURE_TITLE = re.compile(r"(?i)\b(?:senior|principal|staff|lead|director|head|manager|chief)\b")

def transform(result):
    if result.get("status")!="OFFICIAL_BOARD_OBSERVED":
        raise ValueError("official Gen Digital Ashby board was not readable")
    raw = result.get("items")
    if not isinstance(raw,list):
        raise ValueError("missing source roles")
    handoff=[]
    mature=[]
    for item in raw:
        if MATURE_TITLE.search(item.get("title") or ""):
            mature.append({"title":item.get("title"),"source_id":item.get("source_id")})
            continue
        handoff.append(item)
    return {
        "source":"gen-digital:official-ashby:MY",
        "market":"MY","source_kind":"official_employer",
        "observed_at":result["observed_at"],
        "source_credit":"Gen Digital / MoneyLion official Ashby hiring board",
        "source_observed_total":result["total_listed"],
        "source_technical_my":len(raw),
        "mature_title_not_enqueued":mature,
        "items":handoff,
        "liveness_scope":"publicly listed Ashby exact roles, not candidate eligibility"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    raw=run()
    if raw["status"]!="OFFICIAL_BOARD_OBSERVED":
        raise SystemExit("Source unavailable: no queue changes")
    handoff=transform(raw)
    a.out_dir.mkdir(parents=True,exist_ok=True)
    (a.out_dir/"gen-digital-source-raw.json").write_text(
       json.dumps(raw,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    (a.out_dir/"gen-digital-my-candidates.json").write_text(
       json.dumps(handoff,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps({"total_source":raw["total_listed"],
      "technical_my":len(raw["items"]),
      "mature_titles_deferred":len(handoff["mature_title_not_enqueued"]),
      "early_career_handoff":len(handoff["items"]),
      "exact_ids":[x["source_id"] for x in handoff["items"]]},ensure_ascii=False))

if __name__=="__main__":main()
