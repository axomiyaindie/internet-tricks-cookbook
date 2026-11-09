<div align="center">

<img src="assets/logo.svg" alt="Internet Tricks Cookbook" width="480">

<br>

**Practical tricks, settings, scripts, and shortcuts for getting more out of the web.**

<br>

[![Stars](https://img.shields.io/github/stars/rakibuilds/internet-tricks-cookbook?style=for-the-badge&logo=github&color=2563eb)](https://github.com/rakibuilds/internet-tricks-cookbook/stargazers)
[![Forks](https://img.shields.io/github/forks/rakibuilds/internet-tricks-cookbook?style=for-the-badge&logo=git&logoColor=white&color=7c3aed)](https://github.com/rakibuilds/internet-tricks-cookbook/network/members)
[![Issues](https://img.shields.io/github/issues/rakibuilds/internet-tricks-cookbook?style=for-the-badge&logo=githubactions&logoColor=white&color=0ea5e9)](https://github.com/rakibuilds/internet-tricks-cookbook/issues)
[![License](https://img.shields.io/github/license/rakibuilds/internet-tricks-cookbook?style=for-the-badge&color=22c55e)](LICENSE)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square&logo=git&logoColor=white)](https://github.com/rakibuilds/internet-tricks-cookbook/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/rakibuilds/internet-tricks-cookbook?style=flat-square&logo=github)](https://github.com/rakibuilds/internet-tricks-cookbook/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/rakibuilds/internet-tricks-cookbook?style=flat-square&logo=files)](https://github.com/rakibuilds/internet-tricks-cookbook)
[![Contributors](https://img.shields.io/github/contributors/rakibuilds/internet-tricks-cookbook?style=flat-square&logo=githubsponsors&logoColor=white)](https://github.com/rakibuilds/internet-tricks-cookbook/graphs/contributors)
![Maintained](https://img.shields.io/badge/maintained-yes-blue?style=flat-square)

[Categories](#categories) |
[Recipes](#recipes) |
[Quick Start](#quick-start) |
[Rules](#rules) |
[Contributing](#contributing) |
[License](#license)

</div>

---

## About

Internet Tricks Cookbook is an open-source library of short, self-contained recipes. Each recipe solves one specific problem: a hidden browser setting, a search shortcut, a privacy fix, or a small automation script.

It is built for two audiences:

- **Everyday users** who want cleaner browsing, better privacy, and faster workflows. No programming needed.
- **Developers** who want reusable scripts, DevTools snippets, and API recipes.

> [!NOTE]
> Every recipe starts with a short header stating what it does, what it needs, and how to use it.

---

## Categories

| | Category | What it covers |
|:-:|---|---|
| ![](https://img.shields.io/badge/-%20-2563eb?style=flat-square&logo=googlechrome&logoColor=white) | [**Browser and Search**](browser-and-search) | Search operators, hidden browser flags, reader settings, performance tweaks |
| ![](https://img.shields.io/badge/-%20-7c3aed?style=flat-square&logo=protonmail&logoColor=white) | [**Privacy and Accounts**](privacy-and-accounts) | Email aliasing, tracking-parameter removal, permission and cookie hygiene |
| ![](https://img.shields.io/badge/-%20-ef4444?style=flat-square&logo=youtube&logoColor=white) | [**Social and Content**](social-and-content) | Clean link sharing, feed resets, notification and autoplay controls |
| ![](https://img.shields.io/badge/-%20-22c55e?style=flat-square&logo=cashapp&logoColor=white) | [**Everyday Savings**](everyday-savings) | Flight and hotel price comparison, regional pricing checks |
| ![](https://img.shields.io/badge/-%20-f59e0b?style=flat-square&logo=python&logoColor=white) | [**Automation and Scraping**](automation) | Text extraction, RSS feed generation, page monitoring |
| ![](https://img.shields.io/badge/-%20-0ea5e9?style=flat-square&logo=googlechrome&logoColor=white) | [**DevTools**](devtools) | Console snippets, network throttling profiles, UI debugging |
| ![](https://img.shields.io/badge/-%20-64748b?style=flat-square&logo=gnubash&logoColor=white) | [**API and Webhooks**](api-and-webhooks) | Uptime checks, alerts, dynamic DNS updaters, integration recipes |

---

## Recipes

<details open>
<summary><b>All recipes</b> (click to collapse)</summary>

<br>

| Recipe | Category | Description |
|---|---|---|
| [`advanced-search-operators.txt`](browser-and-search/advanced-search-operators.txt) | Browser and Search | Cheat sheet of search commands for precise results |
| [`hidden-flags-config.txt`](browser-and-search/hidden-flags-config.txt) | Browser and Search | Browser settings to speed up page loads and block autoplay |
| [`disposable-email-routing.md`](privacy-and-accounts/disposable-email-routing.md) | Privacy and Accounts | Use aliases to protect your primary inbox |
| [`remove-tracking-parameters.md`](privacy-and-accounts/remove-tracking-parameters.md) | Privacy and Accounts | Strip tracking junk from links |
| [`clean-video-sharing.md`](social-and-content/clean-video-sharing.md) | Social and Content | Strip tracking tokens from shared video links |
| [`feed-algorithm-resets.md`](social-and-content/feed-algorithm-resets.md) | Social and Content | Clear stale recommendations on major platforms |
| [`price-comparison-tips.md`](everyday-savings/price-comparison-tips.md) | Everyday Savings | Find better flight and hotel prices |
| [`headless-scraper.js`](automation/headless-scraper.js) | Automation and Scraping | Extract clean text from messy web pages |
| [`rss-feed-generator.py`](automation/rss-feed-generator.py) | Automation and Scraping | Turn static pages into custom RSS feeds |
| [`devtools-console-tricks.md`](devtools/devtools-console-tricks.md) | DevTools | Console snippets for rapid UI debugging |
| [`network-throttling-profiles.json`](devtools/network-throttling-profiles.json) | DevTools | Simulate real-world mobile connections |
| [`status-check-webhook.sh`](api-and-webhooks/status-check-webhook.sh) | API and Webhooks | Monitor endpoint uptime and trigger alerts |
| [`dynamic-dns-updater.py`](api-and-webhooks/dynamic-dns-updater.py) | API and Webhooks | Keep a home server IP updated automatically |

</details>

---

## Quick Start

**For guides:** open any `.md` file in a [category folder](#categories) and follow the steps.

**For scripts:**

```bash
git clone https://github.com/rakibuilds/internet-tricks-cookbook.git
cd internet-tricks-cookbook
```

Open a category folder and read the header of the file you want to run for its dependencies and usage notes.

![Markdown](https://img.shields.io/badge/Guides-Markdown-000000?style=flat-square&logo=markdown&logoColor=white)
![JavaScript](https://img.shields.io/badge/Scripts-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Scripts-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Scripts-Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![JSON](https://img.shields.io/badge/Configs-JSON-000000?style=flat-square&logo=json&logoColor=white)

---

## Rules

> [!TIP]
> **Allowed**
> - Browser and app settings, UI tweaks, and hidden toggles
> - Privacy and tracking-reduction techniques
> - Search shortcuts and productivity workflows
> - Automation scripts, API recipes, and DevTools snippets

> [!CAUTION]
> **Not allowed**
> - Account hijacking, credential harvesting, or phishing tools
> - Malware, exploits, or anything designed to cause harm
> - Bypassing paywalls, licensing, or access controls on content you have no right to access
> - Anything that violates the law or harms others

Scripts that fetch web pages should respect `robots.txt`, rate limits, and site terms of service.

---

## Contributing

Contributions are welcome. Tricks go stale as platforms change, so fixes and updates matter as much as new recipes. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide, including the repository structure and recipe format.

```mermaid
flowchart LR
    A[Fork the repo] --> B[Create a branch]
    B --> C[Add your recipe]
    C --> D[Open a Pull Request]
    D --> E[Review and merge]
```

1. [Fork the repository](https://github.com/rakibuilds/internet-tricks-cookbook/fork).
2. Create a branch: `git checkout -b trick/your-trick-name`
3. Add your file to the most relevant [category folder](#categories).
4. Copy [`RECIPE_TEMPLATE.md`](RECIPE_TEMPLATE.md) and follow its header (purpose, requirements, usage).
5. [Open a Pull Request](https://github.com/rakibuilds/internet-tricks-cookbook/compare) describing the problem your trick solves.

Found a broken or outdated recipe? [Open an issue](https://github.com/rakibuilds/internet-tricks-cookbook/issues/new).

---

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and redistribute the contents of this repository.

<div align="center">

<br>

If this repo helped you, consider giving it a star.

[![Star](https://img.shields.io/badge/Star%20this%20repo-2563eb?style=for-the-badge&logo=github)](https://github.com/rakibuilds/internet-tricks-cookbook)

</div>