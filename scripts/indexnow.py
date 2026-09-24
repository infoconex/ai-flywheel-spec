#!/usr/bin/env python3
"""Submit the deployed AI Flywheel sitemap to IndexNow."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

ENDPOINT = "https://api.indexnow.org/indexnow"


def main() -> int:
    site_url = os.environ.get(
        "INDEXNOW_SITE_URL", "https://infoconex.github.io/ai-flywheel-spec"
    ).rstrip("/")
    key = os.environ.get("INDEXNOW_KEY", "").strip()
    if not key:
        raise RuntimeError("INDEXNOW_KEY is required")
    key_location = os.environ.get(
        "INDEXNOW_KEY_LOCATION", f"{site_url}/{key}.txt"
    ).strip()

    sitemap_url = f"{site_url}/sitemap.xml"
    request = urllib.request.Request(
        sitemap_url, headers={"User-Agent": "ai-flywheel-indexnow/1.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        root = ET.fromstring(response.read())

    host = urlparse(site_url).netloc.lower()
    urls = sorted(
        {
            node.text.strip()
            for node in root.findall(".//{*}loc")
            if node.text
            and node.text.strip()
            and urlparse(node.text.strip()).netloc.lower() == host
            and urlparse(node.text.strip()).path.startswith("/ai-flywheel-spec/")
        }
    )
    if not urls:
        print("IndexNow: sitemap contained no eligible URLs.")
        return 0

    payload = json.dumps(
        {"host": host, "key": key, "keyLocation": key_location, "urlList": urls}
    ).encode("utf-8")
    submit = urllib.request.Request(
        ENDPOINT,
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "ai-flywheel-indexnow/1.0",
        },
    )
    try:
        with urllib.request.urlopen(submit, timeout=30) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        print(f"IndexNow failed: HTTP {error.code}: {body}", file=sys.stderr)
        return 1

    print(f"IndexNow: submitted {len(urls)} URL(s); HTTP {status}.")
    return 0 if status in {200, 202} else 1


if __name__ == "__main__":
    raise SystemExit(main())
