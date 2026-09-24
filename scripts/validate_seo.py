#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "_config.yml"
SITE_TITLE_SEPARATOR = " | "
MAX_TITLE = 70
MAX_DESCRIPTION = 160
TARGET_DESCRIPTION_MIN = 120
TARGET_DESCRIPTION_MAX = 155

MD_IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<url>[^)\s]+)")
HTML_IMG_RE = re.compile(r"<img\b(?P<attrs>[^>]*)>", re.I)
ALT_RE = re.compile(r"\balt=[\"'](?P<alt>[^\"']*)[\"']", re.I)


def main() -> int:
    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
    site_title = str(config.get("title") or "").strip()
    defaults = config.get("defaults") or []
    errors: list[str] = []
    warnings: list[str] = []
    titles: list[tuple[str, str]] = []
    descriptions: list[tuple[str, str]] = []

    for entry in defaults:
        scope = entry.get("scope") or {}
        values = entry.get("values") or {}
        path = str(scope.get("path") or "").strip()
        title = str(values.get("title") or "").strip()
        description = str(values.get("description") or "").strip()
        if not path or not (title or description):
            continue
        if not (ROOT / path).is_file():
            errors.append(f"SEO metadata references missing file: {path}")
            continue
        if not title:
            errors.append(f"{path}: missing SEO title")
        else:
            generated = f"{title}{SITE_TITLE_SEPARATOR}{site_title}"
            if len(generated) > MAX_TITLE:
                errors.append(f"{path}: generated title is {len(generated)} characters; max {MAX_TITLE}")
            titles.append((title.casefold(), path))
        if not description:
            errors.append(f"{path}: missing description")
        else:
            if len(description) > MAX_DESCRIPTION:
                errors.append(f"{path}: description is {len(description)} characters; max {MAX_DESCRIPTION}")
            elif not TARGET_DESCRIPTION_MIN <= len(description) <= TARGET_DESCRIPTION_MAX:
                warnings.append(
                    f"{path}: description is {len(description)} characters; target "
                    f"{TARGET_DESCRIPTION_MIN}-{TARGET_DESCRIPTION_MAX}"
                )
            descriptions.append((description.casefold(), path))

    for normalized, count in Counter(value for value, _ in titles).items():
        if count > 1:
            paths = [path for value, path in titles if value == normalized]
            errors.append(f"duplicate SEO title: {', '.join(paths)}")
    for normalized, count in Counter(value for value, _ in descriptions).items():
        if count > 1:
            paths = [path for value, path in descriptions if value == normalized]
            errors.append(f"duplicate description: {', '.join(paths)}")

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".md", ".html"}:
            continue
        if any(part in {".git", "_site"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        label = path.relative_to(ROOT)
        for match in MD_IMAGE_RE.finditer(text):
            if not match.group("alt").strip():
                errors.append(f"{label}: Markdown image missing alt text: {match.group('url')}")
        for match in HTML_IMG_RE.finditer(text):
            alt = ALT_RE.search(match.group("attrs"))
            if not alt or not alt.group("alt").strip():
                errors.append(f"{label}: HTML image missing descriptive alt text")

    print(f"SEO pages checked: {len(titles)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
