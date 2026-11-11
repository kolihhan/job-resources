#!/usr/bin/env python3
"""Build an auditable *ephemeral* CN source handoff inside an Actions artifact.

All raw jobs remain in the original artifact. This is NOT a second GitHub
Issues inbox, not an applicant tracker, and NOT proof of current eligibility.
The output is not marked consumed until a separate reviewer verifies it.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import parse_qs, urlsplit, urlunsplit

SIGNALS = re.compile(
    r"AI|LLM|RAG|Agent|NLP|MCP|Python|ML|大模型|智能体|机器学习|深度学习|生成式|"
    r"人工智能|算法|检索|搜索|语音|推理|模型|知识图谱|数据科学|后端|软件工程|软件开发|"
    r"机器视觉|计算机视觉|多模态|推荐系统|数据平台|云原生|Backend|Research|研究|科研|研发",
    re.I,
)
SHARD_SIZE = 25


def normalize_url(url: str) -> str:
    if not isinstance(url, str) or not url.startswith(("https://", "http://")):
        return ""
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    # Tencent's exact job identity lives in ?postid=, not the path.
    # Do not collapse every Tencent requisition to /post_detail.html.
    if host == "join.qq.com" and parts.path == "/post_detail.html":
        ids = parse_qs(parts.query).get("postid", [])
        if len(ids) == 1 and re.fullmatch(r"[0-9]{10,20}", ids[0]):
            return "https://join.qq.com/post_detail.html?postid=" + ids[0]
        return ""
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), "", ""))


def project_liepin(j: dict) -> dict | None:
    source_id = str(j.get("sourceId") or "").strip()
    title = str(j.get("title") or "").strip()
    url = normalize_url(j.get("url") or "")
    if not source_id or not title or not url:
        return None
    return {
        "source_key": "liepin:" + source_id,
        "source": "liepin",
        "source_id": source_id,
        "company": str(j.get("company") or "")[:140],
        "title": title[:180],
        "location": str(j.get("location") or "")[:120],
        "experience": str(j.get("experience") or "")[:50],
        "education": str(j.get("education") or "")[:50],
        "source_url": url,
        "posted_at": str(j.get("date") or ""),
        "requires_jd_verification": True,
    }


def project_jobpro(j: dict) -> dict | None:
    company = str(j.get("company_key") or j.get("company") or "").strip()
    title = str(j.get("title") or "").strip()
    role_id = str(j.get("post_id") or "").strip()
    url = normalize_url(j.get("apply_url") or j.get("url") or "")
    if not company or not title or not (role_id or url):
        return None
    return {
        "source_key": f"jobpro:{company}:{role_id or url}",
        "source": "jobpro",
        "source_id": role_id,
        "company": company[:140],
        "title": title[:180],
        "location": str(j.get("work_cities") or j.get("location") or "")[:120],
        "source_url": url,
        "requires_jd_verification": True,
    }


def build_handoff(liepin: dict, jobpro: dict, known: dict, run_id: str) -> tuple[dict, list[dict]]:
    observed = []
    missing_identity = 0
    for projector, raw in ((project_liepin, liepin.get("jobs", [])), (project_jobpro, jobpro.get("jobs", []))):
        if not isinstance(raw, list):
            continue
        for item in raw:
            result = projector(item) if isinstance(item, dict) else None
            if result is None:
                missing_identity += 1
            else:
                observed.append(result)
    all_roles = {}
    for role in observed:
        all_roles.setdefault(role["source_key"], role)
    urls = set(normalize_url(u) for u in (known.get("strong", {}).get("urls") or []))
    candidates = []
    low_signal_count = 0
    for role in all_roles.values():
        if not SIGNALS.search(role["title"]):
            low_signal_count += 1
            continue
        role["exact_url_known_hint"] = bool(role["source_url"] and role["source_url"] in urls)
        candidates.append(role)
    candidates.sort(key=lambda x: (x["source"], x["source_key"]))
    shards = [candidates[i:i + SHARD_SIZE] for i in range(0, len(candidates), SHARD_SIZE)]
    manifest = {
        "version": 1, "source": "cn-action-discovery", "run_id": str(run_id),
        "status": "AWAITING_VERIFICATION", "raw_observed_rows": len(observed),
        "unique_source_identifiers": len(all_roles),
        "missing_identity_rows": missing_identity, "low_signal_rows_in_raw_artifact": low_signal_count,
        "candidate_count": len(candidates), "known_url_hints": sum(r["exact_url_known_hint"] for r in candidates),
        "shard_size": SHARD_SIZE, "shards": [f"cn-source-candidates-{i:02d}.json" for i in range(1, len(shards) + 1)],
        "raw_artifact_reference": f"cn-raw-{run_id}",
        "identity_sha256": hashlib.sha256("\n".join(r["source_key"] for r in candidates).encode()).hexdigest(),
        "warning": "Raw source artifact retains all unscreened rows. AI must verify all Issue history, actual JD, live route, work authorization and eligibility before APPLY/CHECK.",
    }
    if sum(len(shard) for shard in shards) != manifest["candidate_count"]:
        raise ValueError("candidate count/shard mismatch")
    return manifest, shards


# Only titles with strong AI/research signals enter the bounded recurring
# queue; broader SWE listings remain in the lossless source artifacts.
QUEUE_SIGNAL = re.compile(
    r"AI|LLM|RAG|Agent|NLP|MCP|大模型|智能体|机器学习|深度学习|生成式|"
    r"人工智能|算法|检索|知识图谱|模型评测|Research|研究|研发工程师", re.I)


# These exact employer-controlled portals appear in job-pro's observed
# public JSON result set. Any other source remains in the raw audit artifact,
# not silently admitted to the private queue as an official requisition.
JOBPRO_OFFICIAL_HOSTS = frozenset({
    "jobs.bytedance.com",
    "join.qq.com",
    "campus-talent.alibaba.com",
    "nio.jobs.feishu.cn",
    "agirobot.jobs.feishu.cn",
    "01ai.jobs.feishu.cn",
    "lilithgames.jobs.feishu.cn",
    "vrfi1sk8a0.jobs.feishu.cn",
    "cq6qe6bvfr6.jobs.feishu.cn",
    "xiaopeng.jobs.feishu.cn",
    "xiaomi.jobs.f.mioffice.cn",
})


def native_queue_snapshot(shards: list[list[dict]]) -> dict:
    """Project supported CN platform *and official API* IDs to existing transport.

    Still unverified listings: the private Scout must read employer JD, live
    route, eligibility and both-account application history before an Issue.
    """
    jobs = []
    for shard in shards:
        for candidate in shard:
            source = candidate.get("source")
            url = candidate.get("source_url") or ""
            if (source not in ("liepin", "jobpro") or
                not candidate.get("company") or
                not candidate.get("source_id") or
                not url or not QUEUE_SIGNAL.search(candidate.get("title", ""))):
                continue
            if source == "jobpro" and urlsplit(url).hostname not in JOBPRO_OFFICIAL_HOSTS:
                continue
            is_native = source == "liepin"
            jobs.append({
                "market": "CN",
                "ats": "liepin-native-api" if is_native else "jobpro-employer-api",
                "company": candidate["company"],
                "title": candidate["title"],
                "job_id": candidate["source_id"],
                "key": candidate["source_key"],
                "url": url,
                "location": candidate.get("location") or "",
                "evidence": "listing_only", "lane": "AI",
                "triage_priority": "HIGH",
                "source": "liepin:native-api:CN" if is_native else "jobpro:public-employer-api:CN",
                "source_platform": "猎聘" if is_native else "企业官方招聘入口 (job-pro)",
                "discovery_access": "NATIVE_API_LISTING" if is_native else "PUBLIC_EMPLOYER_API_LISTING",
                "description_excerpt": "",
            })
    return {"market": "CN", "jobs": jobs}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--liepin", type=Path, required=True)
    parser.add_argument("--jobpro", type=Path, required=True)
    parser.add_argument("--known", type=Path, default=Path("discovery-state/known-role-index.json"))
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--run-id", type=str, required=True)
    args = parser.parse_args()
    liepin = json.loads(args.liepin.read_text(encoding="utf-8"))
    jobpro = json.loads(args.jobpro.read_text(encoding="utf-8"))
    known = json.loads(args.known.read_text(encoding="utf-8")) if args.known.exists() else {}
    manifest, shards = build_handoff(liepin, jobpro, known, args.run_id)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for filename, shard in zip(manifest["shards"], shards):
        (args.output_dir / filename).write_text(json.dumps({"version": 1, "run_id": args.run_id,
                            "candidate_count": len(shard), "candidates": shard}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "cn-source-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Reuse the existing source queue intake instead of leaving all native
    # platform leads stranded in short-lived CI artifacts.
    queue_source = native_queue_snapshot(shards)
    (args.output_dir / "cn-native-source.json").write_text(
        json.dumps(queue_source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: manifest[key] for key in ("run_id", "unique_source_identifiers", "candidate_count", "low_signal_rows_in_raw_artifact", "known_url_hints", "identity_sha256")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
