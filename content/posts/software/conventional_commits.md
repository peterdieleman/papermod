---
title: "Conventional Commits"
tags: ["git"]
date: 2023-03-01
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

From [the specs](https://www.conventionalcommits.org/en/v1.0.0/#specification):

```markdown
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types

- `fix:`
- `build:`
- `chore:`
- `ci:`
- `docs:`
- `style:`
- `refactor:`
- `perf:`
- `test:`

## Examples

```markdown
fix:
```

## Relation to Semver

> fix type commits should be translated to PATCH releases. feat type commits should be translated to MINOR releases. Commits with BREAKING CHANGE in the commits, regardless of type, should be translated to MAJOR releases.
