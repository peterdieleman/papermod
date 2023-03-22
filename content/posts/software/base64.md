---
title: "Why base64"
tags: ["tembaspblate"]
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

## Why Not Just Binary?

Main purpose: embedding binary data (like images) inside of text (e.g. XML).

```text
"Media that is designed for textual data is of course eventually binary as well, but textual media often use certain binary values for control characters. Also, textual media may reject certain binary values as non-text.

Base64 encoding encodes binary data as values that can only be interpreted as text in textual media, and is free of any special characters and/or control characters, so that the data will be preserved across textual media as well."
```

- [Stackoverflow](https://stackoverflow.com/questions/3538021/why-do-we-use-base64)

## Padding

See: [Wikipedia](https://en.wikipedia.org/wiki/Base64#Output_padding).
