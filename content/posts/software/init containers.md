---
title: "k8s init containers"
tags: ["init containers"]
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

## Docs

> A Pod can have multiple containers running apps within it, but it can also have one or more init containers, which are run before the app containers are started.
>
> Init containers are exactly like regular containers, except:

> Init containers always run to completion.
> Each init container must complete successfully before the next one starts.

<https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>
