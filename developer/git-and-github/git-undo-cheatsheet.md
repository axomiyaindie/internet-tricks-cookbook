# Git Undo Cheatsheet

**Purpose:** Fix common Git mistakes without panic.
**Requirements:** Git.
**Warning:** Commands marked dangerous can permanently discard work.

| Goal | Command |
|---|---|
| Unstage a file | `git restore --staged file` |
| Discard changes in a file (dangerous) | `git restore file` |
| Edit the last commit message | `git commit --amend -m "new message"` |
| Undo last commit, keep changes | `git reset --soft HEAD~1` |
| Undo last commit, discard changes (dangerous) | `git reset --hard HEAD~1` |
| Undo a pushed commit safely | `git revert <commit-hash>` |
| Find a "lost" commit | `git reflog` |
| Save work temporarily | `git stash`, then `git stash pop` |
| Move work to a new branch | `git switch -c new-branch` |
| Delete a merged local branch | `git branch -d branch-name` |

## Notes

- Amend or reset only commits that are not pushed yet. Use `revert` for shared history.
- `git reflog` keeps a record of where `HEAD` has been, so most mistakes can be recovered.
