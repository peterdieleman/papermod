---
title: "Git reset to single commit"
tags: ["git"]
date: 2023-02-01
# aliases: ["/first"]
# weight: 1
# author: "Peter Dieleman"
# showToc: false
# TocOpen: false
draft: false
# hidemeta: false
# comments: false
# description: "A guide on extending the battery life of your linux laptop"
# disableShare: false
# searchHidden: false
---

Resetting entire repository to a single commit:

```bash
git checkout --orphan newBranch
git add -A  # Add all files and commit them
git commit -m "first commit"
git branch -D main  # Deletes the main branch
git branch -m main  # Rename the current branch to main
git push -f origin main  # Force push main branch to github
git gc --aggressive --prune=all     # remove the old files
```

And additionally check remote branches: `git ls-remote` or delete them through the UI.  And use: `git push origin -d branch-name` to delete those.

From: <https://stackoverflow.com/questions/9683279/make-the-current-commit-the-only-initial-commit-in-a-git-repository>
