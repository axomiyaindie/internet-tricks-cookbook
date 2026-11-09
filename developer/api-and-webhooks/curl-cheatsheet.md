# curl Cheatsheet

**Purpose:** Make HTTP requests from the terminal for testing APIs and checking sites.
**Requirements:** curl (built into Windows 10+, macOS, and most Linux systems).

## Common commands

```bash
curl https://example.com                      # GET a page
curl -I https://example.com                   # headers only
curl -L https://example.com                   # follow redirects
curl -o page.html https://example.com         # save to a file
curl -s https://api.example.com/data | jq .   # quiet output, pretty-print JSON
```

## Sending data

```bash
curl -X POST https://api.example.com/items \
  -H "Content-Type: application/json" \
  -d '{"name":"test"}'

curl -H "Authorization: Bearer $TOKEN" https://api.example.com/me
```

## Debugging

```bash
curl -v https://example.com                   # verbose request and response
curl -w "%{http_code} %{time_total}s\n" -o /dev/null -s https://example.com
curl --retry 3 --max-time 10 https://example.com
```

## Tips

- Keep tokens in environment variables, never in commands you share or commit.
- On Windows PowerShell, use `curl.exe` so PowerShell's alias does not interfere.
