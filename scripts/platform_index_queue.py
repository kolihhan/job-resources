#!/usr/bin/env python3
"""Machine-only SG/MY search-index candidate handoff.

GitHub Issues remain the only actionable opportunity state. This queue is a
transport/ack checkpoint, never an APPLY tracker or proof a role is live.

Commands:
  ingest --market MY --input <provider-or-manual.json> --known <known.json> --state <state.json>
  next --state <state.json> --limit 20
  ack --state <state.json> --receipt <receipt.json> --known <known.json>
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import urlparse
from urllib.request import Request, urlopen

try:
    from probe_public_job_index import candidate_url
except ImportError:
    import importlib.util
    spec=importlib.util.spec_from_file_location("probe_public_job_index",Path(__file__).with_name("probe_public_job_index.py"))
    _module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_module)
    candidate_url=_module.candidate_url

MARKETS={"SG","MY"}
TERMINAL={"HARD_REJECTED","DUPLICATE_CONFIRMED","ISSUE_VERIFIED"}

def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00","Z")

def key_for(market: str,url: str) -> str:
    return market.lower()+":"+hashlib.sha256(url.encode("utf-8")).hexdigest()[:20]

def canonical(url: str,market: str) -> str | None:
    if not isinstance(url,str):
        return None
    return candidate_url(url.strip(),market)

def new_state(market: str) -> dict:
    return {"version":1,"market":market,"next_seq":1,"next_unacknowledged_seq":1,
            "pending":[],"terminal":[],"last_ingestion":None}

def validate_state(s: dict,market: str) -> None:
    if not isinstance(s,dict) or s.get("version")!=1 or s.get("market")!=market:
        raise ValueError("wrong queue state version/market")
    if not isinstance(s.get("pending"),list) or not isinstance(s.get("terminal"),list):
        raise ValueError("queue pending/terminal fields invalid")
    all_rows=s["pending"]+s["terminal"]
    if len({r["key"] for r in all_rows})!=len(all_rows):
        raise ValueError("duplicate candidate key in queue")
    if len({r["seq"] for r in all_rows})!=len(all_rows):
        raise ValueError("duplicate sequence in queue")
    if not isinstance(s.get("next_seq"),int) or s["next_seq"]<=max([r["seq"] for r in all_rows],default=0):
        raise ValueError("next_seq not beyond stored candidates")
    expected=min((r["seq"] for r in s["pending"]),default=s["next_seq"])
    if s.get("next_unacknowledged_seq")!=expected:
        raise ValueError("inconsistent unacknowledged cursor")

def known_urls(index: dict,market: str) -> set[str]:
    out=set()
    for url in index.get("strong",{}).get("urls",[]):
        val=canonical(url,market)
        if val:out.add(val)
    return out

def ingest(state: dict,index: dict,payload: dict) -> tuple[dict,dict]:
    market=state["market"]
    validate_state(state,market)
    items=payload.get("items")
    if not isinstance(items,list):
        raise ValueError("source payload requires items array")
    if not isinstance(payload.get("source"),str) or not payload["source"]:
        raise ValueError("source ID required")
    known_set=known_urls(index,market)
    existing={r["key"] for r in state["pending"]+state["terminal"]}
    stats={"observed":len(items),"new_pending":0,"exact_history":0,
           "already_seen":0,"invalid_url":0,"market_mismatch":0}
    for item in items:
        if not isinstance(item,dict) or not isinstance(item.get("url"),str):
            stats["invalid_url"]+=1
            continue
        if item.get("market",market)!=market:
            stats["market_mismatch"]+=1
            continue
        url=canonical(item["url"],market)
        if not url:
            stats["invalid_url"]+=1
            continue
        key=key_for(market,url)
        if key in existing:
            stats["already_seen"]+=1
            continue
        if url in known_set:
            # Strong URL hit: suppress without spending a JD read.
            stats["exact_history"]+=1
            existing.add(key)
            state["terminal"].append({"key":key,"seq":state["next_seq"],"url":url,
                  "state":"DUPLICATE_CONFIRMED","evidence":"known-role-index:strong.urls"})
            state["next_seq"]+=1
            continue
        # Weak title/company matching cannot auto-suppress a distinct role.
        title=str(item.get("title") or "")[:180]
        company=str(item.get("company") or "")[:150]
        r={"key":key,"seq":state["next_seq"],"url":url,
           "market":market,"platform":str(item.get("platform") or "")[:48],
           "title":title,"company":company,"state":"UNVERIFIED_INDEX",
           "source":payload["source"][:90],"query":str(item.get("query") or "")[:180],
           "first_seen_at":utcnow(),
           "last_error":None,"retries":0}
        state["pending"].append(r)
        state["next_seq"]+=1
        existing.add(key)
        stats["new_pending"]+=1
    state["next_unacknowledged_seq"]=min((r["seq"] for r in state["pending"]),default=state["next_seq"])
    state["last_ingestion"]={"at":utcnow(),"source":payload["source"],"stats":stats}
    validate_state(state,market)
    return state,stats

def verify_issue_readback(issue_url: str,candidate_url: str,token: str) -> bool:
    # A self-reported boolean is not evidence; verify the live GitHub Issue.
    m=re.fullmatch(r"https://github.com/kolihhan/job-resources/issues/(\d+)",issue_url or "")
    if not m:
        raise ValueError("invalid Issue URL")
    if not token:
        raise ValueError("GITHUB_TOKEN required for actual Issue readback")
    req=Request("https://api.github.com/repos/kolihhan/job-resources/issues/"+m.group(1),
       headers={"Accept":"application/vnd.github+json","Authorization":"Bearer "+token,
                "User-Agent":"job-resources-platform-index-ack/1.0"})
    with urlopen(req,timeout=15) as response:
        issue=json.loads(response.read(1_000_000))
    if not isinstance(issue,dict) or issue.get("number")!=int(m.group(1)) or "pull_request" in issue:
        raise ValueError("GitHub Issue readback mismatch")
    body=str(issue.get("body") or "")
    found=re.findall(r"https?://[^\s<>\])]+",body)
    market="SG" if "sg." in candidate_url else "MY"
    if candidate_url not in {canonical(u.strip('.,'),market) for u in found}:
        raise ValueError("Issue body does not reference this exact platform identity")
    return True

def ack(state: dict,receipt: dict,issue_proven: bool=False) -> dict:
    validate_state(state,state["market"])
    if not isinstance(receipt,dict):raise ValueError("invalid receipt")
    key=receipt.get("key")
    action=receipt.get("action")
    rows=[x for x in state["pending"] if x["key"]==key]
    if len(rows)!=1:raise ValueError("receipt key is not an exact pending candidate")
    row=rows[0]
    if action=="RETRY":
        note=str(receipt.get("reason") or "").strip()
        if len(note)<8:raise ValueError("retry requires a useful reason")
        row["last_error"]=note[:300]
        row["retries"]+=1
    elif action in TERMINAL:
        proof=receipt.get("evidence_url")
        if not isinstance(proof,str) or not proof.startswith("https://"):
            raise ValueError("terminal dispositions require an evidence URL")
        if action=="ISSUE_VERIFIED":
            issue=receipt.get("issue_url")
            if not isinstance(issue,str) or not re.fullmatch(r"https://github.com/kolihhan/job-resources/issues/\d+",issue):
                raise ValueError("ISSUE_VERIFIED requires the canonical GitHub Issue URL")
            if not issue_proven:
                raise ValueError("ISSUE_VERIFIED requires a verified live GitHub Issue readback")
            row["issue_url"]=issue
        row["evidence_url"]=proof
        row["state"]=action
        state["pending"]=[x for x in state["pending"] if x["key"]!=key]
        state["terminal"].append(row)
    else:raise ValueError("action must be RETRY or evidence-backed terminal")
    state["next_unacknowledged_seq"]=min((r["seq"] for r in state["pending"]),default=state["next_seq"])
    validate_state(state,state["market"])
    return state

def atomic_write(path: Path,obj: dict) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=".queue.",dir=path.parent)
    try:
        with os.fdopen(fd,"w",encoding="utf8") as f:
            json.dump(obj,f,ensure_ascii=False,indent=2,sort_keys=True)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)

def main():
    ap=argparse.ArgumentParser()
    sub=ap.add_subparsers(dest="cmd",required=True)
    for name in ("ingest","ack","next"):
        p=sub.add_parser(name)
        p.add_argument("--state",type=Path,required=True)
        if name=="ingest":
            p.add_argument("--market",choices=sorted(MARKETS),required=True)
            p.add_argument("--input",type=Path,required=True)
            p.add_argument("--known",type=Path,required=True)
        if name=="ack":p.add_argument("--receipt",type=Path,required=True)
        if name=="next":p.add_argument("--limit",type=int,default=20)
    args=ap.parse_args()
    state=json.loads(args.state.read_text(encoding="utf8")) if args.state.exists() else (new_state(args.market) if args.cmd=="ingest" else None)
    if state is None:raise SystemExit("queue state missing")
    if args.cmd=="next":
        validate_state(state,state["market"])
        print(json.dumps({"market":state["market"],"cursor":state["next_unacknowledged_seq"],
           "pending_total":len(state["pending"]),"items":state["pending"][:max(0,min(100,args.limit))]},ensure_ascii=False,indent=2))
    elif args.cmd=="ack":
        receipt=json.loads(args.receipt.read_text())
        proven=False
        if receipt.get("action")=="ISSUE_VERIFIED":
            candidate=next((x for x in state["pending"] if x["key"]==receipt.get("key")),None)
            if not candidate:raise ValueError("unknown pending Issue acknowledgement")
            proven=verify_issue_readback(receipt.get("issue_url"),candidate["url"],os.environ.get("GITHUB_TOKEN",""))
        state=ack(state,receipt,issue_proven=proven)
        atomic_write(args.state,state)
        print(json.dumps({"pending":len(state["pending"]),"cursor":state["next_unacknowledged_seq"]}))
    else:
        known=json.loads(args.known.read_text())
        payload=json.loads(args.input.read_text())
        state,stats=ingest(state,known,payload)
        atomic_write(args.state,state)
        print(json.dumps({"market":state["market"],"pending":len(state["pending"]),"cursor":state["next_unacknowledged_seq"],"stats":stats}))
if __name__=="__main__":main()
