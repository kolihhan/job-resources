#!/usr/bin/env python3
"""Read-only JD source probe for one FreeHire shard or list of candidates.

No applications, final eligibility decisions, Issue mutations, or claims that a 200
response proves a job is open. Default is an offline source/fallback plan.
"""
import argparse
from html.parser import HTMLParser
import json
import re
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, quote, urlencode, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

PROVIDERS = {"smartrecruiters.com":"smartrecruiters", "greenhouse.io":"greenhouse",
             "lever.co":"lever", "myworkdayjobs.com":"workday", "workable.com":"workable",
             "jobstreet.com":"jobstreet", "nowcoder.com":"nowcoder", "jobs.apple.com":"apple",
             "careers.tencent.com":"tencent", "jobs.bytedance.com":"bytedance"}
TRACKERS = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid", "geoID"}
MARKERS = ("job description", "responsibil", "requirement", "qualification", "what will you do",
           "岗位职责", "岗位要求", "任职要求", "职位要求", "工作职责")


def source_info(url):
    try:
        p = urlsplit(str(url).strip())
        port = p.port
    except ValueError:
        return {"kind":"BAD_URL"}
    if p.scheme != "https" or not p.hostname or p.username or p.password or port not in (None,443):
        return {"kind":"BAD_URL"}
    host = p.hostname.lower()
    provider = next((v for domain,v in PROVIDERS.items() if host==domain or host.endswith("."+domain)),None)
    if not provider:
        return {"kind":"RADAR_OR_UNKNOWN", "url":url}
    params = [(k,v) for k,v in parse_qsl(p.query,keep_blank_values=True)
              if k.lower() not in {t.lower() for t in TRACKERS} and not k.lower().startswith("utm_")]
    clean = urlunsplit(("https",p.netloc,p.path,urlencode(params),""))
    api = None
    parts = [s for s in p.path.split("/") if s]
    if provider == "smartrecruiters" and len(parts)>1 and re.match(r"^\d+", parts[1]):
        ident = re.match(r"^\d+",parts[1]).group()
        api = f"https://api.smartrecruiters.com/v1/companies/{quote(parts[0])}/postings/{ident}"
    if provider == "greenhouse" and len(parts)>2 and parts[1]=="jobs" and parts[2].isdigit():
        api = f"https://boards-api.greenhouse.io/v1/boards/{quote(parts[0])}/jobs/{parts[2]}?content=true"
    return {"kind":"DIRECT_SOURCE", "provider":provider, "url":clean, "api":api}


class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip=0
        self.chunks=[]
    def handle_starttag(self,tag,attrs):
        if tag in ("script","style","noscript","svg"): self.skip+=1
    def handle_endtag(self,tag):
        if tag in ("script","style","noscript","svg") and self.skip:self.skip-=1
    def handle_data(self,data):
        if not self.skip:self.chunks.append(data)


def to_text(raw,content_type):
    if "json" in content_type or raw.lstrip().startswith("{"):
        try:
            obj=json.loads(raw)
            fields=[obj[k] for k in ("title","name","content","description","jobDescription") if isinstance(obj.get(k),str)]
            for section in (obj.get("jobAd",{}).get("sections",{}) or {}).values():
                if isinstance(section,dict):fields.extend(str(v) for v in section.values() if isinstance(v,str))
            raw="\n".join(fields)
        except (ValueError,AttributeError):return ""
    html=TextOnly();html.feed(raw)
    return " ".join(" ".join(html.chunks).split())


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):return None


def fetch_jd(url):
    if source_info(url)["kind"] != "DIRECT_SOURCE":return False,"","UNSUPPORTED"
    try:
        req=Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; JobScoutReadOnly/1.0)","Accept":"text/html,application/json"})
        with build_opener(NoRedirect).open(req,timeout=10) as rsp:
            return True,to_text(rsp.read(450000).decode("utf-8","replace"),rsp.headers.get("Content-Type","text/html")),"HTTP_200"
    except HTTPError as e:return False,"",f"HTTP_{e.code}"
    except (URLError,OSError,ValueError) as e:return False,"",type(e).__name__


