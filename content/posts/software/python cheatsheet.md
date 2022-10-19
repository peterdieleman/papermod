---
title: "Python Cheatsheet"
tags: ["python"]
date: 2023-02-13
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

## Basics

- `brew install pyenv`
- `brew install poetry`
- `pyenv install 3.7`
- `pyenv global 3.7`
- `poetry new demo`
- `poetry add numpy`
- `poetry install`
- `poetry run demo/demo.py`

```ascii
├── README.md
├── demo
│   ├── __init__.py
│   └── demo.py <-- add yourself
├── poetry.lock
├── pyproject.toml
└── tests
    └── __init__.py
```

## Passing in Arguments when using Poetry

From SO: [test](https://stackoverflow.com/questions/67476156/pass-commandline-arguments-to-a-python-script-installed-with-poetry)

- `poetry run arg_script arg1 arg2 arg3`

## Visualizing Dir Structure

`brew install tree`
