# X (Twitter) Search Operators

**Purpose:** Find exact posts quickly with advanced search commands.
**Requirements:** X on the web, or the search box in the app.
**Note:** Operators change over time. The Advanced Search page at `x.com/search-advanced` builds queries for you.

| Operator | Example | Result |
|---|---|---|
| `from:` | `from:nasa` | Posts by an account |
| `to:` | `to:nasa` | Replies to an account |
| `"..."` | `"launch window"` | Exact phrase |
| `-word` | `moon -artemis` | Excludes a word |
| `OR` | `moon OR mars` | Either word |
| `since:` / `until:` | `since:2026-01-01 until:2026-06-30` | Date range |
| `min_faves:` | `min_faves:1000` | At least 1000 likes |
| `min_retweets:` | `min_retweets:100` | At least 100 reposts |
| `filter:media` | `nasa filter:media` | Posts with images or video |
| `filter:links` | `nasa filter:links` | Posts that contain links |
| `-filter:replies` | `nasa -filter:replies` | Hides replies |
| `lang:` | `lang:en` | Language |
| `url:` | `url:example.com` | Posts linking to a domain |

## Example

```
from:nasa filter:media min_faves:1000 since:2026-01-01
```
