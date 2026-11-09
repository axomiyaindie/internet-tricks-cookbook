# Fork, Sync, and Contribute

**Purpose:** Work on a fork, keep it updated, and send changes back to the original repository.
**Requirements:** Git and a GitHub account.

## Set up

```bash
git clone https://github.com/YOUR-USER/REPO.git
cd REPO
git remote add upstream https://github.com/ORIGINAL-OWNER/REPO.git
git remote -v
```

## Keep your fork updated

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

## Contribute

1. Create a branch: `git checkout -b feature/my-change`
2. Commit your work and push: `git push -u origin feature/my-change`
3. On GitHub, open a pull request with the original repository as the base.

## Fix merge conflicts

Git marks the clashing section with three kinds of lines: one starting with seven `<` characters followed by a branch name, one with seven `=` characters, and one with seven `>` characters. Your version sits above the `=` line and theirs below it.

Edit the file to keep what you want, delete all three marker lines, then run `git add` and `git commit`. Search for `<<<<<<<` before committing to be sure none remain.

## 403 errors when pushing

A 403 usually means Git is using saved credentials for a different account. Remove the `git:https://github.com` entry in Windows Credential Manager and try again.
