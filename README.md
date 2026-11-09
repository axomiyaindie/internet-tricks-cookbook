<div align="center">

<img src="assets/logo.svg" alt="Internet Tricks Cookbook" width="480">

<br>

**Practical tricks, settings, scripts, and shortcuts for getting more out of the web.**

<br>

[![Stars](https://img.shields.io/github/stars/rakibuilds/internet-tricks-cookbook?style=for-the-badge&logo=github&color=2563eb)](https://github.com/rakibuilds/internet-tricks-cookbook/stargazers)
[![Forks](https://img.shields.io/github/forks/rakibuilds/internet-tricks-cookbook?style=for-the-badge&logo=git&logoColor=white&color=7c3aed)](https://github.com/rakibuilds/internet-tricks-cookbook/network/members)
[![Issues](https://img.shields.io/github/issues/rakibuilds/internet-tricks-cookbook?style=for-the-badge&logo=githubactions&logoColor=white&color=0ea5e9)](https://github.com/rakibuilds/internet-tricks-cookbook/issues)
[![License](https://img.shields.io/github/license/rakibuilds/internet-tricks-cookbook?style=for-the-badge&color=22c55e)](LICENSE)

![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square&logo=git&logoColor=white)
![Last Commit](https://img.shields.io/github/last-commit/rakibuilds/internet-tricks-cookbook?style=flat-square&logo=github)
![Repo Size](https://img.shields.io/github/repo-size/rakibuilds/internet-tricks-cookbook?style=flat-square&logo=files)
![Contributors](https://img.shields.io/github/contributors/rakibuilds/internet-tricks-cookbook?style=flat-square&logo=githubsponsors&logoColor=white)
![Maintained](https://img.shields.io/badge/maintained-yes-blue?style=flat-square)

[Categories](#categories) |
[Quick Start](#quick-start) |
[Structure](#repository-structure) |
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
| ![](https://img.shields.io/badge/-%20-2563eb?style=flat-square&logo=googlechrome&logoColor=white) | **Browser and Search** | Search operators, hidden browser flags, reader settings, performance tweaks |
| ![](https://img.shields.io/badge/-%20-7c3aed?style=flat-square&logo=protonmail&logoColor=white) | **Privacy and Accounts** | Email aliasing, tracking-parameter removal, permission and cookie hygiene |
| ![](https://img.shields.io/badge/-%20-ef4444?style=flat-square&logo=youtube&logoColor=white) | **Social and Content** | Clean link sharing, feed resets, notification and autoplay controls |
| ![](https://img.shields.io/badge/-%20-22c55e?style=flat-square&logo=cashapp&logoColor=white) | **Everyday Savings** | Flight and hotel price comparison, regional pricing checks |
| ![](https://img.shields.io/badge/-%20-f59e0b?style=flat-square&logo=python&logoColor=white) | **Automation and Scraping** | Text extraction, RSS feed generation, page monitoring |
| ![](https://img.shields.io/badge/-%20-0ea5e9?style=flat-square&logo=googlechrome&logoColor=white) | **DevTools** | Console snippets, network throttling profiles, UI debugging |
| ![](https://img.shields.io/badge/-%20-64748b?style=flat-square&logo=gnubash&logoColor=white) | **API and Webhooks** | Uptime checks, alerts, dynamic DNS updaters, integration recipes |

<details>
<summary><b>Example recipes</b> (click to expand)</summary>

<br>

| File | Description |
|---|---|
| `advanced-search-operators.txt` | Cheat sheet of search commands for precise results |
| `clean-video-sharing.md` | Strip tracking tokens from shared video links |
| `feed-algorithm-resets.md` | Clear stale recommendations on major platforms |
| `hidden-flags-config.txt` | Experimental browser settings to speed up page loads |
| `disposable-email-routing.md` | Use aliases to protect your primary inbox |
| `headless-scraper.js` | Extract clean text from messy web pages |
| `rss-feed-generator.py` | Turn static pages into custom RSS feeds |
| `devtools-console-tricks.md` | Console snippets for rapid UI debugging |
| `network-throttling-profiles.json` | Simulate real-world mobile connections |
| `status-check-webhook.sh` | Monitor endpoint uptime and trigger alerts |
| `dynamic-dns-updater.py` | Keep a home server IP updated automatically |

</details>

---

## Quick Start

**For guides:** open any `.md` file in a category folder and follow the steps.

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

## Repository Structure

```text
internet-tricks-cookbook/
|-- assets/
|   `-- logo.svg
|-- browser-and-search/
|-- privacy-and-accounts/
|-- social-and-content/
|-- everyday-savings/
|-- automation/
|-- devtools/
|-- api-and-webhooks/
|-- LICENSE
`-- README.md
```

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

Contributions are welcome. Tricks go stale as platforms change, so fixes and updates matter as much as new recipes.

```mermaid
flowchart LR
    A[Fork the repo] --> B[Create a branch]
    B --> C[Add your recipe]
    C --> D[Open a Pull Request]
    D --> E[Review and merge]
```

1. Fork the repository.
2. Create a branch: `git checkout -b trick/your-trick-name`
3. Add your file to the most relevant category folder.
4. Write clear steps and include the header (purpose, requirements, usage).
5. Open a Pull Request describing the problem your trick solves.

---

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and redistribute the contents of this repository.

<div align="center">

<br>

If this repo helped you, consider giving it a star.

[![Star](https://img.shields.io/badge/Star%20this%20repo-2563eb?style=for-the-badge&logo=github)](https://github.com/rakibuilds/internet-tricks-cookbook)

</div>
