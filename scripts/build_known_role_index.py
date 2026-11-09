#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import tempfile
import unicodedata
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen

_URL_RE = re.compile(r"https?://[^\s<>()\[\]{}]+", re.IGNORECASE)
_PREFIX_RE = re.compile(r"^(?:\[[^\]]+\])+\s*")
_DASH_RE = re.compile(r"\s+[—–]\s+")


def normalize_url(value: str) -> str:
    text = str(value or "").strip().rstrip(".,;:'\" )")
    if not text:
        return ""
    parsed = urlsplit(text)
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
        return ""
    query = [
        (key, val)
        for key, val in parse_qsl(parsed.query, keep_blank_values=True)
        if not key.lower().startswith("utm_")
    ]
    path = parsed.path or "/"
    if path != "/":
        path = path.rstrip("/")
    return urlunsplit(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            path,
            urlencode(query, doseq=True),
            parsed.fragment,
        )
    )


def _norm_text(value: object) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).lower().strip()
    text = re.sub(r"[^\w\u4e00-\u9fff]+", " ", text, flags=re.UNICODE)
    return " ".join(text.split())


def _weak_company_title(issue_title: str) -> str | None:
    title = _PREFIX_RE.sub("", str(issue_title or "").strip())
    parts = _DASH_RE.split(title)
    if len(parts) < 2:
        return None
    company = _norm_text(parts[0])
    role = _norm_text(parts[1])
    if not company or not role:
        return None
    return f"{company}|{role}"


def _urls_from_issue(issue: dict) -> list[str]:
    text = f"{issue.get('title') or ''}\n{issue.get('body') or ''}"
    urls: list[str] = []
    for match in _URL_RE.findall(text):
        normalized = normalize_url(match)
        if normalized:
            urls.append(normalized)
    return urls


def _freehire_slug(url: str) -> str | None:
    parsed = urlsplit(url)
    if parsed.netloc.lower() not in {"freehire.me", "www.freehire.me"}:
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) >= 2 and parts[0].lower() == "jobs":
        return parts[1].lower()
    return None


def build_index(issues: list[dict], generated_at: str) -> dict:
    urls: set[str] = set()
    freehire_slugs: set[str] = set()
    weak_company_title: set[str] = set()
    wait_employers: set[str] = set()
    issue_numbers: list[int] = []

    for issue in issues:
        if issue.get("pull_request"):
            continue
        number = issue.get("number")
        if isinstance(number, int):
            issue_numbers.append(number)
        for url in _urls_from_issue(issue):
            urls.add(url)
            slug = _freehire_slug(url)
            if slug:
                freehire_slugs.add(slug)
        weak = _weak_company_title(str(issue.get("title") or ""))
        if weak:
            weak_company_title.add(weak)
            # WAIT includes submitted/contacted history. Preserve only the
            # company as a cautious review hint, never a hard duplicate ID.
            if str(issue.get("title") or "").startswith("[WAIT]"):
                wait_employers.add(weak.split("|", 1)[0])

    issue_numbers.sort()
    return {
        "version": 1,
        "generated_at": generated_at,
        "issue_count": len(issue_numbers),
        "issue_numbers": issue_numbers,
        "strong": {
            "urls": sorted(urls),
            "freehire_slugs": sorted(freehire_slugs),
        },
        "weak": {
            "company_title": sorted(weak_company_title),
            "wait_employers": sorted(wait_employers),
        },
    }


def fetch_all_issues(repository: str, token: str) -> list[dict]:
    if "/" not in repository:
        raise ValueError("repository must be owner/name")
    issues: list[dict] = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repository}/issues?state=all&per_page=100&page={page}"
        request = Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "job-resources-known-role-index/1.0",
            },
        )
        with urlopen(request, timeout=30) as response:
            batch = json.loads(response.read().decode("utf-8"))
        if not isinstance(batch, list):
            raise RuntimeError("GitHub issues API returned malformed payload")
        issues.extend(item for item in batch if isinstance(item, dict) and not item.get("pull_request"))
        if len(batch) < 100:
            break
        page += 1
    return issues


def _atomic_write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", "kolihhan/job-resources"))
    parser.add_argument("--output", default="discovery-state/known-role-index.json")
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    args = parser.parse_args(argv)

    token = os.environ.get(args.token_env, "")
    if not token:
        raise SystemExit(f"missing token in ${args.token_env}")
    issues = fetch_all_issues(args.repository, token)
    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    index = build_index(issues, generated_at=generated_at)
    _atomic_write_json(Path(args.output), index)
    print(
        json.dumps(
            {
                "issue_count": index["issue_count"],
                "strong_urls": len(index["strong"]["urls"]),
                "freehire_slugs": len(index["strong"]["freehire_slugs"]),
                "weak_company_title": len(index["weak"]["company_title"]),
                "output": args.output,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
