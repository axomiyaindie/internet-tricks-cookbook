# Internet Tricks Cookbook

An open-source collection of practical tricks, settings, scripts, and shortcuts for getting more out of the web. Each entry is a short, self-contained guide or snippet that solves one specific problem.

Useful for everyday users who want cleaner browsing, better privacy, and faster workflows, and for developers who want reusable automation recipes.

## What You Will Find Here

| Category | What it covers |
|---|---|
| Browser and Search | Search operators, hidden browser flags, reader settings, performance tweaks |
| Privacy and Accounts | Email aliasing, tracking-parameter removal, permission and cookie hygiene |
| Social and Content | Clean link sharing, feed and recommendation resets, notification and autoplay controls |
| Everyday Savings | Price comparison methods for flights and hotels, regional pricing checks |
| Automation and Scraping | Scripts for extracting text, generating RSS feeds, and monitoring pages |
| DevTools | Console snippets, network throttling profiles, UI debugging shortcuts |
| API and Webhooks | Uptime checks, alerts, dynamic DNS updaters, small integration recipes |

## Repository Structure

```
internet-tricks-cookbook/
  browser-and-search/
  privacy-and-accounts/
  social-and-content/
  everyday-savings/
  automation/
  devtools/
  api-and-webhooks/
```

Each trick lives in its own file. Guides are written in Markdown (`.md`), configurations in `.txt` or `.json`, and scripts in their native language (`.js`, `.py`, `.sh`). Every file starts with a short header stating what it does, what it needs, and how to use it.

## Getting Started

No programming experience is needed for the guides. Open any `.md` file and follow the steps.

To use the scripts locally:

```bash
git clone https://github.com/rakibuilds/internet-tricks-cookbook.git
cd internet-tricks-cookbook
```

Open a category folder and read the header of the file you want to run for its dependencies and usage notes.

## Rules

Allowed:
- Browser and app settings, UI tweaks, and hidden toggles
- Privacy and tracking-reduction techniques
- Search shortcuts and productivity workflows
- Automation scripts, API recipes, and DevTools snippets

Not allowed:
- Account hijacking, credential harvesting, or phishing tools
- Malware, exploits, or anything designed to cause harm
- Methods for bypassing paywalls, licensing, or access controls on content you have no right to access
- Anything that violates the law or a service's terms in a way that harms others

Scripts that fetch web pages should respect `robots.txt`, rate limits, and site terms of service.

## Contributing

1. Fork the repository.
2. Create a branch: `git checkout -b trick/your-trick-name`
3. Add your file to the most relevant category folder.
4. Write the steps clearly so anyone can follow them, and include the header (purpose, requirements, usage).
5. Open a Pull Request describing the problem your trick solves.

Tricks go stale as platforms change. If something no longer works, open an issue or submit a fix.

## License

Released under the MIT License. You are free to use, modify, and redistribute the contents of this repository.
