# Custom Search Shortcuts in Chrome and Edge

**Purpose:** Search any site straight from the address bar with a short keyword.
**Requirements:** Chrome or Edge.

## Steps

1. Chrome: Settings > **Search engine** > **Manage search engines and site search**. Edge: `edge://settings/searchEngines`.
2. Under **Site search**, click **Add**.
3. Enter a name, a short keyword, and a URL with `%s` where the search words go.
4. In the address bar, type the keyword, press `Tab` or `Space`, then type your search.

## Examples

| Keyword | URL |
|---|---|
| `yt` | `https://www.youtube.com/results?search_query=%s` |
| `gh` | `https://github.com/search?q=%s` |
| `wiki` | `https://en.wikipedia.org/w/index.php?search=%s` |
| `maps` | `https://www.google.com/maps/search/%s` |

## Tip

To find a site's search URL, search for something on the site and copy the address, then replace your search words with `%s`.
