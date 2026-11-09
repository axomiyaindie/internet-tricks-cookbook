# Remove Tracking Parameters From Links

**Purpose:** Strip tracking junk from URLs before sharing or bookmarking.
**Requirements:** A browser. An extension is optional.

## What to remove

| Parameter | Added by |
|---|---|
| `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content` | Marketing links |
| `fbclid` | Facebook / Meta |
| `gclid` | Google Ads |
| `igshid`, `igsh` | Instagram |
| `si` | YouTube and Spotify share links |
| `mc_eid` | Mailchimp |

Everything after `?` is the query string. Parameters that carry content (like `?v=` on YouTube or `?id=` on shops) must stay.

## Manual method

Delete the unwanted `&name=value` or `?name=value` pieces from the address bar, then copy.

## Browser console snippet

Open DevTools (F12) > Console on the page, paste, and press Enter:

```js
const u = new URL(location.href);
const drop = ["fbclid", "gclid", "igshid", "igsh", "si", "mc_eid"];
[...u.searchParams.keys()]
  .filter(k => k.startsWith("utm_") || drop.includes(k))
  .forEach(k => u.searchParams.delete(k));
console.log(u.href);
```

## Automatic method

- Firefox: Enhanced Tracking Protection strips many known parameters in Strict mode.
- Extensions: ClearURLs (Chrome, Firefox, Edge) removes them as you browse.
