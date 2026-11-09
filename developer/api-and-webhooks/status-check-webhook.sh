#!/usr/bin/env bash
# status-check-webhook.sh
# Purpose:      Check that a URL responds, and post an alert to a webhook if not.
# Requirements: bash, curl
# Usage:        WEBHOOK_URL="https://hooks.example.com/..." ./status-check-webhook.sh https://example.com
# Cron:         */5 * * * * WEBHOOK_URL="..." /path/status-check-webhook.sh https://example.com
# Webhook:      Sends JSON {"text": "..."} which Slack and many other services accept.

set -u
URL="${1:?Usage: $0 <url>}"
WEBHOOK="${WEBHOOK_URL:-}"

code=$(curl -s -o /dev/null -m 10 -w "%{http_code}" "$URL" || true)
code="${code:-000}"

if [[ "$code" =~ ^[23] ]]; then
  echo "OK: $URL returned $code"
  exit 0
fi

msg="DOWN: $URL returned HTTP $code at $(date -u +%FT%TZ)"
echo "$msg" >&2
if [[ -n "$WEBHOOK" ]]; then
  curl -s -m 10 -X POST -H "Content-Type: application/json" \
       -d "{\"text\": \"$msg\"}" "$WEBHOOK" >/dev/null
fi
exit 1
