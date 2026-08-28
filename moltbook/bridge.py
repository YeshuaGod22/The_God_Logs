#!/usr/bin/env python3
"""Small GitHub-Actions transport membrane for Moltbook.

Reads one JSON request from moltbook/outbox/, sends it only to the hard-coded
Moltbook host, and writes an auditable response object to moltbook/inbox/.
The API key is read from MOLTBOOK_API_KEY and is never written to disk.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://www.moltbook.com"

# Deliberately small. Extend by reviewed commit when a new API operation is needed.
ALLOWED = {
    "GET": [
        r"/api/v1/agents/me$",
        r"/api/v1/agents/status$",
        r"/api/v1/feed(?:\?.*)?$",
        r"/api/v1/posts(?:\?.*)?$",
        r"/api/v1/posts/[A-Za-z0-9-]+$",
        r"/api/v1/posts/[A-Za-z0-9-]+/comments(?:\?.*)?$",
        r"/api/v1/search(?:\?.*)?$",
        r"/api/v1/submolts(?:\?.*)?$",
    ],
    "POST": [
        r"/api/v1/posts$",
        r"/api/v1/posts/[A-Za-z0-9-]+/comments$",
        r"/api/v1/verify$",
    ],
}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Never follow redirects with a bearer credential attached."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


def allowed(method: str, path: str) -> bool:
    if not path.startswith("/api/v1/"):
        return False
    parsed = urllib.parse.urlsplit(path)
    # Prevent absolute/scheme-relative URLs and fragments.
    if parsed.scheme or parsed.netloc or parsed.fragment:
        return False
    return any(re.fullmatch(pattern, path) for pattern in ALLOWED.get(method, []))


def redact_headers(headers) -> dict[str, str]:  # noqa: ANN001
    safe = {}
    for key, value in headers.items():
        if key.lower() in {"authorization", "set-cookie", "cookie"}:
            continue
        safe[key] = value
    return safe


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("request_file")
    parser.add_argument("--inbox", default="moltbook/inbox")
    args = parser.parse_args()

    request_path = Path(args.request_file)
    payload = json.loads(request_path.read_text(encoding="utf-8"))

    method = str(payload.get("method", "GET")).upper()
    path = str(payload.get("path", ""))
    request_id = str(payload.get("request_id") or request_path.stem)
    body = payload.get("body")

    if not allowed(method, path):
        raise SystemExit(f"Refusing non-allowlisted request: {method} {path}")

    api_key = os.environ.get("MOLTBOOK_API_KEY")
    if not api_key:
        raise SystemExit("MOLTBOOK_API_KEY is not configured")

    data = None
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "User-Agent": "The-God-Logs-Moltbook-Bridge/0.1",
    }
    if body is not None:
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"

    url = BASE_URL + path
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    opener = urllib.request.build_opener(NoRedirect)

    status = None
    response_headers = {}
    raw = b""
    transport_error = None

    try:
        with opener.open(req, timeout=30) as response:
            status = response.status
            response_headers = redact_headers(response.headers)
            raw = response.read()
    except urllib.error.HTTPError as exc:
        status = exc.code
        response_headers = redact_headers(exc.headers)
        raw = exc.read()
    except Exception as exc:  # preserve transport failure as data
        transport_error = f"{type(exc).__name__}: {exc}"

    text = raw.decode("utf-8", errors="replace")
    try:
        response_body = json.loads(text) if text else None
    except json.JSONDecodeError:
        response_body = {"raw_text": text}

    result = {
        "request_id": request_id,
        "request_file": str(request_path),
        "method": method,
        "path": path,
        "base_url": BASE_URL,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "response_headers": response_headers,
        "response": response_body,
        "transport_error": transport_error,
    }

    inbox = Path(args.inbox)
    inbox.mkdir(parents=True, exist_ok=True)
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", request_id)
    output = inbox / f"{safe_id}.response.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)

    # HTTP errors are still valid observations and should be committed.
    return 0 if transport_error is None else 2


if __name__ == "__main__":
    sys.exit(main())
