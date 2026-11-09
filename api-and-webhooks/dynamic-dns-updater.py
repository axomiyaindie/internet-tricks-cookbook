#!/usr/bin/env python3
"""
dynamic-dns-updater.py
Purpose:      Keep a DNS A record pointed at your home server's public IP.
Requirements: Python 3.8+ (standard library only), a domain on Cloudflare.
Setup:        Create a Cloudflare API token with Zone > DNS > Edit for your zone.
              Find your Zone ID on the zone overview page, and the Record ID via
              GET /zones/{zone_id}/dns_records.
Environment:  CF_API_TOKEN, CF_ZONE_ID, CF_RECORD_ID, CF_RECORD_NAME
Usage:        python dynamic-dns-updater.py
Schedule:     Run every 5 minutes with cron or Windows Task Scheduler.
"""
import json
import os
import sys
import urllib.request

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".last_ip")


def get_public_ip():
    with urllib.request.urlopen("https://api.ipify.org", timeout=10) as r:
        return r.read().decode().strip()


def update_record(ip):
    zone, record = os.environ["CF_ZONE_ID"], os.environ["CF_RECORD_ID"]
    body = json.dumps({
        "type": "A",
        "name": os.environ["CF_RECORD_NAME"],
        "content": ip,
        "ttl": 300,
        "proxied": False,
    }).encode()
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/zones/{zone}/dns_records/{record}",
        data=body,
        method="PUT",
        headers={
            "Authorization": f"Bearer {os.environ['CF_API_TOKEN']}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def main():
    needed = ("CF_API_TOKEN", "CF_ZONE_ID", "CF_RECORD_ID", "CF_RECORD_NAME")
    missing = [k for k in needed if k not in os.environ]
    if missing:
        sys.exit("Missing environment variables: " + ", ".join(missing))

    ip = get_public_ip()
    last = open(STATE_FILE).read().strip() if os.path.exists(STATE_FILE) else ""
    if ip == last:
        print(f"IP unchanged ({ip}).")
        return

    result = update_record(ip)
    if result.get("success"):
        with open(STATE_FILE, "w") as f:
            f.write(ip)
        print(f"Updated {os.environ['CF_RECORD_NAME']} to {ip}")
    else:
        sys.exit(f"Cloudflare error: {result.get('errors')}")


if __name__ == "__main__":
    main()
