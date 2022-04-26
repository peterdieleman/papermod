---
title: "Db Locking"
tags: ["template"]
date: 2022-04-23
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

- <https://dzone.com/articles/concurrency-and-locking-with-jpa-everything-you-ne>
- <https://www.baeldung.com/jpa-pessimistic-locking>
- <https://blog.arnoldgalovics.com/jpa-optimistic-locking/>

> It’s also possible to lock multiple rows at the same time, this can be done by executing a custom select query and setting the lock mode.



# Exclusive lock table

- <https://stackoverflow.com/questions/64224014/include-additional-columns-in-where-clause-of-hibernate-jpa-generated-update-que>

```
@Query(value = "LOCK TABLE SKU IN EXCLUSIVE MODE", nativeQuery = true)
@Modifying
void lockTable();
```