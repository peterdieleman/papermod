---
title: "Java Map"
tags: ["java"]
date: 2023-01-01
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

```java
inputString.map(x -> {
    if (!StringUtils.isBlank(x)) {
        return x;
    } else {
        return Optional.empty();
    }
}).orElse(Optional.empty());
```

```java
inputString.map(x -> {
    return StringUtils.isBlank(x) ? Optional.empty() : x;
}).orElse(Optional.empty());
```
