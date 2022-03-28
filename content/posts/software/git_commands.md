---
title: "Git Commands"
tags: ["git"]
date: 2022-02-01
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

## The Nuclear Option

`git clean -xdf`

## Pull rebase

For current repository:

`git config pull.rebase true`

As a global setting:

`git config --global pull.rebase true`

<https://coderwall.com/p/tnoiug/rebase-by-default-when-doing-git-pull>

## Fix wrong rebase

`git rebase --abort`

`git rebase --quit`

`git am --resolved`

`git am --abort`

See: <https://www.specbee.com/blogs/how-create-and-apply-patch-git-diff-and-git-apply-commands-your-drupal-website>

## Pruning branches from remote list

`git remote update origin --prune`

## Purging Secrets from Repo

Use git-filter-repo or BFG repo cleaner:

<https://www.specbee.com/blogs/how-create-and-apply-patch-git-diff-and-git-apply-commands-your-drupal-website>

Guides:

<https://improveandrepeat.com/2021/06/how-to-use-git-filter-repo-to-remove-files-from-your-git-repository/>
<https://peterbabic.dev/blog/clever-uses-for-git-filter-repo/>
<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>