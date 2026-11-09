# Clean Video Sharing

**Purpose:** Share video links without tracking tokens or an unwanted start time.
**Requirements:** None.

## YouTube

| Link type | Format |
|---|---|
| Standard | `https://www.youtube.com/watch?v=VIDEO_ID` |
| Short | `https://youtu.be/VIDEO_ID` |
| Start at 1m30s | `https://youtu.be/VIDEO_ID?t=90` |

1. Click Share and copy the link.
2. Delete everything starting from `?si=` (or `&si=`) to drop the tracking token.
3. Keep `?t=90` only if you want a specific start time. The number is seconds.

Before: `https://youtu.be/VIDEO_ID?si=AbCdEf123&t=90`
After:  `https://youtu.be/VIDEO_ID?t=90`

## Other platforms

- Instagram: remove `?igsh=...` or `?igshid=...`.
- Spotify: remove `?si=...`.
- X/Twitter: remove `?s=...&t=...`.
- Facebook: remove `?fbclid=...`.

See [Remove Tracking Parameters From Links](../../privacy-and-security/remove-tracking-parameters.md) for a snippet that does this automatically.
