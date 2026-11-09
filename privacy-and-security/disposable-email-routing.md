# Email Aliasing

**Purpose:** Sign up for services without exposing your main inbox, and trace who leaks or sells your address.
**Requirements:** Any email account. Alias services are optional.

## Method 1: Plus addressing (Gmail, Outlook, Proton, Fastmail)

Add `+anything` before the `@`. Mail still arrives in your normal inbox.

```
yourname+shopsite@gmail.com
yourname+newsletter@gmail.com
```

1. Use a different tag for every service.
2. Create a filter: Gmail > Settings > Filters and Blocked Addresses > search `to:yourname+shopsite@gmail.com` > apply a label or "Skip Inbox".
3. If spam arrives at a tagged address, you know which service shared it.

Some sites reject the `+` character. Use Method 2 for those.

## Method 2: Dedicated alias services

| Service | Notes |
|---|---|
| Apple Hide My Email | Built into iCloud+, creates random addresses |
| Firefox Relay | Free masks with a Firefox account |
| DuckDuckGo Email Protection | Free `@duck.com` addresses that strip trackers |
| SimpleLogin / addy.io | Open source, supports custom domains |

Replies go through the alias, so your real address stays hidden. Turn off or delete an alias anytime to stop mail from that service.

## Method 3: Custom domain catch-all

If you own a domain, route `*@yourdomain.com` to one inbox and use a unique address per site, such as `amazon@yourdomain.com`.

## Notes

- Keep your main address for banks, government, and recovery emails.
- Aliases are for privacy and organization, not for evading bans or abusing free trials.
