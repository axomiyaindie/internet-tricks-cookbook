#!/usr/bin/env python3
"""
rss-feed-generator.py
Purpose:      Turn the links on a web page into an RSS feed.
Requirements: Python 3.8+, pip install requests beautifulsoup4
Usage:        python rss-feed-generator.py https://example.com/blog \
                  --selector "article h2 a" --title "Example Blog" --out feed.xml
Be polite:    The script checks robots.txt and refuses disallowed pages.
"""
import argparse
import sys
from email.utils import format_datetime
from datetime import datetime, timezone
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
from xml.sax.saxutils import escape

import requests
from bs4 import BeautifulSoup

USER_AGENT = "internet-tricks-cookbook/1.0"


def allowed_by_robots(url):
    parts = urlparse(url)
    parser = RobotFileParser(f"{parts.scheme}://{parts.netloc}/robots.txt")
    try:
        parser.read()
    except Exception:
        return True
    return parser.can_fetch(USER_AGENT, url)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--selector", default="a", help="CSS selector for links")
    ap.add_argument("--title", default="Generated feed")
    ap.add_argument("--out", default="feed.xml")
    ap.add_argument("--limit", type=int, default=30)
    args = ap.parse_args()

    if not allowed_by_robots(args.url):
        sys.exit("robots.txt disallows fetching this page.")

    resp = requests.get(args.url, headers={"User-Agent": USER_AGENT}, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    now = format_datetime(datetime.now(timezone.utc))
    items, seen = [], set()
    for a in soup.select(args.selector):
        href, text = a.get("href"), a.get_text(strip=True)
        if not href or not text:
            continue
        link = urljoin(args.url, href)
        if link in seen:
            continue
        seen.add(link)
        items.append(
            f"<item><title>{escape(text)}</title><link>{escape(link)}</link>"
            f"<guid>{escape(link)}</guid><pubDate>{now}</pubDate></item>"
        )
        if len(items) >= args.limit:
            break

    feed = (
        '<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel>'
        f"<title>{escape(args.title)}</title><link>{escape(args.url)}</link>"
        f"<description>Feed generated from {escape(args.url)}</description>"
        + "".join(items)
        + "</channel></rss>"
    )
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(feed)
    print(f"Wrote {len(items)} items to {args.out}")


if __name__ == "__main__":
    main()
