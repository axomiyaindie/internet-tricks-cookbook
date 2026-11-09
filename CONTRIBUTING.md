# Contributing

Thanks for helping keep this cookbook useful. Tricks go stale as platforms change, so fixes and updates matter as much as new recipes.

## Repository Structure

```text
internet-tricks-cookbook/
|-- assets/
|   `-- logo.svg
|-- browser-and-search/
|   |-- advanced-search-operators.txt
|   `-- hidden-flags-config.txt
|-- privacy-and-accounts/
|   |-- disposable-email-routing.md
|   `-- remove-tracking-parameters.md
|-- social-and-content/
|   |-- clean-video-sharing.md
|   `-- feed-algorithm-resets.md
|-- everyday-savings/
|   `-- price-comparison-tips.md
|-- automation/
|   |-- headless-scraper.js
|   `-- rss-feed-generator.py
|-- devtools/
|   |-- devtools-console-tricks.md
|   `-- network-throttling-profiles.json
|-- api-and-webhooks/
|   |-- dynamic-dns-updater.py
|   `-- status-check-webhook.sh
|-- CONTRIBUTING.md
|-- LICENSE
|-- RECIPE_TEMPLATE.md
`-- README.md
```

| Folder | What goes here |
|---|---|
| `browser-and-search` | Search operators, browser settings and flags |
| `privacy-and-accounts` | Email aliasing, tracking removal, privacy settings |
| `social-and-content` | Link sharing, feed resets, notification controls |
| `everyday-savings` | Price comparison and savings methods |
| `automation` | Scraping and automation scripts |
| `devtools` | Console snippets, throttling profiles, debugging tips |
| `api-and-webhooks` | Uptime checks, alerts, API integrations |

## Adding a Recipe

1. [Fork the repository](https://github.com/rakibuilds/internet-tricks-cookbook/fork) and clone your fork.
2. Create a branch: `git checkout -b trick/your-trick-name`
3. Add your file to the most relevant category folder.
4. Start from [`RECIPE_TEMPLATE.md`](RECIPE_TEMPLATE.md) for guides.
5. Add your recipe to the Recipes table in [`README.md`](README.md).
6. Commit, push, and [open a Pull Request](https://github.com/rakibuilds/internet-tricks-cookbook/compare) describing the problem your trick solves.

## Recipe Format

Every recipe starts with a short header:

- **Purpose:** one sentence on the problem it solves.
- **Requirements:** browser, tool, or account needed (or "None").
- **Usage or steps:** clear instructions anyone can follow.

Guides use Markdown (`.md`) or plain text (`.txt`). Scripts use their native extension (`.js`, `.py`, `.sh`) with the header written as a comment at the top. Use lowercase file names with hyphens, such as `my-new-trick.md`.

## Rules

Allowed:
- Browser and app settings, UI tweaks, and hidden toggles
- Privacy and tracking-reduction techniques
- Search shortcuts and productivity workflows
- Automation scripts, API recipes, and DevTools snippets

Not allowed:
- Account hijacking, credential harvesting, or phishing tools
- Malware, exploits, or anything designed to cause harm
- Bypassing paywalls, licensing, or access controls on content you have no right to access
- Anything that violates the law or harms others

Scripts that fetch web pages must respect `robots.txt`, rate limits, and site terms of service.

## Security

Never commit passwords, API tokens, or keys. Read credentials from environment variables, as `dynamic-dns-updater.py` does.

## Fixing Outdated Recipes

If a menu moved or a setting changed, edit the recipe and note the version or date you tested it on. You can also [open an issue](https://github.com/rakibuilds/internet-tricks-cookbook/issues/new) to report a broken recipe.
