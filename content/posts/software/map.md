---
title: "Map / Filter / Lambda / Stream snippets"
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

## Map

```java
inputString.map(x -> {
    if (!StringUtils.isBlank(x)) {
        return x;
    } else {
        return Optional.empty();
    }
}).orElse(Optional.empty());
```

## Filter

Java < 16

```java
return thing.getAllSubEntities()
        .stream()
        .filter(e -> e.isDisabled())
        .collect(Collectors.toList());
```

Java >= 16

```java
return thing.getAllSubEntities()
        .stream()
        .filter(e -> e.isDisabled())
        .tolist();
```