def probe(row,fetch=False):
    source=source_info(row.get("source_url",""))
    title=str(row.get("title") or "").strip()
    company=str(row.get("company") or "").strip()
    source_id = re.search(r"(?i)(?:JR\d{5,}|WD\d{4,}|R\d{6,}|\b\d{10,}\b)", source.get("url") or "")
    search = f'"{company}" "{title}"' + (f' "{source_id.group()}"' if source_id else '')
    out={"candidate_seq":row.get("candidate_seq"),"company":company,"title":title,
         "source_id_hint":source_id.group() if source_id else None,
         "source_kind":source["kind"],"provider":source.get("provider"),
         "canonical_url":source.get("url"),"api_url":source.get("api"),
         "fallback_search":search + " careers job",
         "status":"NOT_FETCHED" if not fetch else "SOURCE_UNVERIFIED",
         "job_live":"UNKNOWN","application_route":"UNKNOWN","requires_human_review":True}
    if not fetch or source["kind"]!="DIRECT_SOURCE":return out
    attempts=[]
    for url in (source.get("api"),source["url"]):
        if not url:continue
        ok,text,status=fetch_jd(url)
        low=text.lower()
        words=[w.lower() for w in re.findall(r"[\w\u4e00-\u9fff]+",title) if len(w)>2]
        title_ok=title.lower() in low or (bool(words) and sum(w in low for w in words)>=min(2,len(words)))
        is_jd=ok and len(text)>=250 and title_ok and any(s in low for s in MARKERS)
        attempts.append({"source":url,"http_status":status,"chars":len(text),"title_match":title_ok,"substantive_jd":is_jd})
        if is_jd:
            out["status"]="JD_CONTENT_FOUND"  # Not proof that role is open or eligible!
            break
    out["attempts"]=attempts
    return out


def test():
    row={"candidate_seq":743,"company":"NCS3","title":"#EG AI Engineer",
         "source_url":"https://jobs.smartrecruiters.com/NCS3/6000000001474348--eg-ai-engineer?utm_source=freehire.me"}
    info=source_info(row["source_url"])
    assert info["url"]=="https://jobs.smartrecruiters.com/NCS3/6000000001474348--eg-ai-engineer"
    assert info["api"].endswith("/6000000001474348")
    assert source_info("http://127.0.0.1/")["kind"]=="BAD_URL"
    assert source_info("https://freehire.me/jobs/xyz")["kind"]=="RADAR_OR_UNKNOWN"
    html="<h1>#EG AI Engineer</h1><p>Job Description "+"RAG evaluation and AI engineering. "*25+"</p><p>Qualifications: 4–5 years.</p>"
    assert len(to_text(html,"text/html"))>250
    assert "Qualifications" in to_text(json.dumps({"title":"#EG AI Engineer","jobAd":{"sections":{"qualification":{"text":"Qualifications: 4 years"}}}}),"application/json")
    assert probe(row)["job_live"]=="UNKNOWN"
    assert probe(row)["status"]=="NOT_FETCHED"
    assert "JR00048554" in probe({"company":"ABB","title":"应用软件开发(AI)","source_url":"https://abb.wd3.myworkdayjobs.com/x/-AI-_JR00048554"})["fallback_search"]
    assert source_info("https://dbs.wd3.myworkdayjobs.com/DBS_Careers/job/Guangzhou/AI-Engineer_WD89063")["provider"] == "workday"
    assert source_info("https://jobs.bytedance.com/experienced/position/7688617050661488901/detail")["provider"] == "bytedance"
    assert source_info("https://job-boards.greenhouse.io/binance/jobs/5002667101")["api"].endswith("/binance/jobs/5002667101?content=true")
    real_fetch = globals()["fetch_jd"]
    try:
        globals()["fetch_jd"] = lambda url: (True, to_text(html, "text/html"), "HTTP_200")
        assert probe(row, fetch=True)["status"] == "JD_CONTENT_FOUND"
        assert probe(row, fetch=True)["job_live"] == "UNKNOWN"
        globals()["fetch_jd"] = lambda url: (True, "Loading...", "HTTP_200")
        assert probe(row, fetch=True)["status"] == "SOURCE_UNVERIFIED"
        globals()["fetch_jd"] = lambda url: (False, "", "HTTP_403")
        assert probe(row, fetch=True)["status"] == "SOURCE_UNVERIFIED"
    finally:
        globals()["fetch_jd"] = real_fetch
    print("PASS: URL canonicalization, ATS ID, safe sources, HTML/JSON JD extraction, conservative liveness")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",help="JSON list or shard with candidates key; read-only")
    p.add_argument("--fetch",action="store_true",help="Bounded public GET, 10-second timeout")
    p.add_argument("--limit",type=int,default=10)
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    if a.self_test:test();return
    if not a.input or not 1<=a.limit<=15:p.error("--input and --limit 1..15 required")
    with open(a.input,encoding="utf-8") as f:payload=json.load(f)
    rows=payload if isinstance(payload,list) else payload.get("candidates",[])
    if not isinstance(rows,list):p.error("expected list of candidates")
    for row in rows[:a.limit]:
        if isinstance(row,dict):print(json.dumps(probe(row,a.fetch),ensure_ascii=False))


if __name__=="__main__":main()
